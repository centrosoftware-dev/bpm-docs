# Menù contestuale e Pannello attributi

Il menù contestuale appare quando si preme il tasto destro del mouse su un oggetto nel canvas. Il pannello attributi invece è la sidebar di destra che appare quando si seleziona un elemento.

In base all'oggetto cliccato le entrate di entrambi saranno differenti. 

## Menù Contestuale

### Colore e font

Generalmente, in un oggetto è possibile cambiare:

* Colore e font della targhetta dell'elemento.
* Colore dello sfondo.
* Colore e spessore e del bordo.

### Allineamento

L'entrata **_Allineamento_** a sua volta ha 10 scelte: 

#### Allinea

Allineano gli elemento selezionati secondo il tipo di allineamento in base alla posizione dell'elemento su cui è stato cliccato il tasto destro.

#### Porta davanti e Porta dietro

Modifica lo Z-index di un oggetto: se un oggetto risulta sovrapposto ad un altro, per portarlo in avanti è sufficiente cliccare **_Porta avanti_** per portarlo in primo piano. 
Lo stesso, ma al contrario, vale per **_Porta dietro_**.

#### Distribuisci

Selezionando più oggetti(1)è possibile spostarli in massa distrubuendoli su uno dei loro assi utilizzando le due entrate **_Distribuisci verticalmente_** o **_Distribuisci orizzontalmente_**.
{ .annotate }

1.  Per selezionare più oggetti è necessario tenere premuto ++ctrl++ o ++shift++ quando si va a cliccare, col tasto sinistro, su un elemento. Altrimenti, cliccando su una parte vuota del canvas e tenendo premuto, è possibile delineare un'area i cui elementi interno verranno selezionati.

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
Questa pagina, chiamata **_Magazzino delle variabili_**, viene trattata e approfondita nella sua sezione apposita [qui](MagazzinoVariabili.md).
Per aggiungere una Variabile da richiedere, basta prenderne una dalla lista di sinistra e trascinarla nel canvas.
Così facendo, gli utenti a cui è assegnata la task, dovranno inserire i valori delle variabili così definite.

![](../assets/inserimentoVarUserTask.gif)

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

Le **_Operazioni_** vengono svolte in ordine Top to Bottom.

Le **_Operazioni_** sono azioni specifiche e complesse, per approfondimenti e spiegazioni è nmecessario rifarsi alla loro sezione [qui]().

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


## Pannello attributi

### Aspetto

Nel Pannello attributi, **_Aspetto_** contiene tutte le informazioni di un oggetto relative all'allineamento della targhetta, ai colori e ai font.

### Dati

La sezione **_Dati_** comprende le proprietà più specifiche di un singolo elemento.  

Gli attributi elencati forniscono informazioni e impostazioni per personalizzare il comportamento e la gestione della task all'interno del flusso. Si tratta di proprietà che riguardano ambiti funzionali, priorità, gestione utenti e operazioni specifiche, oltre ad altre configurazioni utili per determinare come la task interagisce con il sistema o con altri elementi del flusso.

#### Ambito e Descrizione

L'**_Ambito_** è un campo di testo libero.  
Dalla to-do list è possibile ricercare tutte le task con uno stesso **_Ambito_**.

Impostando la **_Descrizione_** è possibile fornire informazioni testuali riguardanti una task, utili a chi dovrà poi dovrà svolgerla. Apparirà infatti nella tab **_Istruzioni_** quando un utente starà eseguendo la task.

#### Escalation
 
Con l'utilizzo dell'**_Escalation_** è possibile, dopo un determinato numero di giorni inserito dall'utente, eseguire le 3 azioni seguenti:

* Non variare attività
* Riassegna attività, cedendo ad altri utenti la possibilità di mandare avanti il processo
* Chiudi attività

Dall'Escalation poi è possibile iniziare un collegamento, così da poter instradare il processo altrove in caso si dovesse riassegnare o chiudere la task.

#### Operazioni

Da **_Operazioni_** si apre un popup che permette di eseguire delle operazioni in diversi momenti della task.  
In base all'elemento su cui si apre il popup, i momenti in cui sarà possibile svolgere un'operazione saranno diversi.  
Per svolgere un'operazione basta trascinarla dalla colonna **_Operazioni disponibili_** a quella del momento in cui si desidera svolgerla.(1) 
{ .annotate }

1. Il titolo della colonna è il momento in cui verrà svolta l'operazione.

Le **_Operazioni_** vengono svolte in ordine Top to Bottom.

Le **_Operazioni_** sono azioni specifiche e complesse, per approfondimenti e spiegazioni è nmecessario rifarsi alla loro sezione [qui](MagazzinoVariabili.md).

#### Priorità

Tramite **_Priorità_** è possibile assegnare un livello di importanza per lo svolgimento di una task.  

Dalla to-do list è possibile filtrare e ordinare le task in base alla loro priorità.  

I livelli possibili sono: Bassa, Media, Alta o Sospesa.

#### Testo

Il **_Testo_** consente di modificare ciò che appare sul canvas a video nella label di un elemento. Il valore inserito sarà anche un nome secondario dell'elemento, filtrabile anch'esso e che apparirà nella tab **_Dati_** dell'esecuzione di una task.

#### Definire gli Utenti, Utenti cc e Responsabili, le Variabili da richiedere e gli Allegati

Tramite l'entrata **_Utenti_**, **_Utenti cc_** e **_Utenti resp_** è possibile definire chi dovrà svolgere una determinata task.
Cliccando questi attributi verrà aperto un popup dove sarà possibile, tramite delle checkbox, marcare gli utenti che dovranno svolgere la task, supervisionarla o che saranno i responsabili del loro svolgimento.

Analogamente, è possibile definire i dati che, gli utenti precedentemente, assegnati dovranno inserire.
Questo è possibile tramite l'entrata **_Variabili da richiedere_** che, una volta cliccata, aprirà una nuova pagina dedicata all'inserimento delle variabili.  
Questa pagina, chiamata **_Magazzino delle variabili_**, viene trattata e approfondita nella sua sezione apposita [qui]().
Per aggiungere una Variabile da richiedere, basta prenderne una dalla lista di sinistra e trascinarla nel canvas.
Così facendo, gli utenti a cui è assegnata la task, dovranno inserire i valori delle variabili così definite.

Infine, è possibile definire gli allegati da definire tramite l'entrata **_Allegati_**.  
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

### Scadenze/Tempi

L'approfondimento sulle **_Scadenze/Tempi_** è presenta nella sua sezione [qui](#pianificazione-e-scadenze).