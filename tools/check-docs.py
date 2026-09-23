from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INVENTORY = ROOT / "planning" / "inventory"
ALLOWED_STATUSES = {"da-documentare", "da-verificare", "verificato"}
IGNORED_PAGES = {"index.md"}
IGNORED_PREFIXES = {"adr/", "tutorial/"}
REQUIRED_FIELDS = {"id", "tipo", "nome", "percorso_ui", "pagina", "stato", "fonte"}
MARKDOWN_LINK = re.compile(r"!?\[[^]]*]\(([^)]+)\)")
SAFE_PATH_PART = re.compile(r"^[a-z0-9.-]+$")
EXPECTED_ROOT_NAV = [
    {"Inizia": [
        {"Home": "index.md"},
        {"Tutorial": "tutorial/index.md"},
        {"Corso base": "tutorial/corso-base"},
        {"Corso avanzato": "tutorial/corso-avanzato"},
    ]},
    {"Processi": "modelli-di-processo"},
    {"Documenti": "classi-documentali"},
    {"Integrazione e AI": "integrazione-e-ai"},
    {"Amministrazione": "amministrazione"},
    {"Parti comuni": "parti-comuni"},
]
EXPECTED_CONFIGURATION_NAV = [
    "index.md",
    {"Configurazione": [
        {"Opzioni generali": "opzioni-generali"},
        {"Opzioni modelli": "opzioni-modelli"},
        {"Utenti e gruppi": "utenti-e-gruppi"},
        {"Contatti": "contatti"},
        {"Allegati": "allegati"},
        {"Tabelle": "tabelle"},
        {"Altre opzioni": "altre-opzioni"},
    ]},
    {"Sistema": "sistema"},
]


