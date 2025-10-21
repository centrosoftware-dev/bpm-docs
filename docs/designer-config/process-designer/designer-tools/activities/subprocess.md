# Sottoprocesso

![immagine sottoprocesso](../assets/activities/subprocess-img.png)

I **sottoprocessi** sono un tipo particolare di task, rappresentati anche graficamente in modo diverso, che funzionano come **contenitori** di processi secondari.  


## Utilizzo

- Aumentare la **leggibilità** e la **pulizia** grafica di processi complessi, isolando parti ripetitive o di dettaglio.
- **Riutilizzare logiche** che devono essere eseguite più volte in base a condizioni dinamiche.


## Caratteristiche Generali

![configurazione sottoprocesso](../assets/activities/subprocess-config.png)

Ci sono due modalità operative principali, il menu di configurazione varia leggermente in base alla tipologia scelta:

### Sottoprocesso Singolo

- È un processo "figlio" isolato dal flusso principale.
- Serve solo per questioni di organizzazione e leggibilità: la logica è definita dentro il sottoprocesso e viene eseguita una sola volta.
- Si può vedere come una "scatola nera" che puoi aprire per guardare il dettaglio tecnico.

### Sottoprocesso Ricorrente

Quando serve eseguire lo stesso sottoprocesso più volte, su dati diversi.
In pratica, il sottoprocesso "gira" su ogni riga di un gruppo di variabili.
La configurazione di un sottoprocesso ricorrente include:

## ----------- ARRIVATO QUA ------------------

## Modalità di esecuzione

### Parallelo
Tutte le istanze vengono avviate nello stesso momento subito.

### Sequenziale
Ogni istanza parte solo dopo che la precedente è completata.

## Condizione
: una formula logica che stabilisce se eseguire il sottoprocesso per una certa riga.
  Se la condizione è falsa, quella riga viene ignorata.
## Formula testo
: una formula che genera il nome di ciascuna istanza del sottoprocesso, così che nella Todo List gli utenti capiscano a quale "riga" si riferisce ogni task.

## Durata prevista
Se il sottoprocesso non è ancora esploso, ossia non sono ancora generate tutte le istanze, il BPM usa questa stima della durata "complessiva" come riferimento di **pianificazione**.
