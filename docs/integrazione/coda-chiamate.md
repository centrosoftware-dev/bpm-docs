# Coda delle chiamate

La coda delle chiamate è una **porta d'ingresso alternativa** alle [API standard](api-standard/index.md), pensata per i casi in cui il sistema esterno non può chiamare le API ma può scrivere sul database.

!!! info "Un'alternativa, non un'altra API"
    La strada principale per integrare un'applicazione esterna è la chiamata diretta alle [API standard](api-standard/index.md). La coda serve quando questa non è praticabile: software che lavorano solo sul database, trigger, stored procedure, situazioni in cui serve interagire con BPM rapidamente senza una programmazione più strutturata.

Invece di chiamare le API, il sistema esterno **inserisce una riga** nella tabella `ChiamateAPI` del database di BPM. Un servizio di BPM legge la coda, esegue la chiamata corrispondente e scrive l'esito nella stessa riga.

## Come funziona

1. Il sistema esterno inserisce una riga in `ChiamateAPI` con il nome della chiamata e i parametri in JSON.
2. Il servizio di BPM, che controlla la coda ogni pochi secondi, prende in carico la riga ed esegue la chiamata.
3. L'esito viene scritto nella riga: risposta completa, esito sintetico ed eventuale messaggio di errore.
4. Il sistema esterno, se gli serve, rilegge l'esito qualche secondo dopo.

Le chiamate accodate seguono le stesse regole delle chiamate dirette: stesse [credenziali](api-standard/autenticazione.md), stessi parametri, stessi controlli.

## La tabella `ChiamateAPI`

| Colonna | Chi la scrive | Contenuto |
|---|---|---|
| `Funzione` | Sistema esterno | Nome della chiamata, per esempio `CreateNewProcess` o `ExecTask`. |
| `Parametri` | Sistema esterno | Il corpo JSON della chiamata, credenziali comprese. |
| `Data` | Sistema esterno | Data e ora di inserimento. |
| `EseguitoInData` | BPM | Data e ora in cui BPM ha elaborato la riga. Vuota finché la richiesta è in coda. |
| `Response` | BPM | La risposta JSON della chiamata, con `result` e `message`. |
| `Risultato` | BPM | Esito sintetico: `OK` oppure `KO`. |
| `ErrorMessage` | BPM | In caso di `KO`, il messaggio di errore, ripreso da `message`. |

Inserimento diretto:

```sql
INSERT INTO ChiamateAPI (Funzione, Parametri, Data)
VALUES ('ExecTask',
        '{"authorization": {"authenticationToken": "<chiave-api>", "samUser": "2"},
          "model": "APPROVAZIONE ODA", "instanceId": "<id-istanza>", "activity": "Activity3"}',
        GETDATE())
```

## Leggere l'esito

Una riga elaborata ha `EseguitoInData` valorizzata. Se `Risultato` è `KO`, `ErrorMessage` spiega il motivo. Può trattarsi di:

- **un controllo di BPM**: nome di processo già esistente, variabile obbligatoria mancante, validazione non superata, processo non trovato…;
- **un errore delle configurazioni eseguite dalla chiamata**, per esempio una query SQL errata in un'operazione collegata allo start del processo.

Esempi di righe elaborate (colonne principali):

| Funzione | Risultato | ErrorMessage |
|---|---|---|
| `ExecTask` | `OK` | |
| `CreateNewProcess` | `KO` | `Nome processo già esistente: "Sollecito Ordine ID 31"` |
| `UpdateProcess` | `KO` | `Process Not Found: 2024 - 2 - CONTROLLO FATTURE PASSIVE` |

Con la coda gli errori non tornano al chiamante nel momento dell'inserimento: se il sistema esterno deve reagire a un errore, deve rileggere la riga.

## Chiamata diretta o coda?

| | Chiamata diretta | Coda delle chiamate |
|---|---|---|
| Come | Richiesta HTTP alle API standard | Inserimento di una riga in una tabella |
| Esito | Immediato, nella risposta | Asincrono: si legge nella riga dopo qualche secondo |
| Errori di validazione | Il chiamante li riceve subito | Vanno riletti in un secondo momento |
| Adatta quando | Il chiamante deve sapere subito se l'operazione è riuscita | Il sistema esterno scrive facilmente su database ma non gestisce chiamate HTTP, oppure non deve restare in attesa |

## Attivazione

La coda si attiva nei parametri di sistema, scheda **Engine/automatismi**:

- **Attiva esecuzione chiamate api da tabella "chiamateapi"**: abilita il servizio che elabora la coda;
- **url api**: l'indirizzo delle API standard che il servizio chiama.

## Stored procedure per l'inserimento

Per evitare di comporre il JSON a mano, sono disponibili stored procedure che ricevono pochi parametri, costruiscono il JSON e inseriscono la riga in coda.

### BPM_CreateNewProcess

Accoda l'avvio di un processo.

```sql
EXEC BPM_CreateNewProcess
     @user = '2',
     @model = 'APPROVAZIONE ODA',
     @externalID = '1234',
     @externalTable = '',
     @externalCompany = 'A1',
     @startObject = ''
```

| Parametro | Descrizione |
|---|---|
| `@user` | Utente esterno per conto del quale si avvia il processo, risolto tramite gli [alias](api-standard/autenticazione.md#alias-il-collegamento-tra-utente-esterno-e-utente-bpm). |
| `@model` | Modello di processo da avviare. |
| `@externalID` | Identificativo del record esterno da cui nasce il processo. |
| `@externalTable` | Tabella o tipo del record esterno, facoltativo. |
| `@externalCompany` | Azienda del record esterno, facoltativa. |
| `@startObject` | Start da cui avviare il processo; vuoto per lo start predefinito. |

La chiave API viene letta dalla configurazione di BPM: chi scrive il trigger non deve gestirla.

La procedura non restituisce mai errori: se l'inserimento in coda non riesce, l'operazione del sistema chiamante prosegue comunque. È una scelta voluta: usata in un trigger, un errore bloccherebbe l'elaborazione del sistema esterno.

### La convenzione EXTERNAL ID

La stored procedure non passa i dati del processo, ma solo il **riferimento** al record esterno, nelle variabili `EXTERNAL ID`, `EXTERNAL TABLE` ed `EXTERNAL COMPANY`. Il modello di processo deve quindi avere queste tre variabili.

Sarà poi il processo, all'avvio, a recuperare da solo gli altri dati che gli servono, con query o connettori configurati sullo start. Per esempio, per un processo di approvazione di un ordine d'acquisto basta passare l'ID dell'ordine: fornitore, numero, righe e importo vengono letti da BPM.

I vantaggi:

- il trigger sul sistema esterno resta di poche righe e non deve comporre JSON;
- la logica di recupero dei dati si configura in BPM, con gli strumenti grafici del Designer, e si modifica senza toccare il sistema esterno.
