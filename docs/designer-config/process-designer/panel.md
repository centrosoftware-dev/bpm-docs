# Pannello attributi

Il **_Pannello Attributi_** si trova sulla destra del canvas, ma è visibile solo quando un oggetto è selezionato.  
Qui sono raggruppate molte informazioni e impostazioni dell'oggetto selezionato, alcune delle quali comuni a quelle del [menu contestuale](./designer-tools/menu.md). Le voci visibili dipendono dall'oggetto selezionato.

Dall'altro come prima voce, presente a tutti gli oggetti, troviamo il _(Nome)_ dell'oggetto. Questo viene assegnato in modo automatico quando l'oggetto è inserito nel canvas e non può essere modificato in seguito. Il nome è formato dal tipo dell'oggetto seguito da un numero identificativo incrementale (ad esempio: _start1_).

Di seguito troviamo tutte le impostazioni, modificabili dall'utente e raggruppate in gruppi:


## Aspetto
Permette di gestire l'**allineamento** della targhetta, il **colore** e il **font** del **testo** al suo interno, lo **spessore** e il **colore** dei **bordi** dell'oggetto, il **colore** dello **sfondo**, il **tipo di linea** (in caso di un oggetto [link](./designer-tools/activities/link.md)), 


## CONFIGURAZIONE
Questa sezione è presente solo per due oggetti e permette di accedere direttamente alla finestra di configurazione di ciascun oggetto. Essse sono aggiungibili anche tramite menu contestuale e sono illustrate nelle apposite sezioni dedicate (raggiungibili tramite i link contenuti nei nomi degli oggetti qui sotto).  

La sezione contiene un'unica voce, con nome specifico per ciascun oggetto:

- CONFIGURAZIONE **_TIMER_** per l'oggetto [Start a tempo](./designer-tools/events/start-event.md)

- CONFIGURAZIONE **_ATTESA_** per l'oggetto [Attesa](./designer-tools/events/wait.md)


## Dati
Questa sezione contiene proprietà modificabili del singolo oggetto per personalizzarne il comportamento. Molte di queste voci sono comuni con il menu contestuale e portano ai medesimi pannelli di configurazione. Le voci che troviamo sono:

