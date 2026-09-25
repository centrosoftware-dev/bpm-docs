# Coda delle chiamate

In alternativa alla chiamata diretta delle [Web API](index.md), un sistema esterno può **accodare** le richieste in una tabella del database di BPM, la tabella `chiamateapi`. Un servizio di BPM legge la coda, esegue ogni richiesta chiamando le Web API e scrive il risultato nella stessa tabella.

## Come funziona

1. Il sistema esterno inserisce un record nella tabella `chiamateapi`, con la chiamata da eseguire e il relativo contenuto JSON. Per facilitare l'inserimento sono disponibili apposite stored procedure.
2. Il servizio di BPM rileva il nuovo record ed esegue la chiamata alle Web API.
3. L'esito della chiamata, positivo o con il messaggio di errore, viene scritto nel record.
4. Il sistema esterno legge l'esito dal record, dopo qualche secondo.

Le chiamate accodate seguono le stesse regole delle chiamate dirette: stesse [credenziali](autenticazione.md), stessi parametri, stessi controlli.

## Chiamata diretta o coda?

| | Chiamata diretta | Coda delle chiamate |
|---|---|---|
| Come | Richiesta HTTP alle Web API | Inserimento di un record in una tabella |
| Esito | Immediato, nella risposta | Asincrono: si legge nel record dopo qualche secondo |
| Errori di validazione | Il chiamante li riceve subito e può reagire | Vanno letti in un secondo momento |
| Adatta quando | Il chiamante deve sapere subito se l'operazione è riuscita | Il sistema esterno scrive facilmente su database (per esempio da trigger o stored procedure) ma non gestisce chiamate HTTP, oppure non deve restare in attesa |

La differenza conta soprattutto per le chiamate che applicano molte regole, come [CreateNewProcess](processi.md#createnewprocess) ed [ExecTask](attivita.md#exectask): con la chiamata diretta un errore di validazione torna subito al chiamante; con la coda il sistema esterno deve prevedere di rileggere l'esito e gestire gli errori a posteriori.

## Attivazione

La coda si attiva nei parametri di sistema, scheda **Engine/automatismi**:

- **Attiva esecuzione chiamate api da tabella "chiamateapi"**: abilita il servizio che elabora la coda;
- **url api**: l'indirizzo delle Web API che il servizio chiama.

