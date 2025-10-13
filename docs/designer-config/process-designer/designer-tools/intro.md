# Designer Tools

Il **_Designer Tools_** è il pannello che si trova sulla sinistra.

Alla sommità è situata la search bar, digitando al suo interno è possibile filtrare gli oggetti delle varie sezioni. I risultati della ricerca appariranno nella ciascuno nella propria sezione.

Il pannelo è poi suddiviso in 6 sezioni.

### Attività

Sezione contenente gli elementi principali di un flusso:

- [Puntatore](./activities/pointer.md)

- [Link](./activities/link.md)



#### Start

Lo **_Start_** è il punto di inizio di ogni flusso manualmente azionato.  

Un flusso può avere più Start. In tal caso, alla partenza del processo, verrà richiesto all'utente da quale Start partire.  

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

##### Rileva inizio attività

Se impostato su true, rileva la data di inizio dell'attività e non viene dedotta dalla fine della task precedente.

##### Skip activity

Se impostato su True salterà l'esecuzione della task. 

!!! info "Perché inserire nel disegno una task che non verrà mai eseguita?"
    L'attributo **_Skip activity_** serve solamente a rendere il disegno più fruibile, facendo capire all'utente finale il modo in cui determinate azioni vanno svolte o suddivise.

##### Sottoprocesso

Se impostato su True, rende l'Attività un Sottoprocesso.  
Per approfondire il concetto di **_Sottoprocesso_** scendi alla sezione Sottoprocesso o clicca [qui]().

##### Testo pulsante esegui

Attributo di tipo testuale. Il testo inserito apparirà al posto di "Esegui" sul bottone esegui.

##### Tipo attività

Attributo che va scelto da un dropdown. Serve come filtro.

##### Utilizza calendario

**_Utilizza calendario_** è un attributo che aggiunge alle **_Scadenze/Tempi_** la logica per capire quando un giorno è lavorativo o meno, basandosi sul calendario.
Se una task ha una data di scadenza, **_Utilizza calendario_** fa sì che i giorni del weekend non vengano contati.  

