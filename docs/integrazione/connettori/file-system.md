# File System

Il connettore **File System** (`FileSystemConnector`) collega BPM alle cartelle del file system:

- l'evento **IncomingFile**, usato con uno [Start su evento](../../modelli-di-processo/elementi/eventi.md#start-su-evento), avvia un processo per ogni file che arriva in una cartella;
- l'operazione **SaveAttachmentToFileSystem**, usata con un [Connettore attivo](../../modelli-di-processo/elementi/operazioni/index.md#connettore-attivo), salva su file system un file, un allegato, un report o un contenuto base64.

## Usi tipici

- **Acquisizione di documenti da cartella**: uno scanner o un altro sistema deposita i file in una cartella condivisa. BPM è in ascolto sulla cartella indicata in `SourceFilePath` e avvia un processo per ogni file. I parametri di uscita dell'evento (nome, estensione, date, dimensione, percorso completo) finiscono nelle variabili del processo fin dall'avvio, e le attività successive li usano per allegare il file, leggerne il contenuto, smistarlo.
- **Consegna di file a un altro sistema**: al termine di un processo, BPM salva il documento approvato o un report in una cartella da cui l'altro sistema lo preleva.

!!! warning "Permessi sulle cartelle"
    Le cartelle vengono lette e scritte dal **servizio di BPM** sul server. L'account del servizio deve avere i permessi necessari sui percorsi configurati, compresi quelli di rete.

## Riferimento

--8<-- "snippets/connettori/filesystem.md"
