# Documenti e dossier

Chiamate per creare, aggiornare, cercare e scaricare i documenti delle classi documentali, e per inserirli nei dossier. Per le regole comuni vedi [Web API](index.md).

## Concetti

**Nome del documento.** Ogni documento ha un nome (`documentName`, in alcune chiamate `Name`) univoco all'interno della classe documentale. Non è il nome del file: è composto dalle variabili del documento, secondo le regole e gli script della classe documentale, e ne determina l'univocità.

**Dossier.** Un dossier raggruppa documenti di classi documentali diverse che hanno qualcosa in comune, per esempio tutti i documenti di una pratica o di un cliente. È un raggruppatore leggero: ha un identificativo, un nome, una descrizione e un eventuale contatto. L'inserimento dei documenti nei dossier si configura nella classe documentale.

**Parametri con l'iniziale maiuscola.** Alcune chiamate usano parametri con l'iniziale maiuscola (`InstanceId`, `Model`, `Name`): in questa pagina sono riportati così come appaiono nello Swagger.

**Errori.** Le chiamate SearchDocuments, DownloadDocument, DownloadDocumentJSON, DocumentVersions e DocumentSets non restituiscono `result` e `message`: segnalano gli errori con il codice HTTP (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`).

## Contenuto del documento

Le chiamate che creano o aggiornano un documento ricevono il contenuto del file in una di due forme, indicata da `sourceType`:

| `sourceType` | Oggetto da valorizzare | Campi |
|---|---|---|
| `base64` | `base64Source` | `extension` (estensione del file), `content` (contenuto in base64) |
| `filePath` | `filePathSource` | `extension`, `filePath` (percorso del file), `deleteAfter` (elimina il file dopo l'acquisizione) |

```json
"sourceType": "base64",
"base64Source": { "extension": ".pdf", "content": "<contenuto-in-base64>" }
```

!!! warning "Percorsi di file"
    Con `filePath` è il **server BPM** a leggere il file, ed eventualmente a eliminarlo. Il percorso deve essere raggiungibile dal server e l'account del servizio BPM deve avere i permessi di lettura (e di scrittura, se si usa `deleteAfter`) su quella cartella.

### Versioni e copia firmata

| Campo | Descrizione |
|---|---|
| `newVersion` | Modalità della nuova versione: `new_draft` se la versione caricata è una bozza da approvare, `new_active` se diventa subito la versione attiva del documento. |
| `newVersionNumber` | Numero della nuova versione, secondo le regole di numerazione che ci si dà. |
| `newVersionDescription` | Descrizione libera della versione. |
| `newVersionDate` | Data della versione, nel formato `yyyy-mm-dd`. |
| `signedCopy` | `true` se il file caricato è la **copia firmata** del documento: un file aggiuntivo conservato accanto all'originale, per le classi documentali che la prevedono. |

## CreateNewDocument

Crea un nuovo documento in una classe documentale.

`POST /api/ext/CreateNewDocument`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "FATTURE PASSIVE",
  "startObject": "start1",
  "variables": { "Fornitore": "Rossi S.p.A.", "Numero": "123", "Anno": "2026" },
  "sourceType": "base64",
  "base64Source": { "extension": ".pdf", "content": "<contenuto-in-base64>" }
}
```

| Campo | Descrizione |
|---|---|
| `model` | Classe documentale. |
| `startObject` | Start da cui creare il documento. |
| `variables` | Metadati del documento. |
| `attachments` | Allegati, come in [CreateNewProcess](processi.md#allegati-allavvio). |
| `sourceType`, `base64Source`, `filePathSource` | Il file: vedi [Contenuto del documento](#contenuto-del-documento). |
| `barcode` | Codice a barre associato al documento. |

Come per i processi, vengono eseguite formule, validazioni e script collegati alla creazione.

Risposta: `instanceId`, `documentName`, `documentDescription`, `result`, `message`.

Se esiste già un documento con lo stesso nome nella classe documentale, la creazione fallisce: `isDuplicate` vale `true` e `duplicateDocumentName` contiene il nome del documento esistente. Per aggiornarlo in questo caso, usa [CreateOrUpdateDocument](#createorupdatedocument).

## CreateOrUpdateDocument

Crea il documento se non esiste, altrimenti aggiorna quello esistente con lo stesso nome. Accetta gli stessi parametri di [CreateNewDocument](#createnewdocument).

`POST /api/ext/CreateOrUpdateDocument`

In aggiornamento vengono modificati metadati e contenuto; se per la classe documentale è attiva la gestione delle versioni, il nuovo file diventa una nuova versione.

La risposta indica con `created` e `updated` quale delle due operazioni è stata eseguita.

È il comportamento dell'omonima operazione **CreateOrUpdateDocument** disponibile nei processi.

## UpdateDocument

Aggiorna metadati, stato e, facoltativamente, contenuto di un documento esistente.

`POST /api/ext/UpdateDocument`

| Campo | Descrizione |
|---|---|
| `instanceId` oppure `model` + `documentName` | Il documento. |
| `variables` | Metadati da modificare. |
| `resetGroups` | Gruppi da svuotare prima di scrivere le nuove righe. |
| `state` | Stato da impostare. |
| `sourceType`, `base64Source`, `filePathSource` | Nuovo contenuto, facoltativo. |
| `newVersion…`, `signedCopy`, `barcode` | Vedi [Versioni e copia firmata](#versioni-e-copia-firmata). |

Risposta: `instanceId`, `documentName`, `documentDescription`, `result`, `message`.

## UpdateDocumentContent

Sostituisce solo il file di un documento esistente, senza modificarne i metadati.

`POST /api/ext/UpdateDocumentContent`

Parametri: il documento (`instanceId` oppure `model` + `documentName`), il contenuto e, facoltativamente, i dati di versione e `signedCopy`.

## GetDocument

Restituisce i dati di un documento. Funziona come [GetProcess](processi.md#getprocess).

`POST /api/ext/GetDocument`

| Campo | Descrizione |
|---|---|
| `InstanceId` oppure `Model` + `Name` | Il documento. |
| `IncludeVariables` | Metadati da includere: `["*"]` o lista vuota per tutti, oppure i nomi delle variabili. |

La risposta contiene gli stessi campi di GetProcess, compresi `tasks` e `processState`, tranne l'immagine del diagramma. In più:

| Campo | Descrizione |
|---|---|
| `documentDate` | Data del documento, se presente. |
| `documentDueDate` | Data di scadenza, se presente. |
| `documentBarcode` | Codice a barre, se presente. |
| `versions` | Le versioni del documento. |

## SearchDocuments

Cerca documenti per metadati e campi generali.

`POST /api/ext/SearchDocuments`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "Models": ["FATTURE PASSIVE"],
  "Filters": [
    { "Name": "Fornitore", "Value": "Rossi S.p.A." },
    { "Name": "Anno", "ValueIn": ["2025", "2026"] }
  ]
}
```

| Campo | Descrizione |
|---|---|
| `Models` | Obbligatorio. Classi documentali in cui cercare: di solito una sola. Sono considerate solo quelle che l'utente è autorizzato a leggere. |
| `Filters` | Filtri facoltativi: `Name` (nome della variabile o di un [campo generale](index.md#campi-generali), per esempio `fix_documentdate`), `Value` (valore singolo) oppure `ValueIn` (elenco di valori ammessi). |
| `dossierType` | Limita la ricerca ai documenti di un tipo di dossier. |

La risposta è un elenco con le informazioni principali di ogni documento: nome, descrizione, data, utente e metadati.


## DownloadDocument

Scarica il file di un documento.

`POST /api/ext/DownloadDocument`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "InstanceId": "<id-istanza>",
  "Version": 2
}
```

`Version` è facoltativo: permette di scaricare una versione precedente, se per la classe documentale è attivo il salvataggio delle versioni.

La risposta è direttamente il file, con il nome nell'intestazione `Content-Disposition`. L'utente deve avere il diritto di leggere i dati del documento.


## DownloadDocumentJSON

Come [DownloadDocument](#downloaddocument), ma restituisce il file dentro un oggetto JSON:

`POST /api/ext/DownloadDocumentJSON`

| Campo | Descrizione |
|---|---|
| `FileName`, `Extension` | Nome ed estensione del file. |
| `FileData` | Contenuto del file in base64. |
| `Version`, `VersionDate`, `VersionUser` | Versione scaricata, data e utente che l'ha caricata. |

## DocumentVersions

Restituisce l'elenco delle versioni di un documento (`InstanceId` oppure `Model` + `Name`). L'utente deve avere il diritto di leggere i dati del documento.

`POST /api/ext/DocumentVersions`


## DeleteDocument

Elimina un documento (`InstanceId` oppure `Model` + `Name`), con le sue versioni e i suoi dati. Valgono i diritti dell'utente indicato.

`POST /api/ext/DeleteDocument`

Risposta: `result` e `message`.

## DocumentSets

Restituisce l'elenco delle classi documentali configurate e attive, con `Name` e `Description`. Richiede solo le credenziali. Stessa struttura di [ProcessModels](processi.md#processmodels).

`POST /api/ext/DocumentSets`

## AddDocumentToDossier

Inserisce un documento in un dossier. Se il dossier non esiste, viene creato.

`POST /api/ext/AddDocumentToDossier`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "InstanceId": "<id-istanza>",
  "Dossier": {
    "Type": "PRATICA",
    "ID": 0,
    "Name": "Pratica 2026/045",
    "Description": "Pratica cliente Rossi",
    "Contact": "",
    "Company": ""
  }
}
```

| Campo | Descrizione |
|---|---|
| `InstanceId` oppure `Model` + `DocumentName` | Il documento. |
| `Dossier.Type` | Obbligatorio. Tipo di dossier. |
| `Dossier.ID`, `Dossier.Name` | Identificano il dossier. |
| `Dossier.Description`, `Dossier.Contact`, `Dossier.Company` | Dati descrittivi facoltativi. |

Una volta nel dossier, il documento si trova sia dall'interfaccia sia con [SearchDocuments](#searchdocuments).

Risposta: `result` e `message`.
