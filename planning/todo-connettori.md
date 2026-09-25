# To do — Connettori

## Descrizioni nei manifesti

Le descrizioni "vere" di connettori, funzioni e parametri stanno nei manifesti (`D:\BPM\Application\Core\Resources\Connectors\WKF.Connectors\*.connector.json`) e da lì finiscono nella documentazione tramite `tools/genera-connettori.py`. Vanno sistemate alla fonte, gradualmente:

- [ ] Uniformare la lingua: oggi le descrizioni sono metà in inglese e metà in italiano, anche nello stesso connettore.
- [ ] Completare le descrizioni mancanti. Esclusi i connettori SAM: 5 funzioni su 52 e 460 parametri su 653 senza descrizione.
- [ ] Web API [Script] (WebService) non ha parametri nel manifesto: tutto passa dallo script, da documentare a mano.

Dettaglio (generato il 25/9/2026):

- [ ] **CreditSafeConnector**
    - `GetDataByPartitaIVA`: 37 parametri su 37 senza descrizione
    - `GetDataByCodiceFiscale`: 37 parametri su 37 senza descrizione
    - `GetDataByPartitaIVA_CA`: 37 parametri su 37 senza descrizione
    - `GetDataByCodiceFiscale_CA`: 37 parametri su 37 senza descrizione
- [ ] **Cs AI Connector**
    - `AI Document Intelligence (Read)`: 10 parametri su 10 senza descrizione
    - `AI Document Intelligence (Layout)`: 8 parametri su 8 senza descrizione
    - `AI Document Intelligence (Invoice)`: 5 parametri su 32 senza descrizione
    - `Update Index`: 5 parametri su 6 senza descrizione
    - `AI Document Intelligence (IDDocuments)`: 18 parametri su 18 senza descrizione
    - `AI Document Intelligence (Contract)`: 16 parametri su 16 senza descrizione
- [ ] **FileSystemConnector**
    - `IncomingFile`: 1 parametri su 8 senza descrizione
    - `SaveAttachmentToFileSystem`: 10 parametri su 10 senza descrizione
- [ ] **Mail Connector**
    - `IncomingMail`: 4 parametri su 22 senza descrizione
    - `ExtractMail`: 3 parametri su 17 senza descrizione
- [ ] **PowerBI Connector**
    - `Embed Report`: funzione senza descrizione
    - `Embed Report`: 2 parametri su 2 senza descrizione
- [ ] **Pdf Connector**
    - `ExtractTextArea`: 7 parametri su 9 senza descrizione
    - `ExtractMarkdown`: 9 parametri su 10 senza descrizione
    - `ExtractTextReadingOrder`: 9 parametri su 10 senza descrizione
    - `ExtractTextAreaImage`: 7 parametri su 9 senza descrizione
    - `ExtractTableStructures`: 10 parametri su 10 senza descrizione
    - `SplitByGroups`: 5 parametri su 5 senza descrizione
    - `ZIPPDFs`: 3 parametri su 3 senza descrizione
- [ ] **Spreadsheet Connector**
    - `LaunchImport`: 6 parametri su 6 senza descrizione
    - `ImportConfigurationsFromFile`: 6 parametri su 6 senza descrizione
    - `ExportDataFromGroups`: 5 parametri su 6 senza descrizione
    - `ExportExcelToMarkdown`: 6 parametri su 6 senza descrizione
    - `ExportExcelToPDF`: 10 parametri su 10 senza descrizione
    - `ExportExcelToImage`: 10 parametri su 10 senza descrizione
    - `LaunchImport [Client]`: 6 parametri su 6 senza descrizione
- [ ] **UtilityConnector**
    - `CreateOrUpdateDocument`: 11 parametri su 23 senza descrizione
    - `UpdateDocument`: 10 parametri su 21 senza descrizione
    - `UpdateDocumentContent`: 9 parametri su 19 senza descrizione
    - `RouteByBarcode`: 7 parametri su 17 senza descrizione
    - `ExtractBarcodes`: 7 parametri su 16 senza descrizione
    - `AddDocumentToDossier`: 7 parametri su 7 senza descrizione
    - `AddLink`: funzione senza descrizione
    - `AddLink`: 6 parametri su 6 senza descrizione
    - `OpenDocument`: 3 parametri su 3 senza descrizione
    - `AddAttachment`: 19 parametri su 23 senza descrizione
    - `SplitByBarcode`: 9 parametri su 29 senza descrizione
    - `CreateOrUpdateDocument [Client]`: 11 parametri su 23 senza descrizione
    - `AddAttachment [Client]`: 15 parametri su 19 senza descrizione
    - `AddLinkedDocument`: funzione senza descrizione
    - `AddLinkedDocument`: 8 parametri su 8 senza descrizione
    - `DeleteAttachment`: funzione senza descrizione
    - `DeleteAttachment`: 3 parametri su 3 senza descrizione
    - `DeleteDocument`: funzione senza descrizione
    - `DeleteDocument`: 6 parametri su 6 senza descrizione

## Comportamenti non descritti dal manifesto

Da documentare a mano nelle pagine, accanto alla parte generata:

- [ ] Gestioni speciali in configurazione: per esempio, all'aggiunta di un parametro, le regole che aiutano a battezzarlo e che in esecuzione sono importanti.
- [ ] Interazione dei connettori con l'ambiente del processo (variabili, allegati, gruppi) caso per caso.
- [ ] Operazioni native del motore (Invia Email, Carica Dati, Esegui SQL): non hanno manifesto, vanno documentate interamente a mano. Esegui Programma resta fuori dalla documentazione.