### Allegati
Il popup aperto al click di questa voce è il medesimo che possiamo configurare tramite la voce allegati del menu contestuale, illustrata [qui](./designer-tools/menu.md#allegati-da-richiedere).

### Ambito
Un campo di testo libero che permette raggruppare/categorizzare le task.  
Dalla to-do list infatti è possibile ricercare tutte le task con uno stesso ambito.

### Descrizione
Permette di fornire informazioni testuali riguardanti una task, utili a chi dovrà poi dovrà svolgerla.  
Queste informazioni appariranno poi nella tab _Istruzioni_ quando un utente eseguirà quella task.

### Escalation
Cliccando su questo campo verrà aperto lo stesso pannello accessibile tramite la medesima voce del menu contestuale, spiegato nel dettaglio [qui](./designer-tools/menu.md#escalation). 

### Operazioni
Il popup aperto cliccando su questa voce permette di configurare le operazioni relative alla task, nello stesso modo in cui è possibile farlo tramite menu contestuale, come descritto [qui](./designer-tools/menu.md#operazioni)

### Priorità
Permette di assegnare un livello di importanza allo svolgimento di una task.  
Dalla to-do list è poi possibile filtrare e ordinare le task in base alla loro priorità.  
I livelli possibili sono: _Nessuna_, _Bassa_, _Media_, _Alta_ o _Sospesa_.

### Testo
Consente di modificare ciò che appare sul canvas a video nella label di un elemento. Il valore inserito sarà considerato anche come nome secondario dell'elemento, permettendo di filtrare le task in base ad esso e apparendo nella tab _Dati_ dell'esecuzione di una task.

### Utenti, Utenti cc e Utenti responsabili
Quest'entrata serve per definire chi dovrà svolgere una determinata task. Il popup di configurazione è accessibile anche tramite menu contestuale ed è spiegato nel dettaglio [qui](./designer-tools/menu.md#utenti-e-responsabili).

### Variabili da richiedere
Le variabili relative a un task sono configurabili anche tramite menu contestuale tramite la medesima voce, descritta in modo specifico [qui](./designer-tools/menu.md#variabili-da-richiedere).

### Impostazioni
Questa voce, esclusiva dell'oggetto [Ritorno al processo chiamante](./designer-tools/linked-process/return-linked-process.md), apre semplicemente la schermata di configurazione dell'oggetto, la quale viene descritta in modo approfondito nell'apposita sezione dedicata all'oggetto. 


## Gestione **(?)**
In questa sezione troviamo le impostazioni per la gestione del processo nella todo list.  
È presente solo per 4 oggetti, con voci differenti per ognuno di essi.  
Vediamo nel dettaglio cosa è possibile configurare per ciascun oggetto:

 1. #### [Task](./designer-tools/activities/task.md)/[Sottoprocesso](./designer-tools/activities/subprocess.md)
    - _Colore in todo list_: determina il colore della task nella todo list per maggiore organizzazione a livello visivo.
    - _Da confermare_: determina se la task sia da confermare esplicitamente prima di poter essere eseguita **(?)**
    - _Non documentabile_: **(?)**
    - _Rileva inizio attività_: determina se l'attività sia da iniziare espicitamente o se inizia automaticamente all'attivazione, utile per assegnare operazioni automatiche all'inizio dell'attività invece che all'attivazione.
    - _Skip activity_: determina se la task deve essere saltata senza eseguire, andando direttamente alla successiva, o meno. 
    - _Sottoprocesso_: per definire se l'oggetto contiene o meno un sottoprocesso e di che tipo, tramite l'apposita finestra di configurazione illustrata [qui](./designer-tools/activities/subprocess.md)
    - _Testo pulsante esegui_: permette di modificare il testo del link per eseguire la task, presente nella colonna 'Azione' della todo list.
    - _Tipo attività_: permette di categorizzare la task tramite un elenco pre-impostato dei tipi di attività più comuni **(FILTRI?)**.
    - _Utilizza calendario_: determina se utilizzare o meno il calendario per avere riferimenti temporali reali **(?)**.

 2. #### [Stato](./designer-tools/activities/state.md)
    - _Blocca edit_: **(?)**
    - _Stato di chiusura_: **(?)**

 3. #### [Connettore Attivo](./designer-tools/operations/active-connector.md)
    - _Interfaccia_: apre la finestra di configurazione accessibile anche tramite menu contestuale, illustrata nella pagina dedicata a questo connettore.


## Scadenze/Tempi

Questa sezione contiene due voci: _Durata prevista_ e _Scadenza_. Entrambe rimandano allo stesso pannello di configurazione, che contiene le due voci e permette di modificarle. L'approfondimento su questo pannello, essendo accessibile anche tramite menu contestuale, è disponibile [qui](./designer-tools/menu.md#pianificazione-e-scadenze).


## Varie **(?)**

Alcune impostazioni sono specifiche di certi singoli oggetti e non sono assegnabili in uno dei precedenti raggruppamenti.  
Per questo vengono inseriti in questa sezione contenente tutti le voci speciali/extra:

- ### Percorso per pianificazione **(?)**
  Esclusivo dell'oggetto [Link](./designer-tools/activities/link.md), determina il percorso di pianificazione

- ### PosizioniMarkers **(?)**
Esclusivo dell'oggetto [Marker](./designer-tools/other/marker.md), 

- ### FormulaAttivazioneDef **(?)**
Esclusivo dell'oggetto [Avvio processo collegato](./designer-tools/linked-process/start-linked-process.md)

- ### oldCartellaDestinazioneAllegati **(?)**
Esclusivo dell'oggetto [Avvio processo collegato](./designer-tools/linked-process/start-linked-process.md)

### Configurazione
Quest'opzione è presente solamente per: tutti gli [Operatori](./designer-tools/operations/intro.md) e per tutti i [Gateway](./designer-tools/gateways/intro.md) (tranne il 'Sincronizza').  
La schermata di _Configurazione_ è totalmente differente per ogni oggetto e viene approfondita nelle sezioni relative ai singoli elementi.