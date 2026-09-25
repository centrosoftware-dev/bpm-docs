# Utilità

## GetUser

Verifica che un utente esista e ne restituisce i dati principali. È utile per controllare chiave API e [alias](autenticazione.md#alias-il-collegamento-tra-utente-esterno-e-utente-bpm) prima di usare le altre chiamate.

`POST /api/ext/GetUser` (disponibile anche in `GET`, con i parametri nella query string)

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi"
}
```

Oppure, con un utente esterno:

```json
{
  "authorization": {
    "authenticationToken": "<chiave-api>",
    "samUser": "7"
  }
}
```

**Risposta**

```json
{
  "result": true,
  "userName": "mrossi",
  "email": "mario.rossi@azienda.it",
  "isExternal": false,
  "groups": ["Amministrazione", "UTE"]
}
```

- `userName`: il nome dell'utente BPM, anche quando la richiesta indicava un utente esterno.
- `isExternal`: `true` per gli utenti di collaborazione esterna, per esempio i fornitori.
- `groups`: i gruppi a cui l'utente appartiene.

Se l'utente non esiste, `result` è `false` e `message` contiene l'errore.

## CreateOrUpdateUser

Crea un utente BPM oppure aggiorna un utente esistente.

`POST /api/ext/CreateOrUpdateUser`

L'utente indicato in `userName` è quello che esegue l'operazione e deve avere il diritto di gestire utenti e autorizzazioni.

| Campo | Descrizione |
|---|---|
| `targetUserName` | Nome dell'utente da creare o aggiornare. |
| `password` | Password. |
| `email`, `description` | Email e descrizione. |
| `isExternal` | Utente di collaborazione esterna. |
| `passwordExpired` | Password scaduta: l'utente dovrà cambiarla al primo accesso. |
| `singleSignOn` | Accesso con autenticazione di dominio. |
| `systemUserName`, `domain` | Utente di sistema e dominio, per l'accesso con autenticazione di dominio. |
| `groups` | Gruppi a cui l'utente appartiene. |

Risposta: `result`, `message`, `userName` e `created` (`true` se l'utente è stato creato, `false` se aggiornato).


## GetVersion

Restituisce la versione dell'applicazione. Disponibile in `GET` e in `POST`, senza parametri né chiave API: è utile per verificare che le API siano raggiungibili.

`GET /api/ext/GetVersion`

```json
{ "version": "2026.7.3" }
```
