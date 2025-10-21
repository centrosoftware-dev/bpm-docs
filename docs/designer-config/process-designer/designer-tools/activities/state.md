# Stato

![Immagine stato](../assets/activities/state.png)

Lo **Stato** è un'entità astratta all'interno del processo BPM che rappresenta un **punto significativo** nell’evoluzione del flusso, ma **non costituisce un'attività eseguibile (task)**. Si tratta di una **milestone logica** che fotografa la condizione globale del processo in un determinato momento.

Ogni processo definisce autonomamente i propri stati in funzione del dominio applicativo. Esempi comuni includono:

- `INSERITO`
- `IN APPROVAZIONE`
- `APPROVATO`
- `CONCLUSO`
- ...


## Utilizzo

- Serve come **indicatore del progresso** del processo.
- Può essere inserito all'interno del workflow di processo in modo da **attivarsi automaticamente** al completamento dei task ad esso precedenti, permettendo di **monitorare, filtrare o classificare** l’avanzamento dei processi nel sistema.


## Caratteristiche principali

- Lo **stato** non ha una logica esecutiva propria ma viene raggiunto a seguito dell’esecuzione di uno o più task o transizioni definite nel flusso.
- Gli stati sono **esclusivi**: in un determinato momento, un processo può trovarsi in **uno e un solo stato**.
- La transizione da uno stato a un altro può essere **automatica** (guidata dalla logica del workflow) o **manuale** in base ad un'attivazione forzata da un utente owner del processo.
- Nel pannello degli attributi sono presenti alcune voci specifiche per l'oggetto **State**, spiegate nel dettaglio [**qui**](../../panel.md#stato)


## Menu contestuale

Nel menu relativo all'oggetto **Stato**, accessibile tramite tasto destro, sono presenti una serie di funzioni che permettono di configurarne diversi aspetti.  
Per questo elemento le funzioni disponibili sono sostanzialmente quelle standard, ciascuna illustrata in dettaglio nella sezione dedicata al _menu contestuale_, che puoi trovare [**qui**](../menu.md).

L'unica cosa da notare per l'oggetto _State_ è che le _Operazioni_ si possono agganciare solo all'evento di '**attivazione**' dello stato ovvero: il momento in cui stato è stato raggiunto dal workflow oppure quando questo è stato attivato manualmente dall'utente.