def main() -> int:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    inventoried_pages: set[str] = set()
    page_statuses: dict[str, set[str]] = {}

    inventory_files = sorted(INVENTORY.glob("*.yml"))
    if not inventory_files:
        errors.append("Nessun inventario trovato in planning/inventory.")

    for inventory_file in inventory_files:
        try:
            data = yaml.safe_load(inventory_file.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{inventory_file}: YAML non valido: {exc}")
            continue

        entries = data.get("voci", []) if isinstance(data, dict) else []
        if not isinstance(entries, list):
            errors.append(f"{inventory_file}: 'voci' deve essere una lista.")
            continue

        for index, entry in enumerate(entries, start=1):
            location = f"{inventory_file}:{index}"
            if not isinstance(entry, dict):
                errors.append(f"{location}: la voce deve essere una mappa.")
                continue

            missing = REQUIRED_FIELDS - entry.keys()
            if missing:
                errors.append(f"{location}: campi mancanti: {', '.join(sorted(missing))}.")
                continue

            entry_id = str(entry["id"])
            if entry_id in ids:
                errors.append(f"{location}: id duplicato '{entry_id}', gia presente in {ids[entry_id]}.")
            else:
                ids[entry_id] = inventory_file

            status = str(entry["stato"])
            if status not in ALLOWED_STATUSES:
                errors.append(f"{location}: stato non ammesso '{status}'.")

            page = str(entry["pagina"]).replace("\\", "/")
            inventoried_pages.add(page)
            page_statuses.setdefault(page, set()).add(status)
            if any(not SAFE_PATH_PART.fullmatch(part) for part in Path(page).parts):
                errors.append(f"{location}: percorso non conforme alle convenzioni: {page}.")
            if status != "da-documentare" and not (DOCS / page).is_file():
                errors.append(f"{location}: pagina dichiarata presente ma inesistente: {page}.")

    authored_pages = {
        path.relative_to(DOCS).as_posix()
        for path in DOCS.rglob("*.md")
        if path.relative_to(DOCS).as_posix() not in IGNORED_PAGES
        and not any(path.relative_to(DOCS).as_posix().startswith(prefix) for prefix in IGNORED_PREFIXES)
    }

    for page in sorted(authored_pages - inventoried_pages):
        errors.append(f"Pagina non presente nell'inventario: {page}.")

    for page in sorted(authored_pages):
        if not (DOCS / page).read_text(encoding="utf-8").strip():
            errors.append(f"Pagina vuota pubblicata: {page}.")
        if page_statuses.get(page) == {"da-documentare"}:
            errors.append(f"Pagina presente ma dichiarata solo 'da-documentare': {page}.")

    check_navigation(errors)
    check_local_links(errors)

    if errors:
        print("Controllo documentazione fallito:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Inventario valido: {len(ids)} voci, {len(authored_pages)} pagine presenti.")
    return 0


def check_navigation(errors: list[str]) -> None:
    navigated_pages: set[str] = set()
    for nav_file in DOCS.rglob(".nav.yml"):
        try:
            data = yaml.safe_load(nav_file.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{nav_file}: YAML di navigazione non valido: {exc}")
            continue

        nav = data.get("nav", [])
        if nav_file == DOCS / ".nav.yml" and nav != EXPECTED_ROOT_NAV:
            errors.append(f"{nav_file}: le macroaree non corrispondono alla struttura concordata.")
        if nav_file == DOCS / "amministrazione" / ".nav.yml" and nav != EXPECTED_CONFIGURATION_NAV:
            errors.append(f"{nav_file}: le sezioni non corrispondono ad Amministrazione.")

        for target in navigation_targets(nav):
            if target == "...":
                continue
            resolved = resolve_local_target(nav_file.parent, target)
            if resolved is None:
                errors.append(f"{nav_file}: destinazione di navigazione inesistente: {target}.")
            elif resolved.suffix == ".md":
                navigated_pages.add(resolved.relative_to(DOCS).as_posix())

    authored_pages = {
        path.relative_to(DOCS).as_posix()
        for path in DOCS.rglob("*.md")
        if path.relative_to(DOCS).as_posix() not in IGNORED_PAGES
        and not any(path.relative_to(DOCS).as_posix().startswith(prefix) for prefix in IGNORED_PREFIXES)
    }
    for page in sorted(authored_pages - navigated_pages):
        errors.append(f"Pagina non raggiungibile dalla navigazione: {page}.")


def navigation_targets(value: object):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from navigation_targets(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from navigation_targets(item)


def local_target_exists(base: Path, target: str) -> bool:
    return resolve_local_target(base, target) is not None


def resolve_local_target(base: Path, target: str) -> Path | None:
    path = base / unquote(target.split("#", 1)[0])
    if path.is_file():
        return path
    if path.with_suffix(".md").is_file():
        return path.with_suffix(".md")
    if (path / "index.md").is_file():
        return path / "index.md"
    return None


def check_local_links(errors: list[str]) -> None:
    for source in DOCS.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue

            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            fragment = unquote(target.split("#", 1)[1]) if "#" in target else ""
            if path_part:
                base = DOCS if path_part.startswith("/") else source.parent
                resolved = resolve_local_target(base, path_part.lstrip("/"))
            else:
                resolved = source

            if resolved is None:
                relative_source = source.relative_to(ROOT)
                errors.append(f"{relative_source}: collegamento locale inesistente: {target}.")
            elif fragment and resolved.suffix == ".md" and fragment not in markdown_anchors(resolved):
                relative_source = source.relative_to(ROOT)
                errors.append(f"{relative_source}: sezione locale inesistente: {target}.")


def markdown_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        heading = re.sub(r"[`*_\[\]]", "", match.group(1))
        normalized = unicodedata.normalize("NFKD", heading).encode("ascii", "ignore").decode()
        anchor = re.sub(r"[^a-z0-9 _-]", "", normalized.lower()).strip().replace(" ", "-")
        anchor = re.sub(r"-+", "-", anchor)
        count = counts.get(anchor, 0)
        counts[anchor] = count + 1
        anchors.add(anchor if count == 0 else f"{anchor}_{count}")
    return anchors


if __name__ == "__main__":
    sys.exit(main())
