# Web Service

Il connettore **Web Service** (`Web Service Connector`) permette a un processo di chiamare le API REST di un altro sistema: un CRM, un ERP, un servizio di terze parti.

Offre due operazioni:

- **Web API**: la chiamata si descrive con la sola configurazione: indirizzo, metodo HTTP e autenticazione. Il codice di stato della risposta viene scritto in una variabile.
- **Web API [Script]**: la chiamata si descrive con uno script in Visual Basic, con la stessa sintassi delle [formule](../../parti-comuni/formule-e-script/index.md). Serve quando la chiamata richiede logica: costruire il corpo della richiesta dalle variabili, interpretare la risposta, gestire autenticazioni a più passaggi o più chiamate in sequenza.

## Usi tipici

- Creare o aggiornare un record in un CRM quando un'offerta viene approvata.
- Notificare a un altro sistema la conclusione di un processo.
- Leggere dati da un servizio esterno e scriverli nelle variabili.

L'operazione si inserisce nel flusso, per esempio sul ramo *approvata* dopo un gateway, oppure si aggancia alla conclusione di un'attività.

## Riferimento

--8<-- "snippets/connettori/webservice.md"
