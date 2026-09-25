# Autenticazione e utenti

Le Web API usano un sistema a **chiave API**: ogni applicazione esterna riceve una chiave generata in BPM e la invia a ogni chiamata, insieme all'indicazione dell'utente per conto del quale opera.

## Chiave API

La chiave si genera in BPM dal percorso **Configurazione > Configurazione > Chiavi di accesso Web API**, con il comando **Crea nuovo token di autenticazione**. Vedi [Chiavi di accesso Web API](../../../amministrazione/altre-opzioni/chiavi-api-inbound.md).

- Genera una chiave distinta per ogni applicazione esterna, con una descrizione che la identifichi: così è possibile revocarla senza toccare le altre integrazioni.
- Un'applicazione in possesso di una chiave è autorizzata a eseguire **qualunque operazione per conto di qualunque utente**. La chiave va quindi custodita come una password: mai nel codice lato browser, mai in chiaro in documenti condivisi.
- Usa sempre connessioni HTTPS.

## Utente per conto del quale si opera

Ogni chiamata indica anche un utente. BPM applica i controlli di quell'utente: se l'utente non ha il diritto di avviare un processo o di eseguire un'attività, la chiamata fallisce.

Esistono due modi, entrambi validi, per inviare chiave e utente.

### Modalità semplice: `authenticationToken` e `userName`

Chiave e utente BPM si inseriscono direttamente nel corpo della richiesta:

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI"
}
```

È la modalità più diretta quando l'applicazione esterna conosce i nomi degli utenti BPM.

### Modalità con utente esterno: oggetto `authorization`

Quando l'applicazione esterna ha i propri utenti, può identificarli con **il proprio nome utente** e lasciare che sia BPM a risalire all'utente BPM corrispondente. Chiave e utente si inseriscono nell'oggetto `authorization`:

```json
{
  "authorization": {
    "authenticationToken": "<chiave-api>",
    "<tipo>User": "<utente-esterno>",
    "<tipo>Company": "<azienda>"
  },
  "model": "APPROVAZIONE CONTRATTI"
}
```

- `authenticationToken` (oppure `apiKey`): la chiave API, come nella modalità semplice.
- `<tipo>User`: il nome utente nell'applicazione esterna. Il prefisso `<tipo>` indica di quale applicazione si tratta, per esempio `samUser` per un utente di tipo `sam`.
- `<tipo>Company`: l'azienda dell'utente esterno, solo quando l'applicazione esterna gestisce più aziende (per esempio `samPortalUser` e `samPortalCompany` per un utente di tipo `samPortal`).

Se nella richiesta è presente anche `userName`, fuori dall'oggetto `authorization`, prevale l'utente BPM indicato e l'alias non viene usato.

!!! warning "Lo Swagger non descrive questa struttura"
    Nello Swagger `authorization` compare come oggetto generico: i nomi delle proprietà sono quelli riportati in questa pagina.

### Alias: il collegamento tra utente esterno e utente BPM

La corrispondenza tra utente esterno e utente BPM si configura nell'anagrafica degli utenti BPM, sezione **Alias**. Per ogni utente BPM si definiscono uno o più alias, ciascuno composto da:

- il **tipo** di utente esterno, cioè l'applicazione di provenienza (per esempio `sam`);
- il **nome utente** in quell'applicazione.

Quando una chiamata arriva con `samUser: "7"`, BPM cerca l'utente che ha un alias di tipo `sam` con nome `7` e opera per suo conto. Se la chiamata indica anche l'azienda (`samCompany`), la ricerca considera tipo, nome e azienda; senza azienda, basta la coppia tipo e nome. Se nessun alias corrisponde, la chiamata fallisce come per un utente inesistente.

Vedi [Utenti e gruppi](../../../amministrazione/utenti-e-gruppi/index.md).

La stessa struttura si usa anche in altri punti delle API per indicare un utente esterno, per esempio nel filtro `filterByUser` di [GetTodolist](attivita.md#gettodolist) o negli utenti assegnati di [UpdateTask](attivita.md#updatetask).

## Verificare un utente

La chiamata [GetUser](utilita.md#getuser) verifica che l'utente indicato esista e ne restituisce email e gruppi: è utile per controllare la configurazione di chiave e alias prima di usare le altre chiamate.
