# Esegui SQL

**Esegui SQL** è un'operazione nativa di BPM che esegue un'istruzione SQL su una [connessione esterna](connessioni-esterne.md). Si usa soprattutto per **scrivere** su un altro sistema, ma può eseguire qualunque istruzione: `UPDATE`, `INSERT`, query con join, stored procedure.

Caso tipico: al termine dell'approvazione, scrivere nell'ERP che l'ordine è stato approvato, da chi e quando.

## Parametri

I parametri dell'istruzione, indicati con `@`, si collegano alle variabili del processo:

- **parametri di ingresso**: il valore viene preso dalla variabile;
- **parametri di uscita**: il valore restituito dall'istruzione viene scritto nella variabile.

```sql
UPDATE ordini
SET stato = 'APPROVATO', approvato_da = @utente, data_approvazione = @data
WHERE id_ordine = @idOrdine
```

Qui `@utente`, `@data` e `@idOrdine` sono parametri di ingresso collegati alle variabili del processo.

## Quando usarla

- Il sistema esterno accetta scritture dirette sul suo database, oppure espone stored procedure pensate per l'integrazione.
- Non esiste un servizio web o un connettore dedicato per quella scrittura.

Se il sistema esterno espone API, preferisci chiamarle con il connettore [Web Service](connettori/web-service.md): le API applicano le regole del sistema, una scrittura diretta sul database no.

!!! warning "Errori nelle operazioni"
    Se l'istruzione non è corretta, l'operazione fallisce, e con lei l'azione che l'ha eseguita: per esempio l'avvio del processo, anche quando arriva dalle [API standard](api-standard/index.md) o dalla [coda delle chiamate](coda-chiamate.md). Prova sempre le istruzioni prima di pubblicare il modello.
