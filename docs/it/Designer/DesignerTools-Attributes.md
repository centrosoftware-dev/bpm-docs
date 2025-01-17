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

Nel menù contestuale si trova un altro aspetto fondamentale assegnare il processo agli utenti che dovranno inserire le variabili precedentemente dichiarate.
Nel dialog che viene aperto è anche possibile far sì che il flow non potrà essere iniziato prima di essere stato assegnato. 

![](../../assets/inserimentoVarUserTask.gif)

È inoltre possibile richiedere l'inserimento di allegati e lo svolgimento di operazioni, sempre tramite il menù contestuale, alla voce **_Allegati da richiedere_** e **_Operazioni_**.  
Uno Start consente di effettuare delle operazioni **_In esecuzione_** e ad **_Esecuzione terminata_**.  

# Menù contestuale e Pannello Attributi

Il menù contestuale appare quando si preme il tasto destro del mouse su un oggetto nel canvas. In base all'oggetto cliccato le entrate saranno differenti.  
Analogamente, a destra del canvas, si trova il Pannello Attributi, che molto spesso presenta entrate comuni a quelle del menù contestuale.

## Allineamento

Selezionando più oggetti (1) è possibile spostarli in massa seguendo l'allineamento dell'elemento su cui si è cliccato il tasto destro. 
{ .annotate }

    1.  Per selezionare più oggetti è necessario tenere premuto CTRL o SHIFT quando si va a cliccare col tasto sinistro su un elemento.

Gli oggetti che possiedono un'etichetta hanno anche la possibilità di gestire il suo allineamento.

## Aspetto

Contenitore di attributi legati ai font di un oggetto o della sua targhetta.
Generalmente, in un oggetto è possibile cambiare:

* Colore del testo.
* Colore dello sfondo.
* Colore e spessore e del bordo.

## Manipolazione oggetto

Oltre al tagliare e copiare un oggetto, è possibile spostarlo da una pagina ad un'altra del processo tramite l'entrata **_Sposta oggetto alla pagina ..._**.

## Manipolazione Testo e Label

Nel menù contestuale è presente l'entrata **_Sposta testo_** per spostare l'etichetta dell'oggetto dove si vuole nel canvas. Essa rimarrà ancorata al punto dove si è spostata.
L'entrata **_Modifica Testo_** consente di modificare il testo della Label.

## Impostare un oggetto come oggetto di avvio
* Imposta come oggetto di avvio, per rendere l'oggetto il punto di partenza del processo.
* Utenti e Responsabili, per denominare gli utenti che devono eseguire un task, iniziare il progetto o prendere decisioni riguardanti il processo.
* Variabili da richiedere
* Allegati da richiedere
* Operazioni
* Formula di validazione
* Elimina

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


