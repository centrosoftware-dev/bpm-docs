# Modelli di processo

Un **modello di processo** configura un flusso eseguibile: attivita, variabili, assegnazioni, autorizzazioni, regole, integrazioni e rappresentazione grafica. Ogni esecuzione del modello genera un'istanza di processo.

Il **Designer di processo** e l'ambiente nel quale si crea e si modifica il modello. Comprende il canvas, le barre degli strumenti, i pannelli delle proprieta e gli editor collegati.

## Accedere ai modelli

La voce **Modelli di processo** del menu principale apre l'elenco dei modelli, organizzati per gruppo. Una barra di ricerca consente di filtrare l'elenco; da qui si puo aprire un modello esistente oppure crearne uno nuovo.


## Creare un modello di processo

Il modello rappresenta il flusso tramite oggetti collegati, ciascuno con un ruolo specifico.  

Gli oggetti si dispongono sul canvas mediante trascinamento.  

Creare un nuovo modello di processo è semplice: basta recarsi nel pannello delle impostazioni in alto a sinistra, poi cliccare la voce **Modelli di Processo** ed infine cliccare **Nuovo modello di processo**.

![Creazione di un modello](../assets/modelli-di-processo/new-model.gif "Creazione di un modello")

---

## Gli strumenti del Designer

Gli strumenti del Designer sono suddivisi in più sezioni: 

1. Una [barra superiore degli strumenti](designer/barra-degli-strumenti.md) con i comandi generali per il modello, gli elementi e i loro attributi.

2. Una barra laterale sinistra con il [catalogo degli elementi](elementi/index.md) disponibili.

3. Un [pannello degli attributi](designer/pannello-attributi.md) a destra, che mostra le proprieta dell'elemento selezionato. Se viene chiuso, si puo riaprire premendo ++f4++.

4. Una sezione nella parte inferiore contente le etichette delle diverse pagine di lavoro attualmente aperte e una scroll bar per regolare lo zoom su queste pagine. Inizialmente la pagina selezionata è quella del processo, in cui troviamo tutti gli elementi grafici del flusso.  
Subito a sinistra si trova la [pagina Info](pagina-info.md), dedicata alle impostazioni del modello. Le altre schede vengono aggiunte quando si aprono strumenti come l'[Editor delle variabili](../parti-comuni/editor-variabili/index.md).

![Componenti del Designer di processo](../assets/modelli-di-processo/designer-parts.png "Componenti del Designer di processo")

---

## Costruire un modello di processo

Quando creiamo un nuovo modello di processo non troveremo il canvas completamente vuoto, ma sarà già presente un singolo elemento, un punto di inizio, detto Start.

Nella maggior parte dei casi, un flusso ha un inizio e almeno una fine.

L'inizio, può essere sovrascritto: cliccando tasto destro su un altro elemento presente sul canvas, dal menu contestuale si può scegliere l'opzione **Imposta come oggetto di avvio**. Così facendo il flusso inizierà dall'elemento impostato come oggetto di avvio.

!!! danger "Rimozione dello Start"
    È possibile rimuovere lo Start, ma è un comportamento non convenzionale e tendenzialmente sconsigliato in quanto il processo richiederà all'utente di inserire direttamente le variabili da richiedere.

Dalla sidebar di sinistra, sarà ora possibile iniziare a disegnare il processo trascinando direttamente gli oggetti sul canvas. 

Ogni elemento può o deve essere collegato ad altri elementi o a se stesso tramite i **Link**, frecce orientate che indicano i vari percorsi che il processo può instradare.  

Selezionando uno degli oggetti disegnati, sulla destra si aprirà il pannello degli attributi ad esso riferiti. 
Ogni oggetto ha delle proprietà, alcune di esse sono comuni a tutti, mentre altre sono specifiche del tipo di oggetto.   






