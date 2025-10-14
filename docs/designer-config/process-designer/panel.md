## Pannello attributi

Sulla destra del canvas si trova il **_Pannello Attributi_** che, molto spesso, presenta entrate comuni a quelle del menù contestuale.

### Aspetto

Nel Pannello attributi, **_Aspetto_** contiene tutte le informazioni di un oggetto relative all'allineamento della targhetta, ai colori e ai font.

### Dati

La sezione **_Dati_** comprende le proprietà più specifiche di un singolo elemento.  

Gli attributi elencati forniscono informazioni e impostazioni per personalizzare il comportamento e la gestione della task all'interno del flusso. Si tratta di proprietà che riguardano ambiti funzionali, priorità, gestione utenti e operazioni specifiche, oltre ad altre configurazioni utili per determinare come la task interagisce con il sistema o con altri elementi del flusso.

#### Ambito e Descrizione

L'**_Ambito_** è un campo di testo libero.  
Dalla to-do list è possibile ricercare tutte le task con uno stesso **_Ambito_**.

Impostando la **_Descrizione_** è possibile fornire informazioni testuali riguardanti una task, utili a chi dovrà poi dovrà svolgerla. Apparirà infatti nella tab **_Istruzioni_** quando un utente starà eseguendo la task.


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