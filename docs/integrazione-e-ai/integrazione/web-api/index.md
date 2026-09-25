# Web API

Le Web API permettono a un'applicazione esterna di pilotare BPM: avviare processi, farli avanzare, leggerne lo stato, consultare la To-Do List di un utente, caricare allegati e gestire i documenti delle classi documentali.

Sono l'interfaccia più completa per integrare BPM con un altro sistema, quando è **l'applicazione esterna** a prendere l'iniziativa.

## Le stesse regole dell'utente

Una chiamata alle Web API esegue le stesse regole e gli stessi controlli dell'operazione corrispondente fatta da un utente in BPM. Avviare un processo tramite API significa quindi:

- eseguire formule, validazioni e controlli di obbligatorietà;
- eseguire gli script collegati all'avvio;
- verificare che l'utente indicato esista e abbia il diritto di avviare quel processo da quello start.

Se una regola non è soddisfatta, la chiamata fallisce con il messaggio di errore che l'utente avrebbe visto a video.

## Indirizzo delle chiamate

Tutte le chiamate hanno la forma:

```text
https://<indirizzo-bpm>/api/ext/<NomeChiamata>
```

dove `<indirizzo-bpm>` è l'indirizzo dell'applicazione web di BPM, per esempio `https://bpm.azienda.it/BPM`.

L'indirizzo base delle API è configurato nei parametri di sistema, scheda **Engine/automatismi**, campo **url api**.

## Formato delle richieste e delle risposte

