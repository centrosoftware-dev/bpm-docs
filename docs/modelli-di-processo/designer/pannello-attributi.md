# Pannello attributi

Il **_Pannello Attributi_** si trova sulla destra del canvas, ma è visibile solo quando un oggetto è selezionato.  
Qui sono raggruppate molte informazioni e impostazioni dell'oggetto selezionato, alcune delle quali comuni a quelle del [menu contestuale](menu-contestuale.md). Le voci visibili dipendono dall'oggetto selezionato.

Dall'altro come prima voce, presente a tutti gli oggetti, troviamo il _(Nome)_ dell'oggetto. Questo viene assegnato in modo automatico quando l'oggetto è inserito nel canvas e non può essere modificato in seguito. Il nome è formato dal tipo dell'oggetto seguito da un numero identificativo incrementale (ad esempio: _start1_).

Di seguito troviamo tutte le impostazioni, modificabili dall'utente e raggruppate in gruppi:


## Aspetto
Permette di gestire l'**allineamento** della targhetta, il **colore** e il **font** del **testo** al suo interno, lo **spessore** e il **colore** dei **bordi** dell'oggetto, il **colore** dello **sfondo**, il **tipo di linea** (nel caso di un oggetto [Link](../elementi/link.md)).


## Dati
Questa sezione contiene proprietà modificabili del singolo oggetto per personalizzarne il comportamento. Molte di queste voci sono comuni con il menu contestuale e portano ai medesimi pannelli di configurazione. Le voci che troviamo sono:

### Allegati
Il popup e lo stesso accessibile dalla voce Allegati del [menu contestuale](menu-contestuale.md#allegati-da-richiedere).

### Ambito
Un campo di testo libero che permette raggruppare/categorizzare le task.  
Dalla to-do list infatti è possibile ricercare tutte le task con uno stesso ambito.

### Descrizione
Permette di fornire informazioni testuali riguardanti una task, utili a chi dovrà poi dovrà svolgerla.  
Queste informazioni appariranno poi nella tab _Istruzioni_ quando un utente eseguirà quella task.

### Escalation
Cliccando su questo campo si apre lo stesso pannello accessibile dalla voce [Escalation](menu-contestuale.md#escalation) del menu contestuale. 

### Operazioni
Il popup permette di configurare le operazioni relative all'attivita, come descritto nella voce [Operazioni](menu-contestuale.md#operazioni) del menu contestuale.

### Priorità
Permette di assegnare un livello di importanza allo svolgimento di una task.  
Dalla to-do list è poi possibile filtrare e ordinare le task in base alla loro priorità.  
I livelli possibili sono: _Nessuna_, _Bassa_, _Media_, _Alta_ o _Sospesa_.

### Testo
Consente di modificare ciò che appare sul canvas a video nella label di un elemento. Il valore inserito sarà considerato anche come nome secondario dell'elemento, permettendo di filtrare le task in base ad esso e apparendo nella tab _Dati_ dell'esecuzione di una task.

### Utenti, Utenti cc e Utenti responsabili
Questa voce definisce chi dovra svolgere un'attivita. Il popup e descritto in [Utenti e responsabili](menu-contestuale.md#utenti-e-responsabili).

### Variabili da richiedere
Le variabili di un'attivita sono configurabili anche tramite la voce [Variabili da richiedere](menu-contestuale.md#variabili-da-richiedere).

### Impostazioni
Questa voce, esclusiva dell'oggetto **Ritorno al processo chiamante**, apre la schermata di configurazione dell'oggetto.


## Gestione
In questa sezione troviamo le impostazioni per la gestione del processo nella todo list.  
È presente solo per 4 oggetti, con voci differenti per ognuno di essi.  
Vediamo nel dettaglio cosa è possibile configurare per ciascun oggetto:

#### Attivita e Sottoprocesso

Voci disponibili per [Attivita](../elementi/attivita.md) e [Sottoprocesso](../elementi/sottoprocesso.md):
    - _Colore in todo list_: determina il colore della task nella todo list per maggiore organizzazione a livello visivo.
    - _Da confermare_: determina se la task necessiti o meno di un'azione di conferma esplicita prima di poter essere effettivamente eseguita.
    - _Rileva inizio attività_: determina se l'attività sia da iniziare espicitamente o se inizia automaticamente all'attivazione, utile per assegnare operazioni automatiche all'inizio dell'attività invece che all'attivazione.
    - _Skip activity_: determina se la task deve essere saltata senza eseguire, andando direttamente alla successiva, o meno. 
    - _Sottoprocesso_: definisce se l'oggetto contiene un sottoprocesso e di quale tipo, come descritto nella [pagina dedicata](../elementi/sottoprocesso.md).
    - _Testo pulsante esegui_: permette di modificare il testo del link per eseguire la task, presente nella colonna 'Azione' della todo list.
    - _Tipo attività_: permette di categorizzare la task tramite un elenco pre-impostato dei tipi di attività più comuni.
    - _Utilizza calendario_: determina se usare il calendario per il calcolo dei giorni. La stessa opzione e descritta in [Pianificazione e scadenze](menu-contestuale.md#pianificazione-e-scadenze).

#### Stato

- _Blocca edit_: impedisce la modifica dei dati dell'istanza di processo o del documento quando lo stato viene raggiunto.
- _Stato di chiusura_: conclude l'istanza di processo e interrompe le attivita ancora in corso.

#### Connettore attivo

- _Interfaccia_: apre la finestra di configurazione accessibile anche tramite menu contestuale.


## Scadenze/Tempi

Questa sezione contiene _Durata prevista_ e _Scadenza_. Entrambe aprono il pannello descritto in [Pianificazione e scadenze](menu-contestuale.md#pianificazione-e-scadenze).


## Varie

Alcune impostazioni sono specifiche di certi singoli oggetti e non sono assegnabili in uno dei precedenti raggruppamenti.  
Per questo vengono inseriti in questa sezione contenente tutti le voci speciali/extra:

- ### Percorso per pianificazione
  Esclusivo dell'oggetto [Link](../elementi/link.md), determina il percorso predefinito per la pianificazione temporale delle attivita del processo.  
  Utile solo in caso il flusso sia ramificato, ad esempio con percorsi diversi da seguire in base ai valori assunti da alcune variabili di processo.

### Configurazione 
Questa sezione è presente solo per due oggetti e permette di accedere direttamente alla finestra di configurazione di ciascun oggetto. Essse sono aggiungibili anche tramite menu contestuale e sono illustrate nelle apposite sezioni dedicate (raggiungibili tramite i link contenuti nei nomi degli oggetti qui sotto).  

La sezione contiene un'unica voce, con nome specifico per ciascun oggetto:

- CONFIGURAZIONE **_TIMER_** per l'oggetto **Start a tempo**

- CONFIGURAZIONE **_ATTESA_** per l'oggetto **Attesa**

Questa opzione e presente per le [Operazioni](../elementi/operazioni/index.md) e per i [Gateway](../elementi/gateway.md), tranne **Sincronizza**.  
La schermata di _Configurazione_ è totalmente differente per ogni oggetto e viene approfondita nelle sezioni relative ai singoli elementi.
