# Designer Tools e Attributi

In questa pagina verranno descritte dettagliatamente tutte le sezioni e gli elementi al loro interno.  

Il Designer Tools è il pannello che si trova sulla sinistra, gli Attributi invece si trovano nel Menù contestuale e nel Pannello Attributi.

## Designer Tools
Il Designers Tools è suddiviso in 6 sezioni.  

Alla sommità è situata la search bar. Digitando al suo interno è possibile filtrare gli oggetti delle varie sezioni. I risultati della ricerca appariranno nella propria sezione. Se più oggetti corrispondono col termine ricercato, verranno mostrati nelle proprie sezioni, se diverse, collassate.

### Attività

Sezione contenente i principali elementi di un flusso.

#### Puntatore

Cliccandolo, riporta le funzionalità del mouse a quelle standard: click per tasto sinistro e menù contestuale per tasto destro.  

Non essendo trascinabile nel canvas e, quindi, **non essendo un elemento**, non possiede attributi.

#### Link

Il link è un collegamento tra un elemento e un altro.  

Una volta selezionato dal Designer Tools, passando il cursore sopra un elemento, appariranno dei cerchi gialli. Selezionando un cerchio e tenendo premuto il tasto sinistro, inizierà il tracciamento del link.  

Mentre si sta tracciando, passando il cursore su un elemento differente dal primo, è possibile collegarlo ad uno dei punti del destinatario.

![](../../assets/linking.gif)

Fatto ciò, i due elementi saranno collegati: spostandoli all'interno del canvas, il link rimarrà ancorato ad essi.  

Cliccando sul collegamento con il tasto destro del mouse, si aprirà il menù di contesto contenente una lista di proprietà:

* Nome Collegamento, aprirà un dialog dove poter inserire il nome del link che verrà mostrato nel canvas.
* Percorso per Pianificazione, se spuntato, il processo, al suo inizio, riterrà il collegamento come percorso default per determinare le attività future.
* Condizioni Abilitazione, complementari al Percorso per Pianificazione, le condizioni di abilitazione decidono se un Link sia percorribile o meno. Tale decisione è basata sulle formule scritte nel dialog che si apre una volta cliccata l'opzione.
* Imposta variabili, è possibile impostare delle variabili quando il link viene attraversato, arrivando a destinazione coi nuovi valori assegnati.
* Tipo Linea, è possibile decidere tra le varie opzioni il comportamento del link all'interno del canvas.
* Elimina Collegamento

#### Start

Lo Start è il punto di inizio di ogni flusso manualmente azionato.  

Un flusso può avere più Start. In questo caso, alla partenza del processo, verrà richiesto all'utente da quale Start partire.  

Ogni Start ha necessariamente bisogno che le **_Variabili da richiedere_** siano dichiarate.  
Una volta inserite, apparirà una @ accanto allo start nel canvas.
Allo stesso modo, se sono presenti delle Variabili da richiedere, è dovuto specificare gli **_Utenti e Responsabili_** della task.  

È inoltre possibile richiedere l'inserimento di allegati e lo svolgimento di operazioni, sempre tramite il menù contestuale, alla voce **_Allegati da richiedere_** e **_Operazioni_**.  
Uno Start consente di effettuare delle operazioni **_In esecuzione_** e ad **_Esecuzione terminata_**.

#### Attività

Le **_Attività_** sono il blocco fondamentale dei processi.
Servono a definire il lavoro di ogni persona. Attività per attività, un processo viene concluso, portando a termine lavori che, senza il BPM, risulterebbero tediosi e ad alto compenso di tempo.

Le **_Attività_**, nel pannello degli attributi, presentano una serie di caratteristiche che rendono la task personalizzabile e utilizzabile in ogni ambito.
Nella sezione **_Gestione_** si trovano gli attributi principali di un'attività:

##### Da confermare

Attributo che aggiunge la necessità di confermare la fine dell'attività per poter mandare avanti il flusso.

##### Non documentabile

##### Rileva inizio attività

##### Skip activity

Se impostato su True salterà l'esecuzione della task

##### Sottoprocesso

Se impostato su True, rende l'Attività un Sottoprocesso.  
Per approfondire il concetto di **_Sottoprocesso_** scendi alla sezione Sottoprocesso o clicca [qui]().

##### Testo pulsante esegui

Attributo di tipo testuale. Il testo inserito apparirà al posto di "Esegui" sul bottone esegui.

##### Tipo attività

##### Utilizza calendario

#### Stato processo

L'elemento **_Stato processo_** serve a visualizzare graficamente lo stato del processo.
Uno Stato processo consente di effettuare delle operazioni solo **_In attivazione_**.

Nella sezione Gestione ci sono 2 attributi:

##### Blocca edit

##### Stato di chiusura

Impostando questo attributo a True, si sancisce la fine del processo.

#### Sottoprocesso