- Le chiamate sono quasi tutte di tipo `POST`, con un oggetto JSON nel corpo della richiesta. Anche le chiamate di sola lettura, come GetProcess o GetTodolist, usano `POST`: i loro parametri sono oggetti complessi (filtri, elenchi, credenziali) che non si possono passare comodamente nell'indirizzo, come avverrebbe con una `GET`.
- Ogni richiesta contiene le credenziali di accesso: vedi [Autenticazione e utenti](autenticazione.md).
- La maggior parte delle risposte contiene il campo `result` (`true` se l'operazione è riuscita) e il campo `message`, valorizzato con il messaggio di errore in caso di esito negativo. Fanno eccezione alcune chiamate sui documenti e sugli elenchi dei modelli, che segnalano gli errori con il codice HTTP: sono indicate nelle rispettive pagine.

```json
{
  "result": false,
  "message": "Messaggio di errore …"
}
```

### Identificare un'istanza

Le chiamate che lavorano su un processo o un documento esistente accettano due modi alternativi per identificarlo:

- `instanceId`: l'identificativo univoco dell'istanza, restituito alla creazione;
- `model` + `documentName`: il nome del modello e il nome dell'istanza, univoco all'interno del modello (per esempio `APPROVAZIONE CONTRATTI` e `P004A.19.1`).

Basta valorizzare una delle due forme.

### Variabili

Le variabili si passano nell'oggetto `variables` come coppie nome-valore, usando i nomi delle variabili del modello. I nomi non distinguono tra maiuscole e minuscole. Le variabili di gruppo (testata-dettaglio) si passano come array, con un elemento per ogni riga:

```json
"variables": {
  "Ragione Sociale": "Rossi S.p.A.",
  "Data Apertura": "2026-01-18T00:00:00",
  "Importo": 179.58,
  "Righe": [
    { "Codice": "P01", "Descrizione": "Descrizione P01" },
    { "Codice": "P02", "Descrizione": "Descrizione P02" }
  ]
}
```

Regole sui valori:

- **Numeri**: numero JSON oppure stringa convertibile.
- **Date**: stringa nel formato `yyyy-mm-dd` (con l'ora, `yyyy-mm-ddThh:mm:ss`).
- **Booleani**: `true` / `false`.
- **Testo esteso (Memo)**: stringa semplice; per il testo formattato si può passare un oggetto `{ "HTML": "<p>…</p>" }`. Nelle risposte le variabili Memo sono restituite come oggetto con `Text` e `HTML`.
- **Nomi sconosciuti**: una variabile che non esiste nel modello viene ignorata senza restituire errori; l'avviso viene scritto nel log del servizio **WkfApi**, il processo del server BPM che gestisce le chiamate. Se un valore sembra non arrivare, controlla i nomi delle variabili e il log di WkfApi.


Per sapere quali variabili richiede un'attività o uno start, usa [GetSchema](processi.md#getschema).

### Campi generali

Oltre alle variabili definite nel modello, ogni processo e ogni documento ha dei **campi generali**, sempre presenti, che ne descrivono lo stato. Hanno il prefisso `fix_`: si possono leggere con [GetProcess](processi.md#getprocess) e [GetDocument](documenti.md#getdocument) e si possono usare come filtri in [SearchDocuments](documenti.md#searchdocuments).

| Campo | Etichetta in BPM | Contenuto |
|---|---|---|
| `fix_name` | Nome | Nome dell'istanza, univoco nel modello. |
| `fix_descrizione` | Descrizione | Descrizione dell'istanza. |
| `fix_text` | Testo | Testo descrittivo dell'istanza. |
| `fix_lifecycle` | Modello | Nome del modello di processo o della classe documentale. |
| `fix_version` | Versione | Versione del modello. |
| `fix_state` | Stato | Stato corrente. |
| `fix_active` | Attivo | Indica se l'istanza è ancora attiva. |
| `fix_activestep` | Task attivo | Attività attive in questo momento. |
| `fix_useractivestep` | Utente task attivo | Utenti assegnati alle attività attive. |
| `fix_owners` | Proprietari | Proprietari dell'istanza. |
| `fix_data` | Data creazione | Data di creazione. |
| `fix_utecreazione` | Utente creazione | Utente che ha creato l'istanza. |
| `fix_dataultimamodifica` | Data ultima modifica | Data dell'ultima modifica. |
| `fix_utemodifica` | Utente ultima modifica | Utente che ha eseguito l'ultima modifica. |
| `fix_tipoultimamodifica` | Tipo ultima modifica | Tipo dell'ultima modifica. |
| `fix_has_attachments` | Presenza allegati | Indica se l'istanza ha allegati. |

Solo per i documenti delle classi documentali:

| Campo | Etichetta in BPM | Contenuto |
|---|---|---|
| `fix_documentdate` | Data documento | Data del documento. |
| `fix_duedate` | Data scadenza | Data di scadenza del documento. |
| `fix_barcode` | Barcode | Codice a barre. |
| `fix_filename` | Nome file | Nome del file del documento. |
| `fix_currentversion` | Versione file | Versione corrente del file. |
| `fix_has_document` | Presenza documento | Indica se al documento è associato un file. |
| `fix_has_signedcopy` | Presenza copia firmata | Indica se è presente la copia firmata. |
| `fix_has_versions` | Presenza versioni | Indica se il documento ha più versioni. |

Anche i nomi dei campi generali non distinguono tra maiuscole e minuscole.

## Le chiamate disponibili

| Area | Chiamate |
|---|---|
| [Processi](processi.md) | CreateNewProcess, GetProcess, UpdateProcess, DeleteProcess, UploadAttachment, AddLink, ProcessModels, GetSchema |
| [Attività e To-Do List](attivita.md) | GetTodolist, GetPageTodoList, ExecTask, UpdateTask |
| [Documenti e dossier](documenti.md) | CreateNewDocument, CreateOrUpdateDocument, UpdateDocument, UpdateDocumentContent, GetDocument, SearchDocuments, DownloadDocument, DownloadDocumentJSON, DocumentVersions, DeleteDocument, DocumentSets, AddDocumentToDossier |
| [Utilità](utilita.md) | GetUser, CreateOrUpdateUser, GetVersion |

## Swagger e strumenti di prova

Ogni installazione espone la descrizione completa delle API in formato Swagger (OpenAPI 2.0) all'indirizzo:

```text
https://<indirizzo-bpm>/api/swagger/docs/v1
```

Lo Swagger elenca tutte le chiamate e i relativi parametri, ma non riporta la struttura dell'oggetto `authorization` né il significato dei campi: per questi fa fede questa documentazione.

### Provare le chiamate

Per provare le chiamate senza scrivere codice è disponibile una collection per **Postman** con tutte le chiamate di questa sezione e un esempio di richiesta per ciascuna:

- [:material-download: Collection BPM Web API](postman/bpm-web-api.postman-collection.json){ download="bpm-web-api.postman-collection.json" }
- [:material-download: Ambiente BPM](postman/bpm.postman-environment.json){ download="bpm.postman-environment.json" }

Per iniziare:

1. In Postman, importa i due file con **Import**.
2. Seleziona l'ambiente **BPM** e compila le variabili: `bpmUrl` (indirizzo dell'applicazione web, per esempio `https://bpm.azienda.it/BPM`), `apiKey` (la [chiave API](autenticazione.md#chiave-api)) e `userName`.
3. Adatta i nomi di modello, classe documentale, start e attività agli oggetti della tua installazione.

CreateNewProcess e CreateNewDocument salvano automaticamente nell'ambiente l'identificativo dell'istanza creata, che le chiamate successive usano subito.

La collection si importa anche in altri strumenti compatibili con il formato Postman, come Bruno.
