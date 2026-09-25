# Carica Dati

**Carica Dati** è un'operazione nativa di BPM che legge dati da una tabella o vista e li copia nelle variabili del processo o del documento.

Si usa tipicamente all'**inizio** di un processo: l'utente, o il sistema che avvia il processo, fornisce solo un codice, e l'operazione recupera il resto. Per esempio, dall'ID di un ordine legge fornitore, data e importo; dal codice cliente legge ragione sociale e agente.

## Come si configura

L'operazione usa la stessa finestra delle [fonti dati delle variabili](dati-esterni.md):

1. si sceglie la fonte: tabella o vista tramite una [connessione esterna](connessioni-esterne.md), tabella locale o tabella di un connettore;
2. si indica la condizione di ricerca, legando la colonna chiave alla variabile che contiene il valore da cercare;
3. si collegano le colonne da leggere alle variabili da valorizzare.

L'operazione si inserisce nel flusso oppure si aggancia a un momento del ciclo di vita di un'attività, per esempio all'attivazione.

## Carica Dati o Esegui SQL?

| | Carica Dati | Esegui SQL |
|---|---|---|
| Configurazione | Guidata: tabella, chiave, colonne | Un'istruzione SQL scritta a mano |
| Adatta per | Leggere un record a partire da una chiave | Scritture, query complesse (join, aggregazioni), stored procedure |
| Errori | Pochi: la finestra conosce tabelle e colonne | Dipendono dalla correttezza della query |

Per le letture semplici preferisci Carica Dati; passa a [Esegui SQL](esegui-sql.md) quando serve di più.
