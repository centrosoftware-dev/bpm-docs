"""Genera la parte meccanica della documentazione dei connettori dai manifesti JSON.

Uso:
    python tools/genera-connettori.py <cartella-manifesti> <cartella-output>

Per ogni file *.connector.json produce un file Markdown con:
- i parametri di configurazione del connettore;
- la tabella delle funzioni esposte (operazioni, eventi, azioni client);
- per ogni funzione, la tabella dei parametri.

I file generati sono pensati per essere inclusi nelle pagine scritte a mano
(estensione pymdownx.snippets). Non vanno modificati a mano: si rigenerano.
Le interfacce di tipo "tabella" (Tipo 0) sono escluse.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

TIPI = {1: "operazione", 2: "evento", 3: "azione client"}
ESCLUSI_PREFISSO = "SAM"  # connettori SAM: documentati nella sezione dedicata


def carica(path: Path):
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-16"):
        try:
            return json.loads(raw.decode(enc))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"Manifesto non leggibile: {path}")


def slug(testo: str) -> str:
    t = unicodedata.normalize("NFKD", testo).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def cella(testo) -> str:
    t = (testo or "").strip().replace("|", "\\|").replace("\n", " ")
    return t if t else "—"


def tabella_parametri(parametri) -> list[str]:
    righe = ["| Parametro | Direzione | Obbligatorio | Descrizione |", "|---|---|---|---|"]
    for p in sorted(parametri, key=lambda x: x.get("Ordinamento") or 0):
        direzione = "uscita" if p.get("Output") else "ingresso"
        if p.get("Dettaglio"):
            direzione += " (righe)"
        obbl = "sì" if p.get("Obbligatorio") else ""
        righe.append(f"| `{p['Nome']}` | {direzione} | {obbl} | {cella(p.get('Descrizione'))} |")
    return righe


def genera(manifesto: dict) -> str:
    out = [f"<!-- Generato da tools/genera-connettori.py dal manifesto {manifesto['Nome']} "
           f"versione {manifesto.get('Versione', '')}. Non modificare a mano. -->", ""]
    conf = manifesto.get("Parametri") or []
    if conf:
        out += ["### Configurazione del connettore", ""]
        out += tabella_parametri(conf) + [""]
    interfacce = [i for i in manifesto.get("Interfacce") or [] if i.get("Tipo") in TIPI]
    out += ["### Funzioni disponibili", "", "| Funzione | Tipo | Descrizione |", "|---|---|---|"]
    for i in interfacce:
        out.append(f"| [{i['Nome']}](#{slug(i['Nome'])}) | {TIPI[i['Tipo']]} | {cella(i.get('Descrizione'))} |")
    out.append("")
    for i in interfacce:
        out += [f"### {i['Nome']}", "", f"*{TIPI[i['Tipo']].capitalize()}.* {cella(i.get('Descrizione'))}", ""]
        parametri = i.get("Parametri") or []
        out += (tabella_parametri(parametri) if parametri else ["Nessun parametro."]) + [""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    sorgente, destinazione = Path(sys.argv[1]), Path(sys.argv[2])
    destinazione.mkdir(parents=True, exist_ok=True)
    for f in sorted(sorgente.glob("*.connector.json")):
        m = carica(f)
        if m["Nome"].upper().startswith(ESCLUSI_PREFISSO) or f.name.upper().startswith(ESCLUSI_PREFISSO):
            continue
        nome = slug(f.name.replace(".connector.json", ""))
        (destinazione / f"{nome}.md").write_text(genera(m), encoding="utf-8")
        print(f"{nome}.md  <- {m['Nome']} v{m.get('Versione', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
