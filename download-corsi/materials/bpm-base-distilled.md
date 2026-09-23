# BPM Base

## Introduzione

**BPM** (Business Process Modeler) è il prodotto di Digit Company per la modellazione grafica di processi aziendali: un motore di workflow che permette di digitalizzare attività oggi gestite in modo destrutturato — scambi di e-mail, fogli Excel, personalizzazioni ad hoc sui vari sistemi aziendali. Il punto di partenza concettuale è sempre **il processo**: la sequenza di operazioni necessarie a gestire una pratica reale, dalla sua apertura fino alla sua conclusione.

BPM è un prodotto standalone — può funzionare in totale autonomia — ma nella pratica quasi sempre si integra con altri sistemi (un gestionale/ERP per le anagrafiche, SAP, un documentale). Esistono connettori preconfigurati per SAP ("SAM"); l'integrazione con gestionali generici richiede più lavoro custom.

Questo materiale copre i fondamentali del prodotto: architettura client/web, gli oggetti del Designer, la gestione di utenti e gruppi, il magazzino delle variabili, pubblicazione e versionamento, esecuzione e monitoraggio dei processi, allegati, sotto-processi e il sistema di permessi. Il filo conduttore è un caso reale usato a scopo didattico: un processo di **richiesta di autorizzazione investimento**, dall'inserimento della richiesta fino al collaudo di quanto acquistato.

---

## Concetti

### 1. Architettura

#### 1.1 I tre pilastri di ogni soluzione BPM

Ogni soluzione costruita in BPM si basa su tre elementi che ricorrono in tutto il prodotto:

1. **Il processo** — il diagramma di attività, gateway ed eventi.
2. **Utenti e gruppi** — chi fa cosa.
3. **Le variabili di processo** ("magazzino delle variabili") — i dati che il processo porta con sé.

#### 1.2 Client desktop vs. applicazione Web

