# Tutorial 4 — Configurare un connettore attivo verso SAM per la creazione di una commessa

Obiettivo: da un'attività del processo, generare automaticamente una nuova commessa in SAM tramite il connettore attivo, mappando testata, dettaglio righe e recuperando il numero commessa generato. –

1. Verifica preliminare (lato ambiente): il connettore "SAM v5" deve essere configurato in Configurazione → connettori, marcato **Attivo**, con almeno un'azienda ("nuova azienda") configurata con i parametri di connessione (server DB, credenziali, endpoint web service dell'azienda). Il modulo **Web Import** di SAM deve essere installato e raggiungibile.
2. Nel diagramma di processo, trascina l'operazione **Connettore Attivo** nel punto del flusso dove deve avvenire la creazione della commessa.
3. Fai doppio clic sull'operazione appena inserita.
4. Scegli l'interfaccia XML preconfezionata pertinente (es. "xml commessa").
5. Nella schermata dei parametri di input (testata), mappa ciascun campo richiesto su una variabile di processo corrispondente (es. codice cliente, descrizione commessa) oppure lascialo come valore fisso quando appropriato.
6. Se serve un campo di testata non presente nell'elenco default, usa l'helper di aggiunta campo (che conosce le colonne della tabella target in SAM) per aggiungerlo e mappalo a sua volta.
7. Se l'interfaccia prevede parametri di output (es. l'ID/numero della commessa creata), mappali su una variabile di processo dedicata (es. `numero_commessa`).
8. Se il processo include un gruppo di dettaglio corrispondente (es. "lista codici" articoli), apri la sezione parametri di dettaglio/riga e mappa ciascuna colonna del gruppo sul nodo XML di dettaglio ripetuto corrispondente (es. `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`).
9. Salva la configurazione dell'operazione.
10. Pubblica il processo e collauda l'esecuzione dell'attività: verifica in SAM che la commessa sia stata effettivamente creata con i dati attesi, e che `numero_commessa` sia stato valorizzato correttamente nell'istanza di processo.
11. In caso di errore, ricorda che BPM è un semplice pass-through verso il web import di SAM: un campo obbligatorio mancante o non valido produce un errore restituito da SAM, non da BPM.