Un **_Sottoprocesso_** è un processo avviato dall'interno di un altro processo.
Nel canvas dove viene inserito un Sottoprocesso (o un'attività con attributo Sottoprocesso impostato a true) l'elemento apparirà uguale ad una semplice attività, ma con una croce sotto la label descrittiva.  
Cliccando due volte sopra l'elemento, si entra nel canvas del Sottoprocesso.
Le funzionalità sono le stesse di un processo normale. L'unica differenza è nello start, che avviene non appena l'elemento principale del Sottoprocesso entra in esecuzione.  

Gli attributi che differenziano un'attività da un Sottoprocesso sono nella sezione **_Scadenze/Tempi_**. Entrambi questi attributi vengono approfonditi nella loro sezione [qui]().

## Menù contestuale

Il menù contestuale appare quando si preme il tasto destro del mouse su un oggetto nel canvas. In base all'oggetto cliccato le entrate saranno differenti.  
Analogamente, a destra del canvas si trova il Pannello Attributi che, molto spesso, presenta entrate comuni a quelle del menù contestuale.

### Allineamento

Selezionando più oggetti(1)è possibile spostarli in massa seguendo l'allineamento dell'elemento su cui si è cliccato il tasto destro. 
{ .annotate }

1.  Per selezionare più oggetti è necessario tenere premuto CTRL o SHIFT quando si va a cliccare, col tasto sinistro, su un elemento.

Gli oggetti che possiedono un'etichetta hanno anche la possibilità di gestire il suo allineamento.

### Aspetto

Contenitore di attributi legati ai font di un oggetto o della sua targhetta.
Generalmente, in un oggetto è possibile cambiare:

* Colore del testo.
* Colore dello sfondo.
* Colore e spessore e del bordo.

### Manipolazione oggetto

Oltre al tagliare e copiare un oggetto, è possibile spostarlo da una pagina ad un'altra del processo tramite l'entrata **_Sposta oggetto alla pagina ..._**.

### Manipolazione Testo e Label

Nel menù contestuale è presente l'entrata **_Sposta testo_** per spostare l'etichetta dell'oggetto dove si vuole nel canvas. Essa rimarrà ancorata al punto dove si è spostata.
L'entrata **_Modifica Testo_** consente di modificare il testo della Label.

### Impostare un oggetto come oggetto di avvio

!!! danger "Rimozione dello Start"
    È possibile rimuovere lo Start, ma è un comportamento non convenzionale e tendenzialmente sconsigliato in quanto il processo richiederà all'utente di inserire direttamente le variabili da richiedere.

Premendo tasto destro, l'entrata **_Imposta come oggetto di avvio_** renderà l'oggetto su cui si è cliccato, il punto di partenza.

### Definire gli Utenti e i Responsabili, le Variabili da richiedere e gli Allegati da richiedere

Tramite l'entrata **_Utenti e responsabili_** è possibile definire chi dovrà svolgere una determinata task.

Analogamente, è possibile definire i dati che, gli utenti precedentemente, assegnati dovranno inserire.
Questo è possibile tramite l'entrata **_Variabili da richiedere_** che, una volta cliccata, aprirà una nuova pagina dedicata all'inserimento delle variabili.  
Questa pagina, chiamata **_Magazzino delle variabili_**, viene trattata e approfondita nella sua sezione apposita [qui]().
Per aggiungere una Variabile da richiedere, basta prenderne una dalla lista di sinistra e trascinarla nel canvas.
Così facendo, gli utenti a cui è assegnata la task, dovranno inserire i valori delle variabili così definite.

![](../../assets/inserimentoVarUserTask.gif)

Infine, è possibile definire gli allegati da definire tramite l'entrata **_Allegati da richiedere_**.  
In questo caso non è possibile definire gli allegati che andranno inseriti, bensì dei filtri che vadano a scremare i possibili allegati inseribili. Tutto questo tramite un popup.  
Il popup presenta due checkbox:

* La prima, se spuntata, renderà funzionanti i filtri e le preferenze che vengono definite nel resto del popup.
* La seconda, invece, fa sì che gli allegati caricati non possano essere poi modificati.

Dopodiché una sezione dedicata ai filtri: qui è possibile infatti definire il **_Gruppo allegato_**, il **_Tipo allegato_** e il **_Percorso_**.  

Il **_Gruppo allegato_** e il **_Tipo Allegato_** sono definibili dal menù delle impostazioni alla sezione **_Configurazione_**, sottogruppo **_Allegati_**.  

Per il **_Percorso_** invece è necessario scegliere una delle cartelle interne al processo.  
Per crearne una è necessario cliccare la voce **_Allegati_** dalla **_barra degli strumenti_**.  
Da lì si apriranno le impostazioni generali del processo relative agli allegati.  
Cliccando tasto destro sulla lista delle cartelle, sarà possibile crearne una nuova. Una volta fatto, sarà presente tra le scelte disponibili per determinare il percorso degli allegati di una task.

Sotto i Filtri, è possibile gestire la **_Dimensione Massima in KB_** (Dim. Massima kb), tramite un input numerico.
Il numero immesso sarà il tetto massimo per la dimensione di un file.  

Nella parte bassa del popup invece si ha il gruppo relativo ai Tipi di file consentiti.  
Tramite una serie di checkbox è possibile definire le estensioni dei file che possono essere accettati.  
L'input di testo finale invece è riservato ad estensioni specifiche per gli utenti che ne hanno bisogno. **_Tali estensioni vanno separate dalla virgola e includendo il punto_**.

``` title="Altre Estensioni" linenums="1"
.cad,.php,.bat
```

### Operazioni

L'entrata relativa alle **_Operazioni_** apre un popup che permette di eseguire delle operazioni in diversi momenti della task.  
In base all'elemento su cui si apre il popup, i momenti in cui sarà possibile svolgere un'operazione saranno diversi.  
Per svolgere un'operazione basta trascinarla dalla colonna **_Operazioni disponibili_** a quella del momento in cui si desidera svolgerla.(1) 
{ .annotate }

1. Il titolo della colonna è il momento in cui verrà svolta l'operazione.

Le operazioni vengono svolte in ordine Top to Bottom.

Ogni operazione è trattata e approfondita nell'apposita sezione [qui]().

### Formula di validazione

La **_Formula di validazione_** è una formula che determina se è possibile continuare con la task successiva del processo.
Cliccando su questa entrata, verrà aperto il popup per la scrittura delle formule.  
Le formule di validazione degli elementi del canvas sono in una relazione AND con le altre formule definibili dalla barra degli strumenti della pagina delle variabili.

### Escalation

L'**_Escalation_** è un'entrata del menù contestuale specifica di alcuni elementi.  
Con l'utilizzo dell'**_Escalation_** è possibile, dopo un determinato numero di giorni inserito dall'utente, eseguire le 3 azioni seguenti:

* Non variare attività
* Riassegna attività, cedendo ad altri utenti la possibilità di mandare avanti il processo
* Chiudi attività

Dall'Escalation poi è possibile iniziare un collegamento, così da poter instradare il processo altrove in caso si dovesse riassegnare o chiudere la task.

### Pianificazione e Scadenze

Il popup "Pianificazione e Scadenze" permette di impostare i dettagli di pianificazione, scadenze e priorità relativi a una specifica attività (task). È diviso in tre schede principali: Pianificazione e scadenze, Variabili, e Dati aggiuntivi.

In **_Pianificazione e Scadenze_** è possibile impostare la durata prevista e la scadenza di una task.
Inoltre sono presenti 3 checkbox:

* Da confermare
* Rileva inizio
* Utilizza calendario

La tab **_Variabili_** consente di associare variabili ai campi relativi a una pianificazione aggiornata dell'attività. I campi configurabili includono:

* Data inizio prevista aggiornata, consente di collegare una variabile alla data di inizio pianificata dell'attività nel calendario.
* Data fine aggiornata, permette di associare una variabile alla data di fine dell'attività pianificata.
* Durata prevista (giorni), offre la possibilità di collegare una variabile che rappresenta la durata stimata dell'attività (in giorni).
* Scadenza dell'attività, configura una variabile per rappresentare la data di scadenza dell'attività.
* Priorità dell'attività, consente di associare una variabile alla priorità assegnata all'attività.

La scheda **_Dati aggiuntivi_** consente di associare variabili a campi specifici relativi ai dati pianificati e ai dati effettivi di un'attività. Questa scheda è divisa in due sezioni principali: Dati Previsti/Pianificati e Dati Effettivi.

Nel gruppo **_Dati Previsti/Pianificati_** è possibile configurare le variabili per i dati pianificati dell'attività. I campi disponibili sono:

* Data inizio prevista/pianificata, permette di collegare una variabile alla data di inizio pianificata dell'attività nel calendario.
* Data fine prevista/pianificata, consente di associare una variabile alla data di fine pianificata dell'attività.
* Durata prevista (giorni), Collega una variabile che rappresenta la durata stimata dell'attività in giorni.

Il Gruppo **_Dati Effettivi_** permette di configurare le variabili per i dati effettivi dell'attività, ovvero i valori realmente registrati. I campi configurabili sono:

* Data inizio dell'attività, associa una variabile che rappresenta la data di inizio effettiva dell'attività.
* Data fine dell'attività, collega una variabile alla data di completamento effettiva dell'attività.
* Durata effettiva (giorni), consente di collegare una variabile che rappresenta la durata effettiva dell'attività in giorni.

### Configurazione

L'entrata **_Configurazione_** è differente per ogni elemento e viene approfondita nelle sezioni relative ai singoli elementi.


Il Pannello Attributi presenta delle entrate comuni e generali tra gli elementi disegnabili sul canvas.  Esse sono:

* 
* Allineamento, 
* 
* Dati, sezione che comprende:
    - Testo, presente in parti diverse a seconda dell'oggetto.
    - Utenti, Utenti CC e Utenti Responsabili quando è necessaria l'assegnazione di una task.
    - Variabili da richiedere.
    - Allegati da richiedere.
    - Ambito, necessario se quando si filtrano le attività della to-do list.
    - Descrizione.
    - Operazioni.