- **Client desktop**: copre la modellazione/progettazione del processo, la configurazione (utenti, dashboard, report, strutture, opzioni di posta, allegati) e l'uso operativo (avvio/ricerca processi, To-Do List). È l'ambiente in cui il consulente passa la maggior parte del tempo di progettazione (frames/013_002835_client-vs-architecture-overview.jpg).
- **Applicazione Web**: solo operativa (To-Do List, avvio nuovo processo, ricerca, storico) — nessuna superficie di configurazione/progettazione. È stata recentemente riscritta secondo il tema visivo "Portale 6.0" e, secondo il docente, è destinata a raggiungere piena parità funzionale con il client fino a diventare il **client consigliato per gli utenti finali** (viene usato internamente anche in Digit). Storicamente il web era indietro su alcune funzionalità (es. la gestione allegati era diversa non solo esteticamente, ma anche funzionalmente); al momento della registrazione la parità è quasi raggiunta, con un residuo di lavoro stimato in circa un trimestre.
- Il web utilizza un **modello a pannelli impilati**: passando dalla To-Do List al dettaglio di un processo, la To-Do List resta "dietro" (recuperabile tramite un'icona di stack) invece di essere sostituita da una navigazione a pagina intera — così più record possono restare aperti contemporaneamente.
- Attenzione al layout: client e web usano font e spaziature diverse (il web è più "arioso", basato su Bootstrap); una schermata progettata in uno dei due ambienti va sempre verificata anche nell'altro prima del rilascio. Le preferenze di colonne/griglia (es. colonne della To-Do List) sono salvate **per utente ma separatamente** tra client e web.
- Il client desktop resta comunque l'ambiente primario per **progettazione/configurazione** e test rapidi in locale durante la costruzione di un processo.

---

### 2. Il Designer e gli oggetti di processo

#### 2.1 Layout e flusso di lavoro del Designer

Il Designer è organizzato in tre pannelli: la **palette degli oggetti/strumenti** (raggruppati in Attività, Eventi, Gateway, Operazioni/automazioni e altri oggetti di supporto), un **pannello proprietà** (contestuale a ciò che è selezionato — cliccando sull'area bianca del canvas compaiono le proprietà del processo, cliccando lo Start compaiono le proprietà dello Start) e il canvas stesso. Una ribbon in alto raccoglie i comandi di disegno/allineamento.

- Più modelli di processo possono essere aperti contemporaneamente in tab paralleli, e le tab possono essere affiancate in vista side-by-side (utile per confrontare o copiare elementi tra due modelli) (frames/014_003629_designer-menu-tour.jpg).
- **Buona prassi**: abbozzare una versione grezza del processo rapidamente — anche in diretta con il cliente/l'utente business — prima di raffinare nomi, regole e dettagli. È una prassi iterativa normale, non un mancato lavoro di pianificazione: bozza → prova → correzione del tiro (frames/016_004116_sketch-first-refine-later.jpg).
- **Terminologia**: "Modello di processo" è il template/design riutilizzabile; "Processo" è un'esecuzione/istanza in corso di quel template.

#### 2.2 Le shape principali

| Shape | Significato |
|---|---|
| Cerchio verde | Evento di **Start** — dove inizia un'istanza di processo |
| Rettangolo | **Task/Attività** — lavoro da svolgere da parte di un utente/gruppo |
| Shape rotonda "stato" | **Stato** — un'etichetta di milestone/checkpoint (non è lavoro, è un marcatore di stato, es. "Inserito", "Approvata") |
| Rombo | Marcatore implicito di ramo su una freccia semplice condizionata, oppure l'oggetto **Gateway** dedicato |
| Box distinto | **Sotto-processo** — un mini-diagramma annidato, progettato separatamente |
| Cerchio "Fine" | Marcatore di fine opzionale, puramente cosmetico |

La notazione utilizzata è un **sottoinsieme dello standard BPMN** — non tutte le shape BPMN sono implementate, solo quelle con una funzionalità rilevante per BPM.

**Attività (Task)**

- Trascinando un'attività sul canvas le viene assegnato un codice interno permanente (Activity1, Activity2,...) usato come ID immutabile; il **nome visualizzato**, leggibile dagli utenti, si imposta separatamente con tasto destro > "Modifica testo" (es. "Presa in carico da ufficio sicurezza") (frames/017_004219_creating-and-naming-activities.jpg).
- Consiglio: nomi chiari ma non troppo lunghi. Tasto destro > "Sposta testo" permette di staccare visivamente un'etichetta dalla propria shape (restando comunque logicamente collegata) — utile occasionalmente per l'evento di Start (es. rietichettarlo "Inserimento richiesta").
- Lo strumento **Link** disegna i collegamenti tra le shape, creando punti di ancoraggio; la ribbon offre strumenti di allineamento/uniformazione delle dimensioni per tenere ordinati i diagrammi grandi (i diagrammi sono visti dagli utenti finali, quindi la leggibilità conta) (frames/018_004444_connecting-activities-with-the-link-tool.jpg).

**Stati (milestone)**

Un oggetto "Stato" marca un punto importante nel ciclo di vita complessivo del processo, indipendentemente da quale specifica attività sia in corso (es. "Inserito" all'inizio, "Approvata" alla fine, "Annullata" in caso di annullamento). Gli stati sono puramente etichette, senza alcun significato di sistema al di là dell'essere interrogabili/ricercabili in seguito (es. interrogare "tutte le richieste annullate") (frames/019_004648_state-objects-milestones.jpg).

**Fine vs. Termina processo**

- **Nessun oggetto di fine esplicito è necessario**: la regola generale di BPM è "quando non ci sono più attività da fare, il processo è concluso" — automaticamente, senza alcuna configurazione particolare.
- **Fine**: opzionale, puramente un marcatore visivo/di documentazione, senza alcun effetto funzionale (frames/020_004757_end-is-optional-cosmetic.jpg).
- **Termina processo**: funzionalmente diverso — il raggiungimento di questo oggetto uccide/interrompe forzatamente ogni altro ramo ancora in corso di quella istanza di processo (frames/021_004830_fine-vs-termina-processo.jpg).

#### 2.3 Diramazioni: condizioni e gateway

Esistono due modi — equivalenti ma con diversa chiarezza — per esprimere la logica di diramazione in BPM, entrambi basati sul **motore delle formule** (vedi 4.7):

1. **Freccia semplice condizionata** (il "baffetto"): tasto destro sulla freccia in uscita > "Condizione di abilitazione" e scrittura di una formula (es. `esito approvazione CDG = "Approvata"`). Compatta, ma il motore **non** impone la mutua esclusività — le condizioni in uscita possono sovrapporsi o lasciare vuoti; è responsabilità di chi progetta scrivere condizioni complementari (frames/047_023344_condition-on-a-transition-arrow.jpg).
2. **Oggetto Gateway** (il rombo in palette): doppio clic/tasto destro > "Configurazione" mostra *tutti* i percorsi in uscita e le relative condizioni in un'unica schermata; le valuta in ordine e prende il primo match vero, con un ramo marcabile come **default/"else"** (quindi N rami richiedono solo N−1 condizioni esplicite). Più "professionale" secondo lo standard BPMN e più autoesplicativo nel diagramma, particolarmente utile con 3 o più rami, al costo di un po' più di spazio nel disegno (frames/048_023529_exclusive-gateway-object.jpg).

Varianti di Gateway:

- **Esclusivo** (il rombo di default): esattamente un percorso in uscita si attiva — un if/else rigoroso.
- **Parallelo**: si dirama in rami simultanei (es. "Collaudo" e "Parte amministrativa" partono insieme dopo l'approvazione); la stessa shape Gateway si riusa a valle per **sincronizzare**/attendere che tutti i rami diramati finiscano prima che il flusso prosegua. Nota: è *possibile* disegnare più frecce non condizionate in uscita da un semplice task con lo stesso effetto, ma non è BPMN rigoroso — il Gateway è il modo pulito per esprimerlo (frames/050_024327_parallel-gateways-fork-join.jpg).
- **Inclusivo**: una via di mezzo — un qualsiasi sottoinsieme (0, 1 o più) dei rami in uscita può attivarsi in base alle condizioni, utile quando i rami non sono né puramente alternativi (esclusivo) né puramente obbligatori insieme (parallelo) (frames/051_024543_inclusive-gateway.jpg).

#### 2.4 Visualizzazione a runtime

Consultando un'istanza di processo in esecuzione, il diagramma colora l'avanzamento (frames/045_022116_diagram-color-coding.jpg):

- **Grigio** = attività già eseguita
- **Giallo** = attività in corso ("ha il pallino/token")
- **Verde** = stato attivo (un oggetto Stato attualmente in vigore)
- **Verde chiaro** = "pianificata" — attività che il motore sa già che raggiungerà in futuro (alimenta la **vista Gantt/pianificazione**); questo insieme si aggiorna dinamicamente man mano che i dati vengono raccolti, poiché il percorso futuro può dipendere da condizioni non ancora note
- Bianco = non ancora visitata

---

### 3. Utenti e assegnazione attività

#### 3.1 Ruoli per attività

Per ogni attività, BPM permette di indicare (frames/006_000848_users-roles-executor-responsible-cc.jpg):

- **Esecutore** — la persona/il gruppo che trova il task nella propria To-Do List. Usato in circa il 90% dei casi reali.
- **Responsabile** — può smistare il task a un membro specifico del proprio gruppo.
- **In conoscenza** (CC) — deve solo sapere che l'attività è avvenuta.

#### 3.2 Due modalità di assegnazione

1. **Assegnazione diretta al gruppo** (il caso più comune): si assegna un **gruppo** (es. "Controllo di gestione") come Esecutore. Tutti i membri del gruppo vedono il task nella propria To-Do List; il primo che agisce lo completa e il processo avanza. Si usano gruppi invece di singoli individui perché "le persone cambiano, i ruoli/gruppi restano"; i gruppi sono tipicamente **costruiti ad hoc per il singolo processo** piuttosto che importati integralmente da Active Directory (i gruppi AD raramente rispecchiano la granularità realmente necessaria) (frames/024_005637_assigning-a-group-as-task-executor.jpg).
2. **Assegnazione poi esecuzione**: si spunta il flag "Task deve essere assegnato prima di poter essere eseguito" — aggiunge un passaggio esplicito di smistamento in cui un Responsabile sceglie manualmente una persona specifica del gruppo, e solo quella persona vede poi il task. Più burocratico; usato selettivamente (es. scenari su commessa/progetto con un passaggio di triage in ufficio tecnico) (frames/025_005815_must-be-assigned-before-execution-flag.jpg).
3. **Assegnazione dinamica tramite una variabile di tipo Utente**: la finestra "Utenti e responsabili" elenca anche le **variabili di tipo Utente** del processo (es. "richiedente") come possibili esecutori — si sceglie la variabile e il task viene instradato a chiunque quella variabile contenga in quel momento. Uso classico: rimandare un task a chi ha originariamente inoltrato la richiesta (frames/049_024235_dynamic-assignment-to-a-process-variable-user.jpg).

#### 3.3 Nota per la fase di sviluppo

Un'attività temporaneamente lasciata senza utente assegnato è visibile solo all'amministratore — va bene durante la progettazione/i test, ma va sistemata prima del go-live (ogni attività deve avere un proprietario reale).

---

### 4. Le variabili di processo (il magazzino)

Il **magazzino delle variabili** è l'unica superficie di progettazione che contiene tutti i campi dati che un processo porta con sé — si accede da Strumenti > "Inserimento modifica variabili", e appare come una pagina/tab aggiuntiva del processo (frames/028_010543_opening-the-variable-warehouse.jpg).

Modello mentale di progettazione: si abbozza il processo → si ragiona su quali dati devono entrare/uscire in ogni punto → si creano le variabili corrispondenti nel magazzino → poi, per ogni attività, si trascina il sottoinsieme rilevante tramite **"Variabili da richiedere"** (vedi 4.2). Le variabili generano automaticamente i campi database sottostanti — non serve progettare tabelle/SQL a mano.

- Le variabili possono essere organizzate in più **pagine** (tab), convenzionalmente prefissate `01`, `02`, `03`... poiché le pagine si ordinano alfabeticamente. Buona prassi: seguire liberamente il flusso cronologico del processo nell'organizzare le pagine, per leggibilità (non obbligatorio).
- I campi possono essere allineati/ridimensionati (multi-selezione con Ctrl) per un layout ordinato lato utente finale — la superficie di progettazione è letteralmente ciò che l'utente vedrà.

#### 4.1 Tipi di variabile

| Tipo | Note |
|---|---|
| Stringa (String) | Testo libero, limite di default 250 caratteri (adatto a codici/campi brevi tipicamente provenienti da un ERP); può essere flaggata multiriga |
| Numerico | Può essere flaggato come **Contatore** auto-incrementante (perpetuo, oppure raggruppato/azzerato da un altro campo, es. azzeramento per "anno") |
| Booleano | Renderizzato di default come checkbox, oppure come **Bottone** statefull/stateless — vedi 4.8 |
| Data | Le impostazioni di base controllano principalmente la formattazione |
| Valuta | Una specializzazione del tipo numerico |
| Memo | Testo lungo/blob, lunghezza di fatto illimitata, adatto a note formattate/lunghe |
| Lista Valori (Value List) | Un insieme piccolo e fisso di scelte (una dropdown); supporta un **codice di iscrizione** interno separato dall'etichetta visualizzata, così rietichettare non rompe i codici già memorizzati |
| Utente (User type) | Limitato al registro di utenti/gruppi BPM; può essere ristretto a un gruppo specifico tramite "Tipo impostazioni di base" |
| Etichetta (Label) | Testo di visualizzazione read-only, non persistito, con editor rich-text — vedi 4.4 |

#### 4.2 "Variabili da richiedere" (il sottoinsieme per singolo task)

È la controparte, a livello di ogni Task/Start/bottone, del magazzino globale: tasto destro su un task (o su una variabile, per il proprio sotto-form) > "Variabili da richiedere" e trascinamento dei soli campi rilevanti in quel punto (frames/031_012035_variabili-da-richiedere-per-task.jpg).

Relazione chiave: il magazzino e la schermata "variabili da richiedere" di ogni task sono **collegati per nome della variabile** (fonte unica di verità per variabile, un solo valore per istanza di processo) ma **indipendenti in layout/posizionamento** — rimuovere una variabile dalla schermata di un task non la cancella dal magazzino né azzera il suo valore altrove.

Impostazioni locali/per-task su una variabile posizionata (indipendenti dai default a livello di magazzino):

- **Obbligatorio** — impostabile globalmente nel magazzino oppure, come buona prassi, localmente per task (poiché un campo può essere obbligatorio in un punto del processo ma non in un altro).
- **Sola lettura / "Ridolli"** — es. per mostrare dati di contesto a monte a un utente di un task successivo senza permettergli di modificarli (pattern comune: rimostrare richiedente/data/tipo come sola lettura su un task a valle).
- **Formula di validazione** locale (vedi 4.7).

**Scorciatoia esporta/importa**: una pagina (o l'intero layout "variabili da richiedere" di un task) può essere esportata su file locale e importata in un altro task, evitando di ritrascinare manualmente molti campi — molto usato quando si riutilizza un layout (es. copiare il form dello Start su un successivo task "Revisione da parte del richiedente") (frames/032_012254_export-import-variable-layouts.jpg).

#### 4.3 Proprietà fondamentali di una variabile

- **Nome** — la chiave interna/DB; **immutabile** una volta creata (frames/034_013929_variable-name-is-immutable.jpg).
- **Descrizione** (etichetta) — liberamente modificabile, localizzabile, mostrata accanto al campo; può essere abbreviata (es. "Rich.") indipendentemente dal nome sottostante.
- **Descrizione su interrogazioni** — un'etichetta separata usata specificamente nelle colonne delle griglie di ricerca, che può essere più verbosa/svincolata dal contesto rispetto all'etichetta nel form.
- **Obbligatorio / Ridolli (sola lettura)** — come sopra, impostabile a livello globale o locale.
- **Variabile senza salvataggio** — valore non persistito su DB, puro stato di interfaccia, tipicamente abbinato a un campo di visualizzazione calcolato tramite formula che non si vuole memorizzare (frames/035_014300_variabile-senza-salvataggio.jpg).
- **Sottocategoria** — assegnare la stessa etichetta di sottocategoria a un gruppo di variabili selezionate con Ctrl disegna una barra divisoria a tutta larghezza sopra di esse nel form, per organizzare visivamente form densi; la sottocategoria della variabile più in alto determina la posizione della barra.
- **Testo di aiuto** — tooltip mostrato al passaggio del mouse, utile per guidare l'utente (es. "inserire l'importo secondo il modulo XXXX").
- **Valore di default** vs. **Formula per default** — una costante fissa contro un valore iniziale calcolato tramite logica (utente corrente, data corrente, ecc.) — vedi 4.7.
- **Variabili di intestazione** — flag e numerazione (1, 2, 3...) di una manciata delle variabili più importanti (es. numero richiesta, codice stabilimento) affinché emergano in modo prominente in tutta l'applicazione (colonne della To-Do List, intestazioni), oltre alla singola schermata di dettaglio processo.
- **Tag**, flag "nascondi su mobile", dimensione del font (piccolo/medio/grande — differenza visiva minore).
- **Gruppo** — assegna una variabile a un gruppo master-detail (vedi 4.6).

#### 4.4 Variabili di tipo Etichetta (Label)

Una variabile di tipo Label non è un campo DB reale: contiene un "Testo" rich-text che può includere **segnaposto di variabile** (tasto destro > inserisci variabile, es. "Richiesta numero {numero richiesta}") e persino immagini (es. un logo incollato). Un pattern comune: sostituire diversi campi read-only trascinati separatamente su un form con un'unica label che li compone in un'intestazione riassuntiva più curata, riutilizzabile su più schermate di task (frames/033_013319_label-type-variable.jpg).

#### 4.5 Tabelle di origine (lookup) — valore singolo

La "Tabella di origine" trasforma una variabile Stringa da testo libero in una **scelta legata a una fonte dati** (frames/036_014503_tabella-di-origine-source-table.jpg):

- **Tabella locale** — una tabella creata direttamente nel database BPM (prefisso `P_...`), oppure una **vista** SQL creata lì.
- **Dati esterni** — richiede una stringa di connessione (server, database, utente, password; SQL o ODBC) verso il database di un sistema esterno (es. un database usato anche da SAP/SAM). Stringhe di connessione nominate/riutilizzabili possono essere predisposte per azienda/ambiente (es. "SAM A1", "SAM B") invece di codificare una stringa grezza in ogni campo.
- Scorciatoia sconsigliata ma a volte usata: creare una **vista dentro il DB di BPM che a sua volta punta cross-database al sistema esterno** — fragile (si rompe se spostata su un altro ambiente cliente) rispetto a una connessione esterna pulita (frames/064_035352_source-table-lookup-local-vs-external.jpg).
- ODBC funziona ma può essere problematico con alcuni sistemi legacy (es. AS400); web service o connettori dedicati sono spesso preferibili in quei casi.
- La configurazione richiede di mappare la **colonna chiave** (colonna della tabella sorgente → variabile guida, obbligatoria) e poi mappature aggiuntive arbitrarie di **altre colonne** (altre colonne sorgente → altre variabili target), così selezionare un valore riempie automaticamente campi denormalizzati collegati (es. selezionare un codice fornitore riempie automaticamente la sua ragione sociale).
- **Lookup dai dati di gruppo del processo stesso** (fonte "Variabili locali"): invece di una tabella esterna, un campo può recuperare una riga da uno dei gruppi del processo (es. far scegliere all'utente "il preventivo vincente" dal gruppo "Lista Preventivi" già inserito in precedenza nello stesso processo, riempiendo automaticamente una coppia "Codice fornitore scelto"/"Ragione sociale scelta") (frames/073_045439_lookup-from-local-group-data.jpg).
- I **connettori preconfigurati** (es. un connettore SAM/SAP) sono un meccanismo correlato ma distinto: configurati per azienda (non con una stringa di connessione grezza) e, in particolare, a volte l'*unico* modo supportato per **scrivere** dati verso il sistema esterno (contro il sola-lettura di una connessione semplice). Approfondimento riservato a una sessione successiva (frames/065_040110_preview-connectors-e-g-sam.jpg).

#### 4.6 Variabili di gruppo — dati master-detail (1-a-molti)

Il meccanismo di BPM per dati 1-a-molti (es. N preventivi di fornitori su un'unica richiesta di investimento) (frames/061_033236_group-master-detail-variables.jpg):

1. Si crea normalmente una variabile nel magazzino (es. "Codice Fornitore").
2. Invece di lasciarla a valore singolo, si clicca il pulsante "..." di configurazione e la si assegna a un **Gruppo** nuovo o esistente (es. "Lista Preventivi") — questo la trasforma nella prima colonna di una tabella di dettaglio virtuale/griglia.
3. Si aggiungono altre colonne semplicemente **trascinando ulteriori variabili direttamente sulla griglia** — il modo più rapido e comune (usato nel 99% dei casi). Ogni variabile ulteriore rilasciata dentro la griglia si unisce automaticamente allo stesso gruppo.

Vincoli e note:

- Una variabile appartiene a **esattamente un** gruppo.
- I gruppi sono una struttura **piatta/a un solo livello** — BPM deliberatamente **non** supporta sottogruppi annidati: un compromesso di usabilità, dato che chi progetta/configura è tipicamente un consulente, non un programmatore.
- Un processo può avere più gruppi indipendenti tra loro (es. "Lista Preventivi" e un separato gruppo "Team utenti").
- A runtime, il gruppo viene renderizzato come una **griglia modificabile** dove l'utente può aggiungere/rimuovere righe liberamente (a meno che non vengano aggiunte regole di obbligatorietà sui campi per riga, es. rendere obbligatori fornitore/importo *all'interno* di ogni riga — una questione separata dal "richiedere almeno una riga").
- Un **bottone stateless trascinato nella griglia** ("Dettagli...") può aprire un pop-up più grande con il form di una singola riga (tramite le proprie "Variabili da richiedere") — risolve il problema di colonne di griglia troppo strette per campi come note lunghe (frames/063_034841_detail-pop-up-form-for-a-grid-row.jpg).
- Le colonne di un gruppo supportano le stesse **Tabelle di origine** delle variabili ordinarie (vedi 4.5), compreso il lookup da dati locali di un altro gruppo o del gruppo stesso.

#### 4.7 Formule

Le formule sono il livello di scripting integrato di BPM, scritte in sintassi **Visual Basic**, modificate tramite un editor di formule con un menu di supporto al tasto destro (anno/utente/data correnti, e un albero ricercabile di tutte le variabili di processo per pagina). Le espressioni one-liner in stile Excel funzionano direttamente (es. `Year([data richiesta])`); la logica multi-riga richiede un'istruzione `Return` esplicita e supporta `If/Then/Else`. Le formule **si ricalcolano automaticamente** ogni volta che una variabile da cui dipendono cambia (tracciamento delle dipendenze, come in un foglio di calcolo) (frames/039_015258_the-formula-editor-visual-basic.jpg).

Tipi di formula, e dove si configurano:

- **Formula** (a livello di magazzino, "la" formula) — un valore calcolato sempre valido a livello globale, es. `anno = Year(data_richiesta)`, oppure un totale corrente `totale_costi = importo_richiesta + costi_accessori` (frames/043_020607_calculated-total-via-formula.jpg).
- **Formula di validazione** — impostata per task su "variabili da richiedere" (non globale); ritorna vero/falso per validare un campo oltre il semplice flag obbligatorio (es. `data_richiesta >= Today()`), e può impostare un messaggio di errore personalizzato mostrato all'utente (`Errore = "..."`). Usabile anche per esprimere "obbligatorio *se* [condizione]", cosa che un semplice flag obbligatorio non può fare (frames/040_015538_formula-di-validazione.jpg).
- **Formula di visibilità** — mostra/nasconde dinamicamente un campo in base a una condizione.
- **Formula per default** — imposta il valore *iniziale* di una variabile solo la prima volta che viene aperta mentre è ancora non valorizzata (es. richiedente = utente corrente, data = oggi); distinta dal costante **Valore di default** fisso (frames/042_020133_formula-per-default-vs-valore-di-default.jpg).
- **Formula per ridolli** — rende un campo condizionalmente in sola lettura in determinate circostanze; considerata una tecnica più avanzata/specifica.
- **Condizione di abilitazione** — la formula collegata a una freccia di transizione o a un ramo di gateway per controllare l'instradamento (vedi 2.3).

Indicazione del docente: il motore è abbastanza potente da gestire complessità arbitraria, ma la raccomandazione è di mantenere le formule semplici quanto la logica di business richiede realmente, senza ingegnerizzare eccessivamente.

#### 4.8 Bottoni e "Variabili da impostare"

Una variabile Booleana può essere renderizzata come checkbox oppure come **Bottone** (statefull — si comporta come un interruttore che resta "premuto" — oppure stateless, un comando puro). I bottoni sono più potenti di una semplice checkbox perché è possibile agganciare loro delle azioni:

- **Variabili da impostare**: un'alternativa imperativa a una Formula reattiva — si aggancia al bottone una lista di azioni che valorizzano variabili target solo al momento del click (es. un bottone "Ricalcola totali" che imposta esplicitamente `totale_costi`), in contrapposizione a una Formula che si ricalcola automaticamente a ogni cambio di dipendenza. Due varianti dello stesso obiettivo di fondo, scelte in base a se si vuole un comportamento "sempre live" oppure "solo su richiesta" (frames/044_021322_variabili-da-impostare-button-actions.jpg).
- Comportamento del bottone **Aggiunta allegati** — vedi sezione 7.2.
- Un bottone può anche avere una propria sotto-form **"Variabili da richiedere"** (vedi 4.2), usata sia per l'inserimento di dettaglio in pop-up standalone sia per il pattern "Dettagli" a livello di riga di gruppo (vedi 4.6).

---

### 5. Pubblicazione e versioni

- **Pubblicare** rende un modello vivo/utilizzabile dagli utenti citati al suo interno. Esegue una validazione (mostra warning, ma in genere consente comunque di pubblicare) e crea una nuova versione numerata (R00, R01,...); **tutte le versioni vengono conservate** — sia per motivi tecnici (le istanze in corso fanno riferimento a versioni precedenti), sia per motivi organizzativi/di audit (frames/009_001536_publishing-a-process.jpg).
- Un modello di processo richiede un **Nome modello** (la chiave usata per trovarlo/sovrascriverlo) prima di poter essere pubblicato o salvato. Si imposta cliccando sull'area bianca del canvas > proprietà del processo (frames/027_010205_naming-and-publishing-the-model.jpg).
- Due ulteriori **formule a livello di processo** sono richieste per una pubblicazione pulita (la validazione avvisa se mancano) (frames/052_024811_process-name-description-formulas.jpg):
 - **Formula per il calcolo del nome del processo** — costruisce il titolo/business-key di ogni istanza, tipicamente da un contatore o una variabile data, es. `[numero richiesta] & "/" & [anno]`.
 - **Formula per la descrizione del processo** — costruisce una stringa libera di intestazione, es. `"Richiesta numero " & [numero] & " " & [stabilimento]`.
 Questi nome/descrizione sono ciò che appare nella To-Do List, nelle griglie di ricerca e nelle intestazioni, al posto degli ID interni grezzi.
- **Salva su file**: un processo (l'intero design — diagramma, variabili, form, formule) può essere esportato su un unico file **JSON** locale (estensione `.jbkf`) invece della/in aggiunta alla pubblicazione — il modo standard per spostare una configurazione tra ambienti (es. portatile → ambiente cliente). Report e dashboard fanno eccezione: hanno vita propria perché possono coprire più processi contemporaneamente.
- **Comportamento del versionamento per le istanze in corso**: ripubblicare **non** modifica retroattivamente le istanze già in esecuzione — ogni istanza resta ancorata alla versione del modello attiva quando è stata avviata. Un pulsante a livello di processo, **"Aggiornamento processo"**, consente di allineare manualmente un'istanza in corso specifica a una versione più recente (es. "Aggiorna dalla versione 16 alla 17"). Alcune modifiche (interventi sul magazzino, nuovi binding di tabella) vengono recepite automaticamente dalle istanze in corso; le aggiunte di layout/UI a un task già eseguito tipicamente richiedono questa azione di aggiornamento esplicita. Se il salto di versione è troppo grande/incompatibile, l'unica soluzione è riavviare l'istanza e replicarne manualmente l'avanzamento (frames/066_040224_versioning-running-instances-pin-to-their-version.jpg).
- **Override riservati agli amministratori**, per casi eccezionali:
 - **Forzatura dei valori del magazzino** su un'istanza in corso, dalla sua schermata di dettaglio processo, fuori dal flusso normale ("forzatura extra processo") — richiede conferma/scarto alla chiusura, ed è interamente tracciata in Storico (frames/060_032544_admin-force-edit-outside-the-process-flow.jpg).
 - **Forzatura dell'avanzamento del processo**: tasto destro su un task in modalità modifica > "Imposta oggetto attivo" per saltare/far avanzare forzatamente il motore a un dato passo — esplicitamente definito "barare" dal docente, ma utile in fase di sviluppo (passi dimenticati) o per sbloccare un processo realmente incastrato senza un intervento di un programmatore sul database.

---

### 6. Esecuzione e monitoraggio

#### 6.1 To-Do List

L'interfaccia concreta e quotidiana per partecipare ai processi. Si apre di default al login (frames/011_001906_watching-the-token-move.jpg).

- **Filtri**: ambito utente ("Tutti gli utenti visibili" = l'amministratore vede tutti; "Tutto" = i propri task e quelli dei propri gruppi — il filtro normale per un utente comune), intervallo date (giorno/settimana/mese/tutti gli aperti) e **stato dell'attività**.
- **Tre stati di attività**, visibili sia qui che nel diagramma: **Eseguita** (completata), **In corso** (disponibile ora), **Pianificata** (futura/pianificata — verde chiaro) (frames/053_025552_three-activity-states.jpg).
- La griglia supporta il **raggruppamento** con tasto destro (es. per modello di processo) e il riordino delle colonne; le preferenze di layout sono **salvate automaticamente per utente**. Colonne di default: Utente, Attività, Modello, Nome processo, Data inizio prevista, Priorità (un'etichetta libera senza significato funzionale, utile solo per ordinamento/promemoria), Scadenza, % completamento (frames/054_025806_customizing-the-to-do-list-grid.jpg).
- **Esecuzione di un task**: si clicca "Esegui" per compilare i campi (validati contro le regole di obbligatorietà/formula — un indicatore rosso blocca l'invio finché non è soddisfatto); **Completato** invia e fa avanzare il processo; **Salva/Salva e chiudi** persiste una bozza senza far avanzare il processo (i dati restano per dopo).

#### 6.2 Schermata di dettaglio/ispezione processo

Accessibile dalla To-Do List (soggetta ai permessi di visualizzazione/modifica — vedi sezione 9). Tab disponibili (frames/055_030322_process-detail-inspection-screen.jpg):

- **Variabili** — il magazzino completo, organizzato secondo la stessa struttura di pagine/tab progettata a monte.
- **Intestazione** (anagrafica) — campi di sistema fissi: nome processo, descrizione, modello sorgente, attività corrente, data creazione, proprietario (chi ha avviato il processo).
- **Allegati** — il dossier documentale (vedi sezione 7).
- **Processi collegati** — collegamenti verso altre istanze di processo correlate.
- **Pianificazione** — informazioni su asse temporale/vista Gantt-style.
- **Storico** — il log di audit completo (vedi sezione 8).

Questa schermata è spesso usata da un **proprietario** di processo per monitorare avanzamento/tempistiche/stato tra istanze diverse; l'accesso può essere concesso in sola lettura o lettura/scrittura a seconda del pubblico.

#### 6.3 Ricerca processi

"Ricerca processi" restituisce **una riga per istanza di processo** (non per task), coprendo sia istanze aperte che chiuse/archiviate (nulla viene cancellato a meno che non venga applicata una politica di archiviazione esplicita) (frames/012_002441_searching-and-filtering-process-instances.jpg).

- La vista di default include molte colonne di sistema generiche di scarso interesse; **"Modifica visualizzazione"** permette di scegliere le colonne rilevanti (es. anno, codice stabilimento, richiedente, tipo richiesta, importo, note).
- È possibile salvare più viste con nome; marcarne una come **"Pubblicato"** la rende visibile a tutti gli utenti, non solo a chi l'ha creata — un tipico compito dell'amministratore è costruire buone viste di ricerca di default per gli utenti finali, dato che la vista di default "out of the box" non è molto utile (frames/057_030853_custom-search-views.jpg).
- Le griglie in tutto BPM (To-Do List, ricerca, griglie collegate al magazzino) supportano filtri di colonna sia a dropdown che testuali liberi.

#### 6.4 Voci di menu personalizzate

Configurazione > Opzioni generali > **Menu personalizzati** permette a un amministratore di aggiungere scorciatoie dirette (fino a 3 livelli: menu radice / sottomenu / descrizione) collegate a un'azione specifica su un processo (es. "avvia Richiesta INV" o "cerca richieste Richiesta INV"), permettendo agli utenti finali di bypassare i menu generici "Nuovo processo"/"Ricerca processi". I menu personalizzati si aggiornano solo al login/riavvio successivo dell'applicativo (frames/059_032017_custom-menu-entries.jpg).

#### 6.5 Storico (log di audit)

Ogni visualizzazione, modifica ed esecuzione di task su un'istanza di processo viene registrata con **timestamp + utente** (es. creata alle 14:38, visualizzata alle 14:41, campi modificati alle 14:45/14:47, task X eseguito alle 14:47...). Doppio clic su una voce di log mostra un **diff prima/dopo a livello di campo** di esattamente cosa è cambiato (frames/056_030614_storico-full-audit-log.jpg).

Scopo: oltre alla semplice tracciabilità, è esplicitamente indicato come prezioso per la **certificazione di qualità/compliance** — dimostrare che una procedura progettata è stata effettivamente seguita come specificato. La visibilità dello Storico agli utenti finali (contro il solo amministratore/proprietario) è una scelta configurabile.

---

### 7. Allegati

#### 7.1 Concetto

BPM ha una propria gestione documentale/allegati, sempre ambientata **all'interno di un processo** (un documento non vive mai standalone in BPM — è sempre parte del "dossier"/"plico" di un processo). I documenti possono essere organizzati in **cartelle virtuali** create dentro il tab Allegati del processo ("Visualizza elenco" vista a lista / "Visualizza struttura" vista ad albero), es. "Preventivi", "Scheda Investimento" (frames/067_040716_attachments-overview.jpg).

**Visualizzatore documenti integrato**: PDF, Word, Excel, e-mail (.msg) e immagini si anteprimano direttamente dentro BPM; altri tipi di file si aprono con doppio clic nell'applicazione associata dal sistema operativo. E-mail e allegati possono essere **trascinati direttamente da Outlook**, utile quando un processo è innescato da uno scambio di e-mail.

#### 7.2 Abilitare gli allegati per task

**"Allegati da richiedere"** è la controparte file-management di "Variabili da richiedere" (frames/068_040924_allegati-da-richiedere.jpg):

- Attiva/disattiva la gestione allegati per un dato task.
- Può fissare la cartella target di default del task (es. lo Start punta a "Scheda Investimento").
- Può essere impostato in **sola lettura** su un task puramente per esporre la visibilità dei documenti già raccolti senza permetterne la modifica (es. mostrare tutti gli allegati, in sola lettura, su un passo di revisione successivo).

Un **pattern di allegato obbligatorio**: si crea una variabile Bottone stateless (es. "Inserisci scheda richiesta"), la si configura in "Tipo impostazioni di base" come **Aggiunta allegati**, si sceglie una cartella target e opzionalmente si restringono le estensioni file ammesse, poi la si trascina nelle "variabili da richiedere" di un task e la si marca obbligatoria — pura configurazione, senza scripting, per forzare il caricamento di uno specifico documento richiesto prima che il processo possa avanzare. Applicabile sia a livello di processo (es. una "scheda investimento" PDF obbligatoria allo Start) sia a livello di riga di gruppo (es. un bottone "Allega preventivo" dentro ogni riga di preventivo in una griglia di dettaglio) (frames/070_042244_mandatory-attachment-via-a-button.jpg).

#### 7.3 Storage: Database vs. File System

Un nuovo processo nasce con una root di allegati **su database** di default ("Attachments" — lo stream del file memorizzato come tabella dentro il database di BPM stesso). Si possono creare **root aggiuntive** (frames/069_041300_storage-roots-database-vs-file-system.jpg):

- **Su database**, oppure
- **Su file system**, dato un path di base (tipicamente una share di rete raggiungibile da tutti) che può essere **costruito dinamicamente da variabili di processo** (es. un pattern di path che combina stabilimento + numero richiesta), così BPM crea automaticamente a runtime una sottocartella reale per-istanza su disco — rispecchiando come molti clienti già organizzano i documenti su unità condivise per stabilimento/numero richiesta.

Root dei due tipi possono essere **liberamente mescolate** all'interno di uno stesso processo; visivamente, le cartelle file system hanno un'icona distinta (con tinta blu) nell'albero, ma funzionalmente, dall'interno di BPM, il caricamento drag-and-drop funziona identicamente in entrambi i casi. Il tasto destro su una cartella offre diverse capacità amministrative a seconda del tipo di storage.

**Avvertenze**:

- Gli allegati su DB sono interamente governati da BPM (cancellazione in BPM = definitiva; si applicano i permessi BPM).
- Gli allegati su file system restano accessibili/modificabili/cancellabili in modo indipendente **direttamente sulla share, fuori da BPM** — un vero gap, poiché il modello di permessi di BPM non governa i permessi a livello di file system (due sistemi di permessi da mantenere in parallelo). Opinione personale del docente: lo storage su FS è concettualmente la scelta "sbagliata" per un approccio corretto di gestione documentale (sicurezza/logging/accesso dovrebbero vivere in SQL), ma è pragmaticamente supportato e usato nella pratica, specialmente per un rollout iniziale più leggero quando un cliente ha già documenti organizzati su file system (rimandando la migrazione "corretta" al DB a una fase progettuale successiva).
- BPM può anche **pre-generare un intero albero di cartelle template** alla creazione del processo (rispecchiando una tipica struttura di cartelle di commessa/progetto — preventivi/disegni/schede tecniche/...), utile per clienti già abituati a queste convenzioni.
- Buona prassi per i path delle root FS: memorizzare il nome del server in una **variabile d'ambiente** invece di codificarlo in ogni formula di path (raramente fatto realmente sul campo); alcuni clienti mantengono invece una tabella SQL che mappa ogni processo ai propri path di root.

#### 7.4 Metadati e versionamento a livello di allegato

- Un allegato può avere **colonne di metadati personalizzate** (distinte dalle variabili di processo) che vengono legate al valore di una variabile di processo al momento del caricamento (es. aggiungere una colonna "Ragione Sociale" alla griglia allegati, legata alla ragione sociale del fornitore di quella riga di preventivo) — uno snapshot denormalizzato catturato sul file stesso.
- Gli attributi standard di un allegato includono **Revisione** e **Stato** (Attivo/Obsoleto). Il versionamento oggi è **solo manuale**: un allegato può essere marcato "Obsoleto" e la vista può essere alternata per mostrare/nascondere gli obsoleti (es. riallegare un documento revisionato quando un processo torna indietro in un loop) — non esiste un concatenamento automatico delle versioni.
- I caricamenti di allegati sono tracciati in **Storico** (sezione 6.5) esattamente come le modifiche alle variabili.
- Nessun limite di dimensione file rigido è imposto da BPM stesso (file molto grandi rischiano solo timeout/lentezza); una **dimensione massima** può essere esplicitamente configurata su un bottone "Aggiunta allegati".
- Gli allegati possono (argomento riservato a una sessione successiva) essere integrati con il prodotto documentale di Digit ("Globo"), così i file vivono lì invece che in BPM.

---

### 8. Sotto-processi

Una shape Sotto-processo nasconde un mini-flusso annidato, progettato in modo indipendente, dietro un unico box nel diagramma padre (doppio clic per entrare/progettarlo) (frames/071_043856_sub-processes.jpg). Usi tipici:

- Mantenere il diagramma di primo livello pulito/leggibile pur modellando il dettaglio sottostante.
- **Far evolvere** un design: un Task semplice esistente può essere convertito in un Sotto-processo se in seguito si scopre che necessita di una scomposizione interna (es. suddividere un unico task "Approvazione" in passi di pre-approvazione/qualità/tecnico) senza dover riprogettare il flusso padre.

**Sotto-processo ricorrente**: un sotto-processo può essere legato a un **gruppo** (l'insieme di variabili master-detail, vedi 4.6) e marcato "ricorrente" — a runtime genera una istanza completa del proprio flusso interno **per ogni riga** di quel gruppo (es. un mini-flusso di valutazione per ogni preventivo fornitore ricevuto) (frames/072_044146_recurring-sub-process.jpg). Configurabile come:

- **Parallelo** (tutte le istanze generate sono aperte contemporaneamente; l'assegnatario le esegue in qualsiasi ordine) — l'icona mostra barre parallele aggiuntive.
- **Sequenziale** (una alla volta; richiede di indicare la variabile che determina l'ordine di esecuzione) — l'icona mostra linee sequenziali.
- Una "formula per condizione" opzionale può filtrare quali righe generano effettivamente un'istanza.

Il flusso padre procede oltre il sotto-processo solo quando **tutti** i rami generati sono terminati (sincronizzazione/join). Questo pattern è prezioso ogni volta che il numero di sotto-attività parallele è noto solo a runtime, non in fase di progettazione — es. azioni correttive/di miglioramento qualità, passi di ispezione/collaudo, oppure (come dimostrato nel corso) N preventivi fornitore da valutare. Dentro un sotto-processo ricorrente legato a un gruppo, le variabili di quel gruppo appaiono come campi a **valore singolo** (concettualmente si è "dentro una riga"); le variabili di altri gruppi e le variabili di intestazione restano accessibili normalmente.

---

### 9. Permessi

#### 9.1 Regola di base

**Un utente o un gruppo semplicemente citato in un processo** (come Esecutore/Responsabile/in conoscenza su una qualche attività) vede automaticamente e può agire su quell'attività nella propria To-Do List — **non è richiesta alcuna concessione di permesso aggiuntiva** per questo soltanto. I permessi governano tutto ciò che va *oltre* questa baseline (ricerca, creazione generica di nuovi processi dal menu, override in stile amministratore, accesso a tabelle/dashboard/report).

#### 9.2 Utenti e gruppi

- Utenti e Gruppi condividono un'unica tabella/griglia sottostante, filtrabile per tipo. Un utente ha un nome (stringa libera, la convenzione di naming è a discrezione) e una **e-mail** (importante — usata per le mail di notifica generate da BPM).
- Un utente BPM può **opzionalmente** essere collegato a un account Windows/dominio. Effetto: il **client desktop ottiene il single sign-on automatico** quando collegato; il **client Web, in questa versione, richiede ancora la password di dominio** (nessun SSO web per ora) — "l'ultimo username usato" mostrato al login web è solo un cookie, non vero SSO (frames/075_050705_domain-linked-users-single-sign-on.jpg).
- **L'appartenenza a un gruppo serve due scopi distinti**, che spesso si sovrappongono ma non sono identici: (a) ereditare i *permessi* di quel gruppo, e (b) essere un partecipante che riceve i task assegnati a quel gruppo in uno o più processi. Un utente è tipicamente in più gruppi per queste due ragioni distinte contemporaneamente.

#### 9.3 Categorie di permessi

1. **Permessi Menu** (a livello applicativo) — abilitano/disabilitano intere aree dell'app: cambio password, accesso a una "pagina", avvio nuovo processo (generico), visualizzazione processi in corso, ecc. Suddivisi in un set **operativo** (home, nuovo processo, in corso, To-Do sulla schermata processo, import, allegati, pianificazione) e un set di **configurazione** (gestione modelli di processo, tabelle, configurazione, visualizzazione/modifica utenti) — gli utenti finali ordinari tipicamente non hanno alcuno dei permessi del set di configurazione (frames/076_051206_permission-categories-overview.jpg).
2. **Permessi Processi** (per uno specifico modello di processo) — granulari, disattivati di default (rosso): **Creazione** (avviare una nuova istanza di questo modello — nota: richiede anche il permesso *menu* generico "nuovo processo" attivo, cioè una logica AND tra i due livelli), **Visualizzazione** (aprire/cercare il dettaglio del processo in lettura), **Modifica** (forzare la modifica di valori — la capacità di override amministrativo della sezione 5), **Eliminazione** (cancellare permanentemente una specifica istanza — distinto dai pieni diritti di amministratore di sistema; può essere concesso a un "proprietario di processo" non amministratore), **Copia/Duplica**, **Cambio stato processo** (forzare l'avanzamento, stesso meccanismo dell'override amministrativo).
3. **Permessi Tabelle** — per singola tabella locale BPM, separatamente per Visualizza (sfogliare l'area di gestione tabella standalone) contro Modifica (modificare i record) — distinto dal semplice uso di quella tabella come fonte lookup dentro un form di processo.
4. **Permessi Dashboard / Report** — concessione per singola dashboard e per singolo report (le dashboard in particolare sono spesso ristrette, poiché possono esporre cifre sensibili come totali monetari).
5. (Menzionati brevemente, non approfonditi in questo corso) **Prefiltri/alias** sull'accesso ai dati.

#### 9.4 Logica di risoluzione e buone prassi

- I diritti si risolvono in modo **additivo** da due fonti: concessione diretta a livello **utente**, oppure **ereditata via gruppo** di appartenenza (l'interfaccia marca un diritto come "abilitato da gruppo" quando ereditato).
- **Buona prassi: concedere via gruppi, non individui** — es. creare un gruppo solo-permessi "Inserimento richieste INV", concedergli Creazione su "Richiesta INV", poi aggiungere gli utenti a quel gruppo. Regola pratica: *"se ci si ritrova con tanti o più gruppi-permesso quanti utenti, probabilmente c'è qualcosa che non va nel design."*
- **Semantica di override Abilita/Nega**: abilitare un permesso direttamente su un utente quando lo ha già tramite un gruppo rende la concessione "appiccicosa" (sopravvive a una successiva rimozione dal gruppo); rimuovere una concessione utente ridondante ancora coperta dal gruppo non ha effetto; un **"Nega" a livello utente** ha priorità su un'Abilitazione a livello gruppo, permettendo di escludere un membro specifico da una concessione altrimenti valida per tutto il gruppo (frames/077_052605_enable-vs-deny-override-semantics.jpg).
- **Ciò di cui un utente finale tipico ha davvero bisogno**: per un utente che si limita a *ricevere ed eseguire* task dalla To-Do List, non servono essenzialmente **permessi aggiuntivi** oltre all'essere citato nel processo (gli allegati e i campi di cui ha bisogno sono già esposti tramite la configurazione "variabili/allegati da richiedere" del task stesso). L'aggiunta comunemente necessaria è **Creazione** (avviare un nuovo processo), per gli utenti che iniziano nuove richieste dal menu generico (non necessaria se agiscono solo su task già assegnati). Un accesso più ampio come Visualizzazione/Modifica/Eliminazione è riservato a proprietari di processo/amministratori, non ai partecipanti ordinari.

#### 9.5 Considerazione finale del docente

A un livello base, il sistema di permessi richiede una configurazione relativamente contenuta, perché la maggior parte del "pensiero" di controllo accessi è previsto avvenga dentro la **progettazione del processo stesso** (chi è citato su quale task, tramite quale gruppo). Le matrici di permesso più fini (menu/processo/tabella/dashboard/report) sono un livello avanzato che un primo corso "base" può in gran parte sorvolare — questo punto di chiusura segna la fine della parte fondamentale del corso; integrazione SAP, integrazione documentale (Globo), connettori e copertura più approfondita di dashboard/report sono riservati a sessioni successive.

---

## Tutorial passo-passo: costruzione del processo "Richiesta INV"

Questo tutorial ricostruisce in ordine sequenziale il flusso dimostrativo principale del corso: la costruzione, dall'abbozzo del diagramma fino a pubblicazione ed esecuzione, del processo di richiesta di autorizzazione investimento usato come caso guida. Seguendo questi passi è possibile ricreare l'esercizio nel Designer BPM.

### Fase 1 — Abbozzo del diagramma

1. **Aprire il Designer** e creare un nuovo modello di processo. Iniziare trascinando le attività (Task) che compongono, a grandi linee, il flusso di richiesta investimento: non è necessario avere già chiari tutti i dettagli — l'obiettivo è abbozzare rapidamente, eventualmente insieme al cliente/utente business.
2. **Creare la prima attività**, "Presa in carico da ufficio sicurezza": trascinarla sul canvas (riceve un codice interno immutabile, es. Activity1/Activity2), poi tasto destro > "Modifica testo" per assegnarle il nome visibile.
3. **Ribattezzare lo Start**: tasto destro sull'evento di Start (cerchio verde) > "Sposta testo" per staccare l'etichetta e scrivere, ad esempio, "Inserimento richiesta".
4. **Aggiungere le attività successive** del flusso: "Approvazione controllo di gestione" e "Approvazione direzione industriale", collegandole in sequenza con lo strumento **Link** (trascinare dal punto di ancoraggio giallo di un'attività a quella successiva).
5. **Allineare il disegno**: selezionare più shape con Ctrl e usare i comandi della ribbon "Stessa dimensione" e "Allinea" per tenere il diagramma ordinato e leggibile — ricordando che il disegno sarà visto dagli utenti finali.
6. **Aggiungere gli Stati** (milestone): inserire uno stato "Inserito" collegato subito dopo lo Start e uno stato "Approvata" alla fine del flusso principale — sono etichette di avanzamento generale, indipendenti dal task specifico in corso.
7. **Abbozzare i percorsi alternativi**: se la Direzione Industriale non approva, la richiesta torna indietro. Aggiungere un'attività "Revisione da parte del richiedente" collegata dal ramo di non-approvazione del controllo di gestione, da cui il richiedente può a sua volta rimandare la richiesta al controllo di gestione oppure rinunciare, transitando in uno stato "Annullata".
8. **Decidere se usare un oggetto "Fine"**: opzionale, puramente cosmetico — il processo si conclude comunque automaticamente quando non restano attività da eseguire. Un secondo "Fine", ad esempio per il ramo di annullamento, può aiutare la leggibilità del diagramma senza avere alcun effetto funzionale.

### Fase 2 — Utenti e gruppi

9. **Spostarsi in Configurazione > Utenti e Gruppi.** Utenti e gruppi condividono la stessa griglia, filtrabile per tipo.
10. **Creare i gruppi necessari al processo**, ad esempio "AM" (controllo di gestione/amministrazione) e "Direzione Tecnica" — in questa fase basta dare loro un nome, senza preoccuparsi ancora dei permessi. I gruppi vengono tipicamente creati ad hoc per il processo, non importati da Active Directory, perché la granularità richiesta raramente coincide con i gruppi già esistenti nel dominio aziendale.
11. **Tornare al Designer** sull'attività "Approvazione controllo di gestione" e aprire "Utenti e responsabili". Impostare il gruppo "AM" come **Esecutore**: tutti i membri del gruppo (quando ci saranno) troveranno il task nella propria To-Do List; il primo che lo esegue fa avanzare il processo.
12. Ripetere per "Approvazione direzione industriale", assegnando il gruppo "Direzione Tecnica" come Esecutore.
13. In fase di progettazione è ammesso lasciare temporaneamente un'attività priva di utente assegnato (resta visibile solo all'amministratore); va però sistemata prima del go-live.
14. (Nota a margine, non obbligatoria per l'esercizio base) Per un flusso più controllato, è possibile marcare un'attività "Task deve essere assegnato prima di poter essere eseguito", introducendo un passaggio di smistamento esplicito da parte di un Responsabile.

### Fase 3 — Primo salvataggio e pubblicazione

15. **Cliccare sull'area bianca del canvas** per aprire le proprietà del processo e impostare il **Nome modello**, ad esempio "Richiesta INV" — è il prerequisito per poter salvare o pubblicare.
16. **Pubblicare** il modello: il sistema segnala alcuni warning (che verranno risolti più avanti, quando saranno impostate le formule di nome/descrizione processo) ma consente comunque la pubblicazione, creando la versione R00.
17. In alternativa (o in aggiunta), usare **Salva su file** per esportare l'intero processo in un file JSON locale (estensione `.jbkf`) — utile per spostare la configurazione tra ambienti o per consultare i dettagli del modello generato dalla macchina.

### Fase 4 — Il magazzino delle variabili

18. **Aprire il magazzino delle variabili**: Strumenti > "Inserimento modifica variabili" — appare come una nuova pagina/tab del processo, inizialmente vuota.
19. **Creare la prima variabile**: "Nuova variabile" e assegnarle il nome "richiedente". Di default viene creata come tipo Stringa; cambiarne il tipo in **Utente (User type)**, poiché rappresenta la persona che inoltra la richiesta.
20. **Trascinare la variabile "richiedente" sul canvas del form** — a questo punto compare come campo utente, con possibilità di scegliere tra tutti gli utenti/gruppi registrati in BPM.
21. **Creare le variabili aggiuntive di testata**, tipicamente: "data richiesta" (tipo Data), "tipo richiesta" (tipo Lista Valori), "numero richiesta" (tipo Numerico, poi configurato come contatore), "codice stabilimento" (tipo Stringa, con tabella di origine) e "note richiesta" (tipo Memo). Trascinare ciascuna sul form man mano che viene creata.
22. **Organizzare il layout**: selezionare più campi con Ctrl e usare gli strumenti di allineamento ("Allinea in alto", "Allinea a destra", "Stessa dimensione") per un form ordinato — è la schermata che vedranno gli utenti finali.
23. (Opzionale, buona prassi) **Creare una nuova pagina di variabili** per il gruppo di campi legati alle approvazioni (vedi passo 27), prefissandola numericamente (es. "02 - Approvazioni") per mantenere l'organizzazione allineata al flusso cronologico del processo.

### Fase 5 — Variabili da richiedere sui singoli task

24. **Sullo Start**, tasto destro > "Variabili da richiedere" e trascinare i campi che il richiedente deve compilare all'apertura: richiedente, data richiesta, tipo richiesta, numero richiesta, codice stabilimento, note richiesta.
25. **Impostare "obbligatorio"** sui campi che lo richiedono direttamente nella schermata "variabili da richiedere" del task (impostazione locale, indipendente dal default a livello di magazzino).
26. **Riutilizzare il layout su un altro task** (es. "Revisione da parte del richiedente"): dalla pagina dello Start, esportare la categoria/pagina corrente su file, poi sul task di destinazione usare "Importa e sostituisci categoria corrente" per ricrearla identica, evitando di ritrascinare manualmente ogni campo.

### Fase 6 — Approvazioni, condizioni e diramazioni

27. **Creare una nuova pagina di variabili "Approvazioni"** e, al suo interno, le variabili: "esito approvazione CDG" (tipo Lista Valori, con valori "Approvata"/"Non approvata"), "note approvazione CDG" (tipo Memo), e in modo analogo "esito approvazione DirTec" e le relative note.
28. **Sull'attività "Approvazione controllo di gestione"**, aprire "Variabili da richiedere" e trascinare l'intestazione, "esito approvazione CDG" e "note approvazione CDG". Marcare "esito approvazione CDG" come obbligatorio.
29. **Impostare la condizione sulla freccia di approvazione**: selezionare la freccia che esce verso il ramo positivo, tasto destro > "Condizione di abilitazione", cercare la variabile "esito approvazione CDG" e scrivere la condizione (es. `esito approvazione CDG = "Approvata"`).
30. **Impostare la condizione complementare sull'altra freccia** (verso "Revisione da parte del richiedente"): `esito approvazione CDG = "Non approvata"`. Ricordare che il motore non garantisce la mutua esclusività: è responsabilità di chi progetta scrivere condizioni che si bilancino correttamente.
31. **In alternativa, sostituire le frecce condizionate con un oggetto Gateway**: inserire un Gateway (rombo) subito dopo "Approvazione controllo di gestione", ribattezzarlo (es. "Scelta approvazione"), collegarlo ai due rami di uscita, quindi doppio clic/tasto destro > "Configurazione" per impostare in un'unica schermata le condizioni `esito approvazione CDG = "Approvata"` sul primo ramo e marcare il secondo come default/else.
32. **Assegnare un instradamento dinamico**: sul task "Revisione da parte del richiedente", impostare come Esecutore la variabile Utente "richiedente" (invece di un gruppo fisso) — così il task torna sempre a chi ha originato la richiesta.
33. (Facoltativo, per illustrare i gateway paralleli/inclusivi) Dopo l'approvazione finale, inserire un Gateway **Parallelo** che forchi il flusso in due rami simultanei — es. "Collaudo" e "Parte amministrativa" — e un secondo Gateway Parallelo a valle per sincronizzarli prima di proseguire.

### Fase 7 — Formule di processo e nuova pubblicazione

34. **Impostare la formula per il calcolo del nome del processo**, nelle proprietà del processo (area bianca del canvas), ad esempio `[numero richiesta] & "/" & [anno]`.
35. **Impostare la formula per la descrizione del processo**, ad esempio `"Richiesta numero " & [numero richiesta] & " " & [codice stabilimento]`.
36. **Ripubblicare** il modello: questa volta i warning relativi a nome/descrizione dovrebbero sparire, e viene generata una nuova versione (es. R01).

### Fase 8 — Avviare e osservare un'istanza

37. Dal menu, selezionare **"Nuovo processo"** e scegliere il modello "Richiesta INV". Compilare il form dello Start (i campi obbligatori non soddisfatti mostrano un indicatore rosso che blocca l'invio) e confermare.
38. **Osservare il diagramma a runtime**: l'attività appena completata appare in grigio, l'attività corrente in giallo ("ha il pallino"), lo stato attivo in verde, e le attività future già note al motore in verde chiaro (vista pianificazione/Gantt).
39. **Eseguire il task successivo dalla To-Do List**: cliccare "Esegui", compilare i campi richiesti, quindi "Completato" per far avanzare il processo (oppure "Salva"/"Salva e chiudi" per salvare una bozza senza avanzare).
40. **Verificare in Storico** che ogni visualizzazione/modifica/esecuzione sia stata tracciata con utente e timestamp, e che il doppio clic su una voce mostri il diff dei valori prima/dopo.

### Fase 9 — Variabili di gruppo: i preventivi fornitore

41. **Tornare nel magazzino delle variabili** e creare una nuova pagina "Preventivi".
42. **Creare la variabile "Codice Fornitore"** (Stringa), trascinarla sul form, poi cliccare sui "..." di configurazione e assegnarla a un nuovo **Gruppo**, "Lista Preventivi" — diventa così la prima colonna di una griglia di dettaglio virtuale.
43. **Aggiungere le colonne successive trascinandole direttamente sulla griglia**: "Ragione Sociale", "Numero Preventivo", "Importo Preventivo" (Numerico) — ogni variabile trascinata dentro la griglia si unisce automaticamente allo stesso gruppo.
44. **Creare una nuova attività "Ricezione preventivi"**, assegnata come Esecutore all'ufficio acquisti, posizionata dopo l'approvazione. Nelle sue "Variabili da richiedere" trascinare l'intestazione e le variabili del gruppo "Lista Preventivi".
45. **Riutilizzare il layout della pagina "Preventivi"** esportando la categoria corrente e importandola/sostituendola nella schermata "Variabili da richiedere" di "Ricezione preventivi", per non dover ritrascinare manualmente ogni colonna.
46. **Testare**: avviare una nuova istanza, arrivare al task "Ricezione preventivi" ed eseguirlo. A runtime il gruppo appare come una griglia editabile in cui aggiungere/rimuovere righe liberamente.
47. **Rendere obbligatori i campi per riga**: tornare nelle "Variabili da richiedere" di "Ricezione preventivi" e marcare Codice Fornitore, Ragione Sociale, Numero Preventivo e Importo Preventivo come obbligatori — vincolo che si applica a ogni riga inserita, non al numero minimo di righe.
48. **Aggiungere un campo Note per riga**: creare nel magazzino la variabile "Note Preventivo" (Memo) trascinandola direttamente nella griglia del gruppo "Lista Preventivi" (viene automaticamente assegnata al gruppo), poi trascinarla anche nelle "Variabili da richiedere" di "Ricezione preventivi".
49. (Facoltativo, per righe con molti campi) **Aggiungere un bottone "Dettagli..."** stateless dentro la griglia, configurato con una propria sotto-form "Variabili da richiedere", per aprire un pop-up a schermo intero sulla singola riga.

### Fase 10 — Chiusura dell'esercizio

50. Facoltativamente, impostare una **Tabella di origine** sul campo "Codice Fornitore" (locale o esterna) in modo che, invece di testo libero, l'utente scelga il fornitore da un elenco, con auto-compilazione della Ragione Sociale collegata.
51. Ripubblicare il modello per rendere effettive tutte le modifiche e verificare, tramite "Aggiornamento processo", il comportamento di versionamento su un'istanza già in corso avviata con una versione precedente.

A questo punto il processo "Richiesta INV" copre l'intero flusso dimostrativo del corso base: diagramma con diramazioni condizionate, utenti e gruppi, variabili di testata e di gruppo, formule di processo, pubblicazione/versionamento ed esecuzione monitorata tramite To-Do List e Storico. Le estensioni successive — allegati obbligatori, sotto-processi ricorrenti per i preventivi, permessi granulari — si innestano su questa stessa base senza richiedere di ridisegnare il flusso principale.
