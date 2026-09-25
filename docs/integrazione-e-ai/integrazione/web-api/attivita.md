# Attività e To-Do List

Chiamate per leggere la To-Do List di un utente, eseguire un'attività e modificarne assegnazione, priorità e date. Per le regole comuni vedi [Web API](index.md).

## GetTodolist

Restituisce la To-Do List di un utente: le attività visibili o eseguibili, secondo i filtri indicati.

`POST /api/ext/GetTodolist`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "fromDate": "2026-01-01",
  "toDate": "2026-07-31",
  "filterByUser": "Commerciali",
  "filterByText": "",
  "filterByPriority": null,
  "includeCompleted": false,
  "includePlanned": false,
  "includeCC": false
}
```

| Campo | Descrizione |
|---|---|
| `fromDate`, `toDate` | Intervallo di date. Se omesse, nessun limite pratico: dal 1980 a dieci anni nel futuro. |
| `filterByUser` | Utente o gruppo di cui leggere le attività. Può essere anche un utente esterno, con la stessa struttura dell'[oggetto authorization](autenticazione.md#modalita-con-utente-esterno-oggetto-authorization), per esempio `{ "samPortalUser": "14", "samPortalCompany": "A1" }`. Se vuoto, vedi sotto. |
| `filterByText` | Filtro testuale. |
| `filterByPriority` | Filtro per priorità. |
| `includeCompleted` | Include le attività completate. |
| `includePlanned` | Include le attività pianificate, non ancora attive. |
| `includeCC` | Include le attività in cui l'utente è in copia. |

Se `filterByUser` è vuoto, la risposta contiene le attività dell'utente indicato nella richiesta, quelle degli utenti di cui può vedere la To-Do List e quelle non ancora assegnate. Per un amministratore contiene le attività di tutti gli utenti.

Sono considerati solo i modelli attivi.

**Risposta**

```json
{
  "result": true,
  "message": null,
  "todoList": [
    {
      "activityName": "activity12",
      "activityDescription": "FIRMARE ORDINE",
      "instanceID": "<id-istanza>",
      "model": "APPROVAZIONE CONTRATTI",
      "documentName": "P004A.19.1",
      "assignedUsers": [ { "userName": "mrossi", "samUser": "7" } ],
      "state": "active",
      "priority": "high",
      "dueDate": null,
      "processHeaders": [ { "Cliente": "Rossi S.p.A." }, … ],
      "activityLink": "https://<indirizzo-bpm>/todolist?…",
      …
    },
    …
  ]
}
```

- `assignedUsers`: gli assegnatari, ciascuno espresso come utente BPM e, se configurato un alias, come utente dell'applicazione esterna.
- `isCC`: l'attività è in copia per l'utente.
- `state`: `active`, `completed` oppure `planned`.
- `priority`: `suspended`, `none`, `low` (priorità da 1 a 3), `medium` (da 4 a 7) oppure `high` (da 8 a 10).
- `processHeaders`: le intestazioni del processo, cioè l'estratto di variabili che BPM mostra nella To-Do List, come elenco di coppie nome-valore. Presente solo se le intestazioni sono configurate.
- `processHeadersTable`: le stesse intestazioni in forma tabellare, `header1` … `header10`, ciascuna con `name` e `value`.
- `activityLink`, `processLink`: collegamenti diretti all'attività e al processo nell'applicazione web, utili per aprire BPM da un'altra applicazione.

## GetPageTodoList

Come [GetTodolist](#gettodolist), ma restituisce i risultati una pagina alla volta. Ai filtri si aggiungono `Page`, il numero di pagina a partire da `1`, e `Size`, il numero di attività per pagina.

`POST /api/ext/GetPageTodoList`

Oltre a `result`, `message` e `todoList`, la risposta contiene:

| Campo | Descrizione |
|---|---|
| `page`, `size` | Pagina e dimensione richieste. |
| `totalRecords` | Numero totale di attività che soddisfano i filtri. |
| `totalPages` | Numero totale di pagine. |


## ExecTask

Esegue un'attività attiva, facendo avanzare il processo.

`POST /api/ext/ExecTask`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "documentName": "P004A.19.1",
  "activity": "activity4",
  "comments": "",
  "variables": {
    "Esito Approvazione": "APPROVATA"
  }
}
```

| Campo | Descrizione |
|---|---|
| `activity` | Nome **interno** dell'attività, per esempio `activity4`. Si legge nel Designer, nella proprietà **(NOME)** dell'attività: non è il testo visualizzato nel diagramma. |
| `variables` | Valori delle variabili richieste dall'attività. |
| `comments` | Commento all'esecuzione. |

BPM verifica che l'attività sia attiva e presente nella To-Do List dell'utente, e che l'utente abbia il diritto di eseguirla. Poi controlla validazioni e obbligatorietà delle variabili ed esegue gli script collegati all'esecuzione dell'attività. Le righe passate per le variabili di gruppo vengono aggiunte a quelle già presenti.

Errori tipici:

- l'attività indicata non è attiva;
- l'utente non è autorizzato a eseguire l'attività;
- il processo è aperto in modifica da un altro utente in quel momento: la chiamata va ripetuta più tardi;
- una validazione non è superata: `message` riporta il messaggio della validazione.

Risposta: `result` e `message`.

## UpdateTask

Aggiorna i dati di un'attività: assegnatari, priorità, date e durate. Non esegue l'attività.

`POST /api/ext/UpdateTask`

Sono obbligatori solo l'istanza (`instanceId` oppure `model` + `documentName`) e `activityName`. Gli altri campi sono facoltativi: si valorizzano solo quelli da modificare.

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "activityName": "Activity4",
  "assignedUser": { "samUser": "7" },
  "priority": 5,
  "dueDate": "2026-10-31"
}
```

| Campo | Descrizione |
|---|---|
| `assignedUser`, `ccUser`, `respUser` | Assegnatari, utenti in copia e responsabili. Ciascuno può essere un nome utente BPM, un utente esterno con la struttura degli [alias](autenticazione.md#alias-il-collegamento-tra-utente-esterno-e-utente-bpm), oppure un elenco dei due. |
| `priority` | Da 1 a 10. `0`: nessuna modifica. Un valore negativo sospende l'attività. |
| `startDate` | Nuova data di inizio: imposta la data di inizio aggiornata e, se l'attività è già iniziata, anche quella effettiva. |
| `durationDays` | Nuova durata in giorni: equivale a `durationDaysUpdated`. |
| `plannedStartDate`, `updatedStartDate`, `actualStartDate` | Date di inizio pianificata, aggiornata ed effettiva. |
| `durationDaysPlanned`, `durationDaysUpdated` | Durate pianificata e aggiornata. |
| `dueDate` | Data di scadenza. |
| `ignoreCalendar` | Se `true`, l'attività ignora il calendario dei giorni lavorativi. |

Risposta: `result` e `message`.

Vincoli sull'assegnazione:

- se gli assegnatari dell'attività sono definiti da una variabile di processo, non si possono cambiare tramite API;
- se l'attività è assegnata a un gruppo, il nuovo assegnatario deve appartenere a quel gruppo.
