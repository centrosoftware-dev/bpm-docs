# Passaggio di consegne — pubblicazione protetta del sito

Raccolta delle informazioni per spostare il sito da GitHub Pages (pubblico) a un'applicazione ASP.NET protetta da login. Da sviluppare in Claude Code. Nessuna di queste modifiche è stata ancora fatta.

## Obiettivo

- **Subito:** il sito non deve più essere aperto al mondo. Pubblicarlo dietro una piccola applicazione ASP.NET con un'**autenticazione semplice e locale**, per poter iniziare a distribuirlo.
- **In seguito:** sostituire il login locale con l'**accesso aziendale** (OAuth di `portali.centrosoftware.com`, lo stesso di ERP Connect).

## Situazione attuale

- Il sito è generato da MkDocs Material (`mkdocs.yml`, contenuti in `docs/`).
- `mkdocs.yml`: `site_url: https://centrosoftware-dev.github.io/bpm-docs/`, quindi il sito è pubblicato sotto il percorso `/bpm-docs/`.
- La CI (`.github/workflows/ci.yml`), a ogni push su `main`/`master`:
    1. installa `mkdocs-material`, `mkdocs-awesome-nav`, `mkdocs-glightbox`;
    2. esegue `python tools/check-docs.py` (controllo inventario e navigazione);
    3. esegue `mkdocs build --strict`;
    4. pubblica con `mkdocs gh-deploy --force` (ramo `gh-pages`).
- Dipendenze Python in `pyproject.toml` (gestite con `uv`, Python 3.13) e in `requirements.txt` (codifica UTF-16).
- Il sito è interamente statico: HTML, CSS, JS, immagini, `search/search_index.json` per la ricerca, i file Postman scaricabili in `integrazione/api-standard/postman/`.

## Architettura prevista

Un solo repository, con l'applicazione in una cartella dedicata:

```
bpm-docs/
├─ mkdocs.yml, docs/, tools/, planning/   ← come oggi
├─ host/                                  ← applicazione ASP.NET
│  ├─ BpmDocs.Host.csproj
│  └─ Program.cs                          (autenticazione + file statici)
├─ Dockerfile                             ← nella root: vede sia docs/ sia host/
└─ .github/workflows/ci.yml
```

**Dockerfile multi-stage:**

1. fase Python: installa le dipendenze, esegue `tools/check-docs.py` e `mkdocs build --strict` → cartella `site/`;
2. fase .NET: `dotnet publish` di `host/`;
3. immagine finale: solo l'applicazione compilata, con `site/` copiato nella sua `wwwroot`.

La CI si riduce a costruire l'immagine e pubblicarla. MkDocs non sa nulla dell'autenticazione; l'applicazione non sa nulla di MkDocs. In locale per scrivere si continua a usare `mkdocs serve`.

## Fase 1 — autenticazione locale

Requisiti:

- **tutto** dietro login: pagine, immagini, `search_index.json`, file scaricabili (nessun file statico servito prima dell'autenticazione);
- pagina di login semplice, con l'aspetto del sito (colori Shape: fondo `#011e41`, accento `#17ff88`, link `#3093ef`, font Noto Sans);
- sessione con cookie, logout;
- HTTPS.

Scelte da fare in Claude Code:

- **Dove stanno gli utenti:** per iniziare basta un elenco in configurazione (nome utente + password con hash), letto da variabili d'ambiente o da un archivio di segreti (es. Azure Key Vault). Probabilmente eccessivo ASP.NET Core Identity con database. Valutare anche un'unica credenziale condivisa se l'obiettivo è solo "non aperto al mondo".
- Versione di .NET.
- **Percorso base:** mantenere `/bpm-docs/` oppure pubblicare alla radice del dominio. In quest'ultimo caso cambiare `site_url` in `mkdocs.yml`.
- Nomi di dominio e certificato.

Pagine d'errore: MkDocs genera `404.html`, da usare come pagina di "non trovato" dell'applicazione.

## Fase 2 — accesso aziendale (OAuth di `portali`)

Cosa sappiamo, dall'analisi del pulsante "Accedi" di ERP Connect:

```
https://portali.centrosoftware.com/Auth/OAuth/Authorize
  ?client_id=erp_connect_site
  &redirect_uri=https://erpconnect.centrosoftware.com/account/signin
  &response_type=code
  &state=%2F
```

- È un **OAuth 2.0 authorization code flow** con un server di identità interno.
- **Non è OpenID Connect:** non esiste un documento di discovery (`/.well-known/openid-configuration` risponde 404). Riccardo conferma che è codice custom. Quindi niente autenticazione "pronta" di Azure (Easy Auth, Static Web Apps): serve implementare il flusso nell'applicazione, come fa ERP Connect (`/account/signin`, che sembra ASP.NET).

Da chiedere a chi gestisce `portali`:

- registrazione di un nuovo client (es. `bpm_docs`) con il redirect del sito della documentazione;
- endpoint per scambiare il codice con il token;
- come ottenere i dati dell'utente (nome, azienda, ruolo) ed eventualmente limitare l'accesso (per esempio partner e dipendenti);
- se è possibile riusare il codice di `/account/signin` di ERP Connect.

## Pubblicazione

- **Hosting:** Azure App Service oppure Azure Container Apps, con l'immagine costruita dal Dockerfile.
- **CI:** sostituire il passo `mkdocs gh-deploy --force` con build dell'immagine, push su un registro (es. Azure Container Registry) e rilascio su Azure. I segreti (credenziali di pubblicazione, utenti della fase 1) vanno nei secret di GitHub o in Key Vault.

## Chiudere GitHub Pages

Quando il nuovo sito è online:

1. togliere il passo `mkdocs gh-deploy --force` dalla CI;
2. disattivare Pages nelle impostazioni del repository (Settings → Pages);
3. eliminare il ramo `gh-pages`.

Anche con un repository privato, un sito GitHub Pages resta pubblico, salvo i piani Enterprise con controllo degli accessi. Per questo va chiuso, non basta rendere privato il repository.

## Riferimenti

- `Roadmap.md` → "Da fare — Riccardo": i tre compiti su autenticazione e pubblicazione.
- `planning/handoff-2026-09-26.md`: stato generale della documentazione.
