# Integrazione

BPM non lavora mai da solo: nella quasi totalità delle installazioni legge almeno le anagrafiche da un gestionale, e spesso scambia dati in entrambe le direzioni con ERP, CRM, sistemi di produzione e altre applicazioni aziendali.

Questa sezione descrive gli strumenti di integrazione in modo generale, indipendentemente dal sistema con cui BPM dialoga.

## Le modalità di integrazione

| Direzione | Esigenza | Strumento |
|---|---|---|
| **Dall'esterno verso BPM** | Un'applicazione esterna avvia processi, fa avanzare attività, legge la To-Do List, carica documenti | [Web API](web-api/index.md) |
| **Dall'esterno verso BPM** | Un sistema esterno accoda le richieste in una tabella, elaborate in modo asincrono | [Coda delle chiamate](web-api/coda-chiamate.md) |
| **Dall'esterno verso BPM** | I documenti che arrivano in una cartella entrano automaticamente in BPM | Acquisizione automatica dei documenti *(in preparazione)* |
| **Da BPM verso l'esterno** | Un processo legge o scrive dati su un database SQL o ODBC | Operazioni SQL e connettori *(in preparazione)* |
| **Dati esterni dentro BPM** | Una variabile propone i valori di una tabella esterna (clienti, fornitori, articoli…) | Fonti dati delle variabili *(in preparazione)* |
| **Casi complessi** | Logiche di integrazione che richiedono codice | Script di integrazione *(in preparazione)* |

Il catalogo dei componenti tecnici disponibili è descritto in [Connettori](connettori/index.md).

!!! info "Integrazione con SAM ERP2"
    BPM e SAM ERP2 sono spesso installati insieme e dispongono di un'integrazione dedicata. Le pagine di questa sezione descrivono gli strumenti generali; l'integrazione specifica con SAM ERP2 avrà una sezione propria.
