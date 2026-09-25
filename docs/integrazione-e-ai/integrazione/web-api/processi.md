# Processi

Chiamate per avviare, leggere, modificare ed eliminare le istanze di processo, e per caricare allegati. Per le regole comuni (indirizzo, credenziali, identificazione dell'istanza, variabili) vedi [Web API](index.md).

## CreateNewProcess

Avvia una nuova istanza di un modello di processo.

`POST /api/ext/CreateNewProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "startObject": "start1",
  "variables": {
    "Ragione Sociale": "Rossi S.p.A.",
    "Importo": 179.58
  }
}
```

| Campo | Descrizione |
|---|---|
| `model` | Nome del modello di processo da avviare. |
| `startObject` | Nome interno dello start da cui avviare il processo (per esempio `start1`). Un modello può avere più start. |
| `variables` | Valori delle variabili richieste all'avvio. |
| `attachments` | Elenco facoltativo di allegati da caricare all'avvio. Vedi sotto. |

### Allegati all'avvio

Ogni elemento di `attachments` descrive un allegato:

| Campo | Descrizione |
|---|---|
| `fileName` | Nome del file. |
| `content` | Contenuto del file codificato in base64. |
| `root`, `folder` | Cartella allegati del processo in cui inserire il file. È una cartella virtuale di BPM, non una cartella del file system. |
| `group` | Gruppo di allegato, tra i valori previsti nelle tabelle di BPM. |
| `isEmail` | Se `true`, il file è un messaggio email: BPM ne estrae oggetto, mittente e le altre informazioni e le conserva per eventuali elaborazioni. |

Vengono eseguite formule, validazioni, controlli di obbligatorietà e script collegati all'avvio, e viene verificato che l'utente possa avviare il processo da quello start.

**Risposta**

```json
{
  "documentName": "P004A.19.1",
  "instanceId": "<id-istanza>",
  "documentDescription": "…",
  "isDuplicate": false,
  "result": true,
  "message": null
}
```

`documentName` è il nome dell'istanza creata, univoco all'interno del modello. Conserva `instanceId` o `documentName` per le chiamate successive.

Se il modello calcola un nome già esistente, la creazione fallisce: `isDuplicate` vale `true` e `duplicateDocumentName` contiene il nome dell'istanza esistente.

## GetProcess

Restituisce lo stato di avanzamento di un'istanza e, a richiesta, le sue variabili.

`POST /api/ext/GetProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "documentName": "P004A.19.1",
  "includeVariables": ["*"],
  "includeGraph": true
}
```

`includeVariables` stabilisce quali variabili riportare nella risposta:

- `["*"]` oppure lista vuota: tutte le variabili;
- uno o più nomi: solo le variabili indicate.

Con `includeGraph: true` la risposta contiene anche l'immagine del diagramma, con i colori di avanzamento: la stessa che vede l'utente in BPM. Un'applicazione esterna può usarla per mostrare ai propri utenti a che punto è il flusso.

**Risposta**

```json
{
  "model": "RECLAMO",
  "documentName": "2/2026",
  "instanceId": "667cedef-4562-…",
  "state": "PRESO IN CARICO",
  "variables": {
    "ANNO": 2026.0,
    "DATA APERTURA": "2026-03-16T00:00:00+01:00",
    "CREA NC": false,
    "NOTE": { "HTML": "<p>Da valutare</p>", "Text": "Da valutare" },
    "ATTIVITA": [ { "DESCRIZIONE": "Verifica del lotto", "SCADENZA": "20/03/2026" } ],
    …
  },
  "activeTasks": [
    { "activity": "Activity5", "activityDescription": "ORDINE DI SOSTITUZIONE", "userName": "DIRTEC", … }
  ],
  "tasks": {
    "Activity1": { "taskDescription": "PRESA IN CARICO", "state": "Done", "executionCount": 2, … },
    "Activity5": { "taskDescription": "ORDINE DI SOSTITUZIONE", "state": "Active", … },
    …
  },
  "processState": { … },
  "links": [],
  "result": true,
  "message": ""
}
```

Come si leggono le variabili:

- **numeri**: sempre in formato decimale (`2026.0`);
- **date**: formato ISO con fuso orario (`2026-03-16T00:00:00+01:00`);
- **booleani**: `true` / `false`;
- **testo esteso (Memo)**: oggetto con `Text`, il testo semplice, e `HTML`, la versione formattata;
- **gruppi**: array con una riga per elemento.

Come si legge `tasks`: una voce per ogni oggetto del diagramma (attività, stati, gateway, operazioni), identificata dal nome interno.

- `state`: `None` (non ancora raggiunto), `Active` (in corso), `Done` (completato);
- `executionCount`: quante volte l'oggetto è stato eseguito;
- `assignedUsers`, `ccUsers`: assegnatari e utenti in copia;
- date e durate di pianificazione: prevista (`…Plan`), aggiornata (`…Upd`) ed effettiva (`…Actual`);
- `operations`: per le operazioni automatiche, se sono state eseguite, quando, da quale utente ed eventuale errore (`errorText`).

| Campo | Descrizione |
|---|---|
| `documentName`, `documentDescription`, `instanceId` | Identificazione dell'istanza. |
| `documentText` | Testo descrittivo dell'istanza. |
| `state` | Stato corrente del processo. |
| `variables` | Le variabili richieste. I gruppi sono restituiti come array di righe. Vedi anche i [campi generali](index.md#campi-generali). |
| `activeTasks` | Le attività attive: nome interno (`activity`), descrizione, assegnatari in `userName` (separati da `;`) e in `assignedUsers`, con gli eventuali alias dell'applicazione esterna. |
| `links` | Le istanze collegate. |
| `tasks` | Lo stato di tutte le attività del processo, una voce per attività con il suo nome interno. |
| `processState` | Dettagli operativi sull'avanzamento generale del processo. |
| `graph` | Solo con `includeGraph`: immagine PNG del diagramma, codificata in base64. |

Viene sempre verificato che l'utente abbia il diritto di accedere ai dati richiesti.

## UpdateProcess

Modifica le variabili di un'istanza esistente e, facoltativamente, ne forza lo stato.

`POST /api/ext/UpdateProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "variables": { "Importo": 200.00 },
  "resetGroups": ["Righe"],
  "state": ""
}
```

| Campo | Descrizione |
|---|---|
| `variables` | Variabili da modificare. |
| `resetGroups` | Gruppi da svuotare prima di scrivere le nuove righe passate in `variables`. |
| `state` | Stato da impostare. Vuoto per non cambiare lo stato. |

Viene verificato che l'utente abbia il diritto di modificare le variabili e di cambiare stato. Per lo stato, il controllo dipende da come lo stato è raggiungibile: cambio di stato libero oppure secondo il flusso del processo.

## DeleteProcess

Elimina un'istanza di processo, identificata da `instanceId` oppure da `model` + `documentName`.

`POST /api/ext/DeleteProcess`

L'eliminazione è completa: vengono rimossi l'istanza, le sue attività nella To-Do List, gli allegati e le variabili. Come per ogni chiamata, valgono i diritti dell'utente indicato: può eliminare un amministratore o un utente autorizzato a eliminare le istanze del modello.

Risposta: `result` e `message`.

## UploadAttachment

Inserisce un allegato in un'istanza di processo, oppure aggiorna un allegato esistente.

`POST /api/ext/UploadAttachment`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "fileName": "Contratto 123.pdf",
  "fileDescription": "Contratto firmato",
  "root": "ALLEGATI",
  "path": "\\Documenti Amministrativi",
  "content": "<contenuto-in-base64>",
  …
}
```

La combinazione di `fileName`, `root`, `path` e `revision` identifica l'allegato: se esiste già viene aggiornato, altrimenti viene creato. In aggiornamento `content` può restare vuoto, per modificare solo descrizione, gruppo, tipo o variabili.

| Campo | Descrizione |
|---|---|
| `fileName`, `fileDescription` | Nome e descrizione registrati in BPM. |
| `root`, `path` | Percorso di archiviazione all'interno del processo. Valgono sia per gli allegati salvati su database sia per quelli su file system. |
| `group`, `type` | Gruppo e tipo di allegato, facoltativi, tra i valori previsti nelle tabelle di BPM. |
| `revision` | Revisione dell'allegato, se necessaria. |
| `state` | Vuoto: allegato attivo e modificabile. `A`: approvato, non più modificabile. `O`: obsoleto, non più modificabile. |
| `variables` | Variabili **dell'allegato**, non del processo. |
| `content` | Contenuto del file codificato in base64. |

In alternativa a `content`, il contenuto si può fornire con `sourceType` e `filePathSource` o `base64Source`: vedi [Documenti e dossier](documenti.md#contenuto-del-documento).

## AddLink

Collega due istanze di processo.

`POST /api/ext/AddLink`

Ciascuna delle due istanze si identifica con l'id oppure con modello e nome, in qualunque combinazione:

| Campo | Descrizione |
|---|---|
| `instanceId` oppure `model` + `documentName` | L'istanza di partenza. |
| `linkedInstanceId` oppure `linkedModel` + `linkedDocumentName` | L'istanza da collegare. |

L'utente deve essere amministratore oppure avere, sul modello dell'istanza di partenza, il diritto di aggiungere istanze collegate.

Risposta: `result` e `message`.


## ProcessModels

Restituisce l'elenco dei modelli di processo configurati e attivi. Richiede solo le credenziali.

`POST /api/ext/ProcessModels`

**Risposta**

```json
[
  { "Name": "APPROVAZIONE CONTRATTI", "Description": "Approvazione dei contratti di vendita" },
  { "Name": "RICHIESTA INV", "Description": "Richiesta di autorizzazione investimento" }
]
```

La risposta è direttamente l'elenco, senza `result` e `message`. Se la chiave API non è valida, la chiamata restituisce il codice HTTP `401 Unauthorized`.

Per l'elenco delle classi documentali vedi [DocumentSets](documenti.md#documentsets).

## GetSchema

Restituisce la descrizione delle variabili richieste per avviare un processo o per eseguire un'attività. È utile per costruire dinamicamente la maschera di un'applicazione esterna.

Richiede solo la chiave API: la descrizione non dipende dall'utente.

`POST /api/ext/GetSchema`

```json
{
  "authenticationToken": "<chiave-api>",
  "modelName": "INTERVENTI PARCO AUTO",
  "activityName": "start1"
}
```

**Risposta**

```json
{
  "result": true,
  "model": "INTERVENTI PARCO AUTO",
  "activity": "start1",
  "properties": [
    { "propertyName": "TARGA MEZZO", "propertyType": "string", "variableType": "StringType", "required": true },
    { "propertyName": "RICHIEDENTE", "propertyType": "string", "variableType": "UserType", "hasDefault": true },
    {
      "propertyName": "INTERVENTI", "propertyType": "array",
      "subProperties": [
        { "propertyName": "PREZZO", "propertyType": "number", "variableType": "NumericType" },
        …
      ]
    },
    …
  ]
}
```

| Attributo | Descrizione |
|---|---|
| `propertyName` | Nome della variabile. |
| `propertyType` | Tipo JSON: `string`, `number`, `date`, `boolean`, `array`. |
| `variableType` | Tipo della variabile in BPM (per esempio `StringType`, `NumericType`, `UserType`, `ValueListType`). |
| `required` | La variabile è obbligatoria. |
| `readOnly` | La variabile è visualizzata ma non modificabile nell'attività: valorizzata in un passaggio precedente o calcolata. |
| `hasDefault` | Esiste una formula di default: se la variabile non viene passata, si usa il default. |
| `description` | Descrizione della variabile come appare nell'attività. |
| `availableValues` | Per le liste valori, i valori ammessi. |
| `subProperties` | Per i gruppi (`array`), le variabili del gruppo. |
