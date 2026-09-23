# Editor delle variabili

L'**Editor delle variabili** e uno strumento condiviso dai modelli di processo, dalle classi documentali e da altre configurazioni BPM. Consente di creare, organizzare e configurare le variabili impiegate in ciascun contesto.

Grazie a questo strumento è possibile definire i dati che i processi devono trattare, stabilirne la tipologia, il formato e il comportamento, garantendo così una gestione coerente e automatizzata delle informazioni aziendali.


## Scopo della sezione

L’obiettivo principale della sezione **_Variabili_** è quello di fornire un punto centralizzato dove:
- Definire le variabili globali o specifiche per un determinato modello di processo  
- Impostare le caratteristiche di ciascuna variabile (nome, tipo, valore predefinito, visibilità, ecc.)  
- Gestire la logica di interscambio dei dati tra le diverse attività di un processo  
- Creare collegamenti diretti tra variabili, campi documentali e interfacce utente  

Le variabili costituiscono il **ponte logico tra i dati e le azioni**: tutto ciò che un processo riceve, elabora o produce viene gestito attraverso di esse.


## Tipologie di variabili

All’interno del BPM esistono diverse **tipologie di variabili**, ciascuna con un ruolo e un ambito di utilizzo specifico:

1. **Variabili globali**  
   Sono disponibili a tutti i processi e utili per dati condivisi (es. utente corrente, data di sistema, impostazioni generali).

2. **Variabili di processo**  
   Sono specifiche di un singolo modello di processo e vengono create al suo interno per gestire i dati necessari al suo flusso.

3. **Variabili locali**  
   Sono utilizzate solo all’interno di una singola attività o step del processo, per gestire informazioni temporanee o di calcolo.

4. **Variabili di sistema**  
   Create automaticamente dal BPM, servono per monitorare stati e metadati del processo (es. ID del processo, data di creazione, utente assegnato).


## Tipi di dato supportati

Ogni variabile può essere definita con un **tipo di dato specifico**, in base alla natura delle informazioni che deve contenere.  
I principali tipi di dato sono:

- **Testo:** per stringhe di caratteri, nomi o descrizioni  
- **Numero:** per quantità, codici o valori numerici  
- **Data/Ora:** per gestire scadenze, registrazioni temporali o intervalli  
- **Booleano:** per valori logici (vero/falso)  
- **Oggetto/Classe documentale:** per riferimenti a strutture dati più complesse  

Inoltre, il sistema consente di creare **tipi personalizzati**, utili per casi d’uso specifici o integrazioni avanzate con altri moduli del BPM.


## Utilizzo nei processi

Le variabili vengono utilizzate in diversi punti di un processo, tra cui:
- **Condizioni di transizione:** per definire logiche di avanzamento del flusso  
- **Attività automatizzate:** per scambiare dati con sistemi esterni o moduli interni  
- **Form di input/output:** per visualizzare o raccogliere dati da parte degli utenti  
- **Azioni e script:** per eseguire calcoli, verifiche o aggiornamenti dinamici  


## Buone pratiche

Per una gestione ottimale delle variabili, è consigliato:
- Utilizzare **nomi coerenti e descrittivi**, evitando abbreviazioni non chiare  
- Separare le variabili globali da quelle locali per evitare conflitti  
- Documentare la funzione di ciascuna variabile nei commenti del modello  
- Eliminare le variabili non più utilizzate per mantenere pulito l’ambiente  
- Testare sempre le variabili durante le fasi di validazione del processo  


## Approfondimenti

Nei capitoli successivi verranno analizzati nel dettaglio:
- Come creare una nuova variabile  
- Come collegare variabili a campi documentali o form di processo  
- Come utilizzare le variabili nelle espressioni e nelle condizioni logiche  
- Le modalità di esportazione e importazione delle variabili tra modelli  

??? info "Suggerimento"
    Prima di creare una nuova variabile, verifica se esiste già una variabile globale che soddisfa la stessa funzione.  
    In questo modo eviterai duplicazioni e garantirai una gestione più efficiente dei dati all’interno del BPM.