Il concetto di pianificazione e scadenze è approfondito [qui](#pianificazione-e-scadenze)

#### Stato processo

L'elemento **_Stato processo_** serve a visualizzare graficamente lo stato del processo.
Uno Stato processo consente di effettuare delle operazioni solo **_In attivazione_**.

Nella sezione Gestione ci sono 2 attributi:

##### Blocca edit

Quando si entra nello stato il documento non è più modificabile dal magazzino. Anche gli utenti con le dovute autorizzazioni non possono modificare i dati immessi nelle variabili nel processo.

##### Stato di chiusura

Impostando questo attributo a True, si sancisce la fine del processo interrompendo tutte le attività in corso.


#### Sottoprocesso

Un **_Sottoprocesso_** è un processo avviato dall'interno di un altro processo.
Nel canvas dove viene inserito un Sottoprocesso (o un'attività con attributo Sottoprocesso impostato a true) l'elemento apparirà uguale ad una semplice attività, ma con una croce sotto la label descrittiva.  
Cliccando due volte sopra l'elemento, si entra nel canvas del Sottoprocesso.
Le funzionalità sono le stesse di un processo normale. L'unica differenza è nello start, che avviene non appena l'elemento principale del Sottoprocesso entra in esecuzione e alla fine del sottoprocesso si passa all'elemento seguente nel processo principale.  

Gli attributi che differenziano un'attività da un Sottoprocesso sono nella sezione **_Scadenze/Tempi_**. Entrambi questi attributi vengono approfonditi nella loro sezione [qui](#pianificazione-e-scadenze).

### Eventi

La sezione **_Eventi_** raggruppa tutti gli elementi che fungono da Start e gli elementi che fungono da fine.  

!!! note "Variabili da richiedere e Start"
    Essendo tutti elementi predisposti per essere l'inizio di un processo (ad esclusione di quelli di fine processo), è vivamente consigliato di impostare le variabili da richiedere direttamente nello Start.

#### Start

Lo **_Start_** convenzionale è stato trattato [qui](#start).

#### Start su evento

Lo **_Start su evento_** ha la capacità di iniziare un processo quando un evento predefinito che arriva dall'esterno.
Gli eventi sono definiti dai connettori che a loro volta sono elencati nella voce "Elenco connettori" nella sezione "Configurazione" del menù principale.

#### Start a tempo

Lo **_Start a tempo_** ha la capacità di iniziare un processo in modo ricorrente.
Configurando lo **_Start a tempo_** è possibile impostare una descrizione e ogni quanto tempo far partire nuovamente il processo.  
Le opzioni sono:

* Ricorre ogni giorno.
* Ricorre ogni settimana, dove è necessario scegliere il giorno settimanale in cui il processo ricorrerà.
* Ricorre ogni mese, dove è necessario scegliere il numero del mese in cui far ricorrere il processo, altrimenti si può spuntare il checkbox "Ultimo del mese" per avviare il processo nell'ultimo giorno di ogni mese.

In basso, infine, si ha la possibilità di specificare l'ora in cui partirà il processo.

#### Attesa

Analogamente allo start a tempo, l'**_Attesa_** è un genere di start che, una volta avviato un processo, attenderà il tempo stabilito prima di continuare.  

Configurando l'evento, è possibile impostare una descrizione, il numero di giorni da attendere e cosa fare una volta che il tempo prestabilito sia passato.

Tramite l'inpuit numerico iniziale è possibile stabilire il numero di giorni da attendere. Dopodiché tramite è possibile specificare una sola scelta su che azione dovrà svolgere l'elemento:

* Non attendere oltre.
* Attendi il primo X.
* Attendi che sia il primo, secondo, terzo, quarto o ultimo X del mese.
* Attendi che sia il Y del mese.

X è il giorno della settimana scelto tramite un dropdown.
Y è il giorno del mese impostato tramite input numerico.

Infine è anche possibile far attendere l'inizio fino ad una determinata ora del giorno stabilito tramite un'ultima checkbox e impostando l'orario.

#### Fine e Termina processo

**_Fine e Termina processo_** sono due elementi per dichiarare completato un processo.
La differenza tra i due elementi è che **_Termina processo_** termina tutti i rami paralleli e sottoprocessi attivi.

### Gateway e percorsi

La sezione **_Gateway e Percorsi_** raggruppa gli elementi che consentono di instradare il processo in direzioni diverse dipendentemente dalla configurazione dell'elemento.

#### Percorsi alternativi (exclusive)

L'elemento **_Percorsi alternativi (exclusive)_** permette di dividere il percorso del processo.
Da questo gateway è possibile ramificare in percorsi diversi il processo, ognuno con la propria condizione di instradamento.
Le condizioni dei percorsi sono impostate schiacciando tasto destro sul gateway e cliccando sull'entrata **_Configurazione_**.

Una volta aperto il popup di configurazione, è possibile definire le condizioni di ogni percorso cliccando sui bottoni, uno per percorso, situati accanto alle entrate della colonna "Condizione".

![](../assets/ifGateway.gif)

Dalla configurazione è anche impostabile il percorso da considerare come default che sarà quello che il processo percorrerà se nessuna delle condizioni di uscita risulta come True.

!!! info "Cosa succede se più uscite risultano come true?"

    I **_Percorsi alternativi (exclusive)_** sono scelte che vanno ad instradare il processo in un singolo percorso. Di conseguenza, se più condizioni di uscita risultano come True, il percorso instradato sarà il primo.

#### Percorsi paralleli (parallel)

L'elemento **_Percorsi paralleli (parallel)_** funge da sdoppiatore del percorso principale in ramificazioni parallele.
Tutte le ramificazioni parallele sono contemporanee, ma l'avanzamento varia in base allo svolgimento delle task interne di ognuna.

In questo caso non ci sono condizioni, in quanto tutti i rami andranno eseguiti.

#### Percorsi liberi (inclusive) e Complex

Gli elementi **_Percorsi liberi_** e **_Complex_** sono il contrario dei percorsi exclusive: tutte le condizione d'uscita che risultano come True vengono instradate.

#### Sincronizza

L'elemento **_Sincronizza_** serve a convergere le ramificazioni che si sono create utilizzando i Gateway.
Configurando l'elemento, è possibile definire il Number to pass, ovverosia quali percorsi devono essere arrivati all'elemento per far sì che il processo continui.

### Operazioni

Le **_Operazioni_** sono azioni specifiche e complesse: per questo è presente una sezione dedicata a loro che entra nelle specifiche, approfondendo ogni aspetto del loro funzionamento.  

Clicca [qui]() per saltare alla loro sezione.

### Processi collegati

Analogamente alle operazioni, i **_Processi collegati_** hanno una sezione approfondita [qui]().

### Altro

La sezione **_Altro_** raggruppa gli elementi che non rientrano nel resto delle categorie.

#### Gruppo e Swim lane

L'elemento **_Gruppo_** è un raggruppatore di elementi.
Gli elementi all'interno del **_Gruppo_** possono essere svolti dagli utenti assegnati al **_Gruppo_** stesso.

![Utenti differenti](../assets/differentUsers.gif)

L'elemento **_Swim lane_** è analogo a quello di gruppo.
Per aggiungere pioù **_Swim lane_** basta trascinarne quante necessarie nel canvas.
Le **_Swim lane_** suddividono il disegno in corsie, ognuna coi propri utenti associati che potranno svolgere le azioni all'interno della propria corsia.

!!! Warning "Multuple associazioni di Utenti"

    Se ad un **_Gruppo_** o una **_Swim lane_** e ad una task interna ad essi sono associati degli utenti e tali utenti differiscono con quelli associati nel contenitore, la task potrà essere svolta **solo** dagli utenti associati alla task stessa.
    <center>**Task Users > Container Users**</center>

#### Image, Casella di testo e Memo.

**_Image_** è un elemento statico, attraverso cui è possibile inserire un immagine all'interno del canvas.  

La **_Casella di testo_** è del semplice testo slegato ad altri elementi. È utile per dare titoli a parti o sezioni del flusso.  

Il **_Memo_** ha la stessa funzionalità di un postit ed è collegabile ad un task tramite il link. Così facendo, tra la task e il **_Memo_** apparirà una linea tratteggiata gialla. È utile per scrivere note e ricordare agli utenti delle informazioni chiave per lo svolgimento di una task.

#### Marker

Il **_Marker_** è uno strumento utilizzato per navigare all'interno del processo tra diverse pagine. Questo risulta particolarmente utile quando si desidera rendere il processo stampabile, ad esempio su un foglio A4, evitando di estenderlo eccessivamente in verticale.  
In questi casi, si aggiunge una nuova pagina, e il **_Marker_** funge da "collegamento" che consente di proseguire con il processo su un'altra sezione. In pratica, è un riferimento che rimanda a un'altra pagina del processo.

