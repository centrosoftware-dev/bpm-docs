# Mail

Il connettore **Mail** (`Mail Connector`) permette a BPM di ricevere e interpretare messaggi di posta:

- l'evento **IncomingMail**, usato con uno [Start su evento](../../modelli-di-processo/elementi/eventi.md#start-su-evento), avvia un processo per ogni mail che arriva in una cartella di una casella IMAP;
- l'operazione **ExtractMail**, usata con un [Connettore attivo](../../modelli-di-processo/elementi/operazioni/index.md#connettore-attivo), estrae i dati da un file `.eml` o `.msg`, per esempio una mail allegata a un processo.

## Usi tipici

- **Richieste via mail**: ogni mail arrivata a un indirizzo dedicato (ordini, reclami, fatture) avvia un processo. Mittente, oggetto, testo e data diventano variabili del processo; gli allegati vengono archiviati tra gli allegati del processo, anche filtrandoli per tipo (per esempio solo i PDF).
- **Gestione della casella**: dopo la ricezione, la mail può essere eliminata o spostata in un'altra cartella, così la casella resta ordinata.
- **Risposte collegate**: il parametro `ReferenceInstanceId` riconosce il riferimento a un'istanza BPM presente nella mail, utile per collegare la risposta al processo che l'ha generata.

Nei parametri di ingresso dell'evento si indicano la configurazione della casella da usare (`ConfigEmail`, definita a parte in BPM), la cartella da monitorare e cosa fare della mail dopo la lettura. I parametri di uscita (mittente, destinatari, oggetto, testo, data, allegati) finiscono nelle variabili del processo avviato.

## Riferimento

--8<-- "snippets/connettori/mailconnector.md"
