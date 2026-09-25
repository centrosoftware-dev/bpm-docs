import logging
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXPORT_DIR = ROOT / "export"
OUTPUT_DOCX = EXPORT_DIR / "Documentazione-BPM.docx"
INTERMEDIATE_MD = EXPORT_DIR / "_intermediate.md"
GROUP_ROOT = EXPORT_DIR / "_gruppi"
ICON_RE = re.compile(r":(?:material|octicons|fontawesome)-[a-z0-9-]+:(?:\{[^}]*\})?\s?")
SNIPPET_RE = re.compile(r'^\s*--8<--\s+"([^"]+)"\s*$', re.MULTILINE)
DOC_TITLE = "Documentazione BPM"
# I titoli ATX in Markdown/Pandoc supportano al massimo 6 '#': oltre, la riga
# non viene riconosciuta come intestazione (nonostante Word supporti Heading 1-9).
MAX_MARKDOWN_HEADING = 6

HEADING_LINE_RE = re.compile(r"^([-*+]\s+)?(#{1,6})\s+(.*)$")
FENCE_LINE_RE = re.compile(r"^\s*(```|~~~)")
FENCE_OPEN_ATTRS_RE = re.compile(r"^(\s*)(```+|~~~+)\s*(\S.*=.*)$")
FENCE_TITLE_RE = re.compile(r'title="([^"]*)"')
MARKUP_RE = re.compile(r"[`*_\[\]]")
ADMONITION_RE = re.compile(r'^(!!!|\?\?\?)\+?\s+(\S+)(?:\s+"((?:[^"\\]|\\.)*)"|\s+(.+))?\s*$')
KEYS_RE = re.compile(r"\+\+([A-Za-z0-9_-]+)\+\+")
ANNOTATE_LINE_RE = re.compile(r"^[ \t]*\{\s*\.annotate\s*\}[ \t]*$", re.MULTILINE)
IMAGE_RE = re.compile(r'(!\[[^\]]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
LINK_RE = re.compile(r'(?<!!)(\[[^\]]*\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
HEADER_ID_RE = re.compile(r'Header\s+\d+\s*\(\s*"([^"]*)"')
UNHANDLED_MARKERS = {
    "mermaid fence": re.compile(r"^```mermaid", re.MULTILINE),
    "tabbed content": re.compile(r'^===\s+"', re.MULTILINE),
    "critic markup": re.compile(r"\{--|\{\+\+|\{~~"),
}


@dataclass
class NavPage:
    title: str
    path: Path
    depth: int


def resolve_local_target(base: Path, target: str) -> Path | None:
    path = base / unquote(target.split("#", 1)[0])
    if path.is_file():
        return path
    if path.with_suffix(".md").is_file():
        return path.with_suffix(".md")
    if (path / "index.md").is_file():
        return path / "index.md"
    return None


def load_nav(nav_file: Path) -> list:
    data = yaml.safe_load(nav_file.read_text(encoding="utf-8")) or {}
    nav = data.get("nav")
    if not isinstance(nav, list):
        raise ValueError(f"{nav_file}: manca una lista 'nav' valida.")
    return nav


def derive_title(md_path: Path) -> str:
    for line in md_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r"^#\s+(.+?)\s*#*$", stripped)
        if match:
            return MARKUP_RE.sub("", match.group(1)).strip()
        break
    return md_path.stem.replace("-", " ").title()


def titles_match(nav_title: str, body_title: str) -> bool:
    a, b = nav_title.casefold().strip(), body_title.casefold().strip()
    return a == b or a in b or b in a


def walk_nav(nav_file: Path, depth: int, title_override: str | None = None) -> list[NavPage]:
    entries = load_nav(nav_file)
    pages: list[NavPage] = []

    if title_override is not None:
        if not entries or entries[0] != "index.md":
            raise NotImplementedError(
                f"{nav_file}: prima voce attesa 'index.md' per la sezione '{title_override}'."
            )
        index_path = resolve_local_target(nav_file.parent, "index.md")
        if index_path is None:
            raise FileNotFoundError(f"{nav_file}: index.md non trovato per la sezione '{title_override}'.")
        pages.append(NavPage(title=title_override, path=index_path.resolve(), depth=depth))
        remaining = entries[1:]
        child_depth = depth + 1
    else:
        remaining = entries
        child_depth = depth

    pages.extend(walk_nav_items(nav_file, remaining, child_depth))
    return pages


def walk_nav_items(nav_file: Path, remaining: list, child_depth: int) -> list[NavPage]:
    pages: list[NavPage] = []
    for item in remaining:
        if isinstance(item, str):
            resolved = resolve_local_target(nav_file.parent, item)
            if resolved is None:
                raise FileNotFoundError(f"{nav_file}: voce di navigazione inesistente: {item}.")
            pages.append(NavPage(title=derive_title(resolved), path=resolved.resolve(), depth=child_depth))
            continue

        if isinstance(item, dict) and len(item) == 1 and isinstance(next(iter(item.values())), list):
            # Gruppo solo di navigazione (es. "Operazioni: [..]"): intestazione senza pagina.
            title, children = next(iter(item.items()))
            pages.append(NavPage(title=title, path=(GROUP_ROOT / f"{nav_file.parent.name}-{title}").resolve(), depth=child_depth))
            pages.extend(walk_nav_items(nav_file, children, child_depth + 1))
            continue

        if isinstance(item, dict) and len(item) == 1:
            title, target = next(iter(item.items()))
            target_path = (nav_file.parent / unquote(str(target))).resolve()
            if target_path.is_dir():
                nested_nav = target_path / ".nav.yml"
                if nested_nav.is_file():
                    pages.extend(walk_nav(nested_nav, depth=child_depth, title_override=title))
                    continue
                index_path = target_path / "index.md"
                if index_path.is_file():
                    pages.append(NavPage(title=title, path=index_path.resolve(), depth=child_depth))
                    continue
                raise FileNotFoundError(f"{nav_file}: la cartella '{target}' non ha ne' .nav.yml ne' index.md.")

            resolved = resolve_local_target(nav_file.parent, str(target))
            if resolved is None:
                raise FileNotFoundError(f"{nav_file}: voce di navigazione inesistente: {target}.")
            pages.append(NavPage(title=title, path=resolved.resolve(), depth=child_depth))
            continue

        raise NotImplementedError(f"{nav_file}: voce di navigazione non gestita: {item!r}.")

    return pages


def convert_admonitions(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        match = ADMONITION_RE.match(lines[i])
        if not match:
            out.append(lines[i])
            i += 1
            continue

        kind, title_quoted, title_bare = match.group(2), match.group(3), match.group(4)
        label = title_quoted or title_bare or kind.capitalize()

        j = i + 1
        body_lines: list[str] = []
        while j < len(lines) and (lines[j].strip() == "" or lines[j].startswith(("    ", "\t"))):
            body_lines.append(lines[j])
            j += 1
        while body_lines and body_lines[-1].strip() == "":
            body_lines.pop()

        out.append(f"> **{label}**")
        out.append(">")
        for body_line in body_lines:
            if body_line.startswith("    "):
                stripped = body_line[4:]
            elif body_line.startswith("\t"):
                stripped = body_line[1:]
            else:
                stripped = body_line
            out.append(f"> {stripped}" if stripped.strip() else ">")

        # Riga vuota obbligatoria: senza, Pandoc puo' fondere il blocco
        # successivo (es. un'intestazione) dentro il blockquote o un
        # code block adiacente, invece di iniziare un nuovo blocco.
        out.append("")

        i = j

    return "\n".join(out)


def normalize_code_fences(text: str) -> str:
    """Pandoc non riconosce un fence con attributi non tra graffe
    (es. `title="x" linenums="1"`, sintassi pymdownx.superfences): lo
    interpreta come testo inline e rompe il parsing di tutto cio' che segue.
    Il titolo, se presente, diventa un paragrafo in grassetto prima del fence."""
    out: list[str] = []
    for line in text.splitlines():
        match = FENCE_OPEN_ATTRS_RE.match(line)
        if not match:
            out.append(line)
            continue
        indent, fence, info = match.groups()
        title_match = FENCE_TITLE_RE.search(info)
        if title_match:
            out.append(f"**{title_match.group(1)}**")
            out.append("")
        out.append(f"{indent}{fence}")
    return "\n".join(out)


def convert_keys(text: str) -> str:
    def replace(match: re.Match) -> str:
        key = match.group(1)
        label = key.upper() if re.fullmatch(r"f\d+", key, re.IGNORECASE) else key.capitalize()
        return f"`{label}`"

    return KEYS_RE.sub(replace, text)


def strip_annotate_markers(text: str) -> str:
    text = ANNOTATE_LINE_RE.sub("", text)
    return re.sub(r"\n{3,}", "\n\n", text)


def rewrite_image_paths(text: str, source_dir: Path) -> str:
    def replace(match: re.Match) -> str:
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        if url.startswith(("http://", "https://")):
            return match.group(0)
        candidate = (source_dir / unquote(url)).resolve()
        if not candidate.is_file():
            logging.warning("Immagine non trovata: %s (riferita da %s)", url, source_dir)
            return match.group(0)
        return f"{prefix}{candidate.as_posix()}{suffix}"

    return IMAGE_RE.sub(replace, text)


def mkdocs_slugify(heading_text: str, counts: dict[str, int]) -> str:
    cleaned = MARKUP_RE.sub("", heading_text)
    normalized = unicodedata.normalize("NFKD", cleaned).encode("ascii", "ignore").decode()
    anchor = re.sub(r"[^a-z0-9 _-]", "", normalized.lower()).strip().replace(" ", "-")
    anchor = re.sub(r"-+", "-", anchor)
    count = counts.get(anchor, 0)
    counts[anchor] = count + 1
    return anchor if count == 0 else f"{anchor}_{count}"


def rewrite_internal_links(
    text: str,
    source_dir: Path,
    page_top_id: dict[Path, str],
    fragment_id_map: dict[Path, dict[str, str]],
) -> str:
    def replace(match: re.Match) -> str:
        prefix, url, suffix = match.group(1), match.group(2), match.group(3)
        if url.startswith(("http://", "https://", "mailto:")):
            return match.group(0)

        path_part, has_fragment, fragment = url.partition("#")
        if not path_part:
            return match.group(0)

        resolved = resolve_local_target(source_dir, path_part)
        if resolved is None:
            return match.group(0)
        resolved = resolved.resolve()
        if resolved not in page_top_id:
            return match.group(0)

        if has_fragment:
            target_id = fragment_id_map.get(resolved, {}).get(fragment)
            if target_id is None:
                logging.warning("Frammento non trovato per il link interno: %s (in %s)", url, source_dir)
                target_id = page_top_id[resolved]
        else:
            target_id = page_top_id[resolved]

        return f"{prefix}#{target_id}{suffix}"

    return LINK_RE.sub(replace, text)


def shift_and_dedupe_headings(text: str, nav_title: str, base_level: int) -> tuple[str, list[str]]:
    lines = text.splitlines()
    out: list[str] = []
    kept_headings: list[str] = []
    in_fence = False
    first_heading_seen = False

    for line in lines:
        if FENCE_LINE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue

        heading_match = HEADING_LINE_RE.match(line)
        if not heading_match:
            out.append(line)
            continue

        prefix = heading_match.group(1) or ""
        level = len(heading_match.group(2))
        heading_text = heading_match.group(3)

        if not first_heading_seen and not prefix:
            first_heading_seen = True
            cleaned = MARKUP_RE.sub("", heading_text).strip()
            if level == 1 and titles_match(nav_title, cleaned):
                continue

        new_level = level + base_level
        if new_level > MAX_MARKDOWN_HEADING:
            logging.warning(
                "Intestazione oltre il livello 6 dopo lo shift, convertita in paragrafo in grassetto: %s",
                heading_text,
            )
            out.append(f"{prefix}**{heading_text}**")
        else:
            out.append(f"{prefix}{'#' * new_level} {heading_text}")
            kept_headings.append(heading_text)

    return "\n".join(out), kept_headings


def expand_snippets(text: str) -> str:
    def replace(match: re.Match) -> str:
        snippet = ROOT / match.group(1)
        if not snippet.is_file():
            logging.warning("Snippet non trovato: %s", match.group(1))
            return ""
        return snippet.read_text(encoding="utf-8")
    return SNIPPET_RE.sub(replace, text)


def render_page(page: NavPage) -> tuple[str, list[str]]:
    if not page.path.is_file() and GROUP_ROOT.resolve() in page.path.parents:
        heading_level = min(page.depth, MAX_MARKDOWN_HEADING)
        return f"{'#' * heading_level} {page.title}\n", [page.title]
    text = expand_snippets(page.path.read_text(encoding="utf-8"))
    text = ICON_RE.sub("", text)
    text = normalize_code_fences(text)
    text = convert_admonitions(text)
    text = convert_keys(text)
    text = strip_annotate_markers(text)
    text = rewrite_image_paths(text, page.path.parent)
    body, kept_headings = shift_and_dedupe_headings(text, page.title, page.depth)
    heading_level = min(page.depth, MAX_MARKDOWN_HEADING)
    rendered = f"{'#' * heading_level} {page.title}\n\n{body}"
    return rendered, [page.title] + kept_headings


def build_id_maps(
    pages: list[NavPage], headings_by_page: dict[Path, list[str]], pandoc_ids: list[str]
) -> tuple[dict[Path, str], dict[Path, dict[str, str]]]:
    page_top_id: dict[Path, str] = {}
    fragment_id_map: dict[Path, dict[str, str]] = {}
    cursor = 0

    for page in pages:
        headings = headings_by_page[page.path]
        ids_for_page = pandoc_ids[cursor : cursor + len(headings)]
        cursor += len(headings)
        if len(ids_for_page) != len(headings):
            raise RuntimeError(f"Disallineamento tra intestazioni ed id Pandoc per {page.path}.")

        page_top_id[page.path] = ids_for_page[0]
        counts: dict[str, int] = {}
        frag_map: dict[str, str] = {}
        for heading_text, pandoc_id in zip(headings[1:], ids_for_page[1:]):
            slug = mkdocs_slugify(heading_text, counts)
            frag_map[slug] = pandoc_id
        fragment_id_map[page.path] = frag_map

    if cursor != len(pandoc_ids):
        raise RuntimeError(
            f"Numero di intestazioni Pandoc ({len(pandoc_ids)}) diverso da quello atteso ({cursor})."
        )

    return page_top_id, fragment_id_map


def warn_unhandled_markers(pages: list[NavPage]) -> None:
    for page in pages:
        if not page.path.is_file():
            continue
        text = page.path.read_text(encoding="utf-8")
        for name, pattern in UNHANDLED_MARKERS.items():
            if pattern.search(text):
                logging.warning("%s: trovato marcatore non gestito (%s).", page.path, name)


def find_pandoc() -> str | None:
    found = shutil.which("pandoc")
    if found:
        return found
    fallback = Path(os.environ.get("LOCALAPPDATA", "")) / "Pandoc" / "pandoc.exe"
    if fallback.is_file():
        return str(fallback)
    return None


def run_pandoc_native(pandoc_exe: str, input_md: Path) -> str:
    result = subprocess.run(
        [pandoc_exe, str(input_md), "--from=markdown+raw_html", "-t", "native"],
        check=True,
        capture_output=True,
        encoding="utf-8",
    )
    return result.stdout


def run_pandoc(pandoc_exe: str, input_md: Path, output_docx: Path) -> None:
    subprocess.run(
        [
            pandoc_exe,
            str(input_md),
            "--from=markdown+raw_html",
            "--to=docx",
            "--standalone",
            "--toc",
            "--toc-depth=4",
            f"--metadata=title:{DOC_TITLE}",
            "-o",
            str(output_docx),
        ],
        check=True,
    )


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    pandoc_exe = find_pandoc()
    if pandoc_exe is None:
        print("pandoc non trovato. Eseguire: winget install --id JohnMacFarlane.Pandoc")
        return 2

    # Uso: python tools/export-docx.py [sezione]   es. python tools/export-docx.py integrazione
    global OUTPUT_DOCX, DOC_TITLE
    section = sys.argv[1] if len(sys.argv) > 1 else None
    if section:
        section_nav = DOCS / section / ".nav.yml"
        if not section_nav.is_file():
            print(f"Sezione non trovata: {section}")
            return 2
        root_nav = load_nav(DOCS / ".nav.yml")
        section_title = next((t for e in root_nav if isinstance(e, dict) for t, v in e.items() if v == section), section.title())
        DOC_TITLE = f"Documentazione BPM - {section_title}"
        OUTPUT_DOCX = EXPORT_DIR / f"Documentazione-BPM-{section}.docx"
        pages = walk_nav(section_nav, depth=1, title_override=section_title)
    else:
        pages = walk_nav(DOCS / ".nav.yml", depth=1)
    warn_unhandled_markers(pages)

    rendered_by_page: dict[Path, str] = {}
    headings_by_page: dict[Path, list[str]] = {}
    for page in pages:
        rendered, headings = render_page(page)
        rendered_by_page[page.path] = rendered
        headings_by_page[page.path] = headings

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    # Prima passata: scopriamo gli id reali che Pandoc assegna alle intestazioni
    # (necessari per trasformare i link tra pagine in segnalibri interni al
    # documento unico, invece di link esterni ai singoli file .md sorgente).
    pass1_combined = "\n\n".join(rendered_by_page[p.path] for p in pages) + "\n"
    INTERMEDIATE_MD.write_text(pass1_combined, encoding="utf-8")
    try:
        native = run_pandoc_native(pandoc_exe, INTERMEDIATE_MD)
    except subprocess.CalledProcessError as exc:
        print(f"pandoc ha fallito nell'analisi delle intestazioni (exit {exc.returncode}).")
        return 1

    pandoc_ids = HEADER_ID_RE.findall(native)
    expected = sum(len(headings_by_page[p.path]) for p in pages)
    if len(pandoc_ids) != expected:
        raise RuntimeError(
            f"Attese {expected} intestazioni riconosciute da Pandoc, trovate {len(pandoc_ids)}."
        )
    page_top_id, fragment_id_map = build_id_maps(pages, headings_by_page, pandoc_ids)

    final_combined = (
        "\n\n".join(
            rewrite_internal_links(rendered_by_page[p.path], p.path.parent, page_top_id, fragment_id_map)
            for p in pages
        )
        + "\n"
    )
    INTERMEDIATE_MD.write_text(final_combined, encoding="utf-8")

    try:
        run_pandoc(pandoc_exe, INTERMEDIATE_MD, OUTPUT_DOCX)
    except subprocess.CalledProcessError as exc:
        print(f"pandoc ha fallito (exit {exc.returncode}).")
        return 1

    print(f"Esportate {len(pages)} pagine in {OUTPUT_DOCX.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
