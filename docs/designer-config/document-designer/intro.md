# Designer di classi documentali

Il **_Designer di classi documentali_** è lo strumento del BPM dedicato alla **creazione e gestione delle classi documentali**, ovvero delle strutture dati che i processi utilizzano per raccogliere, archiviare e gestire le informazioni.  
Grazie a questa sezione, è possibile definire in modo semplice e intuitivo **i campi, i tipi di dato e le relazioni** che compongono ciascuna classe, permettendo di modellare la logica informativa dei processi aziendali.

![IMG1]  
_Descrizione immagine: schermata iniziale del Designer di classi documentali con la lista delle classi esistenti e i pulsanti per crearne di nuove._

## Scopo della sezione

L’obiettivo principale del **Designer di classi documentali** è fornire all’utente un’interfaccia chiara e completa per:
- Creare nuove classi documentali partendo da zero  
- Modificare strutture già esistenti  
- Gestire campi e proprietà dei documenti  
- Definire le relazioni tra le diverse classi documentali o con i modelli di processo  

Questa sezione è quindi essenziale per costruire la base dati su cui i processi BPM possono operare, garantendo **coerenza, tracciabilità e integrità delle informazioni**.

![IMG2]  
_Descrizione immagine: vista di una classe documentale aperta con i dettagli dei campi e delle proprietà configurabili._

## Elementi principali

All’interno del **Designer di classi documentali**, l’interfaccia si compone generalmente di tre aree operative principali:

1. **Elenco classi documentali**  
   Nella parte sinistra dello schermo è presente la lista di tutte le classi create o disponibili nel sistema.  
   Da qui è possibile selezionare una classe esistente o crearne una nuova tramite l’apposito pulsante **“Nuova classe documentale”**.

2. **Editor di struttura**  
   Al centro della schermata si trova l’area dedicata alla definizione dei campi.  
   È possibile aggiungere nuovi campi, modificarne le proprietà o impostare regole specifiche di validazione e comportamento.

3. **Proprietà e configurazioni avanzate**  
   Nella parte destra si trovano le impostazioni aggiuntive, come le relazioni con altri oggetti, i permessi, le opzioni di visualizzazione e le regole di comportamento nei processi.

![IMG3]  
_Descrizione immagine: interfaccia del Designer con evidenziate le aree principali — elenco a sinistra, editor centrale e pannello proprietà a destra._

## Tipologie di campi

Ogni classe documentale può contenere diversi tipi di campo, ciascuno pensato per gestire un tipo di informazione specifica.  
Alcuni esempi comuni includono:
- **Campo testo:** per l’inserimento di descrizioni o note  
- **Campo numerico:** per quantità, importi o valori misurabili  
- **Campo data/ora:** per registrare eventi temporali  
- **Campo elenco (dropdown):** per selezioni predefinite  
- **Campo relazione:** per collegare la classe ad altre entità o processi  

Nei capitoli successivi verranno approfondite le impostazioni di ciascun tipo di campo, con esempi pratici e consigli di configurazione.

![IMG4]  
_Descrizione immagine: tabella o finestra che mostra l’elenco dei campi con nome, tipo, obbligatorietà e altre proprietà._

## Relazioni e integrazioni

Il Designer consente anche di **stabilire relazioni tra classi documentali**, permettendo così di collegare i dati e creare strutture più complesse.  
Le relazioni possono essere:
- **Uno-a-uno:** un documento collegato a un solo record di un’altra classe  
- **Uno-a-molti:** un documento che contiene o fa riferimento a più elementi correlati  
- **Molti-a-molti:** una relazione bidirezionale tra più record di diverse classi  

Queste relazioni sono utili per la creazione di **flussi documentali dinamici**, che possono essere gestiti e richiamati all’interno dei modelli di processo.

![IMG5]  
_Descrizione immagine: diagramma o esempio visivo di una relazione tra due classi documentali._

## Buone pratiche

Per garantire la massima efficienza nella gestione delle classi documentali, si consiglia di:
- Mantenere una **struttura coerente** dei nomi dei campi e delle classi  
- Documentare chiaramente lo scopo di ciascun campo  
- Evitare la duplicazione di informazioni già presenti in altre classi  
- Utilizzare i campi relazione per collegare dati condivisi tra processi  

Queste accortezze semplificano la manutenzione del sistema e migliorano la leggibilità dei modelli nel tempo.

![IMG6]  
_Descrizione immagine: esempio di schermata con suggerimenti o best practice per la gestione delle classi documentali._

## Approfondimenti

I capitoli successivi entreranno nel dettaglio di ciascun aspetto del **Designer di classi documentali**, illustrando con esempi pratici:
- La creazione di una nuova classe  
- La configurazione avanzata dei campi  
- La gestione delle relazioni e dei permessi  
- L’integrazione con i modelli di processo  

??? info "Suggerimento"
    Se stai iniziando a costruire i tuoi primi modelli di processo, ti consigliamo di creare prima le classi documentali fondamentali.  
    In questo modo potrai associare i dati strutturati fin dall’inizio, evitando modifiche successive ai flussi.