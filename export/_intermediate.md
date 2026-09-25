# Inizia


## Home

---
hide:
  - navigation
  - toc
---

<div class="bpm-hero" markdown>

<p class="bpm-hero__eyebrow">Business Process Modeler</p>

### Processi, documenti e AI.

BPM trasforma il lavoro che coinvolge più persone e reparti, oggi affidato a email, fogli condivisi e passaggi informali, in flussi strutturati: ognuno sa cosa deve fare, i ritardi emergono subito e ogni passaggio resta tracciato secondo le regole aziendali.

[Primi passi](#tutorial){ .md-button .md-button--primary }
[Consulta il riferimento](#processi){ .md-button }

</div>

#### Che cos'è BPM

<div class="grid cards" markdown>

-   **Processi**

    Flussi di lavoro con un inizio e una fine: attività assegnate a persone e gruppi, variabili, scadenze, escalation e storico dei passaggi.

    [Modelli di processo](#processi)

-   **Documenti**

    Tipi di documento con i loro metadati, archiviati e gestiti anche indipendentemente dai processi.

    [Classi documentali](#documenti)

-   **Integrazioni**

    Lettura e scrittura verso ERP, CRM, database e web service tramite connettori; API REST.

    [Integrazione](#integrazione)

-   **AI**

    Acquisizione di documenti da mail e cartelle, estrazione di testo e metadati, comprensione dei contenuti all'interno dei processi.

    [Intelligenza artificiale](#intelligenza-artificiale)

</div>

> **Per BPM tutto è processo**
>
> Processi e documenti condividono variabili, strumenti e connettori. Anche l'acquisizione automatica di un documento è un piccolo processo, senza attività umane.

#### Primi passi

<div class="grid cards" markdown>

-   **Inizia con i processi**

    ---

    Disegna un flusso, definisci chi fa cosa e quali dati servono, pubblicalo e segui il processo che avanza nella To-Do List.

    [Corso base](#corso-base)

-   **Inizia con i documenti**

    ---

    Crea una classe documentale, definisci i metadati e scopri come i documenti entrano in BPM: a mano, dal gestionale, da mail o con l'AI.

    [Classi documentali](#documenti)

</div>

#### Esempi

<div class="grid cards" markdown>

-   **Approvazione ferie**

    Il primo processo: richiesta, approvazione, esito. *In preparazione.*

-   **Documenti dal gestionale**

    Una classe documentale transazionale alimentata dall'ERP. *In preparazione.*

-   **AI al lavoro**

    Lettura delle mail in arrivo e comprensione di un documento, con integrazione ERP. *In preparazione.*

</div>

#### Consulta il riferimento

<div class="grid cards bpm-grid-3" markdown>

-   [**Processi**](#processi)

    Il Designer, gli oggetti di un flusso, l'esecuzione.

-   [**Documenti**](#documenti)

    Classi documentali, metadati, archiviazione.

-   [**Integrazione**](#integrazione)

    API standard, connettori, database, fonti dati esterne.

-   [**Intelligenza artificiale**](#intelligenza-artificiale)

    Estrazione di testo e dati, comprensione dei documenti.

-   [**Amministrazione**](#amministrazione)

    Opzioni, utenti e gruppi, tabelle, sistema.

-   [**Variabili**](#editor-delle-variabili)

    Il magazzino delle variabili, i tipi, gli attributi.

-   [**Formule e script**](#formule-e-script)

    Calcoli, validazioni, condizioni e logiche in Visual Basic.

-   [**Dashboard**](#dashboard)

    Cruscotti per analizzare processi e documenti.

-   [**Report**](#report)

    Documenti e stampe generati dai dati di BPM.

</div>

[Glossario](#glossario){ .bpm-small-link }

<p class="bpm-home-note">Cerca usando l'etichetta mostrata nell'applicazione. Manca qualcosa o non è aggiornato? <a href="https://github.com/centrosoftware-dev/bpm-docs/issues">Segnalalo con una issue</a>.</p>

## Tutorial


Percorsi guidati per imparare a configurare BPM partendo da un caso concreto. A differenza del riferimento, qui l'ordine conta: ogni pagina presuppone le precedenti.

<div class="grid cards" markdown>

-   **[Corso base](#corso-base)**

    Architettura, Designer, utenti e gruppi, variabili, pubblicazione, esecuzione, allegati e permessi. Esercizio guidato: il processo *Richiesta INV*, dall'abbozzo alla pubblicazione.

-   **[Corso avanzato](#corso-avanzato)**

    Griglie dati, gateway, eventi, operazioni automatiche, tabelle P_, report e dashboard, integrazione SAM, pianificazione e Gantt.

</div>

## Corso base

### BPM Base

> **Origine del contenuto**
>
> Pagine ricavate dalla registrazione del corso di formazione. Le schermate possono differire dalla versione attuale del prodotto.

**BPM** (Business Process Modeler) è il prodotto di Digit Company per la modellazione grafica di processi aziendali: un motore di workflow che permette di digitalizzare attività oggi gestite in modo destrutturato — scambi di e-mail, fogli Excel, personalizzazioni ad hoc sui vari sistemi aziendali. Il punto di partenza concettuale è sempre **il processo**: la sequenza di operazioni necessarie a gestire una pratica reale, dalla sua apertura fino alla sua conclusione.

BPM è un prodotto standalone — può funzionare in totale autonomia — ma nella pratica quasi sempre si integra con altri sistemi (un gestionale/ERP per le anagrafiche, SAP, un documentale). Esistono connettori preconfigurati per SAP ("SAM"); l'integrazione con gestionali generici richiede più lavoro custom.

Questo materiale copre i fondamentali del prodotto: architettura client/web, gli oggetti del Designer, la gestione di utenti e gruppi, il magazzino delle variabili, pubblicazione e versionamento, esecuzione e monitoraggio dei processi, allegati, sotto-processi e il sistema di permessi. Il filo conduttore è un caso reale usato a scopo didattico: un processo di **richiesta di autorizzazione investimento**, dall'inserimento della richiesta fino al collaudo di quanto acquistato.

---

#### Come è organizzato

- [Concetti](#concetti): i temi del corso, uno per pagina.
- [Tutorial: processo Richiesta INV](#tutorial-processo-richiesta-inv): l'esercizio guidato, passo per passo.

### Concetti


- [Architettura](#architettura)
- [Il Designer e gli oggetti di processo](#il-designer-e-gli-oggetti-di-processo)
- [Utenti e assegnazione attività](#utenti-e-assegnazione-attivit\224)
- [Le variabili di processo (il magazzino)](#le-variabili-di-processo-il-magazzino)
- [Pubblicazione e versioni](#pubblicazione-e-versioni)
- [Esecuzione e monitoraggio](#esecuzione-e-monitoraggio)
- [Allegati](#allegati)
- [Sotto-processi](#sotto-processi)
- [Permessi](#permessi)

#### Architettura


###### I tre pilastri di ogni soluzione BPM

Ogni soluzione costruita in BPM si basa su tre elementi che ricorrono in tutto il prodotto:

1. **Il processo** — il diagramma di attività, gateway ed eventi.
2. **Utenti e gruppi** — chi fa cosa.
3. **Le variabili di processo** ("magazzino delle variabili") — i dati che il processo porta con sé.

###### Client desktop vs. applicazione Web

- **Client desktop**: copre la modellazione/progettazione del processo, la configurazione (utenti, dashboard, report, strutture, opzioni di posta, allegati) e l'uso operativo (avvio/ricerca processi, To-Do List). È l'ambiente in cui il consulente passa la maggior parte del tempo di progettazione.

    ![client vs architecture overview](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/013_002835_client-vs-architecture-overview.jpg){ loading=lazy }

- **Applicazione Web**: solo operativa (To-Do List, avvio nuovo processo, ricerca, storico) — nessuna superficie di configurazione/progettazione. È stata recentemente riscritta secondo il tema visivo "Portale 6.0" e, secondo il docente, è destinata a raggiungere piena parità funzionale con il client fino a diventare il **client consigliato per gli utenti finali** (viene usato internamente anche in Digit). Storicamente il web era indietro su alcune funzionalità (es. la gestione allegati era diversa non solo esteticamente, ma anche funzionalmente); al momento della registrazione la parità è quasi raggiunta, con un residuo di lavoro stimato in circa un trimestre.
- Il web utilizza un **modello a pannelli impilati**: passando dalla To-Do List al dettaglio di un processo, la To-Do List resta "dietro" (recuperabile tramite un'icona di stack) invece di essere sostituita da una navigazione a pagina intera — così più record possono restare aperti contemporaneamente.
- Attenzione al layout: client e web usano font e spaziature diverse (il web è più "arioso", basato su Bootstrap); una schermata progettata in uno dei due ambienti va sempre verificata anche nell'altro prima del rilascio. Le preferenze di colonne/griglia (es. colonne della To-Do List) sono salvate **per utente ma separatamente** tra client e web.
- Il client desktop resta comunque l'ambiente primario per **progettazione/configurazione** e test rapidi in locale durante la costruzione di un processo.

#### Il Designer e gli oggetti di processo


###### Layout e flusso di lavoro del Designer

Il Designer è organizzato in tre pannelli: la **palette degli oggetti/strumenti** (raggruppati in Attività, Eventi, Gateway, Operazioni/automazioni e altri oggetti di supporto), un **pannello proprietà** (contestuale a ciò che è selezionato — cliccando sull'area bianca del canvas compaiono le proprietà del processo, cliccando lo Start compaiono le proprietà dello Start) e il canvas stesso. Una ribbon in alto raccoglie i comandi di disegno/allineamento.

- Più modelli di processo possono essere aperti contemporaneamente in tab paralleli, e le tab possono essere affiancate in vista side-by-side (utile per confrontare o copiare elementi tra due modelli).

    ![designer menu tour](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/014_003629_designer-menu-tour.jpg){ loading=lazy }

- **Buona prassi**: abbozzare una versione grezza del processo rapidamente — anche in diretta con il cliente/l'utente business — prima di raffinare nomi, regole e dettagli. È una prassi iterativa normale, non un mancato lavoro di pianificazione: bozza → prova → correzione del tiro.

    ![sketch first refine later](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/016_004116_sketch-first-refine-later.jpg){ loading=lazy }

- **Terminologia**: "Modello di processo" è il template/design riutilizzabile; "Processo" è un'esecuzione/istanza in corso di quel template.

###### Le shape principali

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

- Trascinando un'attività sul canvas le viene assegnato un codice interno permanente (Activity1, Activity2,...) usato come ID immutabile; il **nome visualizzato**, leggibile dagli utenti, si imposta separatamente con tasto destro > "Modifica testo" (es. "Presa in carico da ufficio sicurezza").

    ![creating and naming activities](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/017_004219_creating-and-naming-activities.jpg){ loading=lazy }

- Consiglio: nomi chiari ma non troppo lunghi. Tasto destro > "Sposta testo" permette di staccare visivamente un'etichetta dalla propria shape (restando comunque logicamente collegata) — utile occasionalmente per l'evento di Start (es. rietichettarlo "Inserimento richiesta").
- Lo strumento **Link** disegna i collegamenti tra le shape, creando punti di ancoraggio; la ribbon offre strumenti di allineamento/uniformazione delle dimensioni per tenere ordinati i diagrammi grandi (i diagrammi sono visti dagli utenti finali, quindi la leggibilità conta).

    ![connecting activities with the link tool](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/018_004444_connecting-activities-with-the-link-tool.jpg){ loading=lazy }

**Stati (milestone)**

Un oggetto "Stato" marca un punto importante nel ciclo di vita complessivo del processo, indipendentemente da quale specifica attività sia in corso (es. "Inserito" all'inizio, "Approvata" alla fine, "Annullata" in caso di annullamento). Gli stati sono puramente etichette, senza alcun significato di sistema al di là dell'essere interrogabili/ricercabili in seguito (es. interrogare "tutte le richieste annullate").

![state objects milestones](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/019_004648_state-objects-milestones.jpg){ loading=lazy }

**Fine vs. Termina processo**

- **Nessun oggetto di fine esplicito è necessario**: la regola generale di BPM è "quando non ci sono più attività da fare, il processo è concluso" — automaticamente, senza alcuna configurazione particolare.
- **Fine**: opzionale, puramente un marcatore visivo/di documentazione, senza alcun effetto funzionale.

    ![end is optional cosmetic](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/020_004757_end-is-optional-cosmetic.jpg){ loading=lazy }

- **Termina processo**: funzionalmente diverso — il raggiungimento di questo oggetto uccide/interrompe forzatamente ogni altro ramo ancora in corso di quella istanza di processo.

    ![fine vs termina processo](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/021_004830_fine-vs-termina-processo.jpg){ loading=lazy }

###### Diramazioni: condizioni e gateway

Esistono due modi — equivalenti ma con diversa chiarezza — per esprimere la logica di diramazione in BPM, entrambi basati sul **motore delle formule** (vedi 4.7):

1. **Freccia semplice condizionata** (il "baffetto"): tasto destro sulla freccia in uscita > "Condizione di abilitazione" e scrittura di una formula (es. `esito approvazione CDG = "Approvata"`). Compatta, ma il motore **non** impone la mutua esclusività — le condizioni in uscita possono sovrapporsi o lasciare vuoti; è responsabilità di chi progetta scrivere condizioni complementari.

    ![condition on a transition arrow](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/047_023344_condition-on-a-transition-arrow.jpg){ loading=lazy }

2. **Oggetto Gateway** (il rombo in palette): doppio clic/tasto destro > "Configurazione" mostra *tutti* i percorsi in uscita e le relative condizioni in un'unica schermata; le valuta in ordine e prende il primo match vero, con un ramo marcabile come **default/"else"** (quindi N rami richiedono solo N−1 condizioni esplicite). Più "professionale" secondo lo standard BPMN e più autoesplicativo nel diagramma, particolarmente utile con 3 o più rami, al costo di un po' più di spazio nel disegno.

    ![exclusive gateway object](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/048_023529_exclusive-gateway-object.jpg){ loading=lazy }

Varianti di Gateway:

- **Esclusivo** (il rombo di default): esattamente un percorso in uscita si attiva — un if/else rigoroso.
- **Parallelo**: si dirama in rami simultanei (es. "Collaudo" e "Parte amministrativa" partono insieme dopo l'approvazione); la stessa shape Gateway si riusa a valle per **sincronizzare**/attendere che tutti i rami diramati finiscano prima che il flusso prosegua. Nota: è *possibile* disegnare più frecce non condizionate in uscita da un semplice task con lo stesso effetto, ma non è BPMN rigoroso — il Gateway è il modo pulito per esprimerlo.

    ![parallel gateways fork join](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/050_024327_parallel-gateways-fork-join.jpg){ loading=lazy }

- **Inclusivo**: una via di mezzo — un qualsiasi sottoinsieme (0, 1 o più) dei rami in uscita può attivarsi in base alle condizioni, utile quando i rami non sono né puramente alternativi (esclusivo) né puramente obbligatori insieme (parallelo).

    ![inclusive gateway](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/051_024543_inclusive-gateway.jpg){ loading=lazy }

###### Visualizzazione a runtime

Consultando un'istanza di processo in esecuzione, il diagramma colora l'avanzamento:

![diagram color coding](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/045_022116_diagram-color-coding.jpg){ loading=lazy }

- **Grigio** = attività già eseguita
- **Giallo** = attività in corso ("ha il pallino/token")
- **Verde** = stato attivo (un oggetto Stato attualmente in vigore)
- **Verde chiaro** = "pianificata" — attività che il motore sa già che raggiungerà in futuro (alimenta la **vista Gantt/pianificazione**); questo insieme si aggiorna dinamicamente man mano che i dati vengono raccolti, poiché il percorso futuro può dipendere da condizioni non ancora note
- Bianco = non ancora visitata

#### Utenti e assegnazione attività


###### Ruoli per attività

Per ogni attività, BPM permette di indicare:

![users roles executor responsible cc](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/006_000848_users-roles-executor-responsible-cc.jpg){ loading=lazy }

- **Esecutore** — la persona/il gruppo che trova il task nella propria To-Do List. Usato in circa il 90% dei casi reali.
- **Responsabile** — può smistare il task a un membro specifico del proprio gruppo.
- **In conoscenza** (CC) — deve solo sapere che l'attività è avvenuta.

###### Due modalità di assegnazione

1. **Assegnazione diretta al gruppo** (il caso più comune): si assegna un **gruppo** (es. "Controllo di gestione") come Esecutore. Tutti i membri del gruppo vedono il task nella propria To-Do List; il primo che agisce lo completa e il processo avanza. Si usano gruppi invece di singoli individui perché "le persone cambiano, i ruoli/gruppi restano"; i gruppi sono tipicamente **costruiti ad hoc per il singolo processo** piuttosto che importati integralmente da Active Directory (i gruppi AD raramente rispecchiano la granularità realmente necessaria).

    ![assigning a group as task executor](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/024_005637_assigning-a-group-as-task-executor.jpg){ loading=lazy }

2. **Assegnazione poi esecuzione**: si spunta il flag "Task deve essere assegnato prima di poter essere eseguito" — aggiunge un passaggio esplicito di smistamento in cui un Responsabile sceglie manualmente una persona specifica del gruppo, e solo quella persona vede poi il task. Più burocratico; usato selettivamente (es. scenari su commessa/progetto con un passaggio di triage in ufficio tecnico).

    ![must be assigned before execution flag](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/025_005815_must-be-assigned-before-execution-flag.jpg){ loading=lazy }

3. **Assegnazione dinamica tramite una variabile di tipo Utente**: la finestra "Utenti e responsabili" elenca anche le **variabili di tipo Utente** del processo (es. "richiedente") come possibili esecutori — si sceglie la variabile e il task viene instradato a chiunque quella variabile contenga in quel momento. Uso classico: rimandare un task a chi ha originariamente inoltrato la richiesta.

    ![dynamic assignment to a process variable user](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/049_024235_dynamic-assignment-to-a-process-variable-user.jpg){ loading=lazy }

###### Nota per la fase di sviluppo

Un'attività temporaneamente lasciata senza utente assegnato è visibile solo all'amministratore — va bene durante la progettazione/i test, ma va sistemata prima del go-live (ogni attività deve avere un proprietario reale).

#### Le variabili di processo (il magazzino)


Il **magazzino delle variabili** è l'unica superficie di progettazione che contiene tutti i campi dati che un processo porta con sé — si accede da Strumenti > "Inserimento modifica variabili", e appare come una pagina/tab aggiuntiva del processo.

![opening the variable warehouse](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/028_010543_opening-the-variable-warehouse.jpg){ loading=lazy }

Modello mentale di progettazione: si abbozza il processo → si ragiona su quali dati devono entrare/uscire in ogni punto → si creano le variabili corrispondenti nel magazzino → poi, per ogni attività, si trascina il sottoinsieme rilevante tramite **"Variabili da richiedere"** (vedi 4.2). Le variabili generano automaticamente i campi database sottostanti — non serve progettare tabelle/SQL a mano.

- Le variabili possono essere organizzate in più **pagine** (tab), convenzionalmente prefissate `01`, `02`, `03`... poiché le pagine si ordinano alfabeticamente. Buona prassi: seguire liberamente il flusso cronologico del processo nell'organizzare le pagine, per leggibilità (non obbligatorio).
- I campi possono essere allineati/ridimensionati (multi-selezione con Ctrl) per un layout ordinato lato utente finale — la superficie di progettazione è letteralmente ciò che l'utente vedrà.

###### Tipi di variabile

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

###### "Variabili da richiedere" (il sottoinsieme per singolo task)

È la controparte, a livello di ogni Task/Start/bottone, del magazzino globale: tasto destro su un task (o su una variabile, per il proprio sotto-form) > "Variabili da richiedere" e trascinamento dei soli campi rilevanti in quel punto.

![variabili da richiedere per task](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/031_012035_variabili-da-richiedere-per-task.jpg){ loading=lazy }

Relazione chiave: il magazzino e la schermata "variabili da richiedere" di ogni task sono **collegati per nome della variabile** (fonte unica di verità per variabile, un solo valore per istanza di processo) ma **indipendenti in layout/posizionamento** — rimuovere una variabile dalla schermata di un task non la cancella dal magazzino né azzera il suo valore altrove.

Impostazioni locali/per-task su una variabile posizionata (indipendenti dai default a livello di magazzino):

- **Obbligatorio** — impostabile globalmente nel magazzino oppure, come buona prassi, localmente per task (poiché un campo può essere obbligatorio in un punto del processo ma non in un altro).
- **Sola lettura / "Ridolli"** — es. per mostrare dati di contesto a monte a un utente di un task successivo senza permettergli di modificarli (pattern comune: rimostrare richiedente/data/tipo come sola lettura su un task a valle).
- **Formula di validazione** locale (vedi 4.7).

**Scorciatoia esporta/importa**: una pagina (o l'intero layout "variabili da richiedere" di un task) può essere esportata su file locale e importata in un altro task, evitando di ritrascinare manualmente molti campi — molto usato quando si riutilizza un layout (es. copiare il form dello Start su un successivo task "Revisione da parte del richiedente").

![export import variable layouts](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/032_012254_export-import-variable-layouts.jpg){ loading=lazy }

###### Proprietà fondamentali di una variabile

- **Nome** — la chiave interna/DB; **immutabile** una volta creata.

    ![variable name is immutable](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/034_013929_variable-name-is-immutable.jpg){ loading=lazy }

- **Descrizione** (etichetta) — liberamente modificabile, localizzabile, mostrata accanto al campo; può essere abbreviata (es. "Rich.") indipendentemente dal nome sottostante.
- **Descrizione su interrogazioni** — un'etichetta separata usata specificamente nelle colonne delle griglie di ricerca, che può essere più verbosa/svincolata dal contesto rispetto all'etichetta nel form.
- **Obbligatorio / Ridolli (sola lettura)** — come sopra, impostabile a livello globale o locale.
- **Variabile senza salvataggio** — valore non persistito su DB, puro stato di interfaccia, tipicamente abbinato a un campo di visualizzazione calcolato tramite formula che non si vuole memorizzare.

    ![variabile senza salvataggio](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/035_014300_variabile-senza-salvataggio.jpg){ loading=lazy }

- **Sottocategoria** — assegnare la stessa etichetta di sottocategoria a un gruppo di variabili selezionate con Ctrl disegna una barra divisoria a tutta larghezza sopra di esse nel form, per organizzare visivamente form densi; la sottocategoria della variabile più in alto determina la posizione della barra.
- **Testo di aiuto** — tooltip mostrato al passaggio del mouse, utile per guidare l'utente (es. "inserire l'importo secondo il modulo XXXX").
- **Valore di default** vs. **Formula per default** — una costante fissa contro un valore iniziale calcolato tramite logica (utente corrente, data corrente, ecc.) — vedi 4.7.
- **Variabili di intestazione** — flag e numerazione (1, 2, 3...) di una manciata delle variabili più importanti (es. numero richiesta, codice stabilimento) affinché emergano in modo prominente in tutta l'applicazione (colonne della To-Do List, intestazioni), oltre alla singola schermata di dettaglio processo.
- **Tag**, flag "nascondi su mobile", dimensione del font (piccolo/medio/grande — differenza visiva minore).
- **Gruppo** — assegna una variabile a un gruppo master-detail (vedi 4.6).

###### Variabili di tipo Etichetta (Label)

Una variabile di tipo Label non è un campo DB reale: contiene un "Testo" rich-text che può includere **segnaposto di variabile** (tasto destro > inserisci variabile, es. "Richiesta numero {numero richiesta}") e persino immagini (es. un logo incollato). Un pattern comune: sostituire diversi campi read-only trascinati separatamente su un form con un'unica label che li compone in un'intestazione riassuntiva più curata, riutilizzabile su più schermate di task.

![label type variable](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/033_013319_label-type-variable.jpg){ loading=lazy }

###### Tabelle di origine (lookup) — valore singolo

La "Tabella di origine" trasforma una variabile Stringa da testo libero in una **scelta legata a una fonte dati**:

![tabella di origine source table](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/036_014503_tabella-di-origine-source-table.jpg){ loading=lazy }

- **Tabella locale** — una tabella creata direttamente nel database BPM (prefisso `P_...`), oppure una **vista** SQL creata lì.
- **Dati esterni** — richiede una stringa di connessione (server, database, utente, password; SQL o ODBC) verso il database di un sistema esterno (es. un database usato anche da SAP/SAM). Stringhe di connessione nominate/riutilizzabili possono essere predisposte per azienda/ambiente (es. "SAM A1", "SAM B") invece di codificare una stringa grezza in ogni campo.
- Scorciatoia sconsigliata ma a volte usata: creare una **vista dentro il DB di BPM che a sua volta punta cross-database al sistema esterno** — fragile (si rompe se spostata su un altro ambiente cliente) rispetto a una connessione esterna pulita.

    ![source table lookup local vs external](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/064_035352_source-table-lookup-local-vs-external.jpg){ loading=lazy }

- ODBC funziona ma può essere problematico con alcuni sistemi legacy (es. AS400); web service o connettori dedicati sono spesso preferibili in quei casi.
- La configurazione richiede di mappare la **colonna chiave** (colonna della tabella sorgente → variabile guida, obbligatoria) e poi mappature aggiuntive arbitrarie di **altre colonne** (altre colonne sorgente → altre variabili target), così selezionare un valore riempie automaticamente campi denormalizzati collegati (es. selezionare un codice fornitore riempie automaticamente la sua ragione sociale).
- **Lookup dai dati di gruppo del processo stesso** (fonte "Variabili locali"): invece di una tabella esterna, un campo può recuperare una riga da uno dei gruppi del processo (es. far scegliere all'utente "il preventivo vincente" dal gruppo "Lista Preventivi" già inserito in precedenza nello stesso processo, riempiendo automaticamente una coppia "Codice fornitore scelto"/"Ragione sociale scelta").

    ![lookup from local group data](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/073_045439_lookup-from-local-group-data.jpg){ loading=lazy }

- I **connettori preconfigurati** (es. un connettore SAM/SAP) sono un meccanismo correlato ma distinto: configurati per azienda (non con una stringa di connessione grezza) e, in particolare, a volte l'*unico* modo supportato per **scrivere** dati verso il sistema esterno (contro il sola-lettura di una connessione semplice). Approfondimento riservato a una sessione successiva.

    ![preview connectors e g sam](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/065_040110_preview-connectors-e-g-sam.jpg){ loading=lazy }

###### Variabili di gruppo — dati master-detail (1-a-molti)

Il meccanismo di BPM per dati 1-a-molti (es. N preventivi di fornitori su un'unica richiesta di investimento):

![group master detail variables](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/061_033236_group-master-detail-variables.jpg){ loading=lazy }

1. Si crea normalmente una variabile nel magazzino (es. "Codice Fornitore").
2. Invece di lasciarla a valore singolo, si clicca il pulsante "..." di configurazione e la si assegna a un **Gruppo** nuovo o esistente (es. "Lista Preventivi") — questo la trasforma nella prima colonna di una tabella di dettaglio virtuale/griglia.
3. Si aggiungono altre colonne semplicemente **trascinando ulteriori variabili direttamente sulla griglia** — il modo più rapido e comune (usato nel 99% dei casi). Ogni variabile ulteriore rilasciata dentro la griglia si unisce automaticamente allo stesso gruppo.

Vincoli e note:

- Una variabile appartiene a **esattamente un** gruppo.
- I gruppi sono una struttura **piatta/a un solo livello** — BPM deliberatamente **non** supporta sottogruppi annidati: un compromesso di usabilità, dato che chi progetta/configura è tipicamente un consulente, non un programmatore.
- Un processo può avere più gruppi indipendenti tra loro (es. "Lista Preventivi" e un separato gruppo "Team utenti").
- A runtime, il gruppo viene renderizzato come una **griglia modificabile** dove l'utente può aggiungere/rimuovere righe liberamente (a meno che non vengano aggiunte regole di obbligatorietà sui campi per riga, es. rendere obbligatori fornitore/importo *all'interno* di ogni riga — una questione separata dal "richiedere almeno una riga").
- Un **bottone stateless trascinato nella griglia** ("Dettagli...") può aprire un pop-up più grande con il form di una singola riga (tramite le proprie "Variabili da richiedere") — risolve il problema di colonne di griglia troppo strette per campi come note lunghe.

    ![detail pop up form for a grid row](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/063_034841_detail-pop-up-form-for-a-grid-row.jpg){ loading=lazy }

- Le colonne di un gruppo supportano le stesse **Tabelle di origine** delle variabili ordinarie (vedi 4.5), compreso il lookup da dati locali di un altro gruppo o del gruppo stesso.

###### Formule

Le formule sono il livello di scripting integrato di BPM, scritte in sintassi **Visual Basic**, modificate tramite un editor di formule con un menu di supporto al tasto destro (anno/utente/data correnti, e un albero ricercabile di tutte le variabili di processo per pagina). Le espressioni one-liner in stile Excel funzionano direttamente (es. `Year([data richiesta])`); la logica multi-riga richiede un'istruzione `Return` esplicita e supporta `If/Then/Else`. Le formule **si ricalcolano automaticamente** ogni volta che una variabile da cui dipendono cambia (tracciamento delle dipendenze, come in un foglio di calcolo).

![the formula editor visual basic](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/039_015258_the-formula-editor-visual-basic.jpg){ loading=lazy }

Tipi di formula, e dove si configurano:

- **Formula** (a livello di magazzino, "la" formula) — un valore calcolato sempre valido a livello globale, es. `anno = Year(data_richiesta)`, oppure un totale corrente `totale_costi = importo_richiesta + costi_accessori`.

    ![calculated total via formula](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/043_020607_calculated-total-via-formula.jpg){ loading=lazy }

- **Formula di validazione** — impostata per task su "variabili da richiedere" (non globale); ritorna vero/falso per validare un campo oltre il semplice flag obbligatorio (es. `data_richiesta >= Today()`), e può impostare un messaggio di errore personalizzato mostrato all'utente (`Errore = "..."`). Usabile anche per esprimere "obbligatorio *se* [condizione]", cosa che un semplice flag obbligatorio non può fare.

    ![formula di validazione](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/040_015538_formula-di-validazione.jpg){ loading=lazy }

- **Formula di visibilità** — mostra/nasconde dinamicamente un campo in base a una condizione.
- **Formula per default** — imposta il valore *iniziale* di una variabile solo la prima volta che viene aperta mentre è ancora non valorizzata (es. richiedente = utente corrente, data = oggi); distinta dal costante **Valore di default** fisso.

    ![formula per default vs valore di default](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/042_020133_formula-per-default-vs-valore-di-default.jpg){ loading=lazy }

- **Formula per ridolli** — rende un campo condizionalmente in sola lettura in determinate circostanze; considerata una tecnica più avanzata/specifica.
- **Condizione di abilitazione** — la formula collegata a una freccia di transizione o a un ramo di gateway per controllare l'instradamento (vedi 2.3).

Indicazione del docente: il motore è abbastanza potente da gestire complessità arbitraria, ma la raccomandazione è di mantenere le formule semplici quanto la logica di business richiede realmente, senza ingegnerizzare eccessivamente.

###### Bottoni e "Variabili da impostare"

Una variabile Booleana può essere renderizzata come checkbox oppure come **Bottone** (statefull — si comporta come un interruttore che resta "premuto" — oppure stateless, un comando puro). I bottoni sono più potenti di una semplice checkbox perché è possibile agganciare loro delle azioni:

- **Variabili da impostare**: un'alternativa imperativa a una Formula reattiva — si aggancia al bottone una lista di azioni che valorizzano variabili target solo al momento del click (es. un bottone "Ricalcola totali" che imposta esplicitamente `totale_costi`), in contrapposizione a una Formula che si ricalcola automaticamente a ogni cambio di dipendenza. Due varianti dello stesso obiettivo di fondo, scelte in base a se si vuole un comportamento "sempre live" oppure "solo su richiesta".

    ![variabili da impostare button actions](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/044_021322_variabili-da-impostare-button-actions.jpg){ loading=lazy }

- Comportamento del bottone **Aggiunta allegati** — vedi sezione 7.2.
- Un bottone può anche avere una propria sotto-form **"Variabili da richiedere"** (vedi 4.2), usata sia per l'inserimento di dettaglio in pop-up standalone sia per il pattern "Dettagli" a livello di riga di gruppo (vedi 4.6).

#### Pubblicazione e versioni


- **Pubblicare** rende un modello vivo/utilizzabile dagli utenti citati al suo interno. Esegue una validazione (mostra warning, ma in genere consente comunque di pubblicare) e crea una nuova versione numerata (R00, R01,...); **tutte le versioni vengono conservate** — sia per motivi tecnici (le istanze in corso fanno riferimento a versioni precedenti), sia per motivi organizzativi/di audit.

    ![publishing a process](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/009_001536_publishing-a-process.jpg){ loading=lazy }

- Un modello di processo richiede un **Nome modello** (la chiave usata per trovarlo/sovrascriverlo) prima di poter essere pubblicato o salvato. Si imposta cliccando sull'area bianca del canvas > proprietà del processo.

    ![naming and publishing the model](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/027_010205_naming-and-publishing-the-model.jpg){ loading=lazy }

- Due ulteriori **formule a livello di processo** sono richieste per una pubblicazione pulita (la validazione avvisa se mancano):

    ![process name description formulas](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/052_024811_process-name-description-formulas.jpg){ loading=lazy }

 - **Formula per il calcolo del nome del processo** — costruisce il titolo/business-key di ogni istanza, tipicamente da un contatore o una variabile data, es. `[numero richiesta] & "/" & [anno]`.
 - **Formula per la descrizione del processo** — costruisce una stringa libera di intestazione, es. `"Richiesta numero " & [numero] & " " & [stabilimento]`.
 Questi nome/descrizione sono ciò che appare nella To-Do List, nelle griglie di ricerca e nelle intestazioni, al posto degli ID interni grezzi.
- **Salva su file**: un processo (l'intero design — diagramma, variabili, form, formule) può essere esportato su un unico file **JSON** locale (estensione `.jbkf`) invece della/in aggiunta alla pubblicazione — il modo standard per spostare una configurazione tra ambienti (es. portatile → ambiente cliente). Report e dashboard fanno eccezione: hanno vita propria perché possono coprire più processi contemporaneamente.
- **Comportamento del versionamento per le istanze in corso**: ripubblicare **non** modifica retroattivamente le istanze già in esecuzione — ogni istanza resta ancorata alla versione del modello attiva quando è stata avviata. Un pulsante a livello di processo, **"Aggiornamento processo"**, consente di allineare manualmente un'istanza in corso specifica a una versione più recente (es. "Aggiorna dalla versione 16 alla 17"). Alcune modifiche (interventi sul magazzino, nuovi binding di tabella) vengono recepite automaticamente dalle istanze in corso; le aggiunte di layout/UI a un task già eseguito tipicamente richiedono questa azione di aggiornamento esplicita. Se il salto di versione è troppo grande/incompatibile, l'unica soluzione è riavviare l'istanza e replicarne manualmente l'avanzamento.

    ![versioning running instances pin to their version](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/066_040224_versioning-running-instances-pin-to-their-version.jpg){ loading=lazy }

- **Override riservati agli amministratori**, per casi eccezionali:
 - **Forzatura dei valori del magazzino** su un'istanza in corso, dalla sua schermata di dettaglio processo, fuori dal flusso normale ("forzatura extra processo") — richiede conferma/scarto alla chiusura, ed è interamente tracciata in Storico.

     ![admin force edit outside the process flow](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/060_032544_admin-force-edit-outside-the-process-flow.jpg){ loading=lazy }

 - **Forzatura dell'avanzamento del processo**: tasto destro su un task in modalità modifica > "Imposta oggetto attivo" per saltare/far avanzare forzatamente il motore a un dato passo — esplicitamente definito "barare" dal docente, ma utile in fase di sviluppo (passi dimenticati) o per sbloccare un processo realmente incastrato senza un intervento di un programmatore sul database.

#### Esecuzione e monitoraggio


###### To-Do List

L'interfaccia concreta e quotidiana per partecipare ai processi. Si apre di default al login.

![watching the token move](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/011_001906_watching-the-token-move.jpg){ loading=lazy }

- **Filtri**: ambito utente ("Tutti gli utenti visibili" = l'amministratore vede tutti; "Tutto" = i propri task e quelli dei propri gruppi — il filtro normale per un utente comune), intervallo date (giorno/settimana/mese/tutti gli aperti) e **stato dell'attività**.
- **Tre stati di attività**, visibili sia qui che nel diagramma: **Eseguita** (completata), **In corso** (disponibile ora), **Pianificata** (futura/pianificata — verde chiaro).

    ![three activity states](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/053_025552_three-activity-states.jpg){ loading=lazy }

- La griglia supporta il **raggruppamento** con tasto destro (es. per modello di processo) e il riordino delle colonne; le preferenze di layout sono **salvate automaticamente per utente**. Colonne di default: Utente, Attività, Modello, Nome processo, Data inizio prevista, Priorità (un'etichetta libera senza significato funzionale, utile solo per ordinamento/promemoria), Scadenza, % completamento.

    ![customizing the to do list grid](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/054_025806_customizing-the-to-do-list-grid.jpg){ loading=lazy }

- **Esecuzione di un task**: si clicca "Esegui" per compilare i campi (validati contro le regole di obbligatorietà/formula — un indicatore rosso blocca l'invio finché non è soddisfatto); **Completato** invia e fa avanzare il processo; **Salva/Salva e chiudi** persiste una bozza senza far avanzare il processo (i dati restano per dopo).

###### Schermata di dettaglio/ispezione processo

Accessibile dalla To-Do List (soggetta ai permessi di visualizzazione/modifica — vedi sezione 9). Tab disponibili:

![process detail inspection screen](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/055_030322_process-detail-inspection-screen.jpg){ loading=lazy }

- **Variabili** — il magazzino completo, organizzato secondo la stessa struttura di pagine/tab progettata a monte.
- **Intestazione** (anagrafica) — campi di sistema fissi: nome processo, descrizione, modello sorgente, attività corrente, data creazione, proprietario (chi ha avviato il processo).
- **Allegati** — il dossier documentale (vedi sezione 7).
- **Processi collegati** — collegamenti verso altre istanze di processo correlate.
- **Pianificazione** — informazioni su asse temporale/vista Gantt-style.
- **Storico** — il log di audit completo (vedi sezione 8).

Questa schermata è spesso usata da un **proprietario** di processo per monitorare avanzamento/tempistiche/stato tra istanze diverse; l'accesso può essere concesso in sola lettura o lettura/scrittura a seconda del pubblico.

###### Ricerca processi

"Ricerca processi" restituisce **una riga per istanza di processo** (non per task), coprendo sia istanze aperte che chiuse/archiviate (nulla viene cancellato a meno che non venga applicata una politica di archiviazione esplicita).

![searching and filtering process instances](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/012_002441_searching-and-filtering-process-instances.jpg){ loading=lazy }

- La vista di default include molte colonne di sistema generiche di scarso interesse; **"Modifica visualizzazione"** permette di scegliere le colonne rilevanti (es. anno, codice stabilimento, richiedente, tipo richiesta, importo, note).
- È possibile salvare più viste con nome; marcarne una come **"Pubblicato"** la rende visibile a tutti gli utenti, non solo a chi l'ha creata — un tipico compito dell'amministratore è costruire buone viste di ricerca di default per gli utenti finali, dato che la vista di default "out of the box" non è molto utile.

    ![custom search views](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/057_030853_custom-search-views.jpg){ loading=lazy }

- Le griglie in tutto BPM (To-Do List, ricerca, griglie collegate al magazzino) supportano filtri di colonna sia a dropdown che testuali liberi.

###### Voci di menu personalizzate

Configurazione > Opzioni generali > **Menu personalizzati** permette a un amministratore di aggiungere scorciatoie dirette (fino a 3 livelli: menu radice / sottomenu / descrizione) collegate a un'azione specifica su un processo (es. "avvia Richiesta INV" o "cerca richieste Richiesta INV"), permettendo agli utenti finali di bypassare i menu generici "Nuovo processo"/"Ricerca processi". I menu personalizzati si aggiornano solo al login/riavvio successivo dell'applicativo.

![custom menu entries](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/059_032017_custom-menu-entries.jpg){ loading=lazy }

###### Storico (log di audit)

Ogni visualizzazione, modifica ed esecuzione di task su un'istanza di processo viene registrata con **timestamp + utente** (es. creata alle 14:38, visualizzata alle 14:41, campi modificati alle 14:45/14:47, task X eseguito alle 14:47...). Doppio clic su una voce di log mostra un **diff prima/dopo a livello di campo** di esattamente cosa è cambiato.

![storico full audit log](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/056_030614_storico-full-audit-log.jpg){ loading=lazy }

Scopo: oltre alla semplice tracciabilità, è esplicitamente indicato come prezioso per la **certificazione di qualità/compliance** — dimostrare che una procedura progettata è stata effettivamente seguita come specificato. La visibilità dello Storico agli utenti finali (contro il solo amministratore/proprietario) è una scelta configurabile.

#### Allegati


###### Concetto

BPM ha una propria gestione documentale/allegati, sempre ambientata **all'interno di un processo** (un documento non vive mai standalone in BPM — è sempre parte del "dossier"/"plico" di un processo). I documenti possono essere organizzati in **cartelle virtuali** create dentro il tab Allegati del processo ("Visualizza elenco" vista a lista / "Visualizza struttura" vista ad albero), es. "Preventivi", "Scheda Investimento".

![attachments overview](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/067_040716_attachments-overview.jpg){ loading=lazy }

**Visualizzatore documenti integrato**: PDF, Word, Excel, e-mail (.msg) e immagini si anteprimano direttamente dentro BPM; altri tipi di file si aprono con doppio clic nell'applicazione associata dal sistema operativo. E-mail e allegati possono essere **trascinati direttamente da Outlook**, utile quando un processo è innescato da uno scambio di e-mail.

###### Abilitare gli allegati per task

**"Allegati da richiedere"** è la controparte file-management di "Variabili da richiedere":

![allegati da richiedere](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/068_040924_allegati-da-richiedere.jpg){ loading=lazy }

- Attiva/disattiva la gestione allegati per un dato task.
- Può fissare la cartella target di default del task (es. lo Start punta a "Scheda Investimento").
- Può essere impostato in **sola lettura** su un task puramente per esporre la visibilità dei documenti già raccolti senza permetterne la modifica (es. mostrare tutti gli allegati, in sola lettura, su un passo di revisione successivo).

Un **pattern di allegato obbligatorio**: si crea una variabile Bottone stateless (es. "Inserisci scheda richiesta"), la si configura in "Tipo impostazioni di base" come **Aggiunta allegati**, si sceglie una cartella target e opzionalmente si restringono le estensioni file ammesse, poi la si trascina nelle "variabili da richiedere" di un task e la si marca obbligatoria — pura configurazione, senza scripting, per forzare il caricamento di uno specifico documento richiesto prima che il processo possa avanzare. Applicabile sia a livello di processo (es. una "scheda investimento" PDF obbligatoria allo Start) sia a livello di riga di gruppo (es. un bottone "Allega preventivo" dentro ogni riga di preventivo in una griglia di dettaglio).

![mandatory attachment via a button](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/070_042244_mandatory-attachment-via-a-button.jpg){ loading=lazy }

###### Storage: Database vs. File System

Un nuovo processo nasce con una root di allegati **su database** di default ("Attachments" — lo stream del file memorizzato come tabella dentro il database di BPM stesso). Si possono creare **root aggiuntive**:

![storage roots database vs file system](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/069_041300_storage-roots-database-vs-file-system.jpg){ loading=lazy }

- **Su database**, oppure
- **Su file system**, dato un path di base (tipicamente una share di rete raggiungibile da tutti) che può essere **costruito dinamicamente da variabili di processo** (es. un pattern di path che combina stabilimento + numero richiesta), così BPM crea automaticamente a runtime una sottocartella reale per-istanza su disco — rispecchiando come molti clienti già organizzano i documenti su unità condivise per stabilimento/numero richiesta.

Root dei due tipi possono essere **liberamente mescolate** all'interno di uno stesso processo; visivamente, le cartelle file system hanno un'icona distinta (con tinta blu) nell'albero, ma funzionalmente, dall'interno di BPM, il caricamento drag-and-drop funziona identicamente in entrambi i casi. Il tasto destro su una cartella offre diverse capacità amministrative a seconda del tipo di storage.

**Avvertenze**:

- Gli allegati su DB sono interamente governati da BPM (cancellazione in BPM = definitiva; si applicano i permessi BPM).
- Gli allegati su file system restano accessibili/modificabili/cancellabili in modo indipendente **direttamente sulla share, fuori da BPM** — un vero gap, poiché il modello di permessi di BPM non governa i permessi a livello di file system (due sistemi di permessi da mantenere in parallelo). Opinione personale del docente: lo storage su FS è concettualmente la scelta "sbagliata" per un approccio corretto di gestione documentale (sicurezza/logging/accesso dovrebbero vivere in SQL), ma è pragmaticamente supportato e usato nella pratica, specialmente per un rollout iniziale più leggero quando un cliente ha già documenti organizzati su file system (rimandando la migrazione "corretta" al DB a una fase progettuale successiva).
- BPM può anche **pre-generare un intero albero di cartelle template** alla creazione del processo (rispecchiando una tipica struttura di cartelle di commessa/progetto — preventivi/disegni/schede tecniche/...), utile per clienti già abituati a queste convenzioni.
- Buona prassi per i path delle root FS: memorizzare il nome del server in una **variabile d'ambiente** invece di codificarlo in ogni formula di path (raramente fatto realmente sul campo); alcuni clienti mantengono invece una tabella SQL che mappa ogni processo ai propri path di root.

###### Metadati e versionamento a livello di allegato

- Un allegato può avere **colonne di metadati personalizzate** (distinte dalle variabili di processo) che vengono legate al valore di una variabile di processo al momento del caricamento (es. aggiungere una colonna "Ragione Sociale" alla griglia allegati, legata alla ragione sociale del fornitore di quella riga di preventivo) — uno snapshot denormalizzato catturato sul file stesso.
- Gli attributi standard di un allegato includono **Revisione** e **Stato** (Attivo/Obsoleto). Il versionamento oggi è **solo manuale**: un allegato può essere marcato "Obsoleto" e la vista può essere alternata per mostrare/nascondere gli obsoleti (es. riallegare un documento revisionato quando un processo torna indietro in un loop) — non esiste un concatenamento automatico delle versioni.
- I caricamenti di allegati sono tracciati in **Storico** (sezione 6.5) esattamente come le modifiche alle variabili.
- Nessun limite di dimensione file rigido è imposto da BPM stesso (file molto grandi rischiano solo timeout/lentezza); una **dimensione massima** può essere esplicitamente configurata su un bottone "Aggiunta allegati".
- Gli allegati possono (argomento riservato a una sessione successiva) essere integrati con il prodotto documentale di Digit ("Globo"), così i file vivono lì invece che in BPM.

#### Sotto-processi


Una shape Sotto-processo nasconde un mini-flusso annidato, progettato in modo indipendente, dietro un unico box nel diagramma padre (doppio clic per entrare/progettarlo). Usi tipici:

![sub processes](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/071_043856_sub-processes.jpg){ loading=lazy }

- Mantenere il diagramma di primo livello pulito/leggibile pur modellando il dettaglio sottostante.
- **Far evolvere** un design: un Task semplice esistente può essere convertito in un Sotto-processo se in seguito si scopre che necessita di una scomposizione interna (es. suddividere un unico task "Approvazione" in passi di pre-approvazione/qualità/tecnico) senza dover riprogettare il flusso padre.

**Sotto-processo ricorrente**: un sotto-processo può essere legato a un **gruppo** (l'insieme di variabili master-detail, vedi 4.6) e marcato "ricorrente" — a runtime genera una istanza completa del proprio flusso interno **per ogni riga** di quel gruppo (es. un mini-flusso di valutazione per ogni preventivo fornitore ricevuto). Configurabile come:

![recurring sub process](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/072_044146_recurring-sub-process.jpg){ loading=lazy }

- **Parallelo** (tutte le istanze generate sono aperte contemporaneamente; l'assegnatario le esegue in qualsiasi ordine) — l'icona mostra barre parallele aggiuntive.
- **Sequenziale** (una alla volta; richiede di indicare la variabile che determina l'ordine di esecuzione) — l'icona mostra linee sequenziali.
- Una "formula per condizione" opzionale può filtrare quali righe generano effettivamente un'istanza.

Il flusso padre procede oltre il sotto-processo solo quando **tutti** i rami generati sono terminati (sincronizzazione/join). Questo pattern è prezioso ogni volta che il numero di sotto-attività parallele è noto solo a runtime, non in fase di progettazione — es. azioni correttive/di miglioramento qualità, passi di ispezione/collaudo, oppure (come dimostrato nel corso) N preventivi fornitore da valutare. Dentro un sotto-processo ricorrente legato a un gruppo, le variabili di quel gruppo appaiono come campi a **valore singolo** (concettualmente si è "dentro una riga"); le variabili di altri gruppi e le variabili di intestazione restano accessibili normalmente.

#### Permessi


###### Regola di base

**Un utente o un gruppo semplicemente citato in un processo** (come Esecutore/Responsabile/in conoscenza su una qualche attività) vede automaticamente e può agire su quell'attività nella propria To-Do List — **non è richiesta alcuna concessione di permesso aggiuntiva** per questo soltanto. I permessi governano tutto ciò che va *oltre* questa baseline (ricerca, creazione generica di nuovi processi dal menu, override in stile amministratore, accesso a tabelle/dashboard/report).

###### Utenti e gruppi

- Utenti e Gruppi condividono un'unica tabella/griglia sottostante, filtrabile per tipo. Un utente ha un nome (stringa libera, la convenzione di naming è a discrezione) e una **e-mail** (importante — usata per le mail di notifica generate da BPM).
- Un utente BPM può **opzionalmente** essere collegato a un account Windows/dominio. Effetto: il **client desktop ottiene il single sign-on automatico** quando collegato; il **client Web, in questa versione, richiede ancora la password di dominio** (nessun SSO web per ora) — "l'ultimo username usato" mostrato al login web è solo un cookie, non vero SSO.

    ![domain linked users single sign on](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/075_050705_domain-linked-users-single-sign-on.jpg){ loading=lazy }

- **L'appartenenza a un gruppo serve due scopi distinti**, che spesso si sovrappongono ma non sono identici: (a) ereditare i *permessi* di quel gruppo, e (b) essere un partecipante che riceve i task assegnati a quel gruppo in uno o più processi. Un utente è tipicamente in più gruppi per queste due ragioni distinte contemporaneamente.

###### Categorie di permessi

1. **Permessi Menu** (a livello applicativo) — abilitano/disabilitano intere aree dell'app: cambio password, accesso a una "pagina", avvio nuovo processo (generico), visualizzazione processi in corso, ecc. Suddivisi in un set **operativo** (home, nuovo processo, in corso, To-Do sulla schermata processo, import, allegati, pianificazione) e un set di **configurazione** (gestione modelli di processo, tabelle, configurazione, visualizzazione/modifica utenti) — gli utenti finali ordinari tipicamente non hanno alcuno dei permessi del set di configurazione.

    ![permission categories overview](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/076_051206_permission-categories-overview.jpg){ loading=lazy }

2. **Permessi Processi** (per uno specifico modello di processo) — granulari, disattivati di default (rosso): **Creazione** (avviare una nuova istanza di questo modello — nota: richiede anche il permesso *menu* generico "nuovo processo" attivo, cioè una logica AND tra i due livelli), **Visualizzazione** (aprire/cercare il dettaglio del processo in lettura), **Modifica** (forzare la modifica di valori — la capacità di override amministrativo della sezione 5), **Eliminazione** (cancellare permanentemente una specifica istanza — distinto dai pieni diritti di amministratore di sistema; può essere concesso a un "proprietario di processo" non amministratore), **Copia/Duplica**, **Cambio stato processo** (forzare l'avanzamento, stesso meccanismo dell'override amministrativo).
3. **Permessi Tabelle** — per singola tabella locale BPM, separatamente per Visualizza (sfogliare l'area di gestione tabella standalone) contro Modifica (modificare i record) — distinto dal semplice uso di quella tabella come fonte lookup dentro un form di processo.
4. **Permessi Dashboard / Report** — concessione per singola dashboard e per singolo report (le dashboard in particolare sono spesso ristrette, poiché possono esporre cifre sensibili come totali monetari).
5. (Menzionati brevemente, non approfonditi in questo corso) **Prefiltri/alias** sull'accesso ai dati.

###### Logica di risoluzione e buone prassi

- I diritti si risolvono in modo **additivo** da due fonti: concessione diretta a livello **utente**, oppure **ereditata via gruppo** di appartenenza (l'interfaccia marca un diritto come "abilitato da gruppo" quando ereditato).
- **Buona prassi: concedere via gruppi, non individui** — es. creare un gruppo solo-permessi "Inserimento richieste INV", concedergli Creazione su "Richiesta INV", poi aggiungere gli utenti a quel gruppo. Regola pratica: *"se ci si ritrova con tanti o più gruppi-permesso quanti utenti, probabilmente c'è qualcosa che non va nel design."*
- **Semantica di override Abilita/Nega**: abilitare un permesso direttamente su un utente quando lo ha già tramite un gruppo rende la concessione "appiccicosa" (sopravvive a una successiva rimozione dal gruppo); rimuovere una concessione utente ridondante ancora coperta dal gruppo non ha effetto; un **"Nega" a livello utente** ha priorità su un'Abilitazione a livello gruppo, permettendo di escludere un membro specifico da una concessione altrimenti valida per tutto il gruppo.

    ![enable vs deny override semantics](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-base/077_052605_enable-vs-deny-override-semantics.jpg){ loading=lazy }

- **Ciò di cui un utente finale tipico ha davvero bisogno**: per un utente che si limita a *ricevere ed eseguire* task dalla To-Do List, non servono essenzialmente **permessi aggiuntivi** oltre all'essere citato nel processo (gli allegati e i campi di cui ha bisogno sono già esposti tramite la configurazione "variabili/allegati da richiedere" del task stesso). L'aggiunta comunemente necessaria è **Creazione** (avviare un nuovo processo), per gli utenti che iniziano nuove richieste dal menu generico (non necessaria se agiscono solo su task già assegnati). Un accesso più ampio come Visualizzazione/Modifica/Eliminazione è riservato a proprietari di processo/amministratori, non ai partecipanti ordinari.

###### Considerazione finale del docente

A un livello base, il sistema di permessi richiede una configurazione relativamente contenuta, perché la maggior parte del "pensiero" di controllo accessi è previsto avvenga dentro la **progettazione del processo stesso** (chi è citato su quale task, tramite quale gruppo). Le matrici di permesso più fini (menu/processo/tabella/dashboard/report) sono un livello avanzato che un primo corso "base" può in gran parte sorvolare — questo punto di chiusura segna la fine della parte fondamentale del corso; integrazione SAP, integrazione documentale (Globo), connettori e copertura più approfondita di dashboard/report sono riservati a sessioni successive.

### Tutorial: processo Richiesta INV


Questo tutorial ricostruisce in ordine sequenziale il flusso dimostrativo principale del corso: la costruzione, dall'abbozzo del diagramma fino a pubblicazione ed esecuzione, del processo di richiesta di autorizzazione investimento usato come caso guida. Seguendo questi passi è possibile ricreare l'esercizio nel Designer BPM.

1. [Fase 1 — Abbozzo del diagramma](#fase-1-abbozzo-del-diagramma)
1. [Fase 2 — Utenti e gruppi](#fase-2-utenti-e-gruppi)
1. [Fase 3 — Primo salvataggio e pubblicazione](#fase-3-primo-salvataggio-e-pubblicazione)
1. [Fase 4 — Il magazzino delle variabili](#fase-4-il-magazzino-delle-variabili)
1. [Fase 5 — Variabili da richiedere sui singoli task](#fase-5-variabili-da-richiedere-sui-singoli-task)
1. [Fase 6 — Approvazioni, condizioni e diramazioni](#fase-6-approvazioni-condizioni-e-diramazioni)
1. [Fase 7 — Formule di processo e nuova pubblicazione](#fase-7-formule-di-processo-e-nuova-pubblicazione)
1. [Fase 8 — Avviare e osservare un'istanza](#fase-8-avviare-e-osservare-unistanza)
1. [Fase 9 — Variabili di gruppo: i preventivi fornitore](#fase-9-variabili-di-gruppo-i-preventivi-fornitore)
1. [Fase 10 — Chiusura dell'esercizio](#fase-10-chiusura-dellesercizio)

#### Fase 1 — Abbozzo del diagramma


1. **Aprire il Designer** e creare un nuovo modello di processo. Iniziare trascinando le attività (Task) che compongono, a grandi linee, il flusso di richiesta investimento: non è necessario avere già chiari tutti i dettagli — l'obiettivo è abbozzare rapidamente, eventualmente insieme al cliente/utente business.
2. **Creare la prima attività**, "Presa in carico da ufficio sicurezza": trascinarla sul canvas (riceve un codice interno immutabile, es. Activity1/Activity2), poi tasto destro > "Modifica testo" per assegnarle il nome visibile.
3. **Ribattezzare lo Start**: tasto destro sull'evento di Start (cerchio verde) > "Sposta testo" per staccare l'etichetta e scrivere, ad esempio, "Inserimento richiesta".
4. **Aggiungere le attività successive** del flusso: "Approvazione controllo di gestione" e "Approvazione direzione industriale", collegandole in sequenza con lo strumento **Link** (trascinare dal punto di ancoraggio giallo di un'attività a quella successiva).
5. **Allineare il disegno**: selezionare più shape con Ctrl e usare i comandi della ribbon "Stessa dimensione" e "Allinea" per tenere il diagramma ordinato e leggibile — ricordando che il disegno sarà visto dagli utenti finali.
6. **Aggiungere gli Stati** (milestone): inserire uno stato "Inserito" collegato subito dopo lo Start e uno stato "Approvata" alla fine del flusso principale — sono etichette di avanzamento generale, indipendenti dal task specifico in corso.
7. **Abbozzare i percorsi alternativi**: se la Direzione Industriale non approva, la richiesta torna indietro. Aggiungere un'attività "Revisione da parte del richiedente" collegata dal ramo di non-approvazione del controllo di gestione, da cui il richiedente può a sua volta rimandare la richiesta al controllo di gestione oppure rinunciare, transitando in uno stato "Annullata".
8. **Decidere se usare un oggetto "Fine"**: opzionale, puramente cosmetico — il processo si conclude comunque automaticamente quando non restano attività da eseguire. Un secondo "Fine", ad esempio per il ramo di annullamento, può aiutare la leggibilità del diagramma senza avere alcun effetto funzionale.

#### Fase 2 — Utenti e gruppi


9. **Spostarsi in Configurazione > Utenti e Gruppi.** Utenti e gruppi condividono la stessa griglia, filtrabile per tipo.
10. **Creare i gruppi necessari al processo**, ad esempio "AM" (controllo di gestione/amministrazione) e "Direzione Tecnica" — in questa fase basta dare loro un nome, senza preoccuparsi ancora dei permessi. I gruppi vengono tipicamente creati ad hoc per il processo, non importati da Active Directory, perché la granularità richiesta raramente coincide con i gruppi già esistenti nel dominio aziendale.
11. **Tornare al Designer** sull'attività "Approvazione controllo di gestione" e aprire "Utenti e responsabili". Impostare il gruppo "AM" come **Esecutore**: tutti i membri del gruppo (quando ci saranno) troveranno il task nella propria To-Do List; il primo che lo esegue fa avanzare il processo.
12. Ripetere per "Approvazione direzione industriale", assegnando il gruppo "Direzione Tecnica" come Esecutore.
13. In fase di progettazione è ammesso lasciare temporaneamente un'attività priva di utente assegnato (resta visibile solo all'amministratore); va però sistemata prima del go-live.
14. (Nota a margine, non obbligatoria per l'esercizio base) Per un flusso più controllato, è possibile marcare un'attività "Task deve essere assegnato prima di poter essere eseguito", introducendo un passaggio di smistamento esplicito da parte di un Responsabile.

#### Fase 3 — Primo salvataggio e pubblicazione


15. **Cliccare sull'area bianca del canvas** per aprire le proprietà del processo e impostare il **Nome modello**, ad esempio "Richiesta INV" — è il prerequisito per poter salvare o pubblicare.
16. **Pubblicare** il modello: il sistema segnala alcuni warning (che verranno risolti più avanti, quando saranno impostate le formule di nome/descrizione processo) ma consente comunque la pubblicazione, creando la versione R00.
17. In alternativa (o in aggiunta), usare **Salva su file** per esportare l'intero processo in un file JSON locale (estensione `.jbkf`) — utile per spostare la configurazione tra ambienti o per consultare i dettagli del modello generato dalla macchina.

#### Fase 4 — Il magazzino delle variabili


18. **Aprire il magazzino delle variabili**: Strumenti > "Inserimento modifica variabili" — appare come una nuova pagina/tab del processo, inizialmente vuota.
19. **Creare la prima variabile**: "Nuova variabile" e assegnarle il nome "richiedente". Di default viene creata come tipo Stringa; cambiarne il tipo in **Utente (User type)**, poiché rappresenta la persona che inoltra la richiesta.
20. **Trascinare la variabile "richiedente" sul canvas del form** — a questo punto compare come campo utente, con possibilità di scegliere tra tutti gli utenti/gruppi registrati in BPM.
21. **Creare le variabili aggiuntive di testata**, tipicamente: "data richiesta" (tipo Data), "tipo richiesta" (tipo Lista Valori), "numero richiesta" (tipo Numerico, poi configurato come contatore), "codice stabilimento" (tipo Stringa, con tabella di origine) e "note richiesta" (tipo Memo). Trascinare ciascuna sul form man mano che viene creata.
22. **Organizzare il layout**: selezionare più campi con Ctrl e usare gli strumenti di allineamento ("Allinea in alto", "Allinea a destra", "Stessa dimensione") per un form ordinato — è la schermata che vedranno gli utenti finali.
23. (Opzionale, buona prassi) **Creare una nuova pagina di variabili** per il gruppo di campi legati alle approvazioni (vedi passo 27), prefissandola numericamente (es. "02 - Approvazioni") per mantenere l'organizzazione allineata al flusso cronologico del processo.

#### Fase 5 — Variabili da richiedere sui singoli task


24. **Sullo Start**, tasto destro > "Variabili da richiedere" e trascinare i campi che il richiedente deve compilare all'apertura: richiedente, data richiesta, tipo richiesta, numero richiesta, codice stabilimento, note richiesta.
25. **Impostare "obbligatorio"** sui campi che lo richiedono direttamente nella schermata "variabili da richiedere" del task (impostazione locale, indipendente dal default a livello di magazzino).
26. **Riutilizzare il layout su un altro task** (es. "Revisione da parte del richiedente"): dalla pagina dello Start, esportare la categoria/pagina corrente su file, poi sul task di destinazione usare "Importa e sostituisci categoria corrente" per ricrearla identica, evitando di ritrascinare manualmente ogni campo.

#### Fase 6 — Approvazioni, condizioni e diramazioni


27. **Creare una nuova pagina di variabili "Approvazioni"** e, al suo interno, le variabili: "esito approvazione CDG" (tipo Lista Valori, con valori "Approvata"/"Non approvata"), "note approvazione CDG" (tipo Memo), e in modo analogo "esito approvazione DirTec" e le relative note.
28. **Sull'attività "Approvazione controllo di gestione"**, aprire "Variabili da richiedere" e trascinare l'intestazione, "esito approvazione CDG" e "note approvazione CDG". Marcare "esito approvazione CDG" come obbligatorio.
29. **Impostare la condizione sulla freccia di approvazione**: selezionare la freccia che esce verso il ramo positivo, tasto destro > "Condizione di abilitazione", cercare la variabile "esito approvazione CDG" e scrivere la condizione (es. `esito approvazione CDG = "Approvata"`).
30. **Impostare la condizione complementare sull'altra freccia** (verso "Revisione da parte del richiedente"): `esito approvazione CDG = "Non approvata"`. Ricordare che il motore non garantisce la mutua esclusività: è responsabilità di chi progetta scrivere condizioni che si bilancino correttamente.
31. **In alternativa, sostituire le frecce condizionate con un oggetto Gateway**: inserire un Gateway (rombo) subito dopo "Approvazione controllo di gestione", ribattezzarlo (es. "Scelta approvazione"), collegarlo ai due rami di uscita, quindi doppio clic/tasto destro > "Configurazione" per impostare in un'unica schermata le condizioni `esito approvazione CDG = "Approvata"` sul primo ramo e marcare il secondo come default/else.
32. **Assegnare un instradamento dinamico**: sul task "Revisione da parte del richiedente", impostare come Esecutore la variabile Utente "richiedente" (invece di un gruppo fisso) — così il task torna sempre a chi ha originato la richiesta.
33. (Facoltativo, per illustrare i gateway paralleli/inclusivi) Dopo l'approvazione finale, inserire un Gateway **Parallelo** che forchi il flusso in due rami simultanei — es. "Collaudo" e "Parte amministrativa" — e un secondo Gateway Parallelo a valle per sincronizzarli prima di proseguire.

#### Fase 7 — Formule di processo e nuova pubblicazione


34. **Impostare la formula per il calcolo del nome del processo**, nelle proprietà del processo (area bianca del canvas), ad esempio `[numero richiesta] & "/" & [anno]`.
35. **Impostare la formula per la descrizione del processo**, ad esempio `"Richiesta numero " & [numero richiesta] & " " & [codice stabilimento]`.
36. **Ripubblicare** il modello: questa volta i warning relativi a nome/descrizione dovrebbero sparire, e viene generata una nuova versione (es. R01).

#### Fase 8 — Avviare e osservare un'istanza


37. Dal menu, selezionare **"Nuovo processo"** e scegliere il modello "Richiesta INV". Compilare il form dello Start (i campi obbligatori non soddisfatti mostrano un indicatore rosso che blocca l'invio) e confermare.
38. **Osservare il diagramma a runtime**: l'attività appena completata appare in grigio, l'attività corrente in giallo ("ha il pallino"), lo stato attivo in verde, e le attività future già note al motore in verde chiaro (vista pianificazione/Gantt).
39. **Eseguire il task successivo dalla To-Do List**: cliccare "Esegui", compilare i campi richiesti, quindi "Completato" per far avanzare il processo (oppure "Salva"/"Salva e chiudi" per salvare una bozza senza avanzare).
40. **Verificare in Storico** che ogni visualizzazione/modifica/esecuzione sia stata tracciata con utente e timestamp, e che il doppio clic su una voce mostri il diff dei valori prima/dopo.

#### Fase 9 — Variabili di gruppo: i preventivi fornitore


41. **Tornare nel magazzino delle variabili** e creare una nuova pagina "Preventivi".
42. **Creare la variabile "Codice Fornitore"** (Stringa), trascinarla sul form, poi cliccare sui "..." di configurazione e assegnarla a un nuovo **Gruppo**, "Lista Preventivi" — diventa così la prima colonna di una griglia di dettaglio virtuale.
43. **Aggiungere le colonne successive trascinandole direttamente sulla griglia**: "Ragione Sociale", "Numero Preventivo", "Importo Preventivo" (Numerico) — ogni variabile trascinata dentro la griglia si unisce automaticamente allo stesso gruppo.
44. **Creare una nuova attività "Ricezione preventivi"**, assegnata come Esecutore all'ufficio acquisti, posizionata dopo l'approvazione. Nelle sue "Variabili da richiedere" trascinare l'intestazione e le variabili del gruppo "Lista Preventivi".
45. **Riutilizzare il layout della pagina "Preventivi"** esportando la categoria corrente e importandola/sostituendola nella schermata "Variabili da richiedere" di "Ricezione preventivi", per non dover ritrascinare manualmente ogni colonna.
46. **Testare**: avviare una nuova istanza, arrivare al task "Ricezione preventivi" ed eseguirlo. A runtime il gruppo appare come una griglia editabile in cui aggiungere/rimuovere righe liberamente.
47. **Rendere obbligatori i campi per riga**: tornare nelle "Variabili da richiedere" di "Ricezione preventivi" e marcare Codice Fornitore, Ragione Sociale, Numero Preventivo e Importo Preventivo come obbligatori — vincolo che si applica a ogni riga inserita, non al numero minimo di righe.
48. **Aggiungere un campo Note per riga**: creare nel magazzino la variabile "Note Preventivo" (Memo) trascinandola direttamente nella griglia del gruppo "Lista Preventivi" (viene automaticamente assegnata al gruppo), poi trascinarla anche nelle "Variabili da richiedere" di "Ricezione preventivi".
49. (Facoltativo, per righe con molti campi) **Aggiungere un bottone "Dettagli..."** stateless dentro la griglia, configurato con una propria sotto-form "Variabili da richiedere", per aprire un pop-up a schermo intero sulla singola riga.

#### Fase 10 — Chiusura dell'esercizio


50. Facoltativamente, impostare una **Tabella di origine** sul campo "Codice Fornitore" (locale o esterna) in modo che, invece di testo libero, l'utente scelga il fornitore da un elenco, con auto-compilazione della Ragione Sociale collegata.
51. Ripubblicare il modello per rendere effettive tutte le modifiche e verificare, tramite "Aggiornamento processo", il comportamento di versionamento su un'istanza già in corso avviata con una versione precedente.

A questo punto il processo "Richiesta INV" copre l'intero flusso dimostrativo del corso base: diagramma con diramazioni condizionate, utenti e gruppi, variabili di testata e di gruppo, formule di processo, pubblicazione/versionamento ed esecuzione monitorata tramite To-Do List e Storico. Le estensioni successive — allegati obbligatori, sotto-processi ricorrenti per i preventivi, permessi granulari — si innestano su questa stessa base senza richiedere di ridisegnare il flusso principale.

## Corso avanzato

### BPM Avanzato

> **Origine del contenuto**
>
> Pagine ricavate dalla registrazione del corso di formazione. Le schermate possono differire dalla versione attuale del prodotto.

Il corso BPM Avanzato prosegue il percorso formativo iniziato con il corso BPM Base e approfondisce le funzionalità del Designer BPM (Digit Company) destinate a chi deve modellare processi complessi, integrare BPM con sistemi esterni e presidiare l'avanzamento operativo dei processi nel tempo. I macro-argomenti trattati sono: variabili avanzate (griglie dati, filtri su gruppi, formule VB-script e validazione), gateway e sincronizzazione dei rami paralleli, oggetti puramente grafici e swim lane, start multipli ed eventi (attesa, timeout/escalation), operazioni automatiche (mail, processo collegato, set variable, decision table, SQL, get data), tabelle locali personalizzate (tabelle P_), report e dashboard, integrazione con il gestionale esterno SAM (in entrambe le direzioni) e infine pianificazione/Gantt dei processi.

---

#### Come è organizzato

- [Concetti](#concetti-1): i temi del corso, uno per pagina.
- [Tutorial avanzati](#tutorial-avanzati): l'esercizio guidato, passo per passo.

### Concetti


- [Variabili avanzate: data grid e filtri su gruppo](#variabili-avanzate-data-grid-e-filtri-su-gruppo)
- [Gateway e sincronizzazione dei rami](#gateway-e-sincronizzazione-dei-rami)
- [Oggetti grafici, pagine multiple e swim lane](#oggetti-grafici-pagine-multiple-e-swim-lane)
- [Start multipli ed eventi](#start-multipli-ed-eventi)
- [Operazioni automatiche](#operazioni-automatiche)
- [Tabelle locali personalizzate (tabelle P_)](#tabelle-locali-personalizzate-tabelle-p_)
- [Report e dashboard (analisi dati)](#report-e-dashboard-analisi-dati)
- [Integrazione con SAM (ERP)](#integrazione-con-sam-erp)
- [Pianificazione e Gantt](#pianificazione-e-gantt)

#### Variabili avanzate: data grid e filtri su gruppo


###### Griglia dati (data grid)

La griglia dati è un tipo di variabile di processo a sé stante, distinto sia dal campo semplice sia dal gruppo (testata/dettaglio). È un oggetto singolo che visualizza una griglia **in sola lettura**, agganciata a una tabella — locale o esterna.

Si usa per mostrare all'utente dati di contesto senza uscire dal processo: tutti gli ordini di un certo cliente, le righe di un ordine in approvazione, una tabella di budget, ecc. Non è una struttura di inserimento dati (per quello ci sono i gruppi): è una finestra di consultazione dal vivo.

Configurazione:

1. Si crea una variabile e se ne imposta il tipo su Griglia Dati, come per qualunque altra variabile.
2. Si apre la sua configurazione (la stessa schermata usata per l'aggancio tabella dei campi) e si sceglie la tabella sorgente (tabella locale P_, vista, o tabella esposta da un connettore esterno).
3. Si scelgono le colonne da esporre e, opzionalmente, se ne rinominano le intestazioni (utile quando i nomi colonna della sorgente sono criptici o in lingua straniera).
4. Si posiziona nella form/magazzino/variabili da richiedere come qualunque altra variabile, dandole spazio a schermo sufficiente.
5. Dopo la pubblicazione, aprendo un'istanza di processo la griglia appare popolata, filtrabile e raggruppabile come le altre griglie del prodotto, ma non editabile.

L'aggancio di una griglia dati usa lo stesso meccanismo di mappatura dell'aggancio tabella sui campi ("aggancio del tipo di quelle che si fanno per puntare una tabella") — cambia solo la resa a video (griglia persistente anziché combo/popup di ricerca).

###### Filtro per attività su un gruppo

Un gruppo (testata/dettaglio, relazione 1-a-molti) può essere filtrato in modo **diverso per ogni attività/schermata** in cui compare, senza toccare i dati sottostanti.

Esempio reale citato dal docente: due attività parallele di revisione ("valutazione preventivi tipo A" / "tipo B") usano lo stesso gruppo "lista preventivi", ma ogni revisore deve vedere solo il proprio tipo. Un'altra applicazione concreta menzionata è un processo di controllo qualità che smistava i pezzi verso due reparti diversi in base al tipo di pezzo, con esattamente questo schema.

Configurazione, in "variabili da richiedere":

![configure a per task filter on a group variable](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/003_002706_configure-a-per-task-filter-on-a-group-variable.jpg){ loading=lazy }

- Si seleziona una qualunque variabile appartenente al gruppo; le impostazioni locali permettono di disabilitare l'aggiunta/cancellazione righe (navigazione in sola lettura) e di applicare una **condizione di filtro** (es. `tipo preventivo = "tipo A"`).
- Si ripete l'operazione sull'attività parallela con il filtro opposto.

###### Condizionare un percorso in base al contenuto di un gruppo

Si può usare una formula VB-script sulla **condizione di abilitazione** di un link per impedire al processo di percorrere un ramo quando un gruppo non contiene righe corrispondenti (es. non aprire il ramo "revisione tipo A" se non ci sono preventivi di tipo A).

Esempio guidato:

- Tasto destro dentro l'editor della condizione per navigare le variabili disponibili; selezionando un membro del gruppo vengono proposte espressioni helper preconfezionate (es. `Count(tipo preventivo) > 0`), ma un semplice conteggio sull'intero gruppo non è sufficiente quando serve contare solo le righe che soddisfano una condizione specifica.
- **Suggerimento — in BPM non esiste un debugger.** Non essendoci modo di eseguire passo-passo una formula, il docente consiglia di creare variabili helper "usa e getta" nel magazzino (es. `presenza tipo A`, `presenza tipo B`, di tipo stringa) solo per visualizzare cosa calcola una formula mentre la si scrive.

    ![helper variable workaround for debugging formulas](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/004_003043_helper-variable-workaround-for-debugging-formulas.jpg){ loading=lazy }

- La logica di conteggio va scritta come formula sulla stessa variabile helper (una "formula" sul campo, che si ricalcola automaticamente a ogni variazione dei dati):

```vb
Dim i As Integer
For i = 0 To lista_preventivi.Count - 1
 If tipo_preventivo(i) = "tipo A" Then
 Return "sì"
 End If
Next
Return "no"
```

![vb script loop over group rows worked example](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/005_003415_vb-script-loop-over-group-rows-worked-example.jpg){ loading=lazy }

- **Attenzione:** `Return` esce immediatamente dalla formula — a differenza di altri linguaggi (il docente cita Delphi come esempio), l'esecuzione non prosegue oltre un `Return`.
- La condizione di abilitazione del gateway a valle controlla poi semplicemente `presenza tipo A = "sì"`.

Pattern di accesso da ricordare: `variabile(i)` è il modo per indicare l'i-esimo valore di una variabile membro di un gruppo su tutte le righe — questo pattern ricorre costantemente nella logica basata su gruppi.

###### Formula di validazione: a livello di campo vs. globale

- **Formula di validazione a livello di campo:** è agganciata a un singolo campo; viene verificata non appena quel campo viene modificato (es. rifiutare un importo > 1000). Il tasto per attivarla in genere si chiama "formula di attivazione" o "formula di validazione".
- **Formula di validazione globale:** è una formula separata per l'intera schermata, valutata solo quando l'utente clicca "completato" sull'attività. Si usa per regole di business trasversali a più campi, ad esempio "deve esistere almeno un preventivo di qualunque tipo prima di poter proseguire":

```vb
If Count(tipo_preventivo) = 0 Then
 MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
 Return False
End If
Return True
```

![global validation formula vs field level validatio](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/006_003944_global-validation-formula-vs-field-level-validatio.jpg){ loading=lazy }

Nota: `Return True` in fondo è tecnicamente opzionale/implicito, ma scriverlo esplicitamente evita ambiguità.

#### Gateway e sincronizzazione dei rami


###### Sbarra di sincronizzazione (oggetto storico)

È l'oggetto storico di BPM per ricongiungere rami paralleli — visivamente un "cancello" che si apre solo quando tutti i rami entranti configurati sono arrivati.

![legacy sync bar object sbarra di sincronizzazione](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/007_004344_legacy-sync-bar-object-sbarra-di-sincronizzazione.jpg){ loading=lazy }

Modalità di configurazione:

- **TUTTE:** attende ogni ramo che è stato *configurato* come entrante, indipendentemente dal fatto che sia stato effettivamente avviato in quella istanza.
- **TUTTE PIANIFICATE** (tutte lanciate): attende solo i rami effettivamente avviati in quell'istanza — fondamentale quando il gateway di diramazione a monte è condizionale (es. un gateway inclusivo che potrebbe aprire solo uno dei due percorsi). Usare "TUTTE" in quel caso porterebbe il processo in stallo (deadlock).

    ![all vs all planned gotcha on sync bars](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/008_004534_all-vs-all-planned-gotcha-on-sync-bars.jpg){ loading=lazy }

- La sbarra di sincronizzazione può inoltre portare una **formula di attivazione personalizzata** al posto di TUTTE/TUTTE PIANIFICATE, per i casi che richiedono una logica arbitraria: esempio reale citato, progetto "Veneta Cucine".

###### Gateway in stile BPMN moderno

Lo stesso oggetto a forma di rombo assume tre significati diversi a seconda della configurazione:

![three modern gateway types exclusive parallel incl](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/009_004700_three-modern-gateway-types-exclusive-parallel-incl.jpg){ loading=lazy }

- **Percorsi alternativi (esclusivo):** viene percorso esattamente un ramo in uscita; gli esiti sono mutuamente esclusivi.
- **Percorsi paralleli (parallelo/AND):** tutti i rami in uscita vengono sempre percorsi, senza condizioni.
- **Percorsi liberi (inclusivo/OR):** uno, alcuni o tutti i rami in uscita possono essere percorsi, in base alla condizione di ciascuno.

Configurazione: doppio clic (oppure tasto destro → Configurazione) per impostare una condizione su ciascun ramo in uscita. È possibile usare direttamente variabili booleane come condizione, oltre a espressioni più articolate.

Vincolo: un oggetto gateway è **o** una diramazione (1 ingresso → n uscite) **o** un ricongiungimento (n ingressi → 1 uscita) — il designer blocca (disegna in rosso il collegamento) qualunque tentativo di dargli entrambe le funzioni contemporaneamente. La stessa forma diventa automaticamente un "ricongiungimento" quando vi si collegano più link entranti verso un'unica uscita; usato come ricongiungimento non richiede alcuna configurazione (attende semplicemente il completamento dei rami che sono stati effettivamente avviati).

Richiamo — percorso di default ("diamantino"): il rombo nero indica il percorso predefinito/di fallback preso quando nessuna condizione esplicita risulta vera, in modo che il processo non resti mai bloccato.

#### Oggetti grafici, pagine multiple e swim lane


###### Oggetti puramente grafici

- **Casella di testo:** testo libero personalizzabile (font, colore, bordo trasparente), es. un titolo del processo — puramente estetico.

    ![purely graphical objects text box image page setup](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/010_005239_purely-graphical-objects-text-box-image-page-setup.jpg){ loading=lazy }

- **Immagine:** es. il logo aziendale.
- **Pagina e margini:** Configurazione → Strumenti → pagina permette di impostare formato carta (A0–A4) e margini; la maggior parte dei processi viene disegnata su una pagina sovradimensionata ignorando i margini, ma se si vuole un diagramma di processo **stampabile** (es. come documentazione, esportabile in PDF con "stampa su PDF"), lo si impagina per rientrare in pagine reali.
- **Memo/post-it:** una nota libera agganciata vicino a un'attività per annotazioni in fase di progettazione; nessun effetto a runtime.

###### Processi multi-pagina e oggetto Marker

Per processi molto lunghi/complessi, il canvas può essere suddiviso in più pagine (Nuova Pagina). L'oggetto **Marker** funge da "goto"/teletrasporto tra pagine: si posiziona un marker numerato nel punto in cui il flusso lascia la pagina 1 e un marker corrispondente nel punto in cui rientra sulla pagina 2. Non c'è limite al numero di marker/pagine. Utile soprattutto quando il diagramma deve restare leggibile/stampabile come documentazione.

###### Swim lane

Corsie adiacenti e ordinate (come i "pool/lane" BPMN) usate per organizzare visivamente un processo per ruolo/reparto. Trascinando l'oggetto swim lane si crea un insieme di corsie contigue, rinominabili (es. "Inseritore," "Sicurezza," "Controllo di Gestione," "Dirtec").

Comportamento funzionale, non solo cosmetico: impostare gli **"utenti responsabili"** a livello di corsia (tasto destro) assegna automaticamente quell'utente/gruppo a qualunque attività posizionata nella corsia che non abbia già un'assegnazione esplicita propria; un'assegnazione esplicita a livello di attività prevale sempre su quella di corsia.

Configurazione:

- Colore dell'intestazione della corsia, ordine (sposta corsie su/giù).
- Orientamento: verticale (dall'alto in basso, la convenzione preferita dal docente) oppure orizzontale (la convenzione BPMN standard, usata quando i diagrammi devono avere un aspetto "da manuale").

Esempio di progetto reale: un processo multi-reparto (commerciale → tecnico → acquisti → qualità → produzione) impaginato con swim lane — molto leggibile su "chi fa cosa" a colpo d'occhio, ma il docente segnala che questo stile di diagramma è visivamente più disordinato ("a zig-zag") da disegnare e mantenere rispetto a un flusso lineare dall'alto in basso.

![real project zig zag swim lane process](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/014_010728_real-project-zig-zag-swim-lane-process.jpg){ loading=lazy }

###### Oggetto Gruppo (attività)

Un'alternativa alle swim lane per raggruppare/etichettare: supporta anch'esso l'assegnazione di "utenti responsabili" a tutto ciò che contiene, oppure può essere usato puramente come etichetta visiva/riquadro attorno a una sezione del diagramma (es. "ufficio tecnico").

###### Undo vs. storico versioni

- L'**Undo** (~10 passi) è transitorio: copre solo la sessione di editing corrente, dall'apertura alla chiusura del designer.
- Lo storico di **pubblicazione/versioni** è permanente, salvato a database: ogni volta che si "Pubblica," BPM crea una nuova riga di versione numerata. Si può tornare a qualunque versione pubblicata precedente.
- Suggerimento: in fase di pubblicazione, BPM propone un campo libero **"Versione" / note di pubblicazione** dove annotare cosa è cambiato (es. "R01 dev — modificata attività 2"); utile come changelog informale, anche se il contatore di versione sottostante si incrementa comunque.
- Esiste anche uno strumento di pulizia dello storico (per installazioni grandi/datate) per eliminare vecchie versioni, con un controllo di sicurezza che impedisce di cancellare una versione su cui sono ancora attive istanze in esecuzione.

#### Start multipli ed eventi


###### Start multipli

Un processo può avere due o più oggetti Start distinti, ciascuno configurato in modo indipendente (proprie variabili richieste, valori di default, regole di validazione, permessi).

Esempio: "Inserimento richiesta normale" vs. "Inserimento richiesta sicurezza" — lo start sicurezza precompila/snellisce i campi in modo diverso (es. salta un passaggio di revisione, aggiunge un campo note dedicato).

![building two start events normal vs security](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/016_011600_building-two-start-events-normal-vs-security.jpg){ loading=lazy }

All'avvio di un processo con start multipli:

- Comportamento di default: all'utente viene chiesto quale punto di partenza usare.
- **Restrizione per permesso:** si impostano gli "utenti responsabili" su ciascuno Start individualmente, così che solo il gruppo giusto possa usare quel punto di ingresso.
- **Associazione tramite menu personalizzato:** una voce di menu personalizzato ("menu personalizzati") può essere precablata su uno start specifico, dando a ogni punto di ingresso la propria voce di menu dedicata invece di una richiesta generica.
- **Via API/web service:** la chiamata `create-new-process` richiede un parametro esplicito di punto di partenza; ometterlo quando esistono start multipli restituisce un errore invece di sceglierne uno silenziosamente.

###### Start a tempo (avvio schedulato)

Avvia un processo automaticamente secondo una pianificazione, invece che tramite un'azione utente (es. "ogni primo lunedì del mese alle 08:00"). Adatto a processi periodici/amministrativi (chiusure di fine periodo, controlli ricorrenti). Poiché non porta con sé variabili, la prima attività reale del processo deve comunque raccogliere i dati di lavoro effettivi.

###### Evento Attesa (Wait)

Sospende il processo per una durata configurata (es. "attendi 5 giorni", oppure il pattern "il primo lunedì") e poi prosegue automaticamente — durante l'attesa **non esiste alcuna voce in to-do list** (a differenza della semplice pianificazione di un'attività fra 10 giorni, che invece resterebbe comunque nella to-do list di qualcuno per tutto il tempo).

![attesa wait event](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/018_012344_attesa-wait-event.jpg){ loading=lazy }

Esempio reale: il processo interno di "welcome kit" (inserimento di un nuovo dipendente) usa l'evento attesa in più punti per scaglionare i passaggi di un certo numero di giorni.

###### Fine vs. Termina Processo

- **Fine:** un semplice marcatore grafico di chiusura di un ramo — segnala visivamente "questo ramo del diagramma finisce qui", nessun effetto a runtime oltre a questo.
- **Termina Processo:** **uccide** effettivamente l'intera istanza di processo — qualunque attività parallela ancora aperta altrove nel processo viene chiusa forzatamente. Tipicamente usato su rami di eccezione/errore quando si decide che l'intera istanza vada interrotta.

    ![fine vs termina processo distinction](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/019_012600_fine-vs-termina-processo-distinction.jpg){ loading=lazy }

###### Eventi boundary: timeout ed escalation

Un evento agganciato al **bordo di un'attività** (non alla linea di flusso principale) — attiva un percorso alternativo dopo N giorni dalla data di attivazione dell'attività o da una scadenza, es. per attivare un promemoria o un passaggio di mano a un altro utente. Funzionalmente "timeout" ed "escalation" sono lo **stesso** meccanismo; le due icone differiscono solo per convenzione semantica (timeout = "questa attività sta impiegando troppo tempo, sollecita"; escalation = "passa di mano/alza il livello"). Corrisponde al concetto BPMN di "evento di confine" ("boundary event") — l'evento esiste perché l'attività è attiva, non perché il flusso principale l'ha raggiunto.

![timeout escalation boundary event](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/020_012810_timeout-escalation-boundary-event.jpg){ loading=lazy }

#### Operazioni automatiche


Concetto chiave: a differenza delle attività utente (rettangoli, che richiedono un intervento umano) e degli eventi (punti che semplicemente accadono), le **operazioni** sono cose che il motore BPM fa da sé, automaticamente. Possono essere trascinate direttamente nel flusso di processo come qualunque altro oggetto, oppure agganciate a un momento specifico del ciclo di vita di un'attività, oppure agganciate a livello dell'intero processo.

![operations automatic system activities](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/021_013034_operations-automatic-system-activities.jpg){ loading=lazy }

###### Operazione Invio Mail

- Si trascina l'operazione mail nel flusso, poi la si configura selezionando (o creando) un **template di mail**.
- I template di mail sono oggetti che vivono dentro il processo (da Configurazione, oppure direttamente dall'operazione) e sono riutilizzabili su più punti di invio.

    ![building an email notification template](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/022_013406_building-an-email-notification-template.jpg){ loading=lazy }

- Costruzione del template: oggetto e corpo supportano l'inserimento di variabili di processo tramite tasto destro (il menu "generic" espone anche placeholder speciali — vedi sotto).
- **Destinatari:** possono essere un utente BPM fisso, un gruppo fisso, una variabile che contiene un indirizzo email grezzo (es. il campo email di un fornitore), oppure una variabile che contiene un riferimento a utente/gruppo BPM. I destinatari possono anche essere messi in copia conoscenza ("in propria conoscenza").
- **Allegati:** si possono allegare documenti di processo e/o report generati.
- **Placeholder generici utili nei template:**
 - `mia mail` (my own email) — l'email di chi è attualmente assegnatario dell'*attività* (permette di riusare lo stesso template su tante attività/assegnatari diversi).
 - `mia attività` (my activity) — il nome visualizzato dell'attività corrente.
 - **`link web al task`** — inserisce un URL cliccabile che porta direttamente alla schermata di esecuzione di quella specifica attività nel client web (bypassando del tutto la to-do list). Funziona anche per collegarsi all'intero processo o alla sua pagina allegati.

     ![link web al task generic field](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/024_014614_link-web-al-task-generic-field.jpg){ loading=lazy }

- **Insidia comune:** il link diretto funziona solo se **Configurazione → parametri → "URL base link email"** è impostato sul vero hostname visibile esternamente del server; se lasciato a `localhost` (il default facile da dimenticare), ogni link nelle mail si rompe silenziosamente — particolarmente importante quando il server è esposto su un IP pubblico.
- In genere si consiglia di abilitare sempre il modulo web (non serve licenza aggiuntiva, solo un'attività di setup IIS per i sistemisti), perché è necessario affinché questi link diretti funzionino fuori dal client desktop.

###### Operazioni agganciate al ciclo di vita di un'attività

Tasto destro su un'attività → **Operazioni** permette di agganciare qualunque operazione (stesso catalogo delle operazioni di flusso) a uno di quattro momenti:

- **Attivazione:** l'attività è appena diventata disponibile (compare nella to-do list di qualcuno — buon momento per una notifica "hai qualcosa da fare").
- **Inizio:** l'utente ha dichiarato esplicitamente di aver *iniziato* l'attività (scatta solo se "rileva inizio" è abilitato su quell'attività — vedi la sezione sulla pianificazione).
- **Esecuzione:** scatta appena prima che l'attività venga segnata come effettivamente completata (cioè "sta per completarsi").
- **Esecuzione terminata:** scatta subito dopo il completamento, appena prima che l'attività successiva si attivi.

Attivazione vs. Inizio, con precisione: attivazione = l'attività è *pronta*; inizio = l'attività è stata effettivamente *iniziata*. Sono deliberatamente due concetti separati, usati insieme al sistema di pianificazione.

Suggerimento pratico: posizionare operazioni puramente tecniche/di servizio (es. azzerare una variabile obsoleta) direttamente sull'attività, invece che come oggetto visibile nel flusso, mantiene il diagramma di processo focalizzato sulla logica di business invece di affollarlo di passaggi tecnici di "idraulica" interna.

###### Set Variable / operazione formula inline ("un pezzo di scritto")

Un'operazione leggera che esegue un breve script per impostare una o più variabili — distinta da una formula di validazione (che restituisce solo vero/falso).

![set variable formula operation inserire un pezzo d](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/029_021020_set-variable-formula-operation-inserire-un-pezzo-d.jpg){ loading=lazy }

Esempio guidato — azzerare un esito obsoleto in caso di rilavorazione: se un campo "esito approvazione" è impostato a "non approvato" e l'attività viene rimandata indietro al richiedente per revisione e poi torna all'approvatore, il campo mantiene silenziosamente il vecchio valore "non approvato" (fonte comune di confusione: molti si aspettano che torni vuoto). Un'operazione Set Variable agganciata a **Esecuzione Terminata** dell'attività azzera di nuovo il campo, costringendo l'utente a ridecidere consapevolmente, ed evita che il ciclo si ripeta all'infinito perché il controllo "campo obbligatorio" era già banalmente soddisfatto dal valore obsoleto:

![clearing a stale variable on a rework loop](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/030_021119_clearing-a-stale-variable-on-a-rework-loop.jpg){ loading=lazy }

```vb
' agganciata sull'attività "controllo di gestione", su esecuzione terminata
esito_approvazione = Blank
```

Esempio guidato — assegnazione automatica dell'approvatore in base all'importo:

![auto assign an approver by amount threshold](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/031_021517_auto-assign-an-approver-by-amount-threshold.jpg){ loading=lazy }

```vb
If importo_richiesta < 1000 Then
 utente_approvazione_tecnica = "Dir Tech" ' può essere anche un gruppo
Else
 utente_approvazione_tecnica = "Dir Gen"
End If
```

Gli "utenti responsabili" dell'attività vengono poi associati alla variabile `utente_approvazione_tecnica` (variabile di tipo Utente) invece che a un gruppo fisso — una terza modalità di assegnazione, oltre a "assegna a gruppo" e "scegli manualmente una persona": l'**assegnazione guidata da regola**.

###### Decision table

Un'alternativa più recente e dichiarativa alla scrittura manuale di una formula. Si definiscono colonne di input e colonne di output e un insieme di righe-regola; BPM genera il codice VB sottostante in automatico. Disponibile ovunque sia utilizzabile una formula/formula di validazione.

![decision table object introduced](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/032_021905_decision-table-object-introduced.jpg){ loading=lazy }

Esempio guidato — stessa logica di assegnazione approvatore per importo, come tabella:

![decision table demo amount approver](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/033_022039_decision-table-demo-amount-approver.jpg){ loading=lazy }

| Importo Richiesta | → | Utente Approvazione |
|---|---|---|
| < 1000 | | Dir Tech |
| ≥ 1000 | | Dir Gen |

Estesa con una seconda colonna di input (Tipo Richiesta) per regole più complesse:

| Importo Richiesta | Tipo Richiesta | → | Utente Approvazione |
|---|---|---|---|
| < 1000 | Normale | | Dir Tech |
| ≥ 1000 | Normale | | Dir Gen |
| (qualunque) | Sicurezza | | Sicurezza |

- L'ordine delle righe conta e può essere modificato con le frecce su/giù (vince la prima riga che soddisfa le condizioni).
- Lo strumento è consapevole del tipo di variabile: per un campo a lista di valori propone i valori noti; per un campo di tipo Utente propone l'elenco di utenti/gruppi; in un contesto di formula di validazione sa già che l'output deve essere vero/falso.
- **Limite:** la decision table esprime solo condizioni semplici di confronto tra campi — non può esprimere logica procedurale come "scorri un gruppo e conta le righe corrispondenti" (vedi l'esempio della condizione di abilitazione sopra). Per quello serve ancora una formula.
- **Conversione bidirezionale:** un campo formula può essere convertito in decision table (come punto di partenza, se ci si blocca davanti a una formula vuota) e una tabella può essere riconvertita in formula quando la sua logica supera ciò che la tabella può esprimere. Il docente paragona questo utilizzo a partire da codice generato con ChatGPT: mai una risposta finita e affidabile, ma un utile sblocco iniziale.

    ![convert between decision table and formula code](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/034_022747_convert-between-decision-table-and-formula-code.jpg){ loading=lazy }

###### Operazione SQL ("SQL libero")

Un'operazione che esegue un'istruzione SQL arbitraria su una stringa di connessione esterna — non limitata al CRUD di una singola tabella, può eseguire stored procedure, join, qualunque cosa consenta l'SQL.

![sql operation object introduced](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/035_022908_sql-operation-object-introduced.jpg){ loading=lazy }

Esempio guidato:

![sql update query demo with in out parameters](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/036_023018_sql-update-query-demo-with-in-out-parameters.jpg){ loading=lazy }

```sql
UPDATE fornitori SET valore = 1 WHERE ID_numeric = @n
```

con `@n` legato come parametro di input a una variabile di processo; separatamente, una `SELECT` con un parametro di output (`@p`) scrive un valore restituito in una variabile di processo (es. `importo_richiesta`).

Caso d'uso: scrivere in un ERP esterno che un documento è stato firmato/approvato da un certo utente in un certo passaggio (es. "UPDATE ordine SET firmato_da =... WHERE ordine_id =..."), usato come alternativa più leggera al connettore dedicato quando non esiste un'interfaccia di connettore preconfezionata per quella scrittura.

Configurazione: la stringa di connessione si imposta una volta sola sotto **Configurazione → Connessione Esterna** (supporta target SQL Server/tipo ODBC), e viene riusata sia dall'operazione SQL sia da qualunque aggancio tabella sui campi.

###### Aggiorna un altro processo

Permette di scrivere aggiornamenti di variabili su un'istanza di un *altro* processo in esecuzione, in qualunque punto del flusso — non solo al lancio (processo collegato) o al ritorno. Non richiede nemmeno che i due processi siano stati formalmente collegati. Si fornisce una regola di ricerca per trovare l'istanza target: per codice istanza interno BPM, oppure facendo corrispondere il valore di una variabile (es. "trova il processo il cui `numero_richiesta` = il mio"). Si mappano poi variabile sorgente → variabile destinazione, si impostano valori fissi, oppure si usa una formula di passaggio, come nella mappatura del processo collegato. **Attenzione:** se ci si accorge di dover ricorrere a questa operazione troppo spesso, è di solito il segnale di una duplicazione eccessiva di dati fra processi che andrebbe ripensata architetturalmente.

###### Operazioni a livello di processo

Le operazioni possono essere agganciate non solo a una singola attività ma all'**intero processo** — vengono quindi eseguite automaticamente ogni volta che *qualunque* passaggio avanza, senza doverle cablare su ogni singola attività. Uso comune: aggiornare sempre lo stato su un CRM/ERP esterno, oppure sincronizzare sempre i nuovi allegati verso un repository documentale esterno ("documentale Globe"), a ogni avanzamento, senza chiedere conferma all'utente.

###### Operazione Get Data

Un'alternativa strutturata e guidata a una query SQL grezza, per ricerche in sola lettura: si sceglie una tabella/vista sorgente, si fornisce il valore chiave, e si mappano le colonne restituite direttamente su variabili di processo — lo stesso identico meccanismo/interfaccia usato per l'aggancio tabella su un campo, ma invocato come operazione autonoma.

![get data operation introduced](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/039_024119_get-data-operation-introduced.jpg){ loading=lazy }

Esempio guidato: dato un codice fornitore, si consulta la tabella fornitori e si precompila automaticamente la ragione sociale in una variabile `ragione_sociale` — comunemente usato proprio all'**inizio** di un processo, quando l'utente inserisce solo un codice e il resto dei campi anagrafici deve autopopolarsi.

Get Data vs. query SQL grezza: Get Data è più guidato (conosce i tipi di colonne/tabelle, meno soggetto a errori) ma limitato a una semplice ricerca puntuale per chiave; qualunque cosa richieda join, GROUP BY, più righe restituite o logica arbitraria richiede l'operazione SQL.

#### Tabelle locali personalizzate (tabelle P_)

##### Tabelle locali personalizzate (tabelle P_)

Oltre alle viste e liste di valori predefinite, BPM permette di definire tabelle di lookup completamente personalizzate direttamente nel designer. Salvandone una si genera automaticamente una vera tabella SQL con prefisso `P_` (es. `P_area_geografiche`).

![custom local tables tabelle p introduced](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/040_024602_custom-local-tables-tabelle-p-introduced.jpg){ loading=lazy }

Quando usarle:

- Una lista di valori non basta (servono più colonne, non solo codice+descrizione).
- I dati devono essere mantenuti da qualcuno diverso dal progettista del processo, o indipendentemente dal ciclo di pubblicazione di uno specifico processo.
- Serve filtro/ricerca su un elenco troppo lungo per una comoda dropdown.

Caso d'uso reale: usate frequentemente per tabelle di riferimento del reparto qualità (definizioni/standard non presenti nell'ERP principale).

Configurazione:

1. Configurazione → Tabelle → Nuova Tabella; le si dà un nome (gli spazi si convertono automaticamente in underscore per mantenere pulito l'identificatore SQL generato).

    ![demo creating a custom table aree geografiche](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/041_024744_demo-creating-a-custom-table-aree-geografiche.jpg){ loading=lazy }

2. Si progettano le colonne con un editor molto simile a quello delle variabili di processo — ma con limiti reali: **niente gruppi/testata-dettaglio**, **niente formula di validazione**, meno funzionalità avanzate rispetto a una vera variabile di processo.
3. Salvando si crea la tabella SQL. Si popolano le righe direttamente da BPM (Tabelle → la tua tabella → Nuovo).
4. Si usa ovunque sia previsto un aggancio a "tabella locale" (aggancio campo, sorgente di una griglia dati, sorgente Get Data) — comparirà con il prefisso `P_`.
5. Se una tabella `P_...` esiste in SQL ma non è stata creata tramite il designer tabelle di BPM, BPM la elencherà comunque come sorgente di lookup, ma non se ne possono gestire i dati riga da BPM (nessun menu di inserimento valori) — utile se è popolata da un import esterno.

Permessi: le tabelle personalizzate sono soggette a permessi per utente/gruppo (visualizza/modifica), lo stesso meccanismo dei permessi di processo, configurato sotto Utenti e Gruppi.

Menu personalizzati: una tabella personalizzata può essere esposta come propria voce di menu (Configurazione → menu personalizzati → "visualizza tabella"), così l'utente finale può consultarla/mantenerla direttamente senza passare da un processo.

Guida alla scelta — lista di valori vs. tabella personalizzata:

- Usare una **lista di valori** *dentro il processo* quando logica/condizioni altrove nel processo dipendono dai suoi valori esatti — modificare la lista in seguito potrebbe altrimenti rompere silenziosamente quelle condizioni.
- Usare una **tabella personalizzata** quando le opzioni sono numerose, devono essere filtrabili/ricercabili, o chi le mantiene non deve avere il permesso di modificare il processo.

#### Report e dashboard (analisi dati)


Due modalità complementari per estrarre/presentare i dati raccolti in un processo BPM, entrambe basate sulle **variabili di processo** come sorgente dati (nessuna estrazione dati separata necessaria).

![reports dashboards two ways to extract data](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/043_025737_reports-dashboards-two-ways-to-extract-data.jpg){ loading=lazy }

###### Report (documenti pixel-perfect)

Un designer di report di terze parti integrato (stessa famiglia di prodotto di Crystal Reports / dei generatori PDF usati in RGT e "Globe" di SAM) che permette di impaginare un documento in stile PDF e trascinare variabili di processo in segnaposto etichettati.

![report designer embedded 3rd party tool](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/045_030227_report-designer-embedded-3rd-party-tool.jpg){ loading=lazy }

Caso di studio reale — "scheda commessa": prima di BPM, i commerciali di un'azienda compilavano a mano un modulo PDF/Word vuoto per ogni nuovo ordine/commessa, poi lo inviavano via mail in giro e inseguivano manualmente i colleghi ("hai inserito il numero di serie? hai fatto l'ordine?"). Il processo BPM ora replica e migliora questo flusso: la prima attività cattura ~70-80 campi direttamente in BPM (molti commerciali, anche via client web/mobile in trasferta), con molti campi trasformati da testo libero a **selezioni guidate da tabella** (vedi tabelle P_) — pur mantenendo testo libero dove serviva la flessibilità richiesta dal cliente.

![real case study scheda commessa work order form](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/044_025834_real-case-study-scheda-commessa-work-order-form.jpg){ loading=lazy }

Costruzione di un report:

- I campi presentati nel designer sono raggruppati per pagina/nome variabile, rispecchiando l'organizzazione delle variabili nel processo stesso.
- Trascinando una variabile sul canvas si crea un segnaposto agganciato; si aggiungono etichette statiche intorno.
- **Sezioni condizionali:** intere sezioni possono essere mostrate/nascoste in base a una condizione (es. mostrare una sotto-sezione "Gas1/Gas2" solo se quelle caselle sono selezionate) — utile per moduli con molti sotto-blocchi opzionali.
- **Report testata/dettaglio (gruppo):** con un po' di attenzione, un report può rendere una variabile di gruppo (es. elenco preventivi) come blocco "dettaglio" ripetuto, producendo più righe per pagina stampata.
- I report sono salvati nel database BPM (non nel filesystem) come parte del processo; un comando "Stampa" sull'istanza di processo in esecuzione rende i valori correnti nel template.
- Il docente precisa che questo non vuole competere con un vero strumento di reporting/BI — è una comodità integrata, dato che i dati sono già modellati dentro il processo.

###### Dashboard (cruscotti)

Un altro componente analitico di terze parti integrato (basato su DevExpress) per costruire dashboard visive interattive sui dati di processo — distinto dai report PDF pixel-perfect visti sopra.

![dashboard tool introduced](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/073_044836_dashboard-tool-introduced.jpg){ loading=lazy }

Costruzione passo-passo, punto per punto:

1. Si crea una nuova dashboard, si aggiunge una **sorgente dati** agganciata a un processo scelto (es. un processo "reclamo"), la si nomina (es. "elenco reclami") e si importano le variabili che si vogliono avere disponibili come campi.

    ![demo create a dashboard and add a data source](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/074_045008_demo-create-a-dashboard-and-add-a-data-source.jpg){ loading=lazy }

2. Si trascinano widget sul canvas — es. una **Griglia** e un **Grafico a torta**; ogni widget, una volta selezionato, mostra delle zone di aggancio (colonne per la griglia; valori/argomenti per il grafico) da popolare trascinandovi i campi.
3. **Formattazione numerica:** opzioni integrate per abbreviazione unità K/M, separatore delle migliaia, cifre decimali.
4. **Grafico a torta:** si trascina un campo univoco (es. `ID`) su "valore" per ottenere un'aggregazione Count di default, e un campo categorico (es. "marca") su "argomenti" per suddividere per categoria.
5. **Elementi filtro:** un widget "casella combinata" agganciato a un campo (es. una data, raggruppata per giorno/mese/anno) funge da filtro incrociato per tutti gli altri widget della dashboard quando l'utente sceglie un valore.

    ![demo combo box filter element](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/075_045518_demo-combo-box-filter-element.jpg){ loading=lazy }

6. **Campi calcolati:** es. un campo "tempo di risposta" calcolato come `data_risposta − data_apertura`, poi usato con un'aggregazione **Media** per mostrare il tempo di risposta medio.

Prerequisito per KPI significativi — catturare esplicitamente le date chiave: i timestamp grezzi di esecuzione delle attività non sono sempre la metrica che serve (es. "giorni per rispondere a un reclamo" andrebbe misurato da "preso in carico" a "risposto", non da creazione a chiusura del ticket). Il pattern usato: agganciare operazioni **Set Variable** (vedi sopra) a specifiche transizioni di attività che scrivono `Oggi` in variabili data dedicate (`data_presa_in_carico`, `data_risposta`) automaticamente, senza alcun input utente — queste alimentano poi i campi calcolati della dashboard.

![set variable operations capture today at key trans](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/078_045913_set-variable-operations-capture-today-at-key-trans.jpg){ loading=lazy }

Disponibilità: una volta salvata, una dashboard è disponibile agli utenti finali (senza la barra degli strumenti di progettazione) sotto il menu **"Analisi Dati"** (compare solo quando esiste almeno una dashboard/tabella, come per il menu delle tabelle personalizzate) — e la stessa identica dashboard è automaticamente disponibile anche nel **client web**, senza bisogno di ricostruirla.

Posizionamento: esplicitamente *non* un sostituto della BI (nessun cubo, tutto calcolato al volo) — il suo valore è la comodità, dato che i dati sono già connessi dentro BPM.

#### Integrazione con SAM (ERP)


L'integrazione è articolata attorno a **quattro aspetti distinti**, trattati in sequenza:

1. BPM → SAM: scrittura di documenti/anagrafiche (connettore attivo).
2. BPM → SAM: lettura di tabelle (viste-tabella del connettore / SQL grezzo).
3. SAM → BPM: avvio di un processo da un evento lato SAM (web service/stored procedure/trigger).
4. SAM ↔ BPM: la to-do list di SAM che mostra le attività BPM.

###### Architettura del connettore (generale)

Un "connettore" (es. "SAM v5", o il connettore separato "Globe") è modellato come un **plugin** installabile:

- **Definizione** (metadati che vivono nella configurazione BPM): quali aziende esistono, quali interfacce espone il connettore, e i parametri di connessione generali (URL del web service, dettagli di connessione al DB per ciascuna azienda — i connettori SAM usano un approccio *misto*: alcune operazioni via web service, altre via lettura diretta del DB).
- **DLL/plugin esterno**, che deve essere effettivamente installato sull'ambiente (normalmente incluso nell'installazione standard; altrimenti va richiesto come attività di setup) e che fa il lavoro reale dietro la definizione.
- Il connettore espone due tipi di interfaccia:
 - **Interfacce azione** — usate come *operazioni* trascinate nel flusso di processo; *scrivono* su SAM.
 - **Interfacce tabella** — usate come sorgenti di lookup in sola lettura su campi/griglie dati; espongono i dati SAM come se fossero una tabella/vista locale.
- Configurazione azienda/ambiente: Configurazione → connettori → spuntare **Attivo**, aggiungere un'azienda ("nuova azienda") e compilare i parametri per azienda (server DB, credenziali, DB marketing se rilevante, e l'endpoint web service di quell'azienda).

###### Connettore attivo — BPM scrive su SAM

Un tipo di operazione, associata a uno specifico connettore, che scrive un documento o un'anagrafica in SAM (creare un cliente, creare una "commessa", registrare un "intervento", ecc.), inserita nel flusso come qualunque altra operazione. Per **SAM 5**, questa funzionalità è costruita sopra la funzione XML **Web Import** di SAM; per SAM 6 è previsto un supporto più ricco tramite web service JSON.

![connettore attivo active connector operation](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/047_031052_connettore-attivo-active-connector-operation.jpg){ loading=lazy }

Configurazione guidata (es. "creazione commessa"):

![xml template variable mapping demo](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/048_031324_xml-template-variable-mapping-demo.jpg){ loading=lazy }

1. Si trascina l'operazione connettore-attivo nel processo, si fa doppio clic, e si sceglie un'interfaccia XML preconfezionata (es. "xml commessa").
2. L'interfaccia arriva con un template preconfigurato e un insieme finito e fisso di **parametri di input** ("testata", raccomandati dalla documentazione tecnica di SAM stessa) — ciascuno si mappa su una variabile di processo, o si lascia come valore fisso letterale. Un campo obbligatorio mancante causa semplicemente il rifiuto della chiamata da parte del web import di SAM con un errore (BPM stesso non sa cosa l'XML "dovrebbe" contenere — è solo un pass-through).
3. Campi di testata aggiuntivi non presenti nell'elenco di default possono essere aggiunti tramite un piccolo helper (che conosce le colonne della tabella target) e mappati allo stesso modo.
4. **Parametri di output:** se l'interfaccia restituisce dei valori (non tutte lo fanno), possono essere mappati indietro su variabili di processo, es. catturando l'ID interno del nuovo documento / il numero documento in `numero_commessa`.
5. **Parametri di riga/dettaglio:** se il processo ha un gruppo corrispondente (es. "lista codici"), ogni riga del gruppo viene mappata automaticamente su un nodo di dettaglio XML ripetuto — permettendo di inviare in una sola chiamata un intero elenco di righe ordine/distinta (es. mappando `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`). Tutto ciò che non è esplicitamente presente in BPM (es. logica dei prezzi) è lasciato interamente alla configurazione di SAM.

    ![detail row parameters mapping a group to xml rows](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/049_031849_detail-row-parameters-mapping-a-group-to-xml-rows.jpg){ loading=lazy }

Estensibilità: le interfacce preconfezionate coprono un insieme deliberatamente finito di casi comuni (cliente, commessa, intervento, ecc.) — un nuovo template XML genuinamente diverso richiede una richiesta di sviluppo, non è qualcosa che un consulente/cliente possa cablare liberamente dall'interfaccia.

Requisito di attivazione: il **modulo Web Import** di SAM deve essere installato e raggiungibile — tipicamente un ticket sistemistico di routine, nessuna licenza aggiuntiva richiesta.

Alternativa/quando non usarlo: se non esiste un'interfaccia di connettore preconfezionata per ciò che serve, una semplice attività manuale che ricorda a un utente di inserire il record in SAM è un'alternativa legittima — automatizzarla solo per il gusto di farlo può essere in realtà peggio, se significa duplicare logica anagrafica (es. tutte le regole di onboarding cliente) che già vive correttamente dentro SAM. È più appropriato quando serve solo un record segnaposto leggero (es. uno stub cliente con un codice, per poter agganciare documenti contro di esso).

###### Lettura dei dati SAM in BPM (connettori tabella)

Due opzioni per un campo/griglia dati agganciato a una tabella per leggere dati SAM:

- **Vista locale/accesso diretto a tabella esterna** — si costruisce una propria vista SQL con esattamente le colonne desiderate (un certo sforzo iniziale una tantum, ma piena flessibilità).
- **Connettore Dati (interfaccia tabella del connettore)** — si sceglie da un catalogo finito di viste preconfezionate incluse nel connettore; se manca una colonna necessaria, occorre richiederne l'aggiunta a monte, oppure **copiare la vista generata e personalizzare la copia** (modificare l'originale non è sicuro — vedi sotto).

Come vengono generate le viste preconfezionate: eseguire l'"aggiornamento database" del connettore genera automaticamente un insieme di viste SQL con prefisso `vvbpm...` dentro il database SAM (una per ogni interfaccia tabella esposta, es. la vista clienti).

Insidia critica: queste viste auto-generate vengono **rigenerate/sovrascritte** ogni volta che la definizione del connettore viene aggiornata — qualunque modifica manuale alla vista originale va persa. Il pattern sicuro è duplicare la vista sotto un proprio nome e puntare la propria personalizzazione alla copia.

###### La to-do list di SAM mostra le attività BPM

Un modulo di SAM permette alle voci della to-do list BPM ("eventi BPM") di comparire integrate nella to-do list nativa di SAM, per gli utenti che lavorano su entrambi i sistemi e non vogliono cambiare applicazione.

- Doppio clic su un evento BPM dentro SAM mostra un popup di dettaglio dal vivo (nome processo/modello, attività corrente) recuperato **in tempo reale tramite un web service BPM** — nulla riguardo alle attività BPM è cache/salvato nel database di SAM, viene letto fresco ogni volta che si apre la schermata.
- Include lo stesso meccanismo di deep-link usato nelle mail per saltare direttamente a quell'attività nel client web BPM.
- **Sincronizzazione bidirezionale dal vivo:** avanzare un'attività in BPM (es. passare da "firma1" a "firma2") si riflette immediatamente come la stessa attività che compare nella to-do list di SAM — sono la stessa attività sottostante, non due copie mantenute separatamente.

    ![bidirectional sync firma1 firma2 mirrored in both ](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/053_034238_bidirectional-sync-firma1-firma2-mirrored-in-both-.jpg){ loading=lazy }

- Lo stesso meccanismo/modulo è disponibile anche dentro la to-do list di **CRM1**.

Configurazione (lato SAM): Opzioni → cerca "BPM" → impostare il **percorso server BPM** (di nuovo: deve essere il vero hostname raggiungibile esternamente, non localhost) e una **chiave API generata da BPM**.

Generazione della chiave API (lato BPM): Configurazione → **Chiave Web API** — creare una nuova chiave (opzionalmente con data di scadenza); è la credenziale che ogni chiamante esterno (SAM, Postman, codice custom) deve presentare.

Mapping utenti: Configurazione → Utenti e Gruppi → ogni utente ha una sezione **"Alias"** che mappa la sua identità per ciascun connettore esterno (es. `css-admin` di SAM ↔ `admin` di BPM) — ogni connettore può avere il proprio mapping utenti indipendente.

![user alias mapping between bpm and sam](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/054_034451_user-alias-mapping-between-bpm-and-sam.jpg){ loading=lazy }

###### Pilotare BPM da SAM (SAM → BPM)

**Web service standard di BPM:** un insieme deliberatamente **piccolo** di endpoint HTTP che accettano body JSON in POST (descritti come "REST-ish" più che strettamente REST). Tenuto piccolo perché una singola chiamata generica `create-new-process`, parametrizzata sul nome del modello, copre già l'avvio di *qualunque* processo.

Endpoint principali:

- `create-new-process` — avvia una nuova istanza di processo (specifica modello, punto di partenza, variabili iniziali).
- `exec-task` — avanza/esegue un'attività attualmente presente nella to-do list di un utente (simula il clic su "Esegui").
- Caricamento di un allegato su un processo.
- Forzare l'avanzamento di un processo.
- Lettura dei dati variabili di un processo.
- Lettura della to-do list di un utente.

Prova pratica: non serve installare nulla — basta generare una chiave API e qualunque server BPM può essere chiamato. Dimostrato dal vivo con **Postman**:

![postman demo create a new process via web service](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/057_035206_postman-demo-create-a-new-process-via-web-service.jpg){ loading=lazy }

```
POST {bpm-server}/api-ext-create-new-process
Body (JSON): { auth_token, user, model, start, variables{...} }
```

La risposta restituisce successo/fallimento più il nome del processo generato (secondo la regola di naming) ed eventuali messaggi di validazione.

Insidie confermate dal vivo:

- Omettere il punto di partenza su un modello multi-start restituisce un errore esplicito invece di sceglierne uno silenziosamente.
- Campi obbligatori/formule di validazione sono applicati esattamente come lo sarebbero dall'interfaccia utente — un payload incompleto/non valido restituisce `false` senza effetti collaterali.
- `exec-task` è funzionalmente equivalente a cliccare "Esegui" nella to-do list — usato ad es. per far avanzare un processo BPM quando avviene un evento corrispondente lato SAM, anche se il docente è cauto sull'affidarsi troppo a questo meccanismo perché *identificare correttamente* l'evento SAM scatenante è spesso la parte difficile.

Raccomandazione: le chiamate dirette ai web service sono il metodo **ufficiale e più robusto** per qualunque integrazione custom/plugin — restituiscono un vero risultato sincrono di successo/fallimento.

###### Wrapper a stored procedure e trigger (percorso asincrono)

Perché esiste: SAM non ha un meccanismo nativo di evento/webhook in uscita, quindi l'*unico* strumento disponibile per intercettare un evento lato SAM (nuovo ordine, cambio di stato, ecc.) e far partire un processo BPM è un classico **trigger SQL**.

Meccanismo del wrapper a stored procedure: la stessa capacità di "creare processo" è esposta anche come semplice **stored procedure SQL** — ma invece di chiamare il web service in modo sincrono, scrive semplicemente una riga in una tabella di staging (`chiamate API`); un motore in background interno a BPM legge periodicamente quella tabella ed esegue esso stesso la vera chiamata al web service:

```sql
EXEC dbo.usp_bpm_create_process
 @user = 2, @model = 'richieste inv', @start = 1, @external_id = 1
```

Pattern d'uso dei trigger (progetti reali citati: un cliente del settore alimentare, e "Calzavara"): un trigger richiama la stored procedure quando accade un evento di business in SAM (es. un ordine viene approvato); il processo BPM risultante procede e, a ogni passo, usa l'**operazione SQL** per scrivere aggiornamenti di firma/stato indietro su SAM man mano che avanza.

Insidia chiave dell'asincronia: a differenza della chiamata diretta al web service, i trigger e il wrapper a stored procedure sono **fire-and-forget/asincroni** — non c'è un risultato immediato di successo/fallimento, la consegna tipicamente si completa in pochi secondi tramite il motore della tabella di staging, ma questo percorso richiede un **collaudo approfondito**, e la logica del trigger stesso può essere fragile (un bug nel trigger può "mandare in crash" la transazione SAM sottostante).

Convenzione — mantenere il trigger minimale ("External ID"): per evitare di riversare decine di campi in un trigger fragile, il team ha adottato una convenzione rigida: la stored procedure accetta **un solo parametro** — l'ID del documento sorgente — mappato in una variabile di processo BPM chiamata letteralmente **`external_id`**.

BPM si arricchisce da sé dopo l'avvio minimale via trigger, tramite un callback: come primissimo passo del processo (sullo Start, nelle operazioni), BPM richiama subito indietro SAM — usando **Get Data** oppure una **vista-tabella del connettore**, con chiave `external_id` — per recuperare tutti gli altri campi che il processo realmente necessita (ragione sociale del fornitore, indirizzo, termini di pagamento, righe ordine, ecc.). Questo sposta deliberatamente tutta la complessità dal trigger fragile verso gli strumenti BPM, più robusti e testabili.

Via di fuga per casi complessi: se il pattern standard trigger/SP/Get Data non è davvero sufficiente, il codice custom che chiama direttamente i web service è sempre disponibile come alternativa (un collega — Filippo Curati — ne aveva prototipato esattamente una).

###### Buone pratiche e aneddoti reali sull'integrazione

- **Aneddoto — inseguire un evento di business "sfumato":** un cliente voleva un'attività avanzata automaticamente "quando viene inserita la distinta base" in SAM. Il docente spiega che si tratta di un obiettivo di automazione genuinamente difficile: non esiste un singolo evento di database inequivocabile che significhi affidabilmente "la distinta base è davvero finita", e le richieste dei clienti di "automazione totale" portano spesso aspettative poco realistiche che vanno gestite/ridimensionate a monte — meglio promettere meno che costruire qualcosa di fragile che si rompe silenziosamente su casi limite (articolo sbagliato, inserimento duplicato, lotto/partita sbagliati, ecc.).

    ![anecdote a trigger event too fuzzy to automate rel](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/063_041304_anecdote-a-trigger-event-too-fuzzy-to-automate-rel.jpg){ loading=lazy }

- **Buona pratica — minimizzare l'accoppiamento:** evitare di progettare un'integrazione in cui i due sistemi interagiscono continuamente avanti e indietro per tutto il processo (ogni modifica al processo rischia allora di rompere anche il lato SAM). La forma ideale prevede che i due sistemi si parlino solo **all'inizio e alla fine** del processo (es. un trigger per lanciare, una scrittura finale di stato tipo "approvato"/"non approvato" invece di molti micro-stati intermedi sincronizzati avanti e indietro).
- SAM 6 dovrebbe supportare questa integrazione in modo più nativo/flessibile tramite veri web service JSON, riducendo la dipendenza dai workaround dell'era trigger/Web Import descritti sopra.

#### Pianificazione e Gantt


###### Concetto di base

Oltre a tracciare le date/orari effettivi di inizio/fine di ogni attività (cosa che BPM registra sempre di default), BPM offre un livello opzionale di **pianificazione/stima**: durate standard attese per attività, riepilogate automaticamente in un Gantt dal vivo che si aggiorna man mano che il processo procede realmente.

Caratteristiche importanti:

- Le durate sono espresse in **giorni di calendario** (tempo solare), *non* in unità di sforzo/capacità — non esiste in BPM un concetto di capacità/allocazione risorse.
- L'intera funzionalità è opzionale per ogni processo; può essere disattivata interamente tramite permessi quando non è utile per un dato processo (vedi Calendario e permessi, sotto).

###### Impostare durate standard e Gantt auto-generato

1. Su ogni attività, si apre **Pianificazione e Scadenze** e si imposta una durata standard in giorni (es. 5, 7, 15, 2).

    ![demo setting standard task durations on the model](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/065_042229_demo-setting-standard-task-durations-on-the-model.jpg){ loading=lazy }

2. Non appena un'istanza di processo parte, BPM calcola immediatamente una stima Gantt dell'intero processo a partire da queste durate standard, visibile sotto la scheda **Pianificazione** del magazzino delle variabili.
3. Il motore del Gantt modella correttamente la struttura delle dipendenze — inclusi i rami paralleli (due attività affiancate, con logica finish-to-start che alimenta l'attività di ricongiungimento a valle solo dopo la conclusione del ramo parallelo *più lungo*) — "proprio come in Project".

###### Aggiornamenti dal vivo mentre il processo procede

- Man mano che ogni attività viene effettivamente completata, la sua barra Gantt passa dalla durata pianificata originale (mostrata tratteggiata, come "baseline") alla durata compattata/reale, e **tutto ciò che sta a valle si sposta di conseguenza**.
- **Comportamento chiave — il piano spinge solo a destra, mai a sinistra:** se l'avanzamento reale va più tardi del previsto, la pianificazione "aggiornata" slitta più avanti; ma procedere *in anticipo* su un'attività non comprime automaticamente la stima al di sotto delle durate standard per le attività non ancora iniziate.
- Riprogrammare un'attività dalla vista to-do list/calendario (es. trascinando un'attività a una data successiva) rimodella immediatamente anche il Gantt a valle — perché le date della to-do list e le date del Gantt sono letteralmente lo stesso dato sottostante, non due sistemi separati.

###### I tre insiemi di date

Per ogni attività, BPM traccia tre copie parallele dell'intervallo di date:

1. **Programmazione (iniziale/baseline):** il piano originale, punto zero.
2. **Aggiornamento:** la stima corrente, ricalcolata continuamente dal vivo.
3. **Effettiva:** popolata solo una volta che un'attività è realmente iniziata e/o terminata.

###### Data scadenza — separata dalla durata

Concetto: un vincolo di scadenza rigido, imposto dall'esterno (mostrato come un pallino rosso sulla barra del Gantt), impostabile su **qualunque** attività — non solo l'ultima — usato per confrontare la pianificazione aggiornata dal vivo con una data promessa.

Indicazione emersa in sede di Q&A: il modo *corretto* di impostare una scadenza è agganciarla a una vera **variabile data** (qualcosa che l'utente inserisce, o che arriva da un sistema esterno come SAM) piuttosto che a una durata relativa del tipo "N giorni dopo l'inizio" — perché le durate rispondono a "quanto tempo richiede", mentre una scadenza è un vincolo esterno che va catturato come un proprio dato autonomo.

Caso d'uso: scadenze di milestone intermedie a metà processo — es. date di checkpoint del cliente dentro un progetto più lungo, non solo una singola data di fine.

###### Rileva inizio (disaccoppiare inizio attività da attivazione)

Comportamento di default: senza questo flag, l'"inizio" di un'attività si assume coincidente con il momento in cui l'attività precedente è terminata (cioè attivazione = inizio).

Con "rileva inizio" abilitato su un'attività:

- La to-do list mostra un pulsante **"Inizia"** invece di saltare direttamente a "Esegui".
- Finché l'utente non clicca esplicitamente Inizia, la barra Gantt dell'attività ha un contorno sottile/non marcato e nessuna data di inizio effettiva.
- Una volta iniziata, la barra ottiene un bordo marcato e viene registrata una vera data di inizio effettiva.
- Caso d'uso: lavoro che è *pronto ma non ancora iniziato* — es. attività di progettazione/ingegneria che restano "disponibili" per un po' prima che qualcuno le prenda in carico — distingue "in coda" da "in corso".
- Questo si ricollega direttamente ai punti di aggancio delle operazioni Attivazione vs. Inizio: l'aggancio "Inizio" scatta in modo significativo solo su attività con rileva inizio abilitato.

###### Agganciare date/durate a variabili di processo

Sia la **scadenza** sia la **durata pianificata** di un'attività possono essere agganciate a una variabile di processo invece che a un valore fisso di configurazione, rendendo il piano dinamico in base ai dati del processo invece che a un numero statico a livello di modello.

Esempi guidati:

- Scadenza: agganciare "data scadenza" (calendario) a una variabile "data consegna prevista" che il commerciale compila al momento dell'inserimento.
- Durata: un cliente reale aveva una variabile a lista di valori "difficoltà" (A/B/C), e una formula/decision table calcolava la durata standard a partire da essa (es. 5/7/10/12 giorni), che pilotava poi la durata pianificata dell'attività:

```vb
If difficolta = "A" Then
 Return 5
Else
 Return 10
End If
```

###### Da confermare — aggiustamento della baseline iniziale

Concetto: un flag per attività che dà al **proprietario** del processo una finestra una tantum, proprio nel momento in cui l'attività diventa disponibile, per aggiustare manualmente le date pianificate di quella specifica istanza (trascinandole) prima di bloccarle definitivamente.

Flusso operativo:

1. L'attività diventa disponibile con stato "da confermare"; il proprietario può liberamente trascinare/aggiustare le sue date pianificate (e ogni effetto a valle) — questo tocca ancora la baseline *iniziale*, ma solo per questa istanza, non per il modello.
2. Il proprietario clicca **Conferma** (per singola attività, o "conferma tutto"): questo **congela** il piano aggiustato come baseline permanente dell'istanza ("versione 0" / punto di confronto).

    ![demo confirming freezes the baseline plan](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/tutorial/corso-avanzato/082_051243_demo-confirming-freezes-the-baseline-plan.jpg){ loading=lazy }

3. Da quel momento in poi, ogni ulteriore scostamento viene tracciato solo nella pianificazione "aggiornata", relativamente a quella baseline congelata — la baseline confermata in sé non cambia mai più.

- Se un'attività non è marcata "da confermare", nasce già confermata, e il piano derivato dalla durata standard originale è semplicemente, fin dall'inizio, la baseline permanente.

###### Calendario e permessi

- BPM ha un **calendario interno integrato** che tiene conto di weekend e festività; quando viene calcolata una durata attività di "12 giorni", questa copre di default 12 giorni *di calendario* (i weekend sono mostrati in grigio nel Gantt). Un flag per attività ("Utilizza Calendario") permette a un'attività di ignorare il calendario e contare i giorni trascorsi grezzi (es. un passaggio di processo genuinamente attivo 24/7). Il calendario in sé non è facilmente personalizzabile dall'utente finale — lo si usa o non lo si usa.
- L'intera vista di pianificazione/Gantt (visualizzazione e/o modifica) è vincolata da **permessi a livello di processo** ("visualizza pianificazione" / "modifica pianificazione") per utente/gruppo — per i processi in cui il Gantt non ha significato, è meglio nasconderlo del tutto piuttosto che mostrare un grafico confuso o irrilevante.

### Tutorial avanzati


1. [Tutorial 1 — Costruire una griglia dati collegata a una tabella fornitori](#tutorial-1-costruire-una-griglia-dati-collegata-a-una-tabella-fornitori)
1. [Tutorial 2 — Filtrare un gruppo diversamente su due attività parallele e condizionare il gateway](#tutorial-2-filtrare-un-gruppo-diversamente-su-due-attivit\224-parallele-e-condizionare-il-gateway)
1. [Tutorial 3 — Costruire una decision table per l'assegnazione automatica dell'approvatore in base all'importo](#tutorial-3-costruire-una-decision-table-per-lassegnazione-automatica-dellapprovatore-in-base-allimporto)
1. [Tutorial 4 — Configurare un connettore attivo verso SAM per la creazione di una commessa](#tutorial-4-configurare-un-connettore-attivo-verso-sam-per-la-creazione-di-una-commessa)
1. [Tutorial 5 — Impostare la pianificazione/Gantt di un processo con durate standard e scadenza dinamica](#tutorial-5-impostare-la-pianificazionegantt-di-un-processo-con-durate-standard-e-scadenza-dinamica)

#### Tutorial 1 — Costruire una griglia dati collegata a una tabella fornitori


Obiettivo: aggiungere alla form di un processo una griglia in sola lettura che mostri i dati anagrafici dei fornitori, consultabile senza uscire dal processo. –

1. Nel magazzino delle variabili, crea una nuova variabile e imposta il suo tipo su **Griglia Dati**.
2. Apri la configurazione della variabile (la stessa schermata usata per l'aggancio tabella dei campi semplici).
3. Scegli come tabella sorgente la tabella (locale, vista o tabella esposta da connettore) desiderata — nell'esempio del corso, la tabella "fornitori".
4. Nell'elenco delle colonne disponibili, seleziona quelle da esporre nella griglia (nell'esempio: codice, descrizione).
5. Per ciascuna colonna selezionata, se il nome originale non è chiaro per l'utente finale, assegna un'intestazione (caption) più leggibile.
6. Salva la configurazione della variabile.
7. Trascina la variabile griglia dati nella form del processo (pagina del magazzino) e anche nelle "variabili da richiedere" dell'attività/start dove deve comparire, dandole spazio a schermo sufficiente.
8. Pubblica il processo.
9. Avvia (o riapri) un'istanza: la griglia appare popolata con i dati della tabella, filtrabile e raggruppabile come le altre griglie del prodotto, ma non modificabile.

Nota: lo stesso identico meccanismo di aggancio è usato per i campi con lookup su tabella (combo/popup di ricerca) — la differenza è solo nella resa a video.

#### Tutorial 2 — Filtrare un gruppo diversamente su due attività parallele e condizionare il gateway


Obiettivo: due attività parallele di valutazione preventivi (tipo A / tipo B) devono mostrare, dello stesso gruppo "lista preventivi", solo le righe pertinenti al proprio tipo; inoltre il ramo verso ciascuna attività deve aprirsi solo se esistono righe di quel tipo. –

1. Nel diagramma di processo, individua le due attività parallele (es. "valutazione preventivi tipo A" e "valutazione preventivi tipo B"), entrambe collegate allo stesso gruppo "lista preventivi".
2. Sulla prima attività, apri "variabili da richiedere" e seleziona una qualunque variabile appartenente al gruppo "lista preventivi".
3. Nelle impostazioni locali di quella variabile, disabilita l'aggiunta e la cancellazione righe (per rendere la vista di sola consultazione su questa attività) e imposta una **condizione di filtro**, ad esempio `tipo_preventivo = "tipo A"`.
4. Ripeti i passi 2–3 sulla seconda attività, con la condizione opposta (`tipo_preventivo = "tipo B"`).
5. Nel magazzino delle variabili, crea due variabili helper di tipo stringa (es. `presenza_tipo_A`, `presenza_tipo_B`) — servono solo per verificare visivamente il risultato della formula mentre la costruisci, dato che BPM non ha un debugger.
6. Su `presenza_tipo_A`, apri l'editor di formula e scrivi:

    ```vb
    Dim i As Integer
    For i = 0 To lista_preventivi.Count - 1
    If tipo_preventivo(i) = "tipo A" Then
    Return "sì"
    End If
    Next
    Return "no"
    ```

7. Ripeti lo stesso schema per `presenza_tipo_B`, sostituendo la condizione con `"tipo B"`.
8. Sul gateway (o link) che porta verso l'attività "valutazione preventivi tipo A", apri la condizione di abilitazione e imposta `presenza_tipo_A = "sì"`. Ripeti analogamente per il ramo tipo B.
9. Facoltativo — validazione globale: sull'attività di inserimento preventivi, aggiungi una formula di validazione globale che impedisca di proseguire se non è stato inserito alcun preventivo:

    ```vb
    If Count(tipo_preventivo) = 0 Then
    MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
    Return False
    End If
    Return True
    ```

10. Pubblica e collauda con dati di test: inserisci solo preventivi di tipo A e verifica che si apra solo il ramo corrispondente; ripeti con tipo B e con entrambi.

#### Tutorial 3 — Costruire una decision table per l'assegnazione automatica dell'approvatore in base all'importo


Obiettivo: sostituire una formula scritta a mano con una decision table che assegna l'approvatore tecnico in base all'importo della richiesta (ed eventualmente al tipo di richiesta). –

1. Individua il punto del processo dove serve calcolare l'utente approvatore — tipicamente una formula agganciata a una variabile di tipo Utente (es. `utente_approvazione_tecnica`), oppure una decisione da prendere in un'operazione Set Variable.
2. Apri l'editor della formula/valore su quella variabile e scegli l'opzione per convertirla in **decision table** (o creane una nuova direttamente come decision table, se disponibile).
3. Aggiungi una colonna di input: `Importo Richiesta`.
4. Aggiungi una colonna di output: `Utente Approvazione` — essendo di tipo Utente, la tabella propone automaticamente l'elenco di utenti/gruppi disponibili come valori possibili.
5. Inserisci le righe-regola:

 - Riga 1: `Importo Richiesta < 1000` → `Dir Tech`
 - Riga 2: `Importo Richiesta ≥ 1000` → `Dir Gen`

6. Verifica/aggiusta l'ordine delle righe con le frecce su/giù, ricordando che vince la prima riga che soddisfa la condizione.
7. Estendi la tabella con una seconda colonna di input, `Tipo Richiesta` (lista di valori — la tabella ne conosce automaticamente i valori ammessi), e aggiungi/riordina le righe:

 - `< 1000` / `Normale` → `Dir Tech`
 - `≥ 1000` / `Normale` → `Dir Gen`
 - `(qualunque)` / `Sicurezza` → `Sicurezza`

8. Salva la decision table.
9. Sull'attività di approvazione, imposta gli "utenti responsabili" sulla variabile `utente_approvazione_tecnica` (assegnazione guidata da regola) invece che su un gruppo fisso.
10. Pubblica e collauda con richieste di importo/tipo diversi, verificando che l'attività venga assegnata correttamente.
11. Se in seguito la logica dovesse superare ciò che la tabella può esprimere (es. serve scorrere un gruppo e contare righe), converti la tabella in formula e completa la logica a mano in VB.

#### Tutorial 4 — Configurare un connettore attivo verso SAM per la creazione di una commessa


Obiettivo: da un'attività del processo, generare automaticamente una nuova commessa in SAM tramite il connettore attivo, mappando testata, dettaglio righe e recuperando il numero commessa generato. –

1. Verifica preliminare (lato ambiente): il connettore "SAM v5" deve essere configurato in Configurazione → connettori, marcato **Attivo**, con almeno un'azienda ("nuova azienda") configurata con i parametri di connessione (server DB, credenziali, endpoint web service dell'azienda). Il modulo **Web Import** di SAM deve essere installato e raggiungibile.
2. Nel diagramma di processo, trascina l'operazione **Connettore Attivo** nel punto del flusso dove deve avvenire la creazione della commessa.
3. Fai doppio clic sull'operazione appena inserita.
4. Scegli l'interfaccia XML preconfezionata pertinente (es. "xml commessa").
5. Nella schermata dei parametri di input (testata), mappa ciascun campo richiesto su una variabile di processo corrispondente (es. codice cliente, descrizione commessa) oppure lascialo come valore fisso quando appropriato.
6. Se serve un campo di testata non presente nell'elenco default, usa l'helper di aggiunta campo (che conosce le colonne della tabella target in SAM) per aggiungerlo e mappalo a sua volta.
7. Se l'interfaccia prevede parametri di output (es. l'ID/numero della commessa creata), mappali su una variabile di processo dedicata (es. `numero_commessa`).
8. Se il processo include un gruppo di dettaglio corrispondente (es. "lista codici" articoli), apri la sezione parametri di dettaglio/riga e mappa ciascuna colonna del gruppo sul nodo XML di dettaglio ripetuto corrispondente (es. `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`).
9. Salva la configurazione dell'operazione.
10. Pubblica il processo e collauda l'esecuzione dell'attività: verifica in SAM che la commessa sia stata effettivamente creata con i dati attesi, e che `numero_commessa` sia stato valorizzato correttamente nell'istanza di processo.
11. In caso di errore, ricorda che BPM è un semplice pass-through verso il web import di SAM: un campo obbligatorio mancante o non valido produce un errore restituito da SAM, non da BPM.

#### Tutorial 5 — Impostare la pianificazione/Gantt di un processo con durate standard e scadenza dinamica


Obiettivo: dotare un processo di stime di durata per ogni attività, in modo che all'avvio di ogni istanza venga generato automaticamente un Gantt, con una scadenza agganciata a una variabile data. –

1. Verifica i permessi di processo: sotto Utenti e Gruppi, assicurati che "visualizza pianificazione" (e, se necessario, "modifica pianificazione") siano abilitati per i gruppi che dovranno vedere/gestire il Gantt.
2. Per ciascuna attività del processo, apri la scheda **Pianificazione e Scadenze** e imposta una durata standard in giorni (es. 5, 7, 15, 2 a seconda dell'attività).
3. Se un'attività deve avere un vincolo di scadenza esterno (non derivato dalla durata), sulla stessa scheda seleziona l'opzione per agganciare la **data scadenza** a una variabile data del processo (es. `data_consegna_prevista`), invece di lasciarla come valore fisso o come "N giorni dopo l'inizio".
4. Facoltativo — durata dinamica: se la durata standard deve dipendere da un dato del processo (es. una variabile lista di valori "difficoltà" A/B/C), crea una formula o decision table che calcoli la durata in giorni e agganciala al campo durata dell'attività:

    ```vb
    If difficolta = "A" Then
    Return 5
    Else
    Return 10
    End If
    ```

5. Se un'attività rappresenta lavoro che può restare "disponibile" prima di essere effettivamente iniziato (es. attività di progettazione), abilita il flag **Rileva Inizio** su quell'attività.
6. Se il processo richiede che il proprietario possa aggiustare la pianificazione iniziale di ogni singola istanza prima che diventi baseline definitiva, abilita il flag **Da Confermare** sulle attività pertinenti.
7. Verifica, per le attività il cui ritmo di lavoro non segue la settimana lavorativa standard, se disabilitare il flag "Utilizza Calendario" (per contare giorni solari grezzi invece che giorni di calendario aziendale con weekend/festività).
8. Pubblica il processo.
9. Avvia una nuova istanza: verifica, nella scheda **Pianificazione** del magazzino delle variabili, che il Gantt dell'intero processo sia stato generato automaticamente a partire dalle durate standard.
10. Completa la prima attività e osserva che la sua barra passa da tratteggiata (baseline) a piena (reale), e che tutte le attività a valle si aggiornano di conseguenza nella pianificazione "aggiornata".
11. Se un'attività è marcata "Da Confermare", verifica che al momento della sua attivazione il proprietario possa trascinare/aggiustare le date proposte e poi cliccare **Conferma** (o "conferma tutto") per congelarle come nuova baseline dell'istanza.

# Processi

## Modelli di processo

Un **modello di processo** configura un flusso eseguibile: attivita, variabili, assegnazioni, autorizzazioni, regole, integrazioni e rappresentazione grafica. Ogni esecuzione del modello genera un'istanza di processo.

Il **Designer di processo** e l'ambiente nel quale si crea e si modifica il modello. Comprende il canvas, le barre degli strumenti, i pannelli delle proprieta e gli editor collegati.

### Accedere ai modelli

La voce **Modelli di processo** del menu principale apre l'elenco dei modelli, organizzati per gruppo. Una barra di ricerca consente di filtrare l'elenco; da qui si puo aprire un modello esistente oppure crearne uno nuovo.

### Creare un modello di processo

Il modello rappresenta il flusso tramite oggetti collegati, ciascuno con un ruolo specifico.  

Gli oggetti si dispongono sul canvas mediante trascinamento.  

Creare un nuovo modello di processo è semplice: basta recarsi nel pannello delle impostazioni in alto a sinistra, poi cliccare la voce **Modelli di Processo** ed infine cliccare **Nuovo modello di processo**.

![Creazione di un modello](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/new-model.gif "Creazione di un modello")

---

### Gli strumenti del Designer

Gli strumenti del Designer sono suddivisi in più sezioni: 

1. Una [barra superiore degli strumenti](#barra-degli-strumenti) con i comandi generali per il modello, gli elementi e i loro attributi.

2. Una barra laterale sinistra con il [catalogo degli elementi](#elementi) disponibili.

3. Un [pannello degli attributi](#pannello-attributi) a destra, che mostra le proprieta dell'elemento selezionato. Se viene chiuso, si puo riaprire premendo `F4`.

4. Una sezione nella parte inferiore contente le etichette delle diverse pagine di lavoro attualmente aperte e una scroll bar per regolare lo zoom su queste pagine. Inizialmente la pagina selezionata è quella del processo, in cui troviamo tutti gli elementi grafici del flusso.  
Subito a sinistra si trova la [pagina Info](#pagina-info), dedicata alle impostazioni del modello. Le altre schede vengono aggiunte quando si aprono strumenti come l'[Editor delle variabili](#editor-delle-variabili).

![Componenti del Designer di processo](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer-parts.png "Componenti del Designer di processo")

---

### Costruire un modello di processo

Quando creiamo un nuovo modello di processo non troveremo il canvas completamente vuoto, ma sarà già presente un singolo elemento, un punto di inizio, detto Start.

Nella maggior parte dei casi, un flusso ha un inizio e almeno una fine.

L'inizio, può essere sovrascritto: cliccando tasto destro su un altro elemento presente sul canvas, dal menu contestuale si può scegliere l'opzione **Imposta come oggetto di avvio**. Così facendo il flusso inizierà dall'elemento impostato come oggetto di avvio.

> **Rimozione dello Start**
>
> È possibile rimuovere lo Start, ma è un comportamento non convenzionale e tendenzialmente sconsigliato in quanto il processo richiederà all'utente di inserire direttamente le variabili da richiedere.

Dalla sidebar di sinistra, sarà ora possibile iniziare a disegnare il processo trascinando direttamente gli oggetti sul canvas. 

Ogni elemento può o deve essere collegato ad altri elementi o a se stesso tramite i **Link**, frecce orientate che indicano i vari percorsi che il processo può instradare.  

Selezionando uno degli oggetti disegnati, sulla destra si aprirà il pannello degli attributi ad esso riferiti. 
Ogni oggetto ha delle proprietà, alcune di esse sono comuni a tutti, mentre altre sono specifiche del tipo di oggetto.   


## Pagina Info


La sezione **_Pagina Info_** permette di configurare le **impostazioni** principali di un **modello di processo**.  
Da qui è possibile gestire le informazioni di base, le regole di gestione, i contatti associati, i permessi di utilizzo e altro ancora.

Questa sezione è suddivisa in quattro blocchi principali, ciascuno dei quali contiene campi specifici che permettono di definire in modo preciso il comportamento e le proprietà del modello:

##### **Impostazioni base**

In questa parte si impostano le informazioni fondamentali per identificare e organizzare il modello di processo.

**Nome modello**
Nome identificativo univoco del modello di processo. È il titolo con cui verrà visualizzato all’interno dell’applicativo. 

**Descrizione modello**
Campo testuale per inserire una breve descrizione esplicativa del modello.

**Cartella**
Specifica la cartella logica in cui il modello verrà salvato.  

**Gruppi di modelli**
Permette di assegnare il modello a uno o più gruppi di modelli per facilitarne l’organizzazione. 

**Modello Principale**
Indica se il modello rappresenta o meno il processo principale (_True_ / _False_).

**Tabella variabili**
Campo che definisce la tabella delle variabili associate al modello, utile per la gestione delle informazioni interne al processo.

---

##### **Gestione**

Questa sezione include campi che permettono di controllare il comportamento automatico e la modalità di duplicazione del modello.

**Formula nome **
Campo per definire una formula che costruisce il nome delle istanze di processo in base a regole o variabili.

> **Automazione Formula Nome**
>
> Sebbene questo campo sia opzionale, e consigliabile definire una _Formula Nome_. Un modo per rendere univoci i nomi e inserire un **Progressivo**, cioe una variabile numerica incrementata quando viene creata una nuova istanza di processo. La variabile deve essere definita nel [Magazzino delle variabili](#magazzino-delle-variabili).

**Formula descrizione**
Campo per definire una formula che costruisce la descrizione dell'istanza di processo in base a regole o variabili.

**Formula testo**
Campo per definire una formula automatica che genera automaticamente testi personalizzati in base a regole o variabili.

**Schemi di duplicazione**
Indica quali schemi di duplicazione utilizzare per la duplicazione del modello.  

**BPMN**
Opzione booleana che specifica se il modello utilizza o meno la notazione BPMN (_True_ / _False_).  

---

##### **Contatti e utenti**

In questo blocco si configurano i riferimenti a utenti, aziende e contatti legati al modello.

**Contatti**
Campo per associare uno o più contatti esterni al modello.

**Azienda**
Campo per specificare l’azienda o l’ente a cui il modello è collegato.

**Proprietari**
Indica gli utenti proprietari del modello. Solo questi avranno diritti completi di modifica e gestione.

**Persone messe a conoscenza**
Utenti che possono visualizzare il modello, ma senza diritti di modifica.

**Responsabili programmazione**
Utenti incaricati di gestire gli aspetti tecnici o di pianificazione del modello.

---

##### **Permessi**

L’ultima sezione è dedicata alla definizione delle autorizzazioni e delle opzioni di sicurezza applicate al modello. Sono tutti valori _True_ / _False_.

**Autorizzazioni allegati per root**
Determina se gli allegati root ereditano o meno le autorizzazioni specifiche del modello.

**Autorizzazioni per pagina**
Stabilisce se le autorizzazioni sono gestite a livello di singola pagina del processo.

**Abilitazione note salvataggio**
Se impostato su _True_, richiede all’utente di inserire una nota ogni volta che vengono salvate modifiche al modello.  

## Designer


Il **Designer di processo** è l'ambiente nel quale si configura un modello di processo. Comprende il canvas, le barre degli strumenti, il pannello degli attributi e gli editor aperti durante la progettazione.

#### Componenti

- [Barra degli strumenti](#barra-degli-strumenti): comandi per creare, salvare, pubblicare e modificare il modello.
- [Pannello attributi](#pannello-attributi): proprietà dell'oggetto selezionato.
- [Menu contestuale](#menu-contestuale): comandi e configurazioni disponibili con il tasto destro.
- [Puntatore](#puntatore): modalità di selezione degli oggetti.
- [Elementi del Designer](#elementi): catalogo degli oggetti disponibili sul canvas.

Il [canvas](#canvas) è la superficie centrale sulla quale si dispongono e si collegano gli oggetti.

### Barra degli strumenti


##### Home

Qui sono presenti le principali azioni relative al modello di processo, suddivise in quattro sezioni:

![Toolbar Home](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/toolbar-home.png "Toolbar Home")

###### **Workflow**

**Nuovo**

Per creare un nuovo modello.

**Apri**

Per importare un modello da una repository o da un file locale.

**Salva**

Salva il modello in un repository o in locale; permette anche di salvare il disegno come immagine.

**Pubblica**

Per pubblicare le modifiche apportate al modello, una volta salvate, per essere esportate ai processi attivi vanno pubblicate.

**Duplica**

Viene creata una copia del modello in modifica.

###### **Stampa**

**Stampa o Esporta**

Similmente al salvataggio come immagine, qui il modello viene stampato fisicamente o virtualmente in versione PDF.

###### **Ricerca oggetti**

Tramite una textbox, vengono evidenziati gli elementi la cui descrizione coincide col testo scritto al suo interno.

###### **Tools**

**Verifica Workflow**

Mostra in un popup gli avvertimenti e gli errori rilevati nel modello corrente.

---

##### Strumenti

Qui troviamo i principali strumenti per il design del flusso di lavoro e per la gestione delle variabili del processo, divisi in 5 sezioni:

![Toolbar Strumenti](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/toolbar-strumenti.png "Toolbar Strumenti")

###### **Operatività**

**Puntatore**

Il bottone [Puntatore](#puntatore) serve per tornare alla modalita standard del cursore. 

**Strumento di collegamento**

Permette di creare dei [Link](#link) tra gli elementi del modello.

**Undo**

Permette di annullare l'ultima operazione svolta o di scegliere quante annullarne in una sola volta, mostrando un elenco di brevi descrizioni delle ultime azioni compiute.

**Modelli email**

Lo strumento Modelli email apre in un dialog un popup che consente la creazione, la modifica, la duplicazione e l'eliminazione dei modelli email.

**Proprietà**

Permette di visualizzare/nascondere il pannello degli attributi sulla destra.

###### **Generale**

**Inserimento/modifica variabili**

Cliccando su questo pulsante si apre il [Magazzino delle variabili](#magazzino-delle-variabili).

**Variabili per ricerche**

Permette di scegliere dal magazzino delle variabili quali utilizzare per le ricerche.

**Variabili allegati processo**

Permette di visualizzare e modificare le variabili relative agli allegati del processo.

**Allegati**

Permette di inserire ed eliminare gli allegati del processo tramite un dialog, creando anche le apposite directory.

###### **Allineamento e dimensioni**
Qui troviamo diverse diversi pulsanti e dropdown per modificare le dimensioni, l'allineamento e il piano su cui si trovano gli elementi selezionati.

###### **Posizionamento**

Questa sezione contiene due proprietà del canvas utili per la parte grafica:

**Aggancia alla griglia**

Attivando questa proprietà il canvas diventa puntinato: lo spostamento e il ridimensionamento degli oggetti sarà guidato dai punti sul piano di disegno.

**Aggancia agli oggetto**

Attivando questa proprietà lo spostamento e il ridimensionamento degli oggetti sarà guidato dai bordi degli altri oggetti.

###### **Pagina**

In questa sezione sono presenti 5 pulsanti e il dropdown per lo zoom del canvas.

**Nuova pagina**

Il primo bottone, Nuova pagina, crea una nuova pagina nel processo.

**Pagina precedente e Pagina successiva**

Il secondo e terzo bottone servono per cambiare la pagina visualizzata, andando alla precedente o alla successiva.

**Imposta pagina**

Il quarto bottone, Imposta pagina, apre un dialog che mostra le varie impostazioni del canvas/pagina.  
Dal popup è possibile impostare i margini e il formato della pagina, basato sullo standard A dei fogli per stampanti, e il loro orientamento, se Portrait o Landscape.  
In basso e possibile gestire l'orientamento delle [Swim lane](#gruppo-e-swim-lane), scegliendo tra verticale e orizzontale.

**Elimina**

Quest'ultimo bottone serve ad eliminare la pagina corrente.

> **Requirement per cancellazione**
>
> È possibile cancellare solo pagine vuote.

###### **Lingua**

Dall'ultima sezione è possibile scegliere la lingua tramite dropdown.

### Pannello attributi


Il **_Pannello Attributi_** si trova sulla destra del canvas, ma è visibile solo quando un oggetto è selezionato.  
Qui sono raggruppate molte informazioni e impostazioni dell'oggetto selezionato, alcune delle quali comuni a quelle del [menu contestuale](#menu-contestuale). Le voci visibili dipendono dall'oggetto selezionato.

Dall'altro come prima voce, presente a tutti gli oggetti, troviamo il _(Nome)_ dell'oggetto. Questo viene assegnato in modo automatico quando l'oggetto è inserito nel canvas e non può essere modificato in seguito. Il nome è formato dal tipo dell'oggetto seguito da un numero identificativo incrementale (ad esempio: _start1_).

Di seguito troviamo tutte le impostazioni, modificabili dall'utente e raggruppate in gruppi:

##### Aspetto
Permette di gestire l'**allineamento** della targhetta, il **colore** e il **font** del **testo** al suo interno, lo **spessore** e il **colore** dei **bordi** dell'oggetto, il **colore** dello **sfondo**, il **tipo di linea** (nel caso di un oggetto [Link](#link)).

##### Dati
Questa sezione contiene proprietà modificabili del singolo oggetto per personalizzarne il comportamento. Molte di queste voci sono comuni con il menu contestuale e portano ai medesimi pannelli di configurazione. Le voci che troviamo sono:

###### Allegati
Il popup e lo stesso accessibile dalla voce Allegati del [menu contestuale](#allegati-da-richiedere).

###### Ambito
Un campo di testo libero che permette raggruppare/categorizzare le task.  
Dalla to-do list infatti è possibile ricercare tutte le task con uno stesso ambito.

###### Descrizione
Permette di fornire informazioni testuali riguardanti una task, utili a chi dovrà poi dovrà svolgerla.  
Queste informazioni appariranno poi nella tab _Istruzioni_ quando un utente eseguirà quella task.

###### Escalation
Cliccando su questo campo si apre lo stesso pannello accessibile dalla voce [Escalation](#escalation-1) del menu contestuale. 

###### Operazioni
Il popup permette di configurare le operazioni relative all'attivita, come descritto nella voce [Operazioni](#operazioni-1) del menu contestuale.

###### Priorità
Permette di assegnare un livello di importanza allo svolgimento di una task.  
Dalla to-do list è poi possibile filtrare e ordinare le task in base alla loro priorità.  
I livelli possibili sono: _Nessuna_, _Bassa_, _Media_, _Alta_ o _Sospesa_.

###### Testo
Consente di modificare ciò che appare sul canvas a video nella label di un elemento. Il valore inserito sarà considerato anche come nome secondario dell'elemento, permettendo di filtrare le task in base ad esso e apparendo nella tab _Dati_ dell'esecuzione di una task.

###### Utenti, Utenti cc e Utenti responsabili
Questa voce definisce chi dovra svolgere un'attivita. Il popup e descritto in [Utenti e responsabili](#utenti-e-responsabili).

###### Variabili da richiedere
Le variabili di un'attivita sono configurabili anche tramite la voce [Variabili da richiedere](#variabili-da-richiedere-1).

###### Impostazioni
Questa voce, esclusiva dell'oggetto **Ritorno al processo chiamante**, apre la schermata di configurazione dell'oggetto.

##### Gestione
In questa sezione troviamo le impostazioni per la gestione del processo nella todo list.  
È presente solo per 4 oggetti, con voci differenti per ognuno di essi.  
Vediamo nel dettaglio cosa è possibile configurare per ciascun oggetto:

**Attivita e Sottoprocesso**

Voci disponibili per [Attivita](#attivita-1) e [Sottoprocesso](#sottoprocesso):
    - _Colore in todo list_: determina il colore della task nella todo list per maggiore organizzazione a livello visivo.
    - _Da confermare_: determina se la task necessiti o meno di un'azione di conferma esplicita prima di poter essere effettivamente eseguita.
    - _Rileva inizio attività_: determina se l'attività sia da iniziare espicitamente o se inizia automaticamente all'attivazione, utile per assegnare operazioni automatiche all'inizio dell'attività invece che all'attivazione.
    - _Skip activity_: determina se la task deve essere saltata senza eseguire, andando direttamente alla successiva, o meno. 
    - _Sottoprocesso_: definisce se l'oggetto contiene un sottoprocesso e di quale tipo, come descritto nella [pagina dedicata](#sottoprocesso).
    - _Testo pulsante esegui_: permette di modificare il testo del link per eseguire la task, presente nella colonna 'Azione' della todo list.
    - _Tipo attività_: permette di categorizzare la task tramite un elenco pre-impostato dei tipi di attività più comuni.
    - _Utilizza calendario_: determina se usare il calendario per il calcolo dei giorni. La stessa opzione e descritta in [Pianificazione e scadenze](#pianificazione-e-scadenze).

**Stato**

- _Blocca edit_: impedisce la modifica dei dati dell'istanza di processo o del documento quando lo stato viene raggiunto.
- _Stato di chiusura_: conclude l'istanza di processo e interrompe le attivita ancora in corso.

**Connettore attivo**

- _Interfaccia_: apre la finestra di configurazione accessibile anche tramite menu contestuale.

##### Scadenze/Tempi

Questa sezione contiene _Durata prevista_ e _Scadenza_. Entrambe aprono il pannello descritto in [Pianificazione e scadenze](#pianificazione-e-scadenze).

##### Varie

Alcune impostazioni sono specifiche di certi singoli oggetti e non sono assegnabili in uno dei precedenti raggruppamenti.  
Per questo vengono inseriti in questa sezione contenente tutti le voci speciali/extra:

- ###### Percorso per pianificazione
  Esclusivo dell'oggetto [Link](#link), determina il percorso predefinito per la pianificazione temporale delle attivita del processo.  
  Utile solo in caso il flusso sia ramificato, ad esempio con percorsi diversi da seguire in base ai valori assunti da alcune variabili di processo.

###### Configurazione 
Questa sezione è presente solo per due oggetti e permette di accedere direttamente alla finestra di configurazione di ciascun oggetto. Essse sono aggiungibili anche tramite menu contestuale e sono illustrate nelle apposite sezioni dedicate (raggiungibili tramite i link contenuti nei nomi degli oggetti qui sotto).  

La sezione contiene un'unica voce, con nome specifico per ciascun oggetto:

- CONFIGURAZIONE **_TIMER_** per l'oggetto **Start a tempo**

- CONFIGURAZIONE **_ATTESA_** per l'oggetto **Attesa**

Questa opzione e presente per le [Operazioni](#operazioni-2) e per i [Gateway](#gateway-e-percorsi), tranne **Sincronizza**.  
La schermata di _Configurazione_ è totalmente differente per ogni oggetto e viene approfondita nelle sezioni relative ai singoli elementi.

### Menu contestuale


Il **_Menu contestuale_** appare quando si preme il **tasto destro del mouse su un oggetto** nel canvas.  
Le _opzioni visibili saranno differenti per ciascun tipo di oggetto selezionato_, ma alcune di essere saranno invece comuni a tutti gli oggetti.

##### Allineamento
L'entrata Allineamento a sua volta ha 10 scelte, divise in 3 gruppi: 

###### Porta davanti e Porta dietro
Modifica lo _Z-index_ di un oggetto: se un oggetto risulta sovrapposto ad un altro, per portarlo in avanti è sufficiente cliccare _Porta davanti_ per portarlo in primo piano.   
Lo stesso, ma al contrario, vale per _Porta dietro_.

###### Allinea
Permette di allineare gli elementi selezionati secondo il tipo di allineamento scelto, in base alla posizione dell'elemento su cui è stato cliccato il tasto destro. L'allineamento può essere verticale o orizzantale, sia agli estremi che al centro.

###### Distribuisci
Selezionando più oggetti(1)è possibile spostarli in massa distrubuendoli su uno dei loro assi utilizzando le due entrate _Distribuisci verticalmente_ o _Distribuisci orizzontalmente_.

1.  Per selezionare più oggetti è necessario tenere premuto <kbd>ctrl</kbd> o `Shift` quando si va a cliccare, col tasto sinistro, su un elemento. Altrimenti, cliccando su una parte vuota del canvas e tenendo premuto, è possibile delineare un'area i cui elementi interno verranno selezionati.

##### Colore e font

Tramite questa voce è possibile cambiare:

- Colore e font dell'**etichetta** dell'elemento.
- Colore dello **sfondo**.
- Colore del **bordo**.

##### Manipolazione oggetto

- **Taglia**: Rimuove l'oggetto dalla posizione corrente e lo salva temporaneamente in memoria per poterlo incollare altrove.
- **Copia**: Salva in memoria l'oggetto per incollarlo in un'altra posizione, duplicandolo.
- **Sposta oggetto alla pagina ...**: permette di spostare l'oggetto in un'altra pagina del processo.

##### Manipolazione testo e label

- **Sposta testo** per spostare l'etichetta dell'oggetto dove si vuole nel canvas. Essa rimarrà ancorata al punto dove la si è spostata.
- **Modifica Testo** consente di modificare il testo dell'etichetta. Azione eseguibile anche da tastiera tramite il tasto <kbd>F2</kbd> sull'oggetto selezionato.

##### Imposta come oggetto di avvio

Quest'entrata permette di impostare un oggetto come oggetto di avvio,rendendo l'oggetto su cui si è cliccato, il punto di partenza del processo.

> **Rimozione dello Start**
>
> È possibile rimuovere lo Start, ma è un comportamento non convenzionale e tendenzialmente sconsigliato in quanto il processo richiederà all'utente di inserire direttamente le variabili da richiedere.

##### Utenti e responsabili

![Configurazione di utenti e responsabili](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/utenti-resp.png)

Tramite quest'entrata è possibile definire il ruolo degli utenti rispetto ad un oggetto su cui è necessario svolgere una qualsiasi azione da parte di un dipendente.  

Si può lavorare sia su **singoli utenti** sia su **gruppi** di utente.

Oltre a utenti e gruppi statici e possibile gestire variabili di tipo [UserType](#usertype-1), identificate dal simbolo `@` all'inizio del nome.  
L'uso di queste variabili consente il **routing dinamico** dei task sulla base dei dati del processo in corso e garantiscono la massima flessibilità nei workflow complessi, adattandosi automaticamente a chi deve realmente gestire l'attività.

Nella parte inferiore della ffinestra di configurazione è inoltre presente il flag:

-	_Task deve essere assegnato prima di poter essere eseguito_

Non selezionato: Il primo utente disponibile tra gli esecutori può prendere in carico o eseguire direttamente il task. Nessuna assegnazione preventiva è necessaria.
Selezionato: Il responsabile deve assegnare esplicitamente il task a un esecutore. Solo l'assegnatario potrà poi eseguire l'attività.

I ruoli assegnabili a utenti o gruppi sono 3:

- **_Esecutore_** - chi dovrà svolgere effettivamente la task.
- **_Responsabile_** (opzionale) - colui che assegnerà l'attività ad un esercutore prima che venga eseguita (in caso il task sia configurato in questo modo).
- **_Utenti in copia (CC)_** - utenti che ricevono aggiornamenti sull'andamento del task ma non hanno responsabilità operative dirette.

##### Variabili da richiedere

L'entrata **_Variabili da richiedere_** permette di definire i dati che l'utente dovrà inserire o visualizzare durante l'esecuzione dell'oggetto.  

Una volta cliccata, aprirà una nuova pagina dedicata all'inserimento delle variabili, a partire dalla struttura globale delle variabili di processo.  
Questa e una versione limitata dell'[Editor delle variabili](#editor-delle-variabili), in cui:

- Non è possibile creare nuove variabili.
- Si possono solo selezionare variabili esistenti definite a livello di processo o documento.

Per aggiungere una variabile da richiedere, basta prenderne una dalla lista di sinistra e trascinarla nel canvas.
Così facendo, gli utenti a cui è assegnata la task, dovranno inserire i valori delle variabili così definite.

![Configurazione delle variabili da richiedere](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/inserimento-var.gif)

##### Allegati da richiedere

Tramite l'entrata **_Allegati da richiedere_** à inoltre possibile definire gli allegati richiesti e gestiti nell'oggetto.
In questo caso non è possibile definire direttamente gli allegati da inserire, ma piuttosto, creare tramite un popup, dei filtri che vadano a scremare i possibili allegati inseribili.

![Opzioni degli allegati](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/attachment-options.png)

Il popup presenta due checkbox:

- La prima, se spuntata, renderà funzionanti i filtri e le preferenze che vengono definite nel resto del popup. Inoltre, farà si che l'utente assegnato a questo oggetto vedrà durante l'esecuzione un tab con l’albero degli allegati associati al processo/documento.

- La seconda, invece, determina se gli allegati caricati possano essere successivamente modificati o se solamente visti.

Dopodiché una sezione dedicata ai filtri, 3 in particolare:

Il **_Gruppo allegato_** e il **_Tipo Allegato_**, definibili dal menu delle impostazioni alla sezione **_Configurazione_**, nel segmento **_Allegati_**, permettono di accettare solo allegati che appartengono a questi gruppi o tipi.

Il **_Percorso_** permette di filtrare gli allegati sulla base del percorso file in cui sono memorizzati, il quale deve appartenere a una delle cartelle interne al processo.  
Per crearne una e necessario cliccare la voce **Allegati** nella [barra degli strumenti](#barra-degli-strumenti).  
Da li si aprono le impostazioni generali del modello relative agli allegati. Con il tasto destro sulla lista delle cartelle e possibile crearne una nuova, che sara poi disponibile tra i percorsi degli allegati di un'attivita.

Sotto i Filtri, è possibile gestire la **_Dimensione Massima in KB_** (Dim. Massima kb), tramite un input numerico.
Il numero immesso sarà il tetto massimo per la dimensione di un file.  

Nella parte bassa troviamo invece il gruppo relativo ai **_Tipi di file_**_ consentiti.  
Tramite una serie di checkbox è possibile definire le estensioni dei file che possono essere accettati.  
La casella di testo finale permette di specificare ulteriori estensioni in caso ce ne fosse bisogno. 

> **Tali estensioni vanno separate dalla virgola e devono includere il punto**
>

**Esempio di altre estensioni**

```
.cad,.php,.bat
```

> **⚡ Nota: **
>
> in BPM gli allegati sono organizzati in "cartelle" logiche, anche se fisicamente sono salvati nello stesso spazio.

##### Operazioni

![Configurazione delle operazioni](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/operazioni-config.png)

Nel contesto di un processo BPM, le operazioni rappresentano **attività automatiche** (come esecuzione di query SQL, invio di mail, chiamate a web service, ecc.) che possono essere inserite nel workflow esattamente come un task manuale.  
Le operazioni configurabili sono raccolte nella [sezione dedicata](#operazioni-2).

Invece di utilizzare un oggetto per ciascuna operazione come di norma, il sistema consente anche di associare direttamente le operazioni già disponibili nel BPM a momenti di vita specifici dell'oggett, tramite l'entrata **_Operazioni_** del menu contestuale.

Questo comporta diversi vantaggi:

- **Leggibilità**: permette di evitare di appesantire il disegno del flusso con dettagli tecnici di integrazione o automazione, che restano contestualizzati dentro l'oggetto.
- **Centralizzazione**: gestione delle logiche tecniche all'interno di punti strategici, senza sporcare il disegno principale del workflow.
- **Modularità**: ogni oggetto può avere comportamenti automatici senza bisogno di ulteriori nodi nel processo.

Quest'entrata apre una schermata di configurazione dove, in base all'oggetto su cui lo si apre, sarà possibile configurare l'operazione da svolgere in momenti differenti. 
Per assegnare un'operazione basta trascinarla (drag & drop) dalla colonna **_Operazioni disponibili_** a quella del momento in cui si desidera svolgerla (1).  
Le operazioni assegnate vengono poi svolte in ordine *Top to Bottom*.

1. Il titolo della colonna è il momento in cui verrà svolta l'operazione.

I momenti di vita dell'oggetto a cui si possono agganciare le operazioni sono:

1.	**Attivazione**
    - Quando l'oggetto diventa disponibile per l’utente, subito dopo il completamento dei task precedenti.
    > Tipico uso: inviare notifiche agli utenti o ad altri sistemi.

2.	**Inizio**
    - Opzione esclusiva dell'oggetto Attività.
    - Scatta solo se il task ha attiva la proprietà 'Rileva inizio'.
    - Parte quando l’utente inizia effettivamente l'attività dalla sua todo list.
    - In caso contrario, questo evento non viene lanciato.

3.	**In Esecuzione**
    - Scatta subito prima del completamento del task.
    - Dopo il click su "COMPLETATO" da parte dell'utente, ma prima delle formule di validazione.

4.	**Esecuzione Terminata**
    - Scatta dopo il completamento definitivo del task e dopo il superamento delle validazioni.
    - L’effetto è simile a un normale avanzamento nel flusso, ma senza dover disegnare ulteriori task.
    - La differenza con il precedente è sottile, ma in questo caso siamo sicuri che il flusso abbia già superato le formule di validazione senza bloccarsi.

##### Pianificazione e Scadenze

Questa finestra permette di configurare i parametri temporali dell'attività, come: i dettagli di _pianificazione_, le _scadenza_ e le _priorità_.   
È fondamentale per una gestione efficace delle scadenze e per il corretto funzionamento delle automazioni del processo.  
È diviso in 3 schede principali:

###### Pianificazione e Scadenze

![Configurazione della pianificazione](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/pianificazione-1.png)

Permette di impostare:
- **Durata prevista**: il numero di giorni previsti per completare il task. 
- **Scadenza**: Definisce il termine massimo entro cui il task deve essere completato, calcolato in giorni a partire dalla data di inizio.  

Presenta inoltre 3 checkbox per la gestione della pianificazione:

- **Da confermare**: se abilitato, indica che la pianificazione deve essere approvata manualmente.
- **Rileva inizio**: se selezionato, il sistema attiva la rilevazione della data inizio effettivo da parte dell’utente, ossia quando inizia l'attività dalla sua todo list. _Necessaria_ se si vuole assegnare un'operazione all'evento di _Inizio task_.
- **Utilizza calendari**: se abilitato, il calcolo della durata e delle scadenze considera solo i giorni lavorativi definiti nel calendario aziendale (esclude weekend, festività, ecc.). 

###### Dati Attività
Consente di associare variabili a campi specifici relativi ai dati aggiornati/effettivi/pianificati di un'attività.  
I campi configurabili si dividono in 3 gruppi e sono:

1. _Date **Aggiornate** Attività_: 
    * Data _inizio_ aggiornata: permette di collegare una variabile alla data di inizio _aggiornata_ dell'attività nel calendario.
    * Data _fine_ aggiornata: permette di associare una variabile alla data di fine _aggiornata_ dell'attività nel calendario.
    * _Durata_ aggiornata: permette di collegare una variabile che rappresenta la stima della durata _aggiornata_ dell'attività (in giorni).

2. _Date **Effettive** Attività_ 
    * Data _inizio_ effettiva: permette di collegare una variabile alla data di inizio _effettiva_ dell'attività nel calendario.
    * Data _fine_ effettiva: permette di associare una variabile alla data di fine _effettiva_ dell'attività nel calendario.
    * _Durata_ effettiva: permette di collegare una variabile che rappresenta la stima della durata _effettiva_ dell'attività in giorni.

3. _Date **Previste** Attività_
    * Data _inizio_ prevista/pianificata: permette di collegare una variabile alla data di inizio _pianificata_ dell'attività nel calendario.
    * Data _fine_ prevista/pianificata: permette di associare una variabile alla data di fine _pianificata_ dell'attività nel calendario.
    * _Durata_ prevista/pianificata: permette di collegare una variabile che rappresenta la stima della durata _pianificata_ dell'attività in giorni.

###### Dati Aggiuntivi

![Dati aggiuntivi della pianificazione](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/pianificazione-2.png)

Qui possiamo mappare le variabili di processo a 3 campi:

* **_Scadenza_** dell'attività: associa la scadenza calcolata a una variabile del processo per poterla usare altrove (es. notifiche).

* **_Priorità_** dell'attività: associa una variabile di processo alla priorità del task. Possiamo mappare valori specifici con la funzione Mappatura valori.
> **Attenzione**
>
> Se non configuri correttamente questa mappatura, il task potrebbe risultare senza priorità e comportarsi in modo anomalo nelle liste.

* **_Colore_** dell'attività: definisce dinamicamente il colore con cui il task verrà visualizzato nella todo list, in base a una variabile del processo.

##### Formula di validazione

La **_Formula di validazione_** è una formula che determina se è possibile continuare o meno con la task successiva del processo.
Cliccando su questa entrata, verrà aperto il popup per la scrittura della formula.  
Le formule di validazione degli elementi del canvas sono in una relazione **AND** con le altre formule definibili dalla barra degli strumenti della pagina delle variabili.

##### Escalation

![Configurazione dell'escalation](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/escalation.png)

**_Escalation/Timeout_** e una voce del menu contestuale esclusiva dell'oggetto [Attivita](#attivita-1).

Quando un task supera il tempo previsto (scadenza o durata massima), è necessario definire come il processo deve reagire.

La data di trigger del timeout/escalation può essere configurata in due modi:

- Data di **scadenza** + N giorni: scatta dopo un certo numero di giorni dalla scadenza prevista.
- Data di **attivazione** + N giorni: alternativa utile quando vuoi gestire il timeout a partire dall'inizio dell'attività e non dalla scadenza.

I giorni possono essere impostati come giorni lavorativi o qualsiasi tramite l'apposita spunta.

Nella finestra di configurazione è possibile definire il comportamento automatico del sistema in questi casi.

Quando il task supera il limite impostato, sono 3 le azioni sul task stesso che si possono configurare:

-  **Non variare** l'attività: lascia il task aperto, senza fare nulla.

-  **Riassegnare** l'attività: sposta il task su un altro utente o gruppo cedendo ad altri utenti la possibilità di mandare avanti il processo (es. scalando il problema ai livelli superiori).

-  **Terminare** l'attività: termina automaticamente il task come annullato.

###### Attivare flusso alternativo

All'attivazione del trigger dell'escalation/timeout è poi possibile anche reindirizzare il processo su un nuovo percorso.   
Alcuni esempi concreti tipici sono: invio di notifiche/promemoria, assegnazione di nuovi task a chi deve gestire l'eccezione...

Per configurare il **flusso alternativo** è necessario creare un _link 'speciale'_ a partire da un punto specifico del task, indicato dal simbolo:

![Icona dell'escalation](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/menu/escalation-icon.png)

questo collegamento indicherà al processo la strada alternativa da percorrere in caso si verifichi l'escalation/timeout.

> **⚡ Nota operativa**
>
> Dal punto di vista tecnico non cambia nulla scegliere Timeout o Escalation, il sistema reagisce allo stesso modo anche se l'icona è diversa nei due casi.  
> La distinzione serve solo per dare un'indicazione "semantica" su cosa si sta gestendo:
>
> - Timeout → il task semplicemente è scaduto.
> - Escalation → serve l'intervento di livelli superiori o alternative di processo.

##### Configurazione

L'entrata _Configurazione_ è totalmente differente per ogni oggetto e viene approfondita nelle sezioni relative ai singoli elementi.

##### Eliminazione

Tramite questa funzione è possibile **cancellare** l'oggetto selezionato dal canvas.  
In automatico vengono cancellati anche tutti i _collegamenti_ che hanno l'oggetto come punto di partenza o di arrivo.  

Si può anche utilizzare direttamente il tasto <kbd>canc</kbd> da tastiera.

##### Extra: Oggetti tipo Link

Utilizzando il menu contestuale su oggetti di tipo [Link](#link) si possono vedere altre opzioni specifiche per questo elemento:

 - _Percorso per abilitazione_
 - _Condizioni di abilitazione_
 - _Imposta variabili_
 - _Tipo linea_
 - _Elimina collegamento_

Gli scopi di queste voci sono spiegati nella pagina dedicata ai [Link](#link).

### Puntatore


Cliccando sopra alla relativa icona:

![Icona del puntatore](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/pointer-icon.png)

le funzionalità del mouse verranno riportate a quelle standard: 

- **click** per il tasto sinistro 
- [**menu contestuale**](#menu-contestuale) per il tasto destro.  

Non essendo trascinabile nel canvas e, quindi, **non essendo un elemento**, non possiede attributi.

## Elementi


Il pannello **Designer Tools**, a sinistra del canvas, raccoglie gli oggetti disponibili per costruire un modello di processo. La barra di ricerca filtra gli oggetti mantenendoli nelle rispettive sezioni.

#### Attivita

- [Attivita](#attivita-1): lavoro assegnato a uno o piu utenti.
- [Sottoprocesso](#sottoprocesso): flusso secondario contenuto nel modello.
- [Stato](#stato): punto significativo nell'evoluzione dell'istanza di processo.
- [Link](#link): collegamento e regola di avanzamento tra elementi.
- [Puntatore](#puntatore): comando di selezione; non e un elemento del canvas.

#### Altre categorie

- [Eventi](#eventi): avvio, attesa e conclusione del flusso.
- [Gateway e percorsi](#gateway-e-percorsi): diramazione e sincronizzazione dei percorsi.
- [Operazioni](#operazioni-2): azioni automatiche eseguite dal modello.
- **Processi collegati**: avvio di un altro processo e ritorno al chiamante; da documentare.
- [Elementi grafici](#elementi-grafici): gruppi, swim lane, immagini, testi, memo e marker.

Le proprieta comuni agli oggetti sono descritte nel [pannello attributi](#pannello-attributi) e nel [menu contestuale](#menu-contestuale). Le pagine dei singoli oggetti documentano soltanto proprieta, vincoli e comportamenti specifici.

### Attivita

#### Attività (Task)

![Elemento Attivita](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/task.png)

Un'attività rappresenta un'**unità operativa da eseguire** all'interno di un processo.  
Ogni task, prima o poi, finisce nella **todo list** di una o più persone a cui è assegnata, diventando così visibile e gestibile nel flusso di lavoro.

##### Utilizzo
 - Definisce le **azioni** da eseguire all'interno di un flusso di lavoro.
 - Permette agli **utenti** di **interagire con il processo**: eseguendo azioni, assegnando valori alle variabili tramire i relativi campi o anche semplicemente permettendogli di visualizzare dati significativi.

##### Caratteristiche principali

###### Utenti e responsabili
Ogni attività può essere **assegnata** a uno o più **utenti** o **gruppi**.  
È possibile definire queste logiche tramite un'entrata del menu contestuale o del pannello degli attributi dell'oggetto.  
Questa finestra di configurazione, comune anche ad altri oggetti, e descritta in [Utenti e responsabili](#utenti-e-responsabili).   
> In contesti meno formalizzati, è possibile semplificare questa logica: ad esempio, il primo utente che visualizza il task può prenderlo in carico ed eseguirlo direttamente, senza passaggi intermedi o ruoli formali.

###### Variabili associate al task
Ogni task è associato a un insieme di **variabili**, ovvero dati o informazioni necessari per la sua corretta esecuzione.  
Queste possono essere:

- **In lettura**: informazioni che l’esecutore deve conoscere.
- **In scrittura**: dati che devono essere compilati o aggiornati durante il completamento dell’attività.

Quando una variabile viene **associata ad un task**:

- Alcune proprietà della variabile (descrizione, obbligatorietà, posizione, formule di validazione, ecc.) possono essere **personalizzate localmente**, cioè solo per quel task, tramite il relativo pannello degli attributi.
- Le modifiche NON influenzano la definizione della variabile a livello di processo.

Questo meccanismo consente di **riutilizzare** le stesse variabili in task diversi con configurazioni diverse.

Esempi pratici:

- Una variabile "Note" può essere obbligatoria in un task ma facoltativa in un altro.  
- Una variabile "Importo" può avere diverse formule di validazione in base al task.

> ****Attenzione****
>
> Una variabile deve già esistere nel processo per poter essere associata al task. Se manca, va prima creata a livello di processo/documento.

###### Importazione di variabili
Per semplificare la configurazione, esistono degli strumenti per importare intere pagine/gruppi di variabili contemporaneamente.  
Ovviamente non è possibile importare variabili che non siano già presenti a livello di processo.

L'importazione può avvenire tramite due voci della barra degli strumenti:

- **Importa variabili** per importare variabili dal magazzino, già definite a livello di processo.
- **Importa/Esporta**, che contiene le voci per importare variabili da un file locale, descritte nella [barra degli strumenti dell'Editor delle variabili](#barra-degli-strumenti-2).

> **Ricorda**
>
> L'importazione di una pagina è particolarmente utile quando esiste una struttura standard di dati da raccogliere, riducendo il rischio di errori manuali e velocizzando l'implementazione dei task.

##### Menu contestuale

Nel menu relativo all'oggetto **Attività**, accessibile tramite tasto destro, sono presenti una serie di funzioni che permettono di configurarne il funzionamento del task stesso. 

Per questo elemento sono disponibili le funzioni standard descritte nel [menu contestuale](#menu-contestuale).  
Inoltre però troviamo alcune voci **esclusive** dell'oggetto _Attività_:

- **Inizio**: un evento dell'attivita al quale si puo assegnare un'operazione; scatta solo se e attiva l'opzione _Rileva inizio_ in [Pianificazione e scadenze](#pianificazione-e-scadenze).

- **Escalation**: questa voce e descritta nella sezione [Escalation](#escalation-1).

### Sottoprocesso


![Elemento Sottoprocesso](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/subprocess-img.png)

I **sottoprocessi** sono un tipo particolare di task, rappresentati anche graficamente in modo diverso, che funzionano come **contenitori** di processi secondari.  

##### Utilizzo

- Aumentare la **leggibilità** e la **pulizia** grafica di processi complessi, isolando parti ripetitive o di dettaglio.
- **Riutilizzare logiche** che devono essere eseguite più volte in base a condizioni dinamiche.

##### Pannello di configurazione e tipologie di sottoprocesso

![Configurazione del sottoprocesso](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/subprocess-config.png)

Ci sono due modalità operative principali, in base alla configurazione scelta anche il relativo menu varia leggermente.  
I parametri che si possono impostare sono:

##### Sottoprocesso Ricorrente
Quando serve **eseguire lo stesso sottoprocesso più volte, su dati diversi**.  
In pratica, il sottoprocesso "gira" su ogni riga di una tabella di variabili.  
La configurazione di un sottoprocesso ricorrente include:

###### Modalità di esecuzione

**Parallelo**
Tutte le istanze vengono avviate nello stesso momento subito.

**Sequenziale**
Ogni istanza parte solo dopo che la precedente è completata.

###### Gruppo
In questo campo è possibile specificare il gruppo di variabili su cui il sottoprocesso deve lavorare, le quali sono raggruppate sostanzialmente in una tabella.

###### Ordinamento
Quest'opzione, *esclusiva* di un processo ricorrente *sequenziale*, permette di specificare l'ordine secondo il quale le variabili del gruppo scelto vengono elaborate dal sottoprocesso (sarebbe come ordinare la tabella prima di fornirla al sottoprocesso).

###### Condizione
Permette di definire una formula logica che stabilisca se eseguire o meno una determinata istanza del sottoprocesso.
Se la condizione è falsa, le variabili della relativa riga vengono ignorate.

###### Formula testo
Permette di definire una formula per la generazione del nome di ciascuna istanza del sottoprocesso, così che nella Todo list gli utenti capiscano a quale "riga" fa riferimento ogni task.

###### Durata prevista
Se il sottoprocesso non è ancora esploso, ossia non sono ancora generate tutte le istanze, il BPM usa questa stima della durata "complessiva" come riferimento di *pianificazione*.

##### Sottoprocesso Singolo
Si tratta di un **processo "figlio" isolato** dal flusso principale.  
Serve **solo per** questioni di **organizzazione e leggibilità**: la logica è definita dentro il sottoprocesso e viene eseguita una sola volta.  
Si può vedere come una "scatola nera" che puoi aprire per guardare il dettaglio tecnico.

Per questa tipologia di sottoprocesso è possibile definire se esso sia:

- Fisso
- _Customizzabile_: nel caso in cui avessimo un sottoprocesso vuoto nel quale verranno inserite attività custom. In questo caso è possibile anche configurare la _durata prevista_, analogalmente a quanto visto prima. 

### Stato


![Elemento Stato](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/state.png)

Lo **Stato** è un'entità astratta all'interno del processo BPM che rappresenta un **punto significativo** nell’evoluzione del flusso, ma **non costituisce un'attività eseguibile (task)**. Si tratta di una **milestone logica** che fotografa la condizione globale del processo in un determinato momento.

Ogni processo definisce autonomamente i propri stati in funzione del dominio applicativo. Esempi comuni includono:

- `INSERITO`
- `IN APPROVAZIONE`
- `APPROVATO`
- `CONCLUSO`
- ...

##### Utilizzo

- Serve come **indicatore del progresso** del processo.
- Può essere inserito all'interno del workflow di processo in modo da **attivarsi automaticamente** al completamento dei task ad esso precedenti, permettendo di **monitorare, filtrare o classificare** l’avanzamento dei processi nel sistema.

##### Caratteristiche principali

- Lo **stato** non ha una logica esecutiva propria ma viene raggiunto a seguito dell’esecuzione di uno o più task o transizioni definite nel flusso.
- Gli stati sono **esclusivi**: in un determinato momento, un processo può trovarsi in **uno e un solo stato**.
- La transizione da uno stato a un altro può essere **automatica** (guidata dalla logica del workflow) o **manuale** in base ad un'attivazione forzata da un utente owner del processo.
- Nel [pannello degli attributi](#pannello-attributi) sono presenti voci specifiche per l'oggetto **Stato**.

##### Menu contestuale

Nel menu relativo all'oggetto **Stato**, accessibile tramite tasto destro, sono presenti una serie di funzioni che permettono di configurarne diversi aspetti.  
Per questo elemento sono disponibili le funzioni standard descritte nel [menu contestuale](#menu-contestuale).

L'unica cosa particolare dell'oggetto _State_ è che le _Operazioni_ si possono agganciare solo all'evento di '**attivazione**' dello stato ovvero: il momento in cui stato è stato raggiunto dal workflow oppure quando questo è stato attivato manualmente dall'utente.


### Link


Il **_Link_** è un collegamento tra un elemento e un altro.  

Una volta selezionato dal Designer Tools, passando il cursore sopra un elemento, appariranno dei cerchi gialli. Selezionando un cerchio e tenendo premuto il tasto sinistro, inizierà il tracciamento del link.  

Mentre si sta tracciando, passando il cursore su un elemento differente dal primo, è possibile collegarlo ad uno dei punti del destinatario.

![Creazione di un link](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/link-anim.gif)

Fatto ciò, i due elementi saranno collegati: spostandoli all'interno del canvas, il link rimarrà ancorato ad essi. 

> **Note sul Routing**
>
> Durante la creazione dei link:
>
>   - I **punti di ancoraggio** sono visibili come **puntini gialli** sugli oggetti.  
>   - Durante il **drag-and-drop**, una linea **verde** indica che il collegamento è valido; una **rossa** segnala che non è permesso.

##### Funzione del Link

Nel disegno di un processo BPM, i **link** rappresentano i collegamenti logici tra task, stati, operazioni o altri elementi del processo. Un link collega il **termine** di un'attività con l'**inizio** della successiva. Sono fondamentali per determinare il flusso operativo e includono sia **componenti funzionali** che **componenti grafiche**.

Cliccando sul collegamento con il tasto destro del mouse, si aprirà il menù contestuale contenente una lista di proprietà e parametri per configurarlo e personalizzarlo:

![Menu del link](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/link-dropdown-screenshot.png)

###### Nome collegamento
Permette di assegnare un'etichetta testuale al link, utile per identificare percorsi alternativi o indicare il significato logico del collegamento. Questo nome viene visualizzato nel canvas vicino alla linea e non modifica la logica del processo.

###### Percorso per Pianificazione
Se spuntato, il processo, al suo inizio, riterrà il collegamento come percorso default per determinare le attività future.

###### Condizione abilitazione
Definisce una condizione, espressa tramite formula, che deve essere vera affinche il link venga percorso. E una forma compatta per gestire flussi condizionati, alternativa all'uso dei [Gateway](#gateway-e-percorsi).  
Quando è presente una condizione, compare un piccolo **rombo** grafico all'inizio del link.
Se da un elemento sono collegati piu **Link** con uscite diverse, vengono trattati come [percorsi liberi](#percorsi-liberi-inclusive-e-complex). 

![Link condizionato](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/activities/link-cond.png)

###### Imposta variabili
Consente di impostare valori su variabili nel momento in cui il processo percorre quel link. È uno dei diversi modi per iniettare logica personalizzata nel flusso, alternativo all’uso di operazioni nei task o stati.

###### Tipo di Linea
La parte grafica del link può essere personalizzata per migliorare la leggibilità del disegno del processo. 
Le tipologie disponibili sono:

- **Linea diretta**  
  Segmento lineare semplice, senza deviazioni.

- **Linea ortogonale automatica**  
  Percorso generato automaticamente composto solo da segmenti orizzontali e verticali.

- **Linea ortogonale manuale**  
  Come la precedente, ma con controllo manuale del routing. L’utente definisce i punti intermedi.

- **Linea poligonale**  
  Percorso libero composto da segmenti arbitrari, da configurare manualmente.

> 💡 La modalità più utilizzata in fase iniziale è quella **ortogonale automatica**, eventualmente modificata successivamente in manuale per una migliore pulizia grafica.

###### Elimina collegamento
Permette di eliminare il collegamento selezionato, in alernativa si può cancellare anche premendo il tasto <kbd>canc</kbd> da tastiera.

##### Regole di connessione
- Ogni punto può essere condiviso da più link contemporaneamente.
- Tuttavia, **non può essere usato sia come punto di partenza che di arrivo** (un punto utilizzato per un link in uscita non può essere usato per un link in entrata, e viceversa).
- Alcuni oggetti (es. **gateway**) supportano più ingressi o più uscite secondo logiche specifiche.
- Le [operazioni](#operazioni-2) accettano un solo input e un solo output.

##### Superamento dei limiti di routing
In situazioni dove le regole limitano la costruzione desiderata, è possibile utilizzare una **attività con parametro `skip`** come elemento intermedio per aggirare i vincoli.

### Eventi


Gli eventi rappresentano punti di avvio, attesa o conclusione del flusso. Gli eventi che avviano un modello possono richiedere variabili, allegati e operazioni secondo la propria configurazione.

![Gli eventi nella palette del Designer](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/palette-eventi.png){ width=160 }

Gli eventi sono di due tipi:

- **nativi**: Start, Start a tempo, Attesa, Fine, Termina processo;
- **legati a un connettore**: Start su evento, che avvia il processo quando un connettore rileva qualcosa fuori da BPM.

##### Start

**Start** è il punto di inizio di un flusso avviato dall'esterno del motore: da un utente, dai menu di BPM, oppure da un'applicazione con le [API standard](#createnewprocess). Un modello può contenere più Start; in questo caso, all'avvio viene richiesto quale utilizzare.

Lo Start può configurare variabili e allegati da richiedere, utenti e responsabili, e operazioni eseguite durante o al termine dell'esecuzione.

##### Start su evento

**Start su evento** (icona con il triangolo) avvia un'istanza di processo senza che nessuno la richieda: è il motore di BPM a mettersi **in ascolto** e ad avviare il processo quando si verifica l'evento.

L'evento è fornito da un [connettore](#connettori). Nella configurazione dello Start su evento si sceglie il connettore e l'evento, poi si collegano i parametri:

- i **parametri di ingresso** dicono cosa ascoltare e come: per esempio quale cartella monitorare, o quale casella di posta e cosa fare della mail dopo averla letta;
- i **parametri di uscita** vengono scritti nelle variabili del processo appena avviato: per esempio nome, percorso e dimensione del file arrivato, oppure mittente, oggetto, testo e allegati della mail.

Le attività successive del processo lavorano poi su questi dati: allegare il file, leggerne il contenuto, smistarlo.

Esempi: [IncomingFile](#file-system) avvia un processo per ogni file che arriva in una cartella; [IncomingMail](#mail) per ogni mail che arriva in una casella.

L'ascolto degli eventi si attiva, si disattiva e si controlla da una finestra dedicata del menu di configurazione.

##### Start a tempo

**Start a tempo** avvia periodicamente un'istanza di processo. La configurazione definisce descrizione, frequenza giornaliera, settimanale o mensile e orario di avvio.

##### Attesa

**Attesa** sospende l'avanzamento fino al momento configurato. È possibile indicare un numero di giorni, un giorno della settimana o del mese e un orario.

##### Fine e Termina processo

**Fine** conclude il percorso corrente. **Termina processo** conclude anche gli altri rami paralleli e i sottoprocessi ancora attivi.

### Gateway e percorsi


I gateway instradano l'istanza di processo su percorsi differenti o sincronizzano ramificazioni precedenti.

##### Percorsi alternativi (exclusive)

Questo gateway seleziona un solo percorso. Ogni uscita puo avere una condizione configurata tramite formula e una delle uscite puo essere indicata come predefinita.

![Configurazione di un gateway](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/gateway-condizioni.gif)

Se piu condizioni risultano vere, viene percorso il primo percorso applicabile. Questo comportamento deve essere verificato sul prodotto corrente.

##### Percorsi paralleli (parallel)

Questo gateway attiva tutte le ramificazioni in uscita. Le uscite non hanno condizioni perché devono essere percorse tutte.

##### Percorsi liberi (inclusive) e Complex

Questi gateway possono attivare piu uscite quando le rispettive condizioni risultano vere. Le differenze precise tra i due oggetti devono essere documentate.

##### Sincronizza

**Sincronizza** riunisce ramificazioni precedenti. Il parametro **Number to pass** indica quanti percorsi devono raggiungere l'elemento prima che l'istanza possa proseguire.

### Operazioni


Le **operazioni** sono le attività automatiche di un processo: non richiedono un utente, le esegue il motore di BPM.

Un'operazione si usa in due modi:

- **nel flusso**, come oggetto del diagramma, collegata alle altre attività;
- **agganciata a un momento del ciclo di vita** di un altro oggetto, per esempio all'attivazione o alla conclusione di un'attività, o al raggiungimento di uno stato. Si configura nella finestra **Operazioni** dell'oggetto e non appesantisce il disegno.

##### Tipi di operazione

![Le operazioni nella palette del Designer](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/palette-operazioni.png){ width=200 }

| Scopo | Operazione | Cosa fa |
|---|---|---|
| Logica del processo | **Decision Table** | Valorizza variabili in base a una tabella di regole. |
| | **Imposta variabili** | Imposta o calcola variabili con uno script. |
| Comunicazione | **Invia email** | Invia una mail a partire da un modello. |
| Processi | **Aggiorna altro processo** | Modifica un'altra istanza di processo. |
| Dati esterni | **Carica dati** | Legge dati da una tabella o vista e li copia nelle variabili. Vedi [Carica Dati](#carica-dati). |
| | **Esegui sql** | Esegue un'istruzione SQL, tipicamente di scrittura. Vedi [Esegui SQL](#esegui-sql). |
| Estensioni | **Connettore attivo** | Esegue una funzione di un [connettore](#connettori). |

##### Connettore attivo

**Connettore attivo** è la porta d'ingresso a tutte le funzioni dei connettori di tipo *operazione*. Nella sua configurazione si sceglie il connettore e la funzione da eseguire, per esempio Web API del connettore Web Service o SaveAttachmentToFileSystem del connettore File System. BPM presenta allora i parametri della funzione, da valorizzare con valori fissi o da collegare alle variabili del processo, in ingresso e in uscita.

Le funzioni disponibili dipendono dai connettori installati e attivi: integrazione con altri sistemi, gestione di PDF e fogli di calcolo, funzioni del documentale, intelligenza artificiale.

##### Nomi interni

Ogni oggetto del diagramma ha un nome interno, assegnato alla creazione, che compare per esempio nelle risposte delle [API standard](#getprocess). Il prefisso indica il tipo di oggetto:

| Oggetto | Nome interno |
|---|---|
| Connettore attivo | `ActiveConnector1`, `ActiveConnector2`, … |
| Imposta variabili | `SetVar1`, … |
| Invia email | `SendEmail1`, … |
| Start su evento | `EventConnector1`, … |

### Elementi grafici


Gli elementi grafici organizzano e documentano il disegno senza rappresentare necessariamente un'attivita eseguibile.

##### Gruppo e Swim lane

**Gruppo** raccoglie elementi e puo associare utenti al contenitore. **Swim lane** suddivide il disegno in corsie, ciascuna con i propri utenti associati.

![Utenti differenti](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/utenti-differenti.gif)

Se un'attivita interna ha utenti diversi da quelli del contenitore, prevalgono gli utenti assegnati direttamente all'attivita.

##### Immagine, Casella di testo e Memo

**Immagine** inserisce un elemento visivo statico nel canvas. **Casella di testo** aggiunge testo libero. **Memo** aggiunge una nota e puo essere collegato a un'attivita.

##### Marker

**Marker** collega pagine diverse del disegno. E utile quando il modello viene suddiviso in pagine, per esempio per facilitarne la stampa.

# Documenti

## Classi documentali

Una **classe documentale** configura un tipo di documento: variabili, azioni, autorizzazioni e interazioni con i processi.

Il **Designer di classe documentale** ha la stessa struttura del Designer di processo e condivide strumenti come l'[Editor delle variabili](#editor-delle-variabili). Gli oggetti disponibili e le regole applicate cambiano in funzione dello scopo documentale.

### Accedere alle classi documentali

La voce **Classi documentali** del menu principale apre l'elenco delle classi, organizzate per gruppo. Una barra di ricerca consente di filtrare l'elenco; da qui si puo aprire una classe esistente oppure crearne una nuova.

### Scopo della sezione

L’obiettivo principale del **Designer di classe documentale** è fornire all’utente un’interfaccia chiara e completa per:
- Creare nuove classi documentali partendo da zero  
- Modificare strutture già esistenti  
- Gestire campi e proprietà dei documenti  
- Definire le relazioni tra le diverse classi documentali o con i modelli di processo  

Questa sezione è quindi essenziale per costruire la base dati su cui i processi BPM possono operare, garantendo **coerenza, tracciabilità e integrità delle informazioni**.

### Elementi principali

All’interno del **Designer di classe documentale**, l’interfaccia si compone generalmente di tre aree operative principali:

1. **Elenco classi documentali**  
   Nella parte sinistra dello schermo è presente la lista di tutte le classi create o disponibili nel sistema.  
   Da qui è possibile selezionare una classe esistente o crearne una nuova tramite l’apposito pulsante **“Nuova classe documentale”**.

2. **Editor di struttura**  
   Al centro della schermata si trova l’area dedicata alla definizione dei campi.  
   È possibile aggiungere nuovi campi, modificarne le proprietà o impostare regole specifiche di validazione e comportamento.

3. **Proprietà e configurazioni avanzate**  
   Nella parte destra si trovano le impostazioni aggiuntive, come le relazioni con altri oggetti, i permessi, le opzioni di visualizzazione e le regole di comportamento nei processi.

### Tipologie di campi

Ogni classe documentale può contenere diversi tipi di campo, ciascuno pensato per gestire un tipo di informazione specifica.  
Alcuni esempi comuni includono:
- **Campo testo:** per l’inserimento di descrizioni o note  
- **Campo numerico:** per quantità, importi o valori misurabili  
- **Campo data/ora:** per registrare eventi temporali  
- **Campo elenco (dropdown):** per selezioni predefinite  
- **Campo relazione:** per collegare la classe ad altre entità o processi  

Nei capitoli successivi verranno approfondite le impostazioni di ciascun tipo di campo, con esempi pratici e consigli di configurazione.

### Relazioni e integrazioni

Il Designer consente anche di **stabilire relazioni tra classi documentali**, permettendo così di collegare i dati e creare strutture più complesse.  
Le relazioni possono essere:
- **Uno-a-uno:** un documento collegato a un solo record di un’altra classe  
- **Uno-a-molti:** un documento che contiene o fa riferimento a più elementi correlati  
- **Molti-a-molti:** una relazione bidirezionale tra più record di diverse classi  

Queste relazioni sono utili per la creazione di **flussi documentali dinamici**, che possono essere gestiti e richiamati all’interno dei modelli di processo.

### Buone pratiche

Per garantire la massima efficienza nella gestione delle classi documentali, si consiglia di:
- Mantenere una **struttura coerente** dei nomi dei campi e delle classi  
- Documentare chiaramente lo scopo di ciascun campo  
- Evitare la duplicazione di informazioni già presenti in altre classi  
- Utilizzare i campi relazione per collegare dati condivisi tra processi  

Queste accortezze semplificano la manutenzione del sistema e migliorano la leggibilità dei modelli nel tempo.

### Approfondimenti

I capitoli successivi entreranno nel dettaglio di ciascun aspetto del **Designer di classe documentale**, illustrando con esempi pratici:
- La creazione di una nuova classe  
- La configurazione avanzata dei campi  
- La gestione delle relazioni e dei permessi  
- L’integrazione con i modelli di processo  

> **Suggerimento**
>
> Se stai iniziando a costruire i tuoi primi modelli di processo, ti consigliamo di creare prima le classi documentali fondamentali.  
> In questo modo potrai associare i dati strutturati fin dall’inizio, evitando modifiche successive ai flussi.

# Integrazione


BPM non lavora mai da solo. Nella quasi totalità delle installazioni legge almeno le anagrafiche dal gestionale, e spesso scambia dati in entrambe le direzioni con ERP, CRM, sistemi di produzione e servizi web.

Questa sezione risponde alle domande di chi deve collegare BPM ai sistemi dell'azienda: *come leggo i dati del mio ERP? come ci scrivo? come avvio un processo quando nel gestionale succede qualcosa? come chiamo un servizio esterno quando un'attività viene approvata?*

### Le modalità di integrazione

| Esigenza | Strumento |
|---|---|
| Proporre nei campi i dati del gestionale (clienti, fornitori, articoli…) | [Dati esterni nelle variabili](#dati-esterni-nelle-variabili) |
| Leggere dati esterni durante il processo e copiarli nelle variabili | [Carica Dati](#carica-dati) |
| Scrivere sul database di un altro sistema, o eseguire query e stored procedure | [Esegui SQL](#esegui-sql) |
| Chiamare un servizio web (REST) di un altro sistema | [Web Service](#web-service) |
| Avviare un processo quando arriva un file in una cartella o una mail | [File System](#file-system), [Mail](#mail) |
| Salvare allegati e documenti su file system | [File System](#file-system) |
| Far pilotare BPM da un'applicazione esterna | [API standard](#api-standard) |
| Far avviare o avanzare processi da un sistema che lavora solo sul database | [Coda delle chiamate](#coda-delle-chiamate) |

Tutte le modalità che accedono a un database usano le [connessioni esterne](#connessioni-esterne), configurate una volta sola.

### Gli strumenti: operazioni, eventi e connettori

Nel Designer, l'integrazione passa da due famiglie di oggetti.

<div class="grid" markdown>

![Operazioni](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/palette-operazioni.png){ width=200 }

![Eventi](/sessions/rcw-01jyvzbcmvlvs3mtrrenxxmz/mnt/bpm-docs/docs/assets/modelli-di-processo/designer/palette-eventi.png){ width=160 }

</div>

Le **[operazioni](#operazioni-2)** sono le attività automatiche del processo: si inseriscono nel flusso oppure si agganciano a un momento del ciclo di vita di un'attività. Alcune servono alla logica del processo (Decision Table, Imposta variabili, Invia email, Aggiorna altro processo); per l'integrazione contano soprattutto:

- **Carica dati** ed **Esegui sql**, operazioni native per leggere e scrivere su database;
- **Connettore attivo**, che esegue una funzione di un connettore: chiamare un servizio web, salvare un file, e molto altro.

Gli **[eventi](#eventi)** avviano, sospendono o concludono il flusso. Per l'integrazione conta **Start su evento**: il processo non viene avviato da un utente o da un'applicazione, ma dal motore di BPM stesso, in ascolto, quando si verifica l'evento di un connettore (l'arrivo di un file, di una mail).

I **[connettori](#connettori)** sono i moduli che forniscono queste funzioni: le loro operazioni si usano tramite Connettore attivo, i loro eventi tramite Start su evento.

### Due scenari tipici

#### Integrare BPM con l'ERP

Un processo di approvazione degli ordini d'acquisto:

1. **Le anagrafiche restano nell'ERP.** Il campo *Fornitore* propone i fornitori leggendoli dal database dell'ERP ([dati esterni nelle variabili](#dati-esterni-nelle-variabili)): nessuna copia dei dati in BPM.
2. **L'ERP avvia il processo.** Quando un ordine viene inserito, un trigger nell'ERP accoda l'avvio con la [coda delle chiamate](#coda-delle-chiamate), passando solo l'ID dell'ordine (convenzione *EXTERNAL ID*). Se l'ERP può fare chiamate HTTP, può usare direttamente le [API standard](#createnewprocess).
3. **BPM recupera i dati.** All'avvio, un'operazione [Carica Dati](#carica-dati) legge dall'ERP fornitore, importo e righe dell'ordine e valorizza le variabili.
4. **BPM scrive l'esito.** Alla fine dell'approvazione, un'operazione [Esegui SQL](#esegui-sql) aggiorna lo stato dell'ordine nell'ERP, oppure lo fa una chiamata alle API dell'ERP con il connettore [Web Service](#web-service).

#### Chiamare un servizio esterno quando un'offerta viene approvata

Un processo di approvazione delle offerte deve creare l'opportunità nel CRM (per esempio Salesforce) quando l'offerta viene approvata:

1. Dopo l'attività di approvazione, sul ramo *approvata*, si inserisce un'operazione del connettore [Web Service](#web-service), oppure la si aggancia alla conclusione dell'attività.
2. L'operazione chiama l'API del CRM con i dati dell'offerta presi dalle variabili del processo.
3. La risposta del CRM, per esempio l'ID dell'opportunità creata, viene scritta in una variabile e resta nello storico del processo.

Per chiamate che richiedono logica (autenticazione a più passaggi, trasformazione dei dati, più chiamate in sequenza) si usa la variante **Web API [Script]**, che descrive la chiamata con uno script.

## Connessioni esterne


Percorso: **Configurazione > Configurazione > Connessioni esterne**.

Una connessione esterna descrive come raggiungere il database di un altro sistema: server, database, credenziali. Si configura una volta sola, con un nome, e si riusa ovunque serva:

- nei [dati esterni delle variabili](#dati-esterni-nelle-variabili) e nelle griglie dati;
- nell'operazione [Carica Dati](#carica-dati);
- nell'operazione [Esegui SQL](#esegui-sql).

Sono supportati SQL Server e le fonti dati raggiungibili via **ODBC**.

#### Buone pratiche

- **Una connessione per sistema e per ambiente**, con un nome chiaro (per esempio `ERP A1`, `ERP B`): quando il processo passa da un ambiente di prova a quello reale, si cambia la connessione e non i modelli.
- **Evita le viste "ponte"** create nel database di BPM che puntano, a loro volta, al database esterno: funzionano, ma si rompono quando si sposta l'installazione su un altro ambiente. Una connessione esterna è sempre preferibile.
- **ODBC** funziona, ma con alcuni sistemi legacy può dare problemi: in quei casi un servizio web o un connettore dedicato sono spesso la scelta migliore.
- Usa per la connessione un utente del database con i **soli diritti necessari**: lettura per le anagrafiche, scrittura solo dove BPM deve davvero scrivere.

#### Configurazione dei connettori

I [connettori](#connettori) non usano le connessioni esterne: hanno una propria configurazione, in **Configurazione > Connettori**. Lì si attiva il connettore, si aggiungono le aziende e, per ciascuna, si compilano i parametri richiesti (indirizzi di servizi web, credenziali, database).

## Dati esterni nelle variabili


Una variabile può essere collegata a una **fonte dati**: invece del testo libero, l'utente sceglie un valore da una tabella, e la scelta può valorizzare automaticamente altre variabili. È il modo più semplice per usare in BPM le anagrafiche di un altro sistema senza copiarle.

Per esempio, scegliendo il codice fornitore, BPM compila da solo la ragione sociale, la partita IVA e le condizioni di pagamento lette dall'ERP.

#### Fonti dati

| Fonte | Quando usarla |
|---|---|
| **Tabella o vista esterna** | I dati stanno nel database di un altro sistema. Richiede una [connessione esterna](#connessioni-esterne). |
| **Tabella locale** | I dati sono gestiti in BPM, in una tabella personalizzata (prefisso `P_`) o in una vista del database di BPM. |
| **Tabella di un connettore** | Il connettore espone i dati di un sistema come se fossero una tabella (per esempio i connettori per SAM). |
| **Servizio web (REST)** | I dati arrivano da una chiamata a un'API. Possibilità più limitata rispetto alle tabelle. |
| **Variabili del processo** | I valori si scelgono tra le righe di un gruppo dello stesso processo (per esempio il preventivo vincente tra quelli inseriti). |

#### Come si configura

La configurazione avviene nella scheda della variabile, con la stessa finestra usata dall'operazione [Carica Dati](#carica-dati):

1. si sceglie la fonte (connessione e tabella, oppure la query);
2. si indica la **colonna chiave**, collegata alla variabile che si sta configurando;
3. si collegano, se serve, **altre colonne** ad altre variabili, che si valorizzano con la scelta;
4. si impostano le opzioni di ricerca: campi su cui cercare, filtri, prefiltro sul valore già inserito, caricamento dei dati solo dopo una ricerca per le tabelle molto grandi.

#### Griglia dati

La **griglia dati** è un tipo di variabile che mostra in sola lettura una tabella esterna o locale: per esempio tutti gli ordini aperti del cliente del processo. Si configura con la stessa finestra, scegliendo le colonne da mostrare e, se serve, rinominandone le intestazioni.

Non serve a inserire dati, per quello ci sono i gruppi: è una finestra di consultazione sempre aggiornata.

## Operazioni


### Carica Dati


**Carica Dati** è un'operazione nativa di BPM che legge dati da una tabella o vista e li copia nelle variabili del processo o del documento.

Si usa tipicamente all'**inizio** di un processo: l'utente, o il sistema che avvia il processo, fornisce solo un codice, e l'operazione recupera il resto. Per esempio, dall'ID di un ordine legge fornitore, data e importo; dal codice cliente legge ragione sociale e agente.

##### Come si configura

L'operazione usa la stessa finestra delle [fonti dati delle variabili](#dati-esterni-nelle-variabili):

1. si sceglie la fonte: tabella o vista tramite una [connessione esterna](#connessioni-esterne), tabella locale o tabella di un connettore;
2. si indica la condizione di ricerca, legando la colonna chiave alla variabile che contiene il valore da cercare;
3. si collegano le colonne da leggere alle variabili da valorizzare.

L'operazione si inserisce nel flusso oppure si aggancia a un momento del ciclo di vita di un'attività, per esempio all'attivazione.

##### Carica Dati o Esegui SQL?

| | Carica Dati | Esegui SQL |
|---|---|---|
| Configurazione | Guidata: tabella, chiave, colonne | Un'istruzione SQL scritta a mano |
| Adatta per | Leggere un record a partire da una chiave | Scritture, query complesse (join, aggregazioni), stored procedure |
| Errori | Pochi: la finestra conosce tabelle e colonne | Dipendono dalla correttezza della query |

Per le letture semplici preferisci Carica Dati; passa a [Esegui SQL](#esegui-sql) quando serve di più.

### Esegui SQL


**Esegui SQL** è un'operazione nativa di BPM che esegue un'istruzione SQL su una [connessione esterna](#connessioni-esterne). Si usa soprattutto per **scrivere** su un altro sistema, ma può eseguire qualunque istruzione: `UPDATE`, `INSERT`, query con join, stored procedure.

Caso tipico: al termine dell'approvazione, scrivere nell'ERP che l'ordine è stato approvato, da chi e quando.

##### Parametri

I parametri dell'istruzione, indicati con `@`, si collegano alle variabili del processo:

- **parametri di ingresso**: il valore viene preso dalla variabile;
- **parametri di uscita**: il valore restituito dall'istruzione viene scritto nella variabile.

```sql
UPDATE ordini
SET stato = 'APPROVATO', approvato_da = @utente, data_approvazione = @data
WHERE id_ordine = @idOrdine
```

Qui `@utente`, `@data` e `@idOrdine` sono parametri di ingresso collegati alle variabili del processo.

##### Quando usarla

- Il sistema esterno accetta scritture dirette sul suo database, oppure espone stored procedure pensate per l'integrazione.
- Non esiste un servizio web o un connettore dedicato per quella scrittura.

Se il sistema esterno espone API, preferisci chiamarle con il connettore [Web Service](#web-service): le API applicano le regole del sistema, una scrittura diretta sul database no.

> **Errori nelle operazioni**
>
> Se l'istruzione non è corretta, l'operazione fallisce, e con lei l'azione che l'ha eseguita: per esempio l'avvio del processo, anche quando arriva dalle [API standard](#api-standard) o dalla [coda delle chiamate](#coda-delle-chiamate). Prova sempre le istruzioni prima di pubblicare il modello.

## Connettori


Un **connettore** è un modulo che aggiunge a BPM funzioni pronte all'uso. Un connettore non è un oggetto del Designer: le sue funzioni si usano attraverso tre "porte", ciascuna con il proprio oggetto.

| Tipo di funzione | Si usa tramite | Cosa succede | Esempi |
|---|---|---|---|
| **Operazione** | l'operazione [Connettore attivo](#connettore-attivo) | Il motore esegue la funzione quando il flusso la raggiunge, o nel momento del ciclo di vita a cui è agganciata | Web API, SaveAttachmentToFileSystem |
| **Evento** | l'evento di avvio [Start su evento](#start-su-evento) | Il motore resta in ascolto e avvia un processo quando si verifica l'evento | IncomingFile, IncomingMail |
| **Azione client** | un pulsante nell'interfaccia di un processo o di un documento | La funzione viene eseguita quando l'utente preme il pulsante | MergePDFs [Client] |

In tutti i casi, nella configurazione dell'oggetto si sceglie il connettore e la funzione; BPM presenta i **parametri** della funzione, da valorizzare con valori fissi o da collegare alle variabili: in **ingresso** per dire alla funzione cosa fare, in **uscita** per scriverne i risultati nelle variabili.

#### Configurazione

Percorso: **Configurazione > Connettori**.

Qui si attiva il connettore e, se richiede una configurazione (indirizzi, credenziali, chiavi), si aggiungono le aziende e si compilano i parametri per ciascuna.

#### Connettori per l'integrazione

| Connettore | Funzioni |
|---|---|
| [File System](#file-system) | Evento all'arrivo di un file in una cartella; salvataggio di file, allegati e report su file system |
| [Mail](#mail) | Evento all'arrivo di una mail; estrazione dei dati da file `.eml` e `.msg` |
| [Web Service](#web-service) | Chiamata a un'API REST, configurata o descritta da uno script |

Altri connettori riguardano la gestione dei documenti, l'intelligenza artificiale o sistemi specifici, e sono descritti nelle rispettive sezioni.

> **Nomi e descrizioni**
>
> Nelle tabelle di riferimento dei connettori, i nomi di funzioni e parametri sono quelli usati in BPM. Le descrizioni riportano il testo del connettore, talvolta in inglese.

### File System


Il connettore **File System** (`FileSystemConnector`) collega BPM alle cartelle del file system:

- l'evento **IncomingFile**, usato con uno [Start su evento](#start-su-evento), avvia un processo per ogni file che arriva in una cartella;
- l'operazione **SaveAttachmentToFileSystem**, usata con un [Connettore attivo](#connettore-attivo), salva su file system un file, un allegato, un report o un contenuto base64.

##### Usi tipici

- **Acquisizione di documenti da cartella**: uno scanner o un altro sistema deposita i file in una cartella condivisa. BPM è in ascolto sulla cartella indicata in `SourceFilePath` e avvia un processo per ogni file. I parametri di uscita dell'evento (nome, estensione, date, dimensione, percorso completo) finiscono nelle variabili del processo fin dall'avvio, e le attività successive li usano per allegare il file, leggerne il contenuto, smistarlo.
- **Consegna di file a un altro sistema**: al termine di un processo, BPM salva il documento approvato o un report in una cartella da cui l'altro sistema lo preleva.

> **Permessi sulle cartelle**
>
> Le cartelle vengono lette e scritte dal **servizio di BPM** sul server. L'account del servizio deve avere i permessi necessari sui percorsi configurati, compresi quelli di rete.

##### Riferimento
<!-- Generato da tools/genera-connettori.py dal manifesto FileSystemConnector versione 20260511. Non modificare a mano. -->

###### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [IncomingFile](#incomingfile) | evento | This event is raised for each file added to a configured folder |
| [SaveAttachmentToFileSystem](#saveattachmenttofilesystem) | operazione | Save a File, Report, Attachment or base64 to the FileSystem |

###### IncomingFile

*Evento.* This event is raised for each file added to a configured folder

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceFilePath` | ingresso | sì | Source path for files |
| `FileName` | uscita |  | Incoming file name |
| `Extension` | uscita |  | Incoming file extension |
| `CreationDate` | uscita |  | Incoming file creation date |
| `LastModifiedDate` | uscita |  | Incoming file last modified date |
| `FileSize` | uscita |  | Incoming file size |
| `Company` | uscita |  | — |
| `FullPath` | uscita |  | Incoming file FULL PATH |

###### SaveAttachmentToFileSystem

*Operazione.* Save a File, Report, Attachment or base64 to the FileSystem

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.FullName` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.Attachment.DeleteAfter` | ingresso |  | — |
| `Source.FilePath.DeleteAfter` | ingresso |  | — |
| `Dest.FilePath` | ingresso | sì | — |

### Mail


Il connettore **Mail** (`Mail Connector`) permette a BPM di ricevere e interpretare messaggi di posta:

- l'evento **IncomingMail**, usato con uno [Start su evento](#start-su-evento), avvia un processo per ogni mail che arriva in una cartella di una casella IMAP;
- l'operazione **ExtractMail**, usata con un [Connettore attivo](#connettore-attivo), estrae i dati da un file `.eml` o `.msg`, per esempio una mail allegata a un processo.

##### Usi tipici

- **Richieste via mail**: ogni mail arrivata a un indirizzo dedicato (ordini, reclami, fatture) avvia un processo. Mittente, oggetto, testo e data diventano variabili del processo; gli allegati vengono archiviati tra gli allegati del processo, anche filtrandoli per tipo (per esempio solo i PDF).
- **Gestione della casella**: dopo la ricezione, la mail può essere eliminata o spostata in un'altra cartella, così la casella resta ordinata.
- **Risposte collegate**: il parametro `ReferenceInstanceId` riconosce il riferimento a un'istanza BPM presente nella mail, utile per collegare la risposta al processo che l'ha generata.

Nei parametri di ingresso dell'evento si indicano la configurazione della casella da usare (`ConfigEmail`, definita a parte in BPM), la cartella da monitorare e cosa fare della mail dopo la lettura. I parametri di uscita (mittente, destinatari, oggetto, testo, data, allegati) finiscono nelle variabili del processo avviato.

##### Riferimento
<!-- Generato da tools/genera-connettori.py dal manifesto Mail Connector versione 20260902. Non modificare a mano. -->

###### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [IncomingMail](#incomingmail) | evento | Evento che si scatena con l'arrivo di una nuova mail |
| [ExtractMail](#extractmail) | operazione | Extract Mail data from .MSG or .EML files |

###### IncomingMail

*Evento.* Evento che si scatena con l'arrivo di una nuova mail

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `ConfigEmail` | ingresso | sì | Configurazione IMAP da utilizzare per la ricezione mail |
| `ConfigFolder` | ingresso | sì | Folder mail da monitorare |
| `MailAttachmentsGroup` | ingresso |  | Gruppo allegati in cui archiviare il file .EML della mail |
| `Destination.Attachment.Root` | ingresso |  | Root in cui inserire gli allegati alla mail |
| `Destination.Attachment.Folder` | ingresso |  | Folder in cui inserire gli allegati alla mail |
| `Destination.Attachment.FileName` | ingresso |  | Nome allegato da forzare (se lasciato vuoto rimane nome originale dell'allegato da mail) |
| `Destination.Attachment.Filter` | ingresso |  | Filtro per scegliere quali allegati mail prendere (es. *.pdf) |
| `AttachmentsGroup` | ingresso |  | Gruppo allegati in cui inserire gli allegati alla mail |
| `Action` | ingresso |  | Azione da implementare dopo la ricezione della mail (elimina, sposta..) |
| `MoveToMailFolder` | ingresso |  | Folder mail di destinazione per lo spostamento |
| `FromName` | uscita |  | Nome mittente |
| `FromAddress` | uscita |  | Indirizzo mittente |
| `Cc` | uscita |  | — |
| `Bcc` | uscita |  | — |
| `Subject` | uscita |  | Oggetto mail |
| `Text` | uscita |  | Testo mail (plain text) |
| `HtmlText` | uscita |  | Testo mail (html formatted text) |
| `ReferenceInstanceId` | uscita |  | Riferimento a istanza processo/documento BPM (BPM Ref) |
| `AttachmentsData` | uscita |  | — |
| `To` | uscita |  | — |
| `MessageId` | uscita |  | Identificatore univoco messaggio |
| `Date` | uscita |  | Data mail |

###### ExtractMail

*Operazione.* Extract Mail data from .MSG or .EML files

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso | sì | Gruppo allegati in cui trovare il file .EML oppure .MSG da elaborare |
| `Destination.Attachment.Group` | ingresso |  | Gruppo allegati in cui inserire gli allegati alla mail |
| `Destination.Attachment.Root` | ingresso |  | Root in cui inserire gli allegati alla mail |
| `Destination.Attachment.Folder` | ingresso |  | Folder in cui inserire gli allegati alla mail |
| `Destination.Attachment.FileName` | ingresso |  | Nome allegato da forzare (se lasciato vuoto rimane nome originale dell'allegato da mail) |
| `Destination.Attachment.Filter` | ingresso |  | Filtro per scegliere quali allegati mail prendere (es. *.pdf) |
| `FromName` | uscita |  | Nome mittente |
| `FromAddress` | uscita |  | Indirizzo mittente |
| `To` | uscita |  | — |
| `Cc` | uscita |  | — |
| `Bcc` | uscita |  | — |
| `Subject` | uscita |  | Oggetto mail |
| `Text` | uscita |  | Testo mail (plain text) |
| `HtmlText` | uscita |  | Testo mail (html formatted text) |
| `ReferenceInstanceId` | uscita |  | Riferimento a istanza processo/documento BPM (BPM Ref) |
| `MessageId` | uscita |  | Identificatore univoco messaggio |
| `Date` | uscita |  | Data messaggio |

### Web Service


Il connettore **Web Service** (`Web Service Connector`) permette a un processo di chiamare le API REST di un altro sistema: un CRM, un ERP, un servizio di terze parti.

Offre due operazioni:

- **Web API**: la chiamata si descrive con la sola configurazione: indirizzo, metodo HTTP e autenticazione. Il codice di stato della risposta viene scritto in una variabile.
- **Web API [Script]**: la chiamata si descrive con uno script in Visual Basic, con la stessa sintassi delle [formule](#formule-e-script). Serve quando la chiamata richiede logica: costruire il corpo della richiesta dalle variabili, interpretare la risposta, gestire autenticazioni a più passaggi o più chiamate in sequenza.

##### Usi tipici

- Creare o aggiornare un record in un CRM quando un'offerta viene approvata.
- Notificare a un altro sistema la conclusione di un processo.
- Leggere dati da un servizio esterno e scriverli nelle variabili.

L'operazione si inserisce nel flusso, per esempio sul ramo *approvata* dopo un gateway, oppure si aggancia alla conclusione di un'attività.

##### Riferimento
<!-- Generato da tools/genera-connettori.py dal manifesto Web Service Connector versione 20240605. Non modificare a mano. -->

###### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [Web API](#web-api) | operazione | Standard Web API call |
| [Web API [Script]](#web-api-script) | operazione | Custom script Web API call |

###### Web API

*Operazione.* Standard Web API call

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `URL` | ingresso | sì | Web Address |
| `Method` | ingresso | sì | HTTP Method |
| `Authorization` | ingresso |  | Authentication scheme |
| `Response Status` | uscita |  | Response Status Code |

###### Web API [Script]

*Operazione.* Custom script Web API call

Nessun parametro.

## API standard


Le API standard sono le API che BPM mette a disposizione dei sistemi esterni, all'indirizzo `/api/ext`. Permettono a un'applicazione esterna di pilotare BPM: avviare processi, farli avanzare, leggerne lo stato, consultare la To-Do List di un utente, caricare allegati e gestire i documenti delle classi documentali.

Sono l'interfaccia più completa per integrare BPM con un altro sistema, quando è **l'applicazione esterna** a prendere l'iniziativa.

#### Le stesse regole dell'utente

Una chiamata alle API standard esegue le stesse regole e gli stessi controlli dell'operazione corrispondente fatta da un utente in BPM. Avviare un processo tramite API significa quindi:

- eseguire formule, validazioni e controlli di obbligatorietà;
- eseguire gli script collegati all'avvio;
- verificare che l'utente indicato esista e abbia il diritto di avviare quel processo da quello start.

Se una regola non è soddisfatta, la chiamata fallisce con il messaggio di errore che l'utente avrebbe visto a video.

#### Indirizzo delle chiamate

Tutte le chiamate hanno la forma:

```text
https://<indirizzo-bpm>/api/ext/<NomeChiamata>
```

dove `<indirizzo-bpm>` è l'indirizzo dell'applicazione web di BPM, per esempio `https://bpm.azienda.it/BPM`.

L'indirizzo base delle API è configurato nei parametri di sistema, scheda **Engine/automatismi**, campo **url api**.

#### Formato delle richieste e delle risposte

- Le chiamate sono quasi tutte di tipo `POST`, con un oggetto JSON nel corpo della richiesta. Anche le chiamate di sola lettura, come GetProcess o GetTodolist, usano `POST`: i loro parametri sono oggetti complessi (filtri, elenchi, credenziali) che non si possono passare comodamente nell'indirizzo, come avverrebbe con una `GET`.
- Ogni richiesta contiene le credenziali di accesso: vedi [Autenticazione e utenti](#autenticazione-e-utenti).
- La maggior parte delle risposte contiene il campo `result` (`true` se l'operazione è riuscita) e il campo `message`, valorizzato con il messaggio di errore in caso di esito negativo. Fanno eccezione alcune chiamate sui documenti e sugli elenchi dei modelli, che segnalano gli errori con il codice HTTP: sono indicate nelle rispettive pagine.

```json
{
  "result": false,
  "message": "Messaggio di errore …"
}
```

##### Identificare un'istanza

Le chiamate che lavorano su un processo o un documento esistente accettano due modi alternativi per identificarlo:

- `instanceId`: l'identificativo univoco dell'istanza, restituito alla creazione;
- `model` + `documentName`: il nome del modello e il nome dell'istanza, univoco all'interno del modello (per esempio `APPROVAZIONE CONTRATTI` e `P004A.19.1`).

Basta valorizzare una delle due forme.

##### Variabili

Le variabili si passano nell'oggetto `variables` come coppie nome-valore, usando i nomi delle variabili del modello. I nomi non distinguono tra maiuscole e minuscole. Le variabili di gruppo (testata-dettaglio) si passano come array, con un elemento per ogni riga:

```json
"variables": {
  "Ragione Sociale": "Rossi S.p.A.",
  "Data Apertura": "2026-01-18T00:00:00",
  "Importo": 179.58,
  "Righe": [
    { "Codice": "P01", "Descrizione": "Descrizione P01" },
    { "Codice": "P02", "Descrizione": "Descrizione P02" }
  ]
}
```

Regole sui valori:

- **Numeri**: numero JSON oppure stringa convertibile.
- **Date**: stringa nel formato `yyyy-mm-dd` (con l'ora, `yyyy-mm-ddThh:mm:ss`).
- **Booleani**: `true` / `false`.
- **Testo esteso (Memo)**: stringa semplice; per il testo formattato si può passare un oggetto `{ "HTML": "<p>…</p>" }`. Nelle risposte le variabili Memo sono restituite come oggetto con `Text` e `HTML`.
- **Nomi sconosciuti**: una variabile che non esiste nel modello viene ignorata senza restituire errori; l'avviso viene scritto nel log del servizio **WkfApi**, il processo del server BPM che gestisce le chiamate. Se un valore sembra non arrivare, controlla i nomi delle variabili e il log di WkfApi.

Per sapere quali variabili richiede un'attività o uno start, usa [GetSchema](#getschema).

##### Campi generali

Oltre alle variabili definite nel modello, ogni processo e ogni documento ha dei **campi generali**, sempre presenti, che ne descrivono lo stato. Hanno il prefisso `fix_`: si possono leggere con [GetProcess](#getprocess) e [GetDocument](#getdocument) e si possono usare come filtri in [SearchDocuments](#searchdocuments).

| Campo | Etichetta in BPM | Contenuto |
|---|---|---|
| `fix_name` | Nome | Nome dell'istanza, univoco nel modello. |
| `fix_descrizione` | Descrizione | Descrizione dell'istanza. |
| `fix_text` | Testo | Testo descrittivo dell'istanza. |
| `fix_lifecycle` | Modello | Nome del modello di processo o della classe documentale. |
| `fix_version` | Versione | Versione del modello. |
| `fix_state` | Stato | Stato corrente. |
| `fix_active` | Attivo | Indica se l'istanza è ancora attiva. |
| `fix_activestep` | Task attivo | Attività attive in questo momento. |
| `fix_useractivestep` | Utente task attivo | Utenti assegnati alle attività attive. |
| `fix_owners` | Proprietari | Proprietari dell'istanza. |
| `fix_data` | Data creazione | Data di creazione. |
| `fix_utecreazione` | Utente creazione | Utente che ha creato l'istanza. |
| `fix_dataultimamodifica` | Data ultima modifica | Data dell'ultima modifica. |
| `fix_utemodifica` | Utente ultima modifica | Utente che ha eseguito l'ultima modifica. |
| `fix_tipoultimamodifica` | Tipo ultima modifica | Tipo dell'ultima modifica. |
| `fix_has_attachments` | Presenza allegati | Indica se l'istanza ha allegati. |

Solo per i documenti delle classi documentali:

| Campo | Etichetta in BPM | Contenuto |
|---|---|---|
| `fix_documentdate` | Data documento | Data del documento. |
| `fix_duedate` | Data scadenza | Data di scadenza del documento. |
| `fix_barcode` | Barcode | Codice a barre. |
| `fix_filename` | Nome file | Nome del file del documento. |
| `fix_currentversion` | Versione file | Versione corrente del file. |
| `fix_has_document` | Presenza documento | Indica se al documento è associato un file. |
| `fix_has_signedcopy` | Presenza copia firmata | Indica se è presente la copia firmata. |
| `fix_has_versions` | Presenza versioni | Indica se il documento ha più versioni. |

Anche i nomi dei campi generali non distinguono tra maiuscole e minuscole.

#### Le chiamate disponibili

| Area | Chiamate |
|---|---|
| [Processi](#processi-1) | CreateNewProcess, GetProcess, UpdateProcess, DeleteProcess, UploadAttachment, AddLink, ProcessModels, GetSchema |
| [Attività e To-Do List](#attivit\224-e-to-do-list) | GetTodolist, GetPageTodoList, ExecTask, UpdateTask |
| [Documenti e dossier](#documenti-e-dossier) | CreateNewDocument, CreateOrUpdateDocument, UpdateDocument, UpdateDocumentContent, GetDocument, SearchDocuments, DownloadDocument, DownloadDocumentJSON, DocumentVersions, DeleteDocument, DocumentSets, AddDocumentToDossier |
| [Utilità](#utilit\224) | GetUser, CreateOrUpdateUser, GetVersion |

#### Swagger e strumenti di prova

Ogni installazione espone la descrizione completa delle API in formato Swagger (OpenAPI 2.0) all'indirizzo:

```text
https://<indirizzo-bpm>/api/swagger/docs/v1
```

Lo Swagger elenca tutte le chiamate e i relativi parametri, ma non riporta la struttura dell'oggetto `authorization` né il significato dei campi: per questi fa fede questa documentazione.

##### Provare le chiamate

Per provare le chiamate senza scrivere codice è disponibile una collection per **Postman** con tutte le chiamate di questa sezione e un esempio di richiesta per ciascuna:

- [Collection BPM API standard](postman/bpm-api-standard.postman-collection.json){ download="bpm-api-standard.postman-collection.json" }
- [Ambiente BPM](postman/bpm.postman-environment.json){ download="bpm.postman-environment.json" }

Per iniziare:

1. In Postman, importa i due file con **Import**.
2. Seleziona l'ambiente **BPM** e compila le variabili: `bpmUrl` (indirizzo dell'applicazione web, per esempio `https://bpm.azienda.it/BPM`), `apiKey` (la [chiave API](#chiave-api)) e `userName`.
3. Adatta i nomi di modello, classe documentale, start e attività agli oggetti della tua installazione.

CreateNewProcess e CreateNewDocument salvano automaticamente nell'ambiente l'identificativo dell'istanza creata, che le chiamate successive usano subito.

La collection si importa anche in altri strumenti compatibili con il formato Postman, come Bruno.

### Autenticazione e utenti


Le API standard usano un sistema a **chiave API**: ogni applicazione esterna riceve una chiave generata in BPM e la invia a ogni chiamata, insieme all'indicazione dell'utente per conto del quale opera.

##### Chiave API

La chiave si genera in BPM dal percorso **Configurazione > Configurazione > Chiavi di accesso Web API**, con il comando **Crea nuovo token di autenticazione**. Vedi [Chiavi di accesso Web API](#chiavi-di-accesso-web-api).

- Genera una chiave distinta per ogni applicazione esterna, con una descrizione che la identifichi: così è possibile revocarla senza toccare le altre integrazioni.
- Un'applicazione in possesso di una chiave è autorizzata a eseguire **qualunque operazione per conto di qualunque utente**. La chiave va quindi custodita come una password: mai nel codice lato browser, mai in chiaro in documenti condivisi.
- Usa sempre connessioni HTTPS.

##### Utente per conto del quale si opera

Ogni chiamata indica anche un utente. BPM applica i controlli di quell'utente: se l'utente non ha il diritto di avviare un processo o di eseguire un'attività, la chiamata fallisce.

Esistono due modi, entrambi validi, per inviare chiave e utente.

###### Modalità semplice: `authenticationToken` e `userName`

Chiave e utente BPM si inseriscono direttamente nel corpo della richiesta:

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI"
}
```

È la modalità più diretta quando l'applicazione esterna conosce i nomi degli utenti BPM.

###### Modalità con utente esterno: oggetto `authorization`

Quando l'applicazione esterna ha i propri utenti, può identificarli con **il proprio nome utente** e lasciare che sia BPM a risalire all'utente BPM corrispondente. Chiave e utente si inseriscono nell'oggetto `authorization`:

```json
{
  "authorization": {
    "authenticationToken": "<chiave-api>",
    "<tipo>User": "<utente-esterno>",
    "<tipo>Company": "<azienda>"
  },
  "model": "APPROVAZIONE CONTRATTI"
}
```

- `authenticationToken` (oppure `apiKey`): la chiave API, come nella modalità semplice.
- `<tipo>User`: il nome utente nell'applicazione esterna. Il prefisso `<tipo>` indica di quale applicazione si tratta, per esempio `samUser` per un utente di tipo `sam`.
- `<tipo>Company`: l'azienda dell'utente esterno, solo quando l'applicazione esterna gestisce più aziende (per esempio `samPortalUser` e `samPortalCompany` per un utente di tipo `samPortal`).

Se nella richiesta è presente anche `userName`, fuori dall'oggetto `authorization`, prevale l'utente BPM indicato e l'alias non viene usato.

> **Lo Swagger non descrive questa struttura**
>
> Nello Swagger `authorization` compare come oggetto generico: i nomi delle proprietà sono quelli riportati in questa pagina.

###### Alias: il collegamento tra utente esterno e utente BPM

La corrispondenza tra utente esterno e utente BPM si configura nell'anagrafica degli utenti BPM, sezione **Alias**. Per ogni utente BPM si definiscono uno o più alias, ciascuno composto da:

- il **tipo** di utente esterno, cioè l'applicazione di provenienza (per esempio `sam`);
- il **nome utente** in quell'applicazione.

Quando una chiamata arriva con `samUser: "7"`, BPM cerca l'utente che ha un alias di tipo `sam` con nome `7` e opera per suo conto. Se la chiamata indica anche l'azienda (`samCompany`), la ricerca considera tipo, nome e azienda; senza azienda, basta la coppia tipo e nome. Se nessun alias corrisponde, la chiamata fallisce come per un utente inesistente.

Vedi [Utenti e gruppi](#utenti-e-gruppi-1).

La stessa struttura si usa anche in altri punti delle API per indicare un utente esterno, per esempio nel filtro `filterByUser` di [GetTodolist](#gettodolist) o negli utenti assegnati di [UpdateTask](#updatetask).

##### Verificare un utente

La chiamata [GetUser](#getuser) verifica che l'utente indicato esista e ne restituisce email e gruppi: è utile per controllare la configurazione di chiave e alias prima di usare le altre chiamate.

### Processi


Chiamate per avviare, leggere, modificare ed eliminare le istanze di processo, e per caricare allegati. Per le regole comuni (indirizzo, credenziali, identificazione dell'istanza, variabili) vedi [API standard](#api-standard).

##### CreateNewProcess

Avvia una nuova istanza di un modello di processo.

`POST /api/ext/CreateNewProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "startObject": "start1",
  "variables": {
    "Ragione Sociale": "Rossi S.p.A.",
    "Importo": 179.58
  }
}
```

| Campo | Descrizione |
|---|---|
| `model` | Nome del modello di processo da avviare. |
| `startObject` | Nome interno dello start da cui avviare il processo (per esempio `start1`). Un modello può avere più start. |
| `variables` | Valori delle variabili richieste all'avvio. |
| `attachments` | Elenco facoltativo di allegati da caricare all'avvio. Vedi sotto. |

###### Allegati all'avvio

Ogni elemento di `attachments` descrive un allegato:

| Campo | Descrizione |
|---|---|
| `fileName` | Nome del file. |
| `content` | Contenuto del file codificato in base64. |
| `root`, `folder` | Cartella allegati del processo in cui inserire il file. È una cartella virtuale di BPM, non una cartella del file system. |
| `group` | Gruppo di allegato, tra i valori previsti nelle tabelle di BPM. |
| `isEmail` | Se `true`, il file è un messaggio email: BPM ne estrae oggetto, mittente e le altre informazioni e le conserva per eventuali elaborazioni. |

Vengono eseguite formule, validazioni, controlli di obbligatorietà e script collegati all'avvio, e viene verificato che l'utente possa avviare il processo da quello start.

**Risposta**

```json
{
  "documentName": "P004A.19.1",
  "instanceId": "<id-istanza>",
  "documentDescription": "…",
  "isDuplicate": false,
  "result": true,
  "message": null
}
```

`documentName` è il nome dell'istanza creata, univoco all'interno del modello. Conserva `instanceId` o `documentName` per le chiamate successive.

Se il modello calcola un nome già esistente, la creazione fallisce: `isDuplicate` vale `true` e `duplicateDocumentName` contiene il nome dell'istanza esistente.

##### GetProcess

Restituisce lo stato di avanzamento di un'istanza e, a richiesta, le sue variabili.

`POST /api/ext/GetProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "documentName": "P004A.19.1",
  "includeVariables": ["*"],
  "includeGraph": true
}
```

`includeVariables` stabilisce quali variabili riportare nella risposta:

- `["*"]` oppure lista vuota: tutte le variabili;
- uno o più nomi: solo le variabili indicate.

Con `includeGraph: true` la risposta contiene anche l'immagine del diagramma, con i colori di avanzamento: la stessa che vede l'utente in BPM. Un'applicazione esterna può usarla per mostrare ai propri utenti a che punto è il flusso.

**Risposta**

```json
{
  "model": "RECLAMO",
  "documentName": "2/2026",
  "instanceId": "667cedef-4562-…",
  "state": "PRESO IN CARICO",
  "variables": {
    "ANNO": 2026.0,
    "DATA APERTURA": "2026-03-16T00:00:00+01:00",
    "CREA NC": false,
    "NOTE": { "HTML": "<p>Da valutare</p>", "Text": "Da valutare" },
    "ATTIVITA": [ { "DESCRIZIONE": "Verifica del lotto", "SCADENZA": "20/03/2026" } ],
    …
  },
  "activeTasks": [
    { "activity": "Activity5", "activityDescription": "ORDINE DI SOSTITUZIONE", "userName": "DIRTEC", … }
  ],
  "tasks": {
    "Activity1": { "taskDescription": "PRESA IN CARICO", "state": "Done", "executionCount": 2, … },
    "Activity5": { "taskDescription": "ORDINE DI SOSTITUZIONE", "state": "Active", … },
    …
  },
  "processState": { … },
  "links": [],
  "result": true,
  "message": ""
}
```

Come si leggono le variabili:

- **numeri**: sempre in formato decimale (`2026.0`);
- **date**: formato ISO con fuso orario (`2026-03-16T00:00:00+01:00`);
- **booleani**: `true` / `false`;
- **testo esteso (Memo)**: oggetto con `Text`, il testo semplice, e `HTML`, la versione formattata;
- **gruppi**: array con una riga per elemento.

Come si legge `tasks`: una voce per ogni oggetto del diagramma (attività, stati, gateway, operazioni), identificata dal nome interno.

- `state`: `None` (non ancora raggiunto), `Active` (in corso), `Done` (completato);
- `executionCount`: quante volte l'oggetto è stato eseguito;
- `assignedUsers`, `ccUsers`: assegnatari e utenti in copia;
- date e durate di pianificazione: prevista (`…Plan`), aggiornata (`…Upd`) ed effettiva (`…Actual`);
- `operations`: per le operazioni automatiche, se sono state eseguite, quando, da quale utente ed eventuale errore (`errorText`).

| Campo | Descrizione |
|---|---|
| `documentName`, `documentDescription`, `instanceId` | Identificazione dell'istanza. |
| `documentText` | Testo descrittivo dell'istanza. |
| `state` | Stato corrente del processo. |
| `variables` | Le variabili richieste. I gruppi sono restituiti come array di righe. Vedi anche i [campi generali](#campi-generali). |
| `activeTasks` | Le attività attive: nome interno (`activity`), descrizione, assegnatari in `userName` (separati da `;`) e in `assignedUsers`, con gli eventuali alias dell'applicazione esterna. |
| `links` | Le istanze collegate. |
| `tasks` | Lo stato di tutte le attività del processo, una voce per attività con il suo nome interno. |
| `processState` | Dettagli operativi sull'avanzamento generale del processo. |
| `graph` | Solo con `includeGraph`: immagine PNG del diagramma, codificata in base64. |

Viene sempre verificato che l'utente abbia il diritto di accedere ai dati richiesti.

##### UpdateProcess

Modifica le variabili di un'istanza esistente e, facoltativamente, ne forza lo stato.

`POST /api/ext/UpdateProcess`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "variables": { "Importo": 200.00 },
  "resetGroups": ["Righe"],
  "state": ""
}
```

| Campo | Descrizione |
|---|---|
| `variables` | Variabili da modificare. |
| `resetGroups` | Gruppi da svuotare prima di scrivere le nuove righe passate in `variables`. |
| `state` | Stato da impostare. Vuoto per non cambiare lo stato. |

Viene verificato che l'utente abbia il diritto di modificare le variabili e di cambiare stato. Per lo stato, il controllo dipende da come lo stato è raggiungibile: cambio di stato libero oppure secondo il flusso del processo.

##### DeleteProcess

Elimina un'istanza di processo, identificata da `instanceId` oppure da `model` + `documentName`.

`POST /api/ext/DeleteProcess`

L'eliminazione è completa: vengono rimossi l'istanza, le sue attività nella To-Do List, gli allegati e le variabili. Come per ogni chiamata, valgono i diritti dell'utente indicato: può eliminare un amministratore o un utente autorizzato a eliminare le istanze del modello.

Risposta: `result` e `message`.

##### UploadAttachment

Inserisce un allegato in un'istanza di processo, oppure aggiorna un allegato esistente.

`POST /api/ext/UploadAttachment`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "fileName": "Contratto 123.pdf",
  "fileDescription": "Contratto firmato",
  "root": "ALLEGATI",
  "path": "\\Documenti Amministrativi",
  "content": "<contenuto-in-base64>",
  …
}
```

La combinazione di `fileName`, `root`, `path` e `revision` identifica l'allegato: se esiste già viene aggiornato, altrimenti viene creato. In aggiornamento `content` può restare vuoto, per modificare solo descrizione, gruppo, tipo o variabili.

| Campo | Descrizione |
|---|---|
| `fileName`, `fileDescription` | Nome e descrizione registrati in BPM. |
| `root`, `path` | Percorso di archiviazione all'interno del processo. Valgono sia per gli allegati salvati su database sia per quelli su file system. |
| `group`, `type` | Gruppo e tipo di allegato, facoltativi, tra i valori previsti nelle tabelle di BPM. |
| `revision` | Revisione dell'allegato, se necessaria. |
| `state` | Vuoto: allegato attivo e modificabile. `A`: approvato, non più modificabile. `O`: obsoleto, non più modificabile. |
| `variables` | Variabili **dell'allegato**, non del processo. |
| `content` | Contenuto del file codificato in base64. |

In alternativa a `content`, il contenuto si può fornire con `sourceType` e `filePathSource` o `base64Source`: vedi [Documenti e dossier](#contenuto-del-documento).

##### AddLink

Collega due istanze di processo.

`POST /api/ext/AddLink`

Ciascuna delle due istanze si identifica con l'id oppure con modello e nome, in qualunque combinazione:

| Campo | Descrizione |
|---|---|
| `instanceId` oppure `model` + `documentName` | L'istanza di partenza. |
| `linkedInstanceId` oppure `linkedModel` + `linkedDocumentName` | L'istanza da collegare. |

L'utente deve essere amministratore oppure avere, sul modello dell'istanza di partenza, il diritto di aggiungere istanze collegate.

Risposta: `result` e `message`.

##### ProcessModels

Restituisce l'elenco dei modelli di processo configurati e attivi. Richiede solo le credenziali.

`POST /api/ext/ProcessModels`

**Risposta**

```json
[
  { "Name": "APPROVAZIONE CONTRATTI", "Description": "Approvazione dei contratti di vendita" },
  { "Name": "RICHIESTA INV", "Description": "Richiesta di autorizzazione investimento" }
]
```

La risposta è direttamente l'elenco, senza `result` e `message`. Se la chiave API non è valida, la chiamata restituisce il codice HTTP `401 Unauthorized`.

Per l'elenco delle classi documentali vedi [DocumentSets](#documentsets).

##### GetSchema

Restituisce la descrizione delle variabili richieste per avviare un processo o per eseguire un'attività. È utile per costruire dinamicamente la maschera di un'applicazione esterna.

Richiede solo la chiave API: la descrizione non dipende dall'utente.

`POST /api/ext/GetSchema`

```json
{
  "authenticationToken": "<chiave-api>",
  "modelName": "INTERVENTI PARCO AUTO",
  "activityName": "start1"
}
```

**Risposta**

```json
{
  "result": true,
  "model": "INTERVENTI PARCO AUTO",
  "activity": "start1",
  "properties": [
    { "propertyName": "TARGA MEZZO", "propertyType": "string", "variableType": "StringType", "required": true },
    { "propertyName": "RICHIEDENTE", "propertyType": "string", "variableType": "UserType", "hasDefault": true },
    {
      "propertyName": "INTERVENTI", "propertyType": "array",
      "subProperties": [
        { "propertyName": "PREZZO", "propertyType": "number", "variableType": "NumericType" },
        …
      ]
    },
    …
  ]
}
```

| Attributo | Descrizione |
|---|---|
| `propertyName` | Nome della variabile. |
| `propertyType` | Tipo JSON: `string`, `number`, `date`, `boolean`, `array`. |
| `variableType` | Tipo della variabile in BPM (per esempio `StringType`, `NumericType`, `UserType`, `ValueListType`). |
| `required` | La variabile è obbligatoria. |
| `readOnly` | La variabile è visualizzata ma non modificabile nell'attività: valorizzata in un passaggio precedente o calcolata. |
| `hasDefault` | Esiste una formula di default: se la variabile non viene passata, si usa il default. |
| `description` | Descrizione della variabile come appare nell'attività. |
| `availableValues` | Per le liste valori, i valori ammessi. |
| `subProperties` | Per i gruppi (`array`), le variabili del gruppo. |

### Attività e To-Do List


Chiamate per leggere la To-Do List di un utente, eseguire un'attività e modificarne assegnazione, priorità e date. Per le regole comuni vedi [API standard](#api-standard).

##### GetTodolist

Restituisce la To-Do List di un utente: le attività visibili o eseguibili, secondo i filtri indicati.

`POST /api/ext/GetTodolist`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "fromDate": "2026-01-01",
  "toDate": "2026-07-31",
  "filterByUser": "Commerciali",
  "filterByText": "",
  "filterByPriority": null,
  "includeCompleted": false,
  "includePlanned": false,
  "includeCC": false
}
```

| Campo | Descrizione |
|---|---|
| `fromDate`, `toDate` | Intervallo di date. Se omesse, nessun limite pratico: dal 1980 a dieci anni nel futuro. |
| `filterByUser` | Utente o gruppo di cui leggere le attività. Può essere anche un utente esterno, con la stessa struttura dell'[oggetto authorization](#modalit\224-con-utente-esterno-oggetto-authorization), per esempio `{ "samPortalUser": "14", "samPortalCompany": "A1" }`. Se vuoto, vedi sotto. |
| `filterByText` | Filtro testuale. |
| `filterByPriority` | Filtro per priorità. |
| `includeCompleted` | Include le attività completate. |
| `includePlanned` | Include le attività pianificate, non ancora attive. |
| `includeCC` | Include le attività in cui l'utente è in copia. |

Se `filterByUser` è vuoto, la risposta contiene le attività dell'utente indicato nella richiesta, quelle degli utenti di cui può vedere la To-Do List e quelle non ancora assegnate. Per un amministratore contiene le attività di tutti gli utenti.

Sono considerati solo i modelli attivi.

**Risposta**

```json
{
  "result": true,
  "message": null,
  "todoList": [
    {
      "activityName": "activity12",
      "activityDescription": "FIRMARE ORDINE",
      "instanceID": "<id-istanza>",
      "model": "APPROVAZIONE CONTRATTI",
      "documentName": "P004A.19.1",
      "assignedUsers": [ { "userName": "mrossi", "samUser": "7" } ],
      "state": "active",
      "priority": "high",
      "dueDate": null,
      "processHeaders": [ { "Cliente": "Rossi S.p.A." }, … ],
      "activityLink": "https://<indirizzo-bpm>/todolist?…",
      …
    },
    …
  ]
}
```

- `assignedUsers`: gli assegnatari, ciascuno espresso come utente BPM e, se configurato un alias, come utente dell'applicazione esterna.
- `isCC`: l'attività è in copia per l'utente.
- `state`: `active`, `completed` oppure `planned`.
- `priority`: `suspended`, `none`, `low` (priorità da 1 a 3), `medium` (da 4 a 7) oppure `high` (da 8 a 10).
- `processHeaders`: le intestazioni del processo, cioè l'estratto di variabili che BPM mostra nella To-Do List, come elenco di coppie nome-valore. Presente solo se le intestazioni sono configurate.
- `processHeadersTable`: le stesse intestazioni in forma tabellare, `header1` … `header10`, ciascuna con `name` e `value`.
- `activityLink`, `processLink`: collegamenti diretti all'attività e al processo nell'applicazione web, utili per aprire BPM da un'altra applicazione.

##### GetPageTodoList

Come [GetTodolist](#gettodolist), ma restituisce i risultati una pagina alla volta. Ai filtri si aggiungono `Page`, il numero di pagina a partire da `1`, e `Size`, il numero di attività per pagina.

`POST /api/ext/GetPageTodoList`

Oltre a `result`, `message` e `todoList`, la risposta contiene:

| Campo | Descrizione |
|---|---|
| `page`, `size` | Pagina e dimensione richieste. |
| `totalRecords` | Numero totale di attività che soddisfano i filtri. |
| `totalPages` | Numero totale di pagine. |

##### ExecTask

Esegue un'attività attiva, facendo avanzare il processo.

`POST /api/ext/ExecTask`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "APPROVAZIONE CONTRATTI",
  "documentName": "P004A.19.1",
  "activity": "activity4",
  "comments": "",
  "variables": {
    "Esito Approvazione": "APPROVATA"
  }
}
```

| Campo | Descrizione |
|---|---|
| `activity` | Nome **interno** dell'attività, per esempio `activity4`. Si legge nel Designer, nella proprietà **(NOME)** dell'attività: non è il testo visualizzato nel diagramma. |
| `variables` | Valori delle variabili richieste dall'attività. |
| `comments` | Commento all'esecuzione. |

BPM verifica che l'attività sia attiva e presente nella To-Do List dell'utente, e che l'utente abbia il diritto di eseguirla. Poi controlla validazioni e obbligatorietà delle variabili ed esegue gli script collegati all'esecuzione dell'attività. Le righe passate per le variabili di gruppo vengono aggiunte a quelle già presenti.

Errori tipici:

- l'attività indicata non è attiva;
- l'utente non è autorizzato a eseguire l'attività;
- il processo è aperto in modifica da un altro utente in quel momento: la chiamata va ripetuta più tardi;
- una validazione non è superata: `message` riporta il messaggio della validazione.

Risposta: `result` e `message`.

##### UpdateTask

Aggiorna i dati di un'attività: assegnatari, priorità, date e durate. Non esegue l'attività.

`POST /api/ext/UpdateTask`

Sono obbligatori solo l'istanza (`instanceId` oppure `model` + `documentName`) e `activityName`. Gli altri campi sono facoltativi: si valorizzano solo quelli da modificare.

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "instanceId": "<id-istanza>",
  "activityName": "Activity4",
  "assignedUser": { "samUser": "7" },
  "priority": 5,
  "dueDate": "2026-10-31"
}
```

| Campo | Descrizione |
|---|---|
| `assignedUser`, `ccUser`, `respUser` | Assegnatari, utenti in copia e responsabili. Ciascuno può essere un nome utente BPM, un utente esterno con la struttura degli [alias](#alias-il-collegamento-tra-utente-esterno-e-utente-bpm), oppure un elenco dei due. |
| `priority` | Da 1 a 10. `0`: nessuna modifica. Un valore negativo sospende l'attività. |
| `startDate` | Nuova data di inizio: imposta la data di inizio aggiornata e, se l'attività è già iniziata, anche quella effettiva. |
| `durationDays` | Nuova durata in giorni: equivale a `durationDaysUpdated`. |
| `plannedStartDate`, `updatedStartDate`, `actualStartDate` | Date di inizio pianificata, aggiornata ed effettiva. |
| `durationDaysPlanned`, `durationDaysUpdated` | Durate pianificata e aggiornata. |
| `dueDate` | Data di scadenza. |
| `ignoreCalendar` | Se `true`, l'attività ignora il calendario dei giorni lavorativi. |

Risposta: `result` e `message`.

Vincoli sull'assegnazione:

- se gli assegnatari dell'attività sono definiti da una variabile di processo, non si possono cambiare tramite API;
- se l'attività è assegnata a un gruppo, il nuovo assegnatario deve appartenere a quel gruppo.

### Documenti e dossier


Chiamate per creare, aggiornare, cercare e scaricare i documenti delle classi documentali, e per inserirli nei dossier. Per le regole comuni vedi [API standard](#api-standard).

##### Concetti

**Nome del documento.** Ogni documento ha un nome (`documentName`, in alcune chiamate `Name`) univoco all'interno della classe documentale. Non è il nome del file: è composto dalle variabili del documento, secondo le regole e gli script della classe documentale, e ne determina l'univocità.

**Dossier.** Un dossier raggruppa documenti di classi documentali diverse che hanno qualcosa in comune, per esempio tutti i documenti di una pratica o di un cliente. È un raggruppatore leggero: ha un identificativo, un nome, una descrizione e un eventuale contatto. L'inserimento dei documenti nei dossier si configura nella classe documentale.

**Parametri con l'iniziale maiuscola.** Alcune chiamate usano parametri con l'iniziale maiuscola (`InstanceId`, `Model`, `Name`): in questa pagina sono riportati così come appaiono nello Swagger.

**Errori.** Le chiamate SearchDocuments, DownloadDocument, DownloadDocumentJSON, DocumentVersions e DocumentSets non restituiscono `result` e `message`: segnalano gli errori con il codice HTTP (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`).

##### Contenuto del documento

Le chiamate che creano o aggiornano un documento ricevono il contenuto del file in una di due forme, indicata da `sourceType`:

| `sourceType` | Oggetto da valorizzare | Campi |
|---|---|---|
| `base64` | `base64Source` | `extension` (estensione del file), `content` (contenuto in base64) |
| `filePath` | `filePathSource` | `extension`, `filePath` (percorso del file), `deleteAfter` (elimina il file dopo l'acquisizione) |

```json
"sourceType": "base64",
"base64Source": { "extension": ".pdf", "content": "<contenuto-in-base64>" }
```

> **Percorsi di file**
>
> Con `filePath` è il **server BPM** a leggere il file, ed eventualmente a eliminarlo. Il percorso deve essere raggiungibile dal server e l'account del servizio BPM deve avere i permessi di lettura (e di scrittura, se si usa `deleteAfter`) su quella cartella.

###### Versioni e copia firmata

| Campo | Descrizione |
|---|---|
| `newVersion` | Modalità della nuova versione: `new_draft` se la versione caricata è una bozza da approvare, `new_active` se diventa subito la versione attiva del documento. |
| `newVersionNumber` | Numero della nuova versione, secondo le regole di numerazione che ci si dà. |
| `newVersionDescription` | Descrizione libera della versione. |
| `newVersionDate` | Data della versione, nel formato `yyyy-mm-dd`. |
| `signedCopy` | `true` se il file caricato è la **copia firmata** del documento: un file aggiuntivo conservato accanto all'originale, per le classi documentali che la prevedono. |

##### CreateNewDocument

Crea un nuovo documento in una classe documentale.

`POST /api/ext/CreateNewDocument`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "model": "FATTURE PASSIVE",
  "startObject": "start1",
  "variables": { "Fornitore": "Rossi S.p.A.", "Numero": "123", "Anno": "2026" },
  "sourceType": "base64",
  "base64Source": { "extension": ".pdf", "content": "<contenuto-in-base64>" }
}
```

| Campo | Descrizione |
|---|---|
| `model` | Classe documentale. |
| `startObject` | Start da cui creare il documento. |
| `variables` | Metadati del documento. |
| `attachments` | Allegati, come in [CreateNewProcess](#allegati-allavvio). |
| `sourceType`, `base64Source`, `filePathSource` | Il file: vedi [Contenuto del documento](#contenuto-del-documento). |
| `barcode` | Codice a barre associato al documento. |

Come per i processi, vengono eseguite formule, validazioni e script collegati alla creazione.

Risposta: `instanceId`, `documentName`, `documentDescription`, `result`, `message`.

Se esiste già un documento con lo stesso nome nella classe documentale, la creazione fallisce: `isDuplicate` vale `true` e `duplicateDocumentName` contiene il nome del documento esistente. Per aggiornarlo in questo caso, usa [CreateOrUpdateDocument](#createorupdatedocument).

##### CreateOrUpdateDocument

Crea il documento se non esiste, altrimenti aggiorna quello esistente con lo stesso nome. Accetta gli stessi parametri di [CreateNewDocument](#createnewdocument).

`POST /api/ext/CreateOrUpdateDocument`

In aggiornamento vengono modificati metadati e contenuto; se per la classe documentale è attiva la gestione delle versioni, il nuovo file diventa una nuova versione.

La risposta indica con `created` e `updated` quale delle due operazioni è stata eseguita.

È il comportamento dell'omonima operazione **CreateOrUpdateDocument** disponibile nei processi.

##### UpdateDocument

Aggiorna metadati, stato e, facoltativamente, contenuto di un documento esistente.

`POST /api/ext/UpdateDocument`

| Campo | Descrizione |
|---|---|
| `instanceId` oppure `model` + `documentName` | Il documento. |
| `variables` | Metadati da modificare. |
| `resetGroups` | Gruppi da svuotare prima di scrivere le nuove righe. |
| `state` | Stato da impostare. |
| `sourceType`, `base64Source`, `filePathSource` | Nuovo contenuto, facoltativo. |
| `newVersion…`, `signedCopy`, `barcode` | Vedi [Versioni e copia firmata](#versioni-e-copia-firmata). |

Risposta: `instanceId`, `documentName`, `documentDescription`, `result`, `message`.

##### UpdateDocumentContent

Sostituisce solo il file di un documento esistente, senza modificarne i metadati.

`POST /api/ext/UpdateDocumentContent`

Parametri: il documento (`instanceId` oppure `model` + `documentName`), il contenuto e, facoltativamente, i dati di versione e `signedCopy`.

##### GetDocument

Restituisce i dati di un documento. Funziona come [GetProcess](#getprocess).

`POST /api/ext/GetDocument`

| Campo | Descrizione |
|---|---|
| `InstanceId` oppure `Model` + `Name` | Il documento. |
| `IncludeVariables` | Metadati da includere: `["*"]` o lista vuota per tutti, oppure i nomi delle variabili. |

La risposta contiene gli stessi campi di GetProcess, compresi `tasks` e `processState`, tranne l'immagine del diagramma. In più:

| Campo | Descrizione |
|---|---|
| `documentDate` | Data del documento, se presente. |
| `documentDueDate` | Data di scadenza, se presente. |
| `documentBarcode` | Codice a barre, se presente. |
| `versions` | Le versioni del documento. |

##### SearchDocuments

Cerca documenti per metadati e campi generali.

`POST /api/ext/SearchDocuments`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "Models": ["FATTURE PASSIVE"],
  "Filters": [
    { "Name": "Fornitore", "Value": "Rossi S.p.A." },
    { "Name": "Anno", "ValueIn": ["2025", "2026"] }
  ]
}
```

| Campo | Descrizione |
|---|---|
| `Models` | Obbligatorio. Classi documentali in cui cercare: di solito una sola. Sono considerate solo quelle che l'utente è autorizzato a leggere. |
| `Filters` | Filtri facoltativi: `Name` (nome della variabile o di un [campo generale](#campi-generali), per esempio `fix_documentdate`), `Value` (valore singolo) oppure `ValueIn` (elenco di valori ammessi). |
| `dossierType` | Limita la ricerca ai documenti di un tipo di dossier. |

Con `Filters` vuoto la ricerca restituisce tutti i documenti della classe documentale visibili all'utente.

**Risposta**

La risposta è direttamente un elenco, con un elemento per ogni documento trovato. Ogni elemento contiene le variabili della classe documentale, i [campi generali](#campi-generali) e l'identificativo del documento. La struttura dipende quindi dalla classe documentale: per questo lo Swagger non la descrive.

```json
[
  {
    "CODCLI": "000001",
    "DATDOC": "2024-02-05T00:00:00",
    "TOTDOC": 244.0,
    …
    "FIX_NAME": "A1-1",
    "FIX_STATE": "INSERITO",
    "FIX_DOCUMENTDATE": "2024-02-05T00:00:00",
    "FIX_FILENAME": "COM_A1-1.pdf",
    "FIX_HAS_ATTACHMENTS": true,
    …
    "instanceid": "402f9fff-dcf0-4d57-baf1-3fd5dd747435"
  },
  …
]
```

Nella risposta i nomi dei campi generali sono in maiuscolo. `instanceid` è l'identificativo da usare nelle chiamate successive, per esempio [DownloadDocument](#downloaddocument).

##### DownloadDocument

Scarica il file di un documento.

`POST /api/ext/DownloadDocument`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "InstanceId": "<id-istanza>",
  "Version": 2
}
```

`Version` è facoltativo: permette di scaricare una versione precedente, se per la classe documentale è attivo il salvataggio delle versioni.

La risposta è direttamente il file, con il nome nell'intestazione `Content-Disposition`. L'utente deve avere il diritto di leggere i dati del documento.

##### DownloadDocumentJSON

Come [DownloadDocument](#downloaddocument), ma restituisce il file dentro un oggetto JSON:

`POST /api/ext/DownloadDocumentJSON`

| Campo | Descrizione |
|---|---|
| `FileName`, `Extension` | Nome ed estensione del file. |
| `FileData` | Contenuto del file in base64. |
| `Version`, `VersionDate`, `VersionUser` | Versione scaricata, data e utente che l'ha caricata. |

##### DocumentVersions

Restituisce l'elenco delle versioni di un documento (`InstanceId` oppure `Model` + `Name`). L'utente deve avere il diritto di leggere i dati del documento.

`POST /api/ext/DocumentVersions`

**Risposta**

```json
[
  { "Version": 1, "FileName": "Disegno1", "Extension": ".pdf", "Description": "Disegno PXX",
    "UploadDate": "2025-09-23T00:00:00", "Username": "ADMIN", "State": "ACTIVE" },
  { "Version": 2, "FileName": "Disegno2", "Extension": ".pdf", "Description": "Disegno PXX",
    "UploadDate": "2025-09-23T00:00:00", "Username": "ADMIN", "State": "HISTORY" }
]
```

| Campo | Descrizione |
|---|---|
| `Version` | Numero della versione, da usare in `Version` di [DownloadDocument](#downloaddocument). |
| `FileName`, `Extension` | Nome ed estensione del file della versione. |
| `Description` | Descrizione della versione. |
| `UploadDate`, `Username` | Data di caricamento e utente che l'ha caricata. |
| `State` | Stato della versione: `ACTIVE` per la versione attiva, `HISTORY` per le versioni precedenti, `DRAFT` per una bozza da approvare (caricata con `newVersion: "new_draft"`). |

##### DeleteDocument

Elimina un documento (`InstanceId` oppure `Model` + `Name`), con le sue versioni e i suoi dati. Valgono i diritti dell'utente indicato.

`POST /api/ext/DeleteDocument`

Risposta: `result` e `message`.

##### DocumentSets

Restituisce l'elenco delle classi documentali configurate e attive, con `Name` e `Description`. Richiede solo le credenziali. Stessa struttura di [ProcessModels](#processmodels).

`POST /api/ext/DocumentSets`

##### AddDocumentToDossier

Inserisce un documento in un dossier. Se il dossier non esiste, viene creato.

`POST /api/ext/AddDocumentToDossier`

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi",
  "InstanceId": "<id-istanza>",
  "Dossier": {
    "Type": "PRATICA",
    "ID": 0,
    "Name": "Pratica 2026/045",
    "Description": "Pratica cliente Rossi",
    "Contact": "",
    "Company": ""
  }
}
```

| Campo | Descrizione |
|---|---|
| `InstanceId` oppure `Model` + `DocumentName` | Il documento. |
| `Dossier.Type` | Obbligatorio. Tipo di dossier. |
| `Dossier.ID`, `Dossier.Name` | Identificano il dossier. |
| `Dossier.Description`, `Dossier.Contact`, `Dossier.Company` | Dati descrittivi facoltativi. |

Una volta nel dossier, il documento si trova sia dall'interfaccia sia con [SearchDocuments](#searchdocuments).

Risposta: `result` e `message`.

### Utilità


##### GetUser

Verifica che un utente esista e ne restituisce i dati principali. È utile per controllare chiave API e [alias](#alias-il-collegamento-tra-utente-esterno-e-utente-bpm) prima di usare le altre chiamate.

`POST /api/ext/GetUser` (disponibile anche in `GET`, con i parametri nella query string)

```json
{
  "authenticationToken": "<chiave-api>",
  "userName": "mrossi"
}
```

Oppure, con un utente esterno:

```json
{
  "authorization": {
    "authenticationToken": "<chiave-api>",
    "samUser": "7"
  }
}
```

**Risposta**

```json
{
  "result": true,
  "userName": "mrossi",
  "email": "mario.rossi@azienda.it",
  "isExternal": false,
  "groups": ["Amministrazione", "UTE"]
}
```

- `userName`: il nome dell'utente BPM, anche quando la richiesta indicava un utente esterno.
- `isExternal`: `true` per gli utenti di collaborazione esterna, per esempio i fornitori.
- `groups`: i gruppi a cui l'utente appartiene.

Se l'utente non esiste, `result` è `false` e `message` contiene l'errore.

##### CreateOrUpdateUser

Crea un utente BPM oppure aggiorna un utente esistente.

`POST /api/ext/CreateOrUpdateUser`

L'utente indicato in `userName` è quello che esegue l'operazione e deve avere il diritto di gestire utenti e autorizzazioni.

| Campo | Descrizione |
|---|---|
| `targetUserName` | Nome dell'utente da creare o aggiornare. |
| `password` | Password. |
| `email`, `description` | Email e descrizione. |
| `isExternal` | Utente di collaborazione esterna. |
| `passwordExpired` | Password scaduta: l'utente dovrà cambiarla al primo accesso. |
| `singleSignOn` | Accesso con autenticazione di dominio. |
| `systemUserName`, `domain` | Utente di sistema e dominio, per l'accesso con autenticazione di dominio. |
| `groups` | Gruppi a cui l'utente appartiene. |

Risposta: `result`, `message`, `userName` e `created` (`true` se l'utente è stato creato, `false` se aggiornato).

##### GetVersion

Restituisce la versione dell'applicazione. Disponibile in `GET` e in `POST`, senza parametri né chiave API: è utile per verificare che le API siano raggiungibili.

`GET /api/ext/GetVersion`

```json
{ "version": "2026.7.3" }
```

## Coda delle chiamate


La coda delle chiamate è una **porta d'ingresso alternativa** alle [API standard](#api-standard), pensata per i casi in cui il sistema esterno non può chiamare le API ma può scrivere sul database.

> **Un'alternativa, non un'altra API**
>
> La strada principale per integrare un'applicazione esterna è la chiamata diretta alle [API standard](#api-standard). La coda serve quando questa non è praticabile: software che lavorano solo sul database, trigger, stored procedure, situazioni in cui serve interagire con BPM rapidamente senza una programmazione più strutturata.

Invece di chiamare le API, il sistema esterno **inserisce una riga** nella tabella `ChiamateAPI` del database di BPM. Un servizio di BPM legge la coda, esegue la chiamata corrispondente e scrive l'esito nella stessa riga.

#### Come funziona

1. Il sistema esterno inserisce una riga in `ChiamateAPI` con il nome della chiamata e i parametri in JSON.
2. Il servizio di BPM, che controlla la coda ogni pochi secondi, prende in carico la riga ed esegue la chiamata.
3. L'esito viene scritto nella riga: risposta completa, esito sintetico ed eventuale messaggio di errore.
4. Il sistema esterno, se gli serve, rilegge l'esito qualche secondo dopo.

Le chiamate accodate seguono le stesse regole delle chiamate dirette: stesse [credenziali](#autenticazione-e-utenti), stessi parametri, stessi controlli.

#### La tabella `ChiamateAPI`

| Colonna | Chi la scrive | Contenuto |
|---|---|---|
| `Funzione` | Sistema esterno | Nome della chiamata, per esempio `CreateNewProcess` o `ExecTask`. |
| `Parametri` | Sistema esterno | Il corpo JSON della chiamata, credenziali comprese. |
| `Data` | Sistema esterno | Data e ora di inserimento. |
| `EseguitoInData` | BPM | Data e ora in cui BPM ha elaborato la riga. Vuota finché la richiesta è in coda. |
| `Response` | BPM | La risposta JSON della chiamata, con `result` e `message`. |
| `Risultato` | BPM | Esito sintetico: `OK` oppure `KO`. |
| `ErrorMessage` | BPM | In caso di `KO`, il messaggio di errore, ripreso da `message`. |

Inserimento diretto:

```sql
INSERT INTO ChiamateAPI (Funzione, Parametri, Data)
VALUES ('ExecTask',
        '{"authorization": {"authenticationToken": "<chiave-api>", "samUser": "2"},
          "model": "APPROVAZIONE ODA", "instanceId": "<id-istanza>", "activity": "Activity3"}',
        GETDATE())
```

#### Leggere l'esito

Una riga elaborata ha `EseguitoInData` valorizzata. Se `Risultato` è `KO`, `ErrorMessage` spiega il motivo. Può trattarsi di:

- **un controllo di BPM**: nome di processo già esistente, variabile obbligatoria mancante, validazione non superata, processo non trovato…;
- **un errore delle configurazioni eseguite dalla chiamata**, per esempio una query SQL errata in un'operazione collegata allo start del processo.

Esempi di righe elaborate (colonne principali):

| Funzione | Risultato | ErrorMessage |
|---|---|---|
| `ExecTask` | `OK` | |
| `CreateNewProcess` | `KO` | `Nome processo già esistente: "Sollecito Ordine ID 31"` |
| `UpdateProcess` | `KO` | `Process Not Found: 2024 - 2 - CONTROLLO FATTURE PASSIVE` |

Con la coda gli errori non tornano al chiamante nel momento dell'inserimento: se il sistema esterno deve reagire a un errore, deve rileggere la riga.

#### Chiamata diretta o coda?

| | Chiamata diretta | Coda delle chiamate |
|---|---|---|
| Come | Richiesta HTTP alle API standard | Inserimento di una riga in una tabella |
| Esito | Immediato, nella risposta | Asincrono: si legge nella riga dopo qualche secondo |
| Errori di validazione | Il chiamante li riceve subito | Vanno riletti in un secondo momento |
| Adatta quando | Il chiamante deve sapere subito se l'operazione è riuscita | Il sistema esterno scrive facilmente su database ma non gestisce chiamate HTTP, oppure non deve restare in attesa |

#### Attivazione

La coda si attiva nei parametri di sistema, scheda **Engine/automatismi**:

- **Attiva esecuzione chiamate api da tabella "chiamateapi"**: abilita il servizio che elabora la coda;
- **url api**: l'indirizzo delle API standard che il servizio chiama.

#### Stored procedure per l'inserimento

Per evitare di comporre il JSON a mano, sono disponibili stored procedure che ricevono pochi parametri, costruiscono il JSON e inseriscono la riga in coda.

##### BPM_CreateNewProcess

Accoda l'avvio di un processo.

```sql
EXEC BPM_CreateNewProcess
     @user = '2',
     @model = 'APPROVAZIONE ODA',
     @externalID = '1234',
     @externalTable = '',
     @externalCompany = 'A1',
     @startObject = ''
```

| Parametro | Descrizione |
|---|---|
| `@user` | Utente esterno per conto del quale si avvia il processo, risolto tramite gli [alias](#alias-il-collegamento-tra-utente-esterno-e-utente-bpm). |
| `@model` | Modello di processo da avviare. |
| `@externalID` | Identificativo del record esterno da cui nasce il processo. |
| `@externalTable` | Tabella o tipo del record esterno, facoltativo. |
| `@externalCompany` | Azienda del record esterno, facoltativa. |
| `@startObject` | Start da cui avviare il processo; vuoto per lo start predefinito. |

La chiave API viene letta dalla configurazione di BPM: chi scrive il trigger non deve gestirla.

La procedura non restituisce mai errori: se l'inserimento in coda non riesce, l'operazione del sistema chiamante prosegue comunque. È una scelta voluta: usata in un trigger, un errore bloccherebbe l'elaborazione del sistema esterno.

##### La convenzione EXTERNAL ID

La stored procedure non passa i dati del processo, ma solo il **riferimento** al record esterno, nelle variabili `EXTERNAL ID`, `EXTERNAL TABLE` ed `EXTERNAL COMPANY`. Il modello di processo deve quindi avere queste tre variabili.

Sarà poi il processo, all'avvio, a recuperare da solo gli altri dati che gli servono, con query o connettori configurati sullo start. Per esempio, per un processo di approvazione di un ordine d'acquisto basta passare l'ID dell'ordine: fornitore, numero, righe e importo vengono letti da BPM.

I vantaggi:

- il trigger sul sistema esterno resta di poche righe e non deve comporre JSON;
- la logica di recupero dei dati si configura in BPM, con gli strumenti grafici del Designer, e si modifica senza toccare il sistema esterno.

# Intelligenza artificiale


BPM usa l'intelligenza artificiale all'interno di processi e documenti: acquisizione di documenti da mail e cartelle, estrazione di testo e metadati, comprensione dei contenuti.

> **Sezione in preparazione**
>
> Questa sezione descriverà gli strumenti di intelligenza artificiale disponibili e il loro uso nei processi e nelle classi documentali.

# Amministrazione


Questa sezione raccoglie le configurazioni dell'istanza BPM che non appartengono a un singolo modello di processo o a una classe documentale: opzioni generali, utenti e gruppi, tabelle, allegati e funzioni tecniche di sistema.

Le pagine seguono i menu dell'applicazione e riportano il percorso nell'interfaccia, per rendere immediato il collegamento tra applicazione e manuale.

### Configurazione

- [Opzioni generali](#opzioni-generali)
- [Opzioni modelli](#opzioni-modelli)
- [Utenti e gruppi](#utenti-e-gruppi-1)
- [Contatti](#contatti)
- [Allegati](#allegati-2)
- [Tabelle](#tabelle)
- [Altre opzioni](#altre-opzioni)

### Sistema

Funzioni tecniche di gestione e monitoraggio dell'applicazione e del server sottostante.

- [Dizionario e traduzioni](#dizionario-e-traduzioni)
- [Caricamento massivo](#caricamento-massivo)
- [Strumenti di verifica](#strumenti-di-verifica)

Connettori, dashboard e report, che nell'applicazione si trovano nel menu Configurazione, sono descritti rispettivamente in [Integrazione](#integrazione) e nelle [Parti comuni](#parti-comuni).

## Configurazione


### Opzioni generali


Percorso: **Configurazione > Opzioni generali**.

Questa sezione contiene parametri generali, menu personalizzati, contatori, configurazioni email e strumenti per la gestione dei modelli e delle istanze di processo.

#### Parametri


Dalla sezione **_Parametri_** è possibile configurare l'Engine e gli Automatismi, la configurazione generale, e il logo cliente.

###### Engine/automatismi

In **_Engine/automatismi_** sono presenti la configurazione per l'invio della **_Email riepilogo attività_** e la **_Configurazione Engine_**.

L'**_Email riepilogo attività_**, invia agli utenti l'elenco delle attività da svolgere che hanno in sospeso.  
Il riepilogo può essere inviato quotidianamente, settimanalmente e mensilmente, dove è anche possibile scegliere il giorno della settimana e il giorno del mese in cui verrà inviata la mail, scegliendo l'orario, il periodo di riferimento e decidendo se includere cc e le attività ancora aperte.

Tramite la **_Configurazione Engine_** è possibile modificare alcuni dei funzionamenti endogeni del BPM.  
Tramite 4 checkbox è possibile scegliere:

* Se e quando effettuare la ricostruzione indici, se sì, il giorno e l'ora e se effettuare o meno l'update stats.
* Se salvare o meno la tabella pianificazione.
* Se salvare o meno la tabella pianificazione lato server.
* Attivare esecuzione chiamate API da tabella "ChiamateAPI", scegliendo l'URL API e l'URL Base Link Email.

###### Configurazione

La tab di **_Configurazione_** presenta delle impostazioni generali del funzionamento del BPM.

**Edit esclusivo istanze**

Se spuntato, solo un utente alla volta può modificare un determinato processo o documento.  
La stessa cosa vale per le attività in to-do list.  
L'utente che accede alla task per primo è l'unico che può agire al suo interno.

Una volta salvato il documento o completata l'attività, l'istanza ritorna disponibile.

**Nega login con stesso utente da più postazioni contemporaneamente**

Se spuntato, un utente non può accedere da più postazioni contemporaneamente.

**Utilizza password policies su nuovi utenti**

L'utilizzo delle **_Password policies_** fa sì che i nuovi utenti debbano cambiare la password dopo il numero di giorni impostato.   

> **Locazione obsoleta**
>
> La tab di **_Configurazione_** si trova all'interno della sezione parametri per cause di obsolescenza.  
> In futuro potrebbe essere spostata e non trovarsi più qui.

###### Logo Cliente

Nell'ultima tab è possibile impostare il logo del cliente.

#### Menu personalizzati


La sezione **_Menù personalizzati_** apre una schermata dedicata alla creazione di Menù.

Il pannello a sinistra mostra la gerarchia ad albero che rappresenta il menù configurato.  
È possibile espandere o contrarre gli elementi per visualizzare i sottomenù associati.    

###### Barra degli strumenti

La barra superiore degli strumenti contiene una serie di pulsanti che permettono di gestire e configurare i Menù.  

| **Attributo**                | **Descrizione**                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| **Modifica**                 | Permette di modificare un elemento selezionato.                                |
| **Salva**                    | Salva le modifiche apportate.                                                 |
| **Annulla**                  | Annulla le modifiche non salvate.                                              |
| **Nuova Radice**             | Crea una nuova radice del menù.                                               |
| **Nuovo submenù**            | Aggiunge un sottomenù all'elemento selezionato.                                |
| **Nuovo menù**               | Crea un nuovo elemento di menù.                                               |
| **Elimina**                  | Rimuove l'elemento selezionato.                                               |
| **Esporta**                  | Esporta la configurazione del menù.                                           |
| **Importa**                  | Importa una configurazione di menù esistente.                                 |
| **Stampa**                   | Stampa la configurazione attuale del menù.                                    |

###### Pannello delle impostazioni

Nella parte destra dello schermo si trovano le impostazioni dettagliate per l'elemento di menù selezionato:

| **Attributo**                | **Descrizione**                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| **Modello/tabella**          | Specifica il modello o tabella associato.                                      |
| **Tipo di workflow**         | Indica il tipo di workflow (ad esempio, "NESSUNO").                            |
| **Tipo di menù**             | Definisce il tipo di menù (ad esempio, "MODELLO").                             |
| **Azione**                   | L'azione associata all'elemento (ad esempio, "NUOVO").                         |
| **Posizione**                | Indica la posizione dell'elemento nel menù.                                    |
| **Configurazione**           | Specifica ulteriori dettagli di configurazione.                                |
| **Punto di avvio**           | Definisce un trigger o un punto di inizio.                                     |
| **Custom data**              | Campi aggiuntivi personalizzati.                                               |
| **Radice**                   | Nome della radice a cui appartiene l'elemento.                                 |
| **Sottomenù**                | Indica se l'elemento è un sottomenù.                                           |
| **Descrizione**              | Descrizione del menù.                                                         |
| **Variabili**                | Permette di associare variabili per la configurazione dinamica.                |

#### Contatori


In questa sezione sono elencate le variabili presenti nei processi ed impostate come **_Contatori_**.
Nella tabella sono presenti:

* Ciclovita, ovvero il nome del processo a cui appartiene il contatore.
* Chiave, raggruppamento del contatore.
* Variabile, nome della variabile contatore.
* Contatore, valore del contatore.

Tramite Modifica nella barra degli strumenti è possibile settare il valore del **_Contatore_** a quanto si preferisce.

#### Configurazioni Mail


La sezione **_Configurazioni Mail_** apre la pagina di gestione dei profili di posta inseriti.

Cliccando Nuovo o andando a modificare un profilo già esistente si aprirà un popup con tutte le specifiche.

Nella parte superiore della finestra è presente la barra degli strumenti con quattro pulsanti:

* Modifica: Permette di modificare i dettagli della configurazione.
* Salva: Consente di salvare le modifiche apportate.
* Annulla: Annulla le modifiche effettuate.
* Elimina: Elimina la configurazione attualmente selezionata.

###### Configurazione Base

Questa sezione consente di configurare le informazioni generali dell'account email.  

I campi e le opzioni disponibili includono:

* Nome, campo di testo che definisce un nome descrittivo per questa configurazione .
* Email, indirizzo email associato all'account.
* Tipo Server, un menu a tendina da cui è selezionabile il tipo di server tra GMAIL, OUTLOOK e CUSTOM.
* Autenticazione, un altro menu a tendina che consente di scegliere il metodo di autenticazione tra USER_PASSWORD, OAUTH2 e NO_AUTHENTICATION.
* Configurazione di default, una casella di spunta per indicare se questa configurazione è quella predefinita.

###### Sezione SMTP

Questa sezione è dedicata ai parametri del server SMTP (Simple Mail Transfer Protocol) per l'invio delle email:

* Server SMTP, campo di testo con l'indirizzo del server SMTP.
* SSL, una casella di spunta per abilitare la connessione protetta tramite SSL.
* STARTTLS, una casella di spunta per abilitare STARTTLS.
* Porta SMTP, campo numerico per specificare la porta utilizzata per il server SMTP.

###### Sezione IMAP
Questa sezione è dedicata ai parametri del server IMAP (Internet Message Access Protocol) per la ricezione delle email:

* Server IMAP: Campo di testo con l'indirizzo del server IMAP, configurato come "imap.gmail.com".
* SSL: Una casella di spunta per abilitare la connessione protetta tramite SSL (attualmente selezionata).
* STARTTLS: Una casella di spunta per abilitare STARTTLS (attualmente non selezionata).
* Accetta certificati invalidi: Una casella di spunta che consente di accettare certificati non validi (non selezionata).
* Porta IMAP: Campo numerico per specificare la porta utilizzata per il server IMAP. Il valore configurato è "993".

###### Sezione Autenticazione
Sul lato destro, una sezione separata permette di configurare le credenziali dell'account in base al tipo di autenticazione scelta.

Nel caso di USER_PASSWORD:

* Utente: Campo di testo che mostra l'indirizzo email dell'utente (lo stesso configurato in "Email").
* Password: Campo mascherato (con asterischi) per inserire la password associata all'account.

Nel caso di OAUTH2:

* TENANT ID
* CLIENT ID
* CLIENT SECRET

###### Pulsante Inferiore
Nella parte inferiore della finestra, troviamo il pulsante **_Configura gestione risposte email_**, che permette di scegliere quale cartella, all'interno della mail inserita, utilizzare per la gestione delle risposte.

#### Processi con avvio ricorrente


La sezione **_Processi con avvio ricorrente_** elenca i modelli di processo che hanno come inizio uno Start a tempo.

Nella tabella sono presenti:

* Nome del modello.
* Descrizione del timer.
* Stato del modello, attivo o non attivo.

#### Aggiornamento massivo processi


**_Aggiornamento massivo processi_** consente di aggiornare in massa le istanze di un modello di processo.

Viene richiesto se mantenere, dove possibile, l'avanzamento delle istanze oppure azzerarlo e ripartire dallo Start.  
Inoltre è necessario scegliere se non variare le cartelle allegati o aggiornare la struttura allegati in sola aggiunta. 

Dopo aver scelto, si aprirà una tab analoga a quella della ricerca processi.  
Da qui e possibile filtrare le istanze del modello e selezionare quelle da aggiornare all'ultima versione.  

Dopo qualche istante le istanze selezionate saranno aggiornate all'ultima versione del modello.

#### Attiva o disattiva processi

##### Attiva/Disattiva processi

Cliccando su **_Attiva/Disattiva processi_** si apre un popup che elenca i modelli di processo.

Facendo doppio clic su un modello, questo viene attivato o disattivato.

#### Storico generale


**_Visualizza storico generale_** apre la pagina del **Log operazione** ovvero tutte le azioni svolte dall'utente all'interno del BPM.

Nella tabella dei log sono presenti: Nome del modello, Data del log, Utente da cui è stata loggata l'azione, Nome del processo, Descrizione del Processo, Evento e Oggetto evento.

Gli Eventi possono essere:

* Aggiornamento processo da modello
* Creazione processo
* Eliminazione processo
* Esecuzione task
* Modifica ai dati di processo
* Modifica dati task
* Visualizzazione allegato
* Visualizzazione task

Nome e descrizione del processo vengono loggati solo quando l'evento ha come soggetto un processo.  
Oggetto evento quando l'evento parte appunto da un oggetto, come una task, un attributo o un elemento.

La tabella è filtrabile in alto per: Data da/a, Tipologia, Modello, Utente.  

Inoltre, se si dovesse scegliere **Visualizza dettaglio modifiche** appariranno nella tabella altre 7 colonne: Azione, Descrizione oggetto, Variabile, Valore Precedente, Valore nuovo, Gruppo e Riga.

Tramite il bottone esporta si aprirà un nuovo file excel con i dati dei log al suo interno.

### Opzioni modelli


Percorso: **Configurazione > Opzioni modelli**.

La sezione comprende le configurazioni per liste e importazioni da Excel, prefiltri dei processi, tipi di dossier e stampa di codici a barre o QR. Le singole schermate devono ancora essere documentate.

### Utenti e gruppi


Dalla sezione **_Utenti e Gruppi_** è possibile gestire gli utenti e i gruppi.

##### Nuovo utente

Cliccando su **Nuovo utente**, verrà aperta una nuova pagina dove inserire le seguenti informazioni necessarie:

* Nome e iniziali
* Descrizione
* Lingua

Tramite il bottone **Imposta password utente** è possibile impostare la password del profilo che si sta creando.  
Il checkbox *Utilizza password policy*, se spuntato, applica le regole descritte nei [Parametri](#parametri-1).

Se si sta modificando un profilo, il pulsante **Azzera password utente** reimposta la password dell'utente selezionato con una temporanea. L'utente riceverà un'email con la nuova password, che potrà sostituire al prossimo accesso.

Spuntando il checkbox **È un gruppo**, il profilo creato sarà un gruppo invece che un utente.

Cliccando il bottone **Visualizza storico** verranno mostrati tutti i log delle azioni relative agli utenti e gruppi.  
Collassando ogni riga, è possibile visualizzare tutti i dettagli interno, di cui:

* Info modificate
* Permessi aggiunti/rimossi
* Gruppi aggiunti/rimossi
* Filtri aggiunti/rimossi

Cliccando il bottone **Copia autorizzazioni da** tramite il popup specifico, si potranno importare le autorizzazioni di un account a quello che si sta creando.

##### Lista utenti

Dalla lista utenti, tramite la barra degli strumenti, è possibile creare, eliminare, esportare o importare profili, come descritto nella sezione precedente. 

Facendo doppio clic su un profilo nella tabella principale, si accede alle sue informazioni avanzate. 

Il popup visualizzato è simile a quello per la creazione di un profilo, con i dati iniziali nella parte superiore e 11 tab centrali che contengono tutte le informazioni avanzate.

Le 11 tab sono:

| **Tab**                    | **Descrizione**                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------|
| **Dati**                   | Contiene le informazioni anagrafiche e di configurazione dell’utente o gruppo (es. email, recapiti, firma email). |
| **Gruppo**                 | Gestisce l’appartenenza a gruppi o ruoli, utile per organizzare gli utenti in categorie con permessi specifici. |
| **Permessi menù**          | Definisce quali voci di menù l’utente o il gruppo può visualizzare e utilizzare.                     |
| **Permessi processi**      | Specifica i processi o workflow ai quali l’utente o il gruppo può accedere e con quali diritti.      |
| **Permessi Classi Documentali** | Stabilisce le classi di documenti a cui l’utente o il gruppo può accedere e in che modo.                 |
| **Permessi tabelle**       | Determina quali tabelle di dati l’utente o il gruppo può consultare o modificare.                    |
| **Permessi dashboard**     | Regola l’accesso e le autorizzazioni alle dashboard o report visuali.                               |
| **Permessi reports**       | Controlla quali report l’utente o il gruppo può generare o visualizzare.                            |
| **Permessi Dossier**       | Imposta le autorizzazioni di consultazione o modifica sui dossier, ossia raccolte di documenti o pratiche. |
| **Prefiltri**              | Permette di definire e applicare filtri preconfigurati ai dati, facilitando la ricerca e la consultazione. |
| **Aliases**                | Gestisce eventuali alias o nomi alternativi associati all’utente o al gruppo, ad esempio indirizzi email aggiuntivi. |

###### Dati

* Utente non attivo: Casella da selezionare per disattivare l’utente.
* Non avviare con home page: Se spuntata la home page non verrà caricata all'avvio.
* Utente amministratore: Casella selezionata per indicare che l'utente ha privilegi amministrativi.  
#
* Carica Firma: Permette di caricare una firma personalizzata per l'utente.
* Impostazioni notifiche utente: Pulsante che apre la configurazione specifica per gestire le notifiche assegnate all'utente.  
Questo popup consente di configurare in modo dettagliato le notifiche relative alle attività, stabilendo sia come che quando l’utente riceve avvisi via email o all’interno del sistema. Di seguito una panoramica dei principali elementi:

1. Invio riepilogo attività via email

    Casella di spunta per abilitare l’invio di un riepilogo (ad esempio giornaliero o periodico) delle attività via email.

2. Modalità Notifiche

    Opzione per selezionare il canale di notifica (in questo caso “Via email”).

3. Notifiche Scatenate Immediatamente da Azioni

    * Notifica nuova attività (assegnata, delegata): Attiva un avviso non appena viene assegnata o delegata una nuova attività.
    * Notifica spostamento attività: Invia un avviso quando la data di un’attività viene modificata.
    * Notifica cambio data scadenza attività: Avvisa in caso di variazione della data di scadenza di un’attività.

4. Per attività che riguardano

    * Selezioni multiple (checkbox) per definire su quali attività ricevere notifiche, ad esempio:
        * Me (l’utente stesso)
        * Me in CC
        * Il mio gruppo
        * Il mio gruppo in CC
        * Il gruppo che amministro
        * Il gruppo che amministro in CC
5. Notifica X giorni prima della data inizio/scadenza attività
    
    Permette di impostare quanti giorni prima dell’inizio o della scadenza di un’attività deve essere inviata la notifica.

6. Silenzia Notifiche su Processi di Tipo

    Sezione per escludere alcuni tipi di processi (o workflow) dall’invio delle notifiche, riducendo il numero di avvisi non rilevanti.

7. Salva e esci

    Pulsante per confermare le impostazioni e chiudere la finestra di configurazione.

### Contatti


Percorso: **Configurazione > Contatti**.

Questa sezione raccoglie le configurazioni relative ai contatti. Le singole schermate devono ancora essere documentate e verificate sul prodotto corrente.

### Allegati


Percorso: **Configurazione > Allegati**.

Questa sezione raccoglie le configurazioni condivise degli allegati, tra cui gruppi, tipi e modelli di allegato. Le pagine dei modelli di processo e delle classi documentali descrivono come queste configurazioni vengono utilizzate nei rispettivi contesti.

### Tabelle


Percorso: **Configurazione > Tabelle**.

Questa sezione permette di configurare tabelle personalizzate. La definizione dei campi usa l'[Editor delle variabili](#editor-delle-variabili), con eventuali differenze specifiche da documentare in questa sezione.

### Altre opzioni


Percorso: **Configurazione > Altre opzioni**.

Questa sezione raccoglie le configurazioni presenti nell'omonima area dell'applicazione, comprese le variabili di ambiente e le [chiavi di accesso API standard](#chiavi-di-accesso-web-api).

#### Chiavi di accesso Web API


Percorso: **Configurazione > Configurazione > Chiavi di accesso Web API**.

La schermata **Token di accesso per Web API** elenca le chiavi API con cui le applicazioni esterne accedono alle [API standard](#api-standard) di BPM.

###### Comandi

**Crea nuovo token di autenticazione**

Genera una nuova chiave casuale e la aggiunge all'elenco.

###### Colonne

| Colonna | Descrizione |
|---|---|
| **Chiave di autenticazione** | La chiave da comunicare all'applicazione esterna, che la invierà nel campo `authenticationToken`. |
| **Copy to clipboard** | Copia la chiave negli appunti. |
| **Descrizione** | Descrizione libera: indica quale applicazione usa la chiave. |
| **Data** | Data associata alla chiave. |
| **Edit** | Modifica la chiave. |
| **Delete** | Elimina la chiave: le applicazioni che la usano non potranno più accedere. |

> **Sicurezza**
>
> Una chiave consente di operare per conto di qualunque utente. Crea una chiave per ogni applicazione, descrivila con chiarezza ed eliminala quando l'integrazione non è più in uso. Vedi [Autenticazione e utenti](#autenticazione-e-utenti).

## Sistema


Il menu **Sistema** contiene funzioni tecniche di gestione e monitoraggio dell'applicazione e del server sottostante. È meno frequente rispetto alle aree di configurazione, ma fa parte del perimetro del manuale.

#### Contenuti

- [Dizionario e traduzioni](#dizionario-e-traduzioni)
- [Caricamento massivo](#caricamento-massivo)
- [Strumenti di verifica](#strumenti-di-verifica)

### Dizionario e traduzioni


Percorso: **Sistema > Dizionario e traduzioni**.

Questa funzione consente di aggiungere lingue, personalizzare le etichette dell'applicazione, esportare il dizionario in Excel e verificare le voci mancanti.

### Caricamento massivo


Percorso: **Sistema > Caricamento massivo**.

Il caricamento massivo centralizza il caricamento di più configurazioni, tra cui modelli di processo, classi documentali e report, senza passare dai rispettivi menu. I formati e le regole di importazione devono ancora essere documentati.

### Strumenti di verifica


Percorso: **Sistema > Strumenti di verifica**.

Questa sezione raccoglie strumenti tecnici di controllo e monitoraggio, tra cui log, email in uscita e chiamate API in errore. Le singole schermate devono ancora essere documentate.

# Parti comuni


Processi e documenti condividono alcuni strumenti: le variabili, le formule, le dashboard e i report. Questa sezione ne descrive una volta sola il funzionamento; le pagine di [Processi](#processi) e [Documenti](#documenti) spiegano le differenze e rimandano qui.

### Contenuti

- [Editor delle variabili](#editor-delle-variabili)
- [Formule e script](#formule-e-script)
- [Dashboard](#dashboard): configurazione. Le dashboard si consultano dai menu personalizzati e dalle schermate dei processi.
- [Report](#report): configurazione. I report si consultano dai menu personalizzati e dalle schermate dei processi.
- [Glossario](#glossario)

## Editor delle variabili


L'**Editor delle variabili** e uno strumento condiviso dai modelli di processo, dalle classi documentali e da altre configurazioni BPM. Consente di creare, organizzare e configurare le variabili impiegate in ciascun contesto.

Grazie a questo strumento è possibile definire i dati che i processi devono trattare, stabilirne la tipologia, il formato e il comportamento, garantendo così una gestione coerente e automatizzata delle informazioni aziendali.

#### Scopo della sezione

L’obiettivo principale della sezione **_Variabili_** è quello di fornire un punto centralizzato dove:
- Definire le variabili globali o specifiche per un determinato modello di processo  
- Impostare le caratteristiche di ciascuna variabile (nome, tipo, valore predefinito, visibilità, ecc.)  
- Gestire la logica di interscambio dei dati tra le diverse attività di un processo  
- Creare collegamenti diretti tra variabili, campi documentali e interfacce utente  

Le variabili costituiscono il **ponte logico tra i dati e le azioni**: tutto ciò che un processo riceve, elabora o produce viene gestito attraverso di esse.

#### Tipologie di variabili

All’interno del BPM esistono diverse **tipologie di variabili**, ciascuna con un ruolo e un ambito di utilizzo specifico:

1. **Variabili globali**  
   Sono disponibili a tutti i processi e utili per dati condivisi (es. utente corrente, data di sistema, impostazioni generali).

2. **Variabili di processo**  
   Sono specifiche di un singolo modello di processo e vengono create al suo interno per gestire i dati necessari al suo flusso.

3. **Variabili locali**  
   Sono utilizzate solo all’interno di una singola attività o step del processo, per gestire informazioni temporanee o di calcolo.

4. **Variabili di sistema**  
   Create automaticamente dal BPM, servono per monitorare stati e metadati del processo (es. ID del processo, data di creazione, utente assegnato).

#### Tipi di dato supportati

Ogni variabile può essere definita con un **tipo di dato specifico**, in base alla natura delle informazioni che deve contenere.  
I principali tipi di dato sono:

- **Testo:** per stringhe di caratteri, nomi o descrizioni  
- **Numero:** per quantità, codici o valori numerici  
- **Data/Ora:** per gestire scadenze, registrazioni temporali o intervalli  
- **Booleano:** per valori logici (vero/falso)  
- **Oggetto/Classe documentale:** per riferimenti a strutture dati più complesse  

Inoltre, il sistema consente di creare **tipi personalizzati**, utili per casi d’uso specifici o integrazioni avanzate con altri moduli del BPM.

#### Utilizzo nei processi

Le variabili vengono utilizzate in diversi punti di un processo, tra cui:
- **Condizioni di transizione:** per definire logiche di avanzamento del flusso  
- **Attività automatizzate:** per scambiare dati con sistemi esterni o moduli interni  
- **Form di input/output:** per visualizzare o raccogliere dati da parte degli utenti  
- **Azioni e script:** per eseguire calcoli, verifiche o aggiornamenti dinamici  

#### Buone pratiche

Per una gestione ottimale delle variabili, è consigliato:
- Utilizzare **nomi coerenti e descrittivi**, evitando abbreviazioni non chiare  
- Separare le variabili globali da quelle locali per evitare conflitti  
- Documentare la funzione di ciascuna variabile nei commenti del modello  
- Eliminare le variabili non più utilizzate per mantenere pulito l’ambiente  
- Testare sempre le variabili durante le fasi di validazione del processo  

#### Approfondimenti

Nei capitoli successivi verranno analizzati nel dettaglio:
- Come creare una nuova variabile  
- Come collegare variabili a campi documentali o form di processo  
- Come utilizzare le variabili nelle espressioni e nelle condizioni logiche  
- Le modalità di esportazione e importazione delle variabili tra modelli  

> **Suggerimento**
>
> Prima di creare una nuova variabile, verifica se esiste già una variabile globale che soddisfa la stessa funzione.  
> In questo modo eviterai duplicazioni e garantirai una gestione più efficiente dei dati all’interno del BPM.

### Magazzino delle variabili


Il **Magazzino delle variabili** è l'area dell'Editor delle variabili nella quale si definiscono e si dispongono i dati della configurazione corrente.

La barra laterale sinistra, chiamata **Variable List**, contiene le variabili disponibili; quella destra mostra gli attributi della variabile selezionata.

In alto è presente la barra degli strumenti che, sotto la sezione **_Variabili_**, presenta tutti i comandi utili nel contesto del Magazzino.

##### Barra degli strumenti - Variabili

La sezione variabili della barra degli strumenti è divisa in 6 colonne la cui ultima presenta solo il bottone di chiusura della pagina del Magazzino delle variabili.

###### Operatività

La colonna **_Operatività_** contiene i comandi più comuni utilizzabili nel Magazzino.

**Nuova variabile, Duplica variabile e Rimuovi variabile**

**_Nuova variabile_** serve ad aggiungere nuove variabili al Magazzino.  
Cliccando il comando, un dialog si aprirà chiedendo all'utente di inserire il Nome variabile.  
Dopo aver confermato, si aprirà un secondo dialog dove è possibile personalizzare tutti gli attributi di una variabile.

> **Note**
>
>
> Il **_Nome variabile_** non è reimpostabile né dal dialog degli attributi né dal pannello degli attributi.  
> Gli attributi del secondo dialog sono situae nel pannello degli attributi.  

**_Duplica variabile_**, selezionando una variabile all'interno del canvas, duplica la variabile selezionata, chiedendo all'utente di inserire solamente il nome della variabile duplicata.  

**_Rimuovi variabile_** serve a rimuovere una variabile dal canvas.

**Trova riferimenti**

Selezionando una variabile nel canvas, **_Trova riferimenti_** cercherà nel processo tutte i riferimenti alla variabile selezionata.

###### Pagina

Per **_Pagina_** non si intendono nel pagine del progetto, bensì quelle del Magazzino delle variabili, simili a delle schede.

**Nuova pagina, Rinomina pagina e Refresh**

**Nuova pagina**
Crea una nuova scheda all'interno del Magazzino delle variabili.  

**Rinomina pagina**

Rinomina la pagina in cui si sta lavorando.  

**Refresh **

Aggiorna la pagina corrente.

###### Gestione

La colonna **_Gestione_** raggruppa i comandi e le impostazioni per gestire la portabilità e la validazione.

**Formule**

Le **_Formule_** sono 3: **_Validazione, Inizializzazione e Formattazione ricerche_**.

**Validazione**

Formula che valida la fine di un processo.

**Inizializzazione**

**Formattazione ricerche**

**Sqlview**

L'**_Sqlview_** semplifica la scrittura delle query sul database del BPM.
Sul click, si aprirà un file di testo con all'interno una query relative a tutte le variabili nel Magazzino.
Dalla query di default verrà selezionato l'InstanceID del workflow.

**Default query**

```
-- Verranno riportate nella selezione soltanto le variabili di testata (non di gruppo)

Select WKF.InstanceID, v1.aaa
from WKF
left join (Select StringValue As aaa, InstanceID,VariableName  from VAR_FGWTFEFWE ) v1 On  v1.VariableName ='aaa' and v1.InstanceID = wkf.InstanceID
where wkf.Name like 'fgwtfefwe' 
```

**Importa/Esporta**

**_Importa/Esporta_** è un dropdown con 6 possibili scelte.

Tramite le varie opzioni è possibile esportare le variabili del processo corrente o importarne altre da un file esterno.
È possibile, altrimenti, importare/esportare solo la categoria.

**Esporta variabili**

**_Esporta variabili_** serve a spostare localmente le variabili. Ad esempio è possibile esportare le variabili del Mgazzino alle variabili da richiedere di una task.

###### Allineamento

Come nell'[allineamento del Designer di processo](#allineamento-e-dimensioni), la sezione **_Allineamento_** contiene gli strumenti per allineare gli elementi nel canvas del Magazzino delle variabili.

**Allinea a sinistra e Allinea in alto**

Allineano gli elemento selezionati secondo il tipo di allineamento in base alla posizione dell'elemento su cui è stato cliccato il tasto destro.

**Porta davanti e Porta dietro**

Modifica lo Z-index di un oggetto: se un oggetto risulta sovrapposto ad un altro, per portarlo in avanti è sufficiente cliccare **_Porta avanti_** per portarlo in primo piano. 
Lo stesso, ma al contrario, vale per **_Porta dietro_**.

###### Opzioni

La sezione **_Opzioni_** raggruppa 3 opzioni generali del Magazzino.

**Proprietà**

Mostra e nasconde il Pannello degli attributi

**Variabili**

**_Variabili_** è un dropdown che consente di vedere nella Variable list o tutte la variabili ancora da inserire, o tutte le variabili indistintamente.

**Griglia**

**_Griglia_** consente di aumentare o diminuire la distanza tra i punti della griglia.

##### Magazzino delle variabili di un elemento

Il **_Magazzino delle variabili di un elemento_** è lo stesso concetto del Magazzino delle variabili, ma riferito alle variabili da richiedere di un elemento.  

Esso differisce in alcuni punti:

* Non è possibile aggiungere o duplicare variabili.
* È possibile aggiornare le descrizioni di tutte le variabili tramite **_Aggiorna Descrizione_** nella barra degli strumenti.
* Non è possibile eseguire la **_Sqlview_**.

### Barra degli strumenti


##### Operatività

##### Pagina

##### Gestione

###### Importa/Esporta

**Importa**

Importa Pagina:	Consente di caricare in blocco tutte le variabili appartenenti a una specifica pagina del processo.

**Esporta**

##### Allineamento

##### Opzioni

##### Chiudi

### Attributi

Nel Pannello Attributi sulla destra sono elencati tutti gli **_Attributi di una variabile_** suddivisi in 3 sezioni.

##### Impostazioni base

###### Nome variabile

Il **_Nome della variabile_** è il nome tecnico con cui ci si riferisce alla variabile.  
Esso Non può essere modificato dopo l'inizializzazione.

###### Descrizione

La Descrizione di una variabile definisce la label che appare nel canvas.  
Serve ad un utente per capire che genere di dato inserire in un input.

###### Descrizione su interrogazioni

Utilizzando la ricerca processi, la **_Descrizione su interrogazioni_** è l'attributo che viene ricercato e mostrato in caso combaciasse coi filtri di ricerca.

> **Note**
>
> Si consiglia di impostare la **_Descrizione su interrogazioni_** in modo che sia più accurata e specifica rispetto alla Descrizione normale, in quanto la **_Descrizione su interrogazioni_** viene letta in una pagina dove l'utente non vede il flusso disegnato.

###### Gruppo
Definisce il gruppo logico o categoria a cui appartiene la variabile.

###### Obbligatoria
Booleano (True/False) che indica se il valore della variabile è obbligatorio.

###### Readonly
Booleano (True/False) che determina se la variabile è di sola lettura.

###### Senza salvataggio
Specifica se la variabile non deve essere salvata nei dati.

###### Sezione/sottocategoria
Permette di organizzare la variabile in una sezione o sottocategoria.

###### Tabella di origine
Indica se la variabile deriva da una tabella di dati specifica.

###### Tipo impostazioni di base
Indica il tipo di impostazioni predefinite (ad esempio, Testo).

###### Tipo variabile
Determina il tipo specifico della variabile (es. StringType, NumericType, ecc.).
Ogni **_Tipo variabile_** viene approfondito nella sezione Tipo di variabili [qui](#tipi-di-variabili).

##### Altre impostazioni
###### Attività collegate
Indica se ci sono attività o azioni associate alla variabile.

###### Autocomplete
Booleano che definisce se il campo deve supportare il completamento automatico.

###### Campo chiave
Specifica se la variabile rappresenta un campo chiave.

###### Formula
Formula personalizzata per calcolare il valore della variabile.

###### Formula di validazione
Formula per convalidare il valore della variabile.

###### Formula formattazione
Formula per definire il formato del valore della variabile.

###### Formula default
Formula per impostare il valore predefinito della variabile.

###### Formula per visibilità
Specifica una condizione per mostrare o nascondere la variabile.

###### Formula readonly
Formula che determina se la variabile è di sola lettura.

###### Help text
Testo di aiuto visualizzato all'utente per spiegare l'uso della variabile.

###### Imposta variabili
Opzione per configurare o modificare dinamicamente altre variabili in base al valore corrente.

###### Valore di default
Il valore iniziale o predefinito della variabile.

###### Variabile di intestazione
Booleano che indica se la variabile è utilizzata come intestazione.

###### Formula intestazione (p.)
Permette di definire una formula per le intestazioni.

###### Variabili da richiedere
Numero o elenco di variabili che devono essere richieste quando questa è utilizzata.

##### Altro

###### Dimensione carattere
Lo stile o dimensione del carattere associato.

###### Location
Coordinate X, Y che indicano la posizione dell'elemento.

###### Nascosta su mobile device
Indica se la variabile è nascosta sui dispositivi mobili.

###### Pagina/categoria
La pagina o categoria a cui appartiene la variabile.

###### TAG
Tag o etichette per identificare ulteriormente la variabile.

##### Tipi di variabili

###### StringType
Una variabile di tipo testo semplice.

###### NumericType
Una variabile numerica (interi o decimali).

###### BooleanType
Una variabile booleana (valori True/False).

###### DataType
Una variabile per rappresentare una data (senza ora).

###### CurrencyType
Una variabile per valori monetari.

###### MemoType
Una variabile per testi lunghi, simile a un campo memo.

###### ValueListType
Una variabile che offre una lista di valori selezionabili.

###### UserType
Una variabile che rappresenta un utente (es. ID o nome utente).

###### LABEL
Una variabile di tipo etichetta (non modificabile, solo visualizzazione).

###### DateTimeType
Una variabile per rappresentare una data e un'ora.

###### SignType
Una variabile per firme (es. digitali o grafiche).

###### LINK
Una variabile per memorizzare o gestire collegamenti ipertestuali.

###### DataGrid
Una variabile che rappresenta una griglia o tabella di dati.

### Tipi di variabile


Il tipo determina quali valori può contenere una variabile, come viene presentata e quali proprietà aggiuntive sono disponibili.

L'elenco attuale dei tipi e delle relative proprietà deve essere verificato con lo studio dettagliato delle configurazioni reali. Le descrizioni già disponibili sono raccolte negli [attributi delle variabili](#tipi-di-variabili).

#### UserType


Variabile UserType: Placeholder dinamico risolto a runtime in base ai dati del processo (es: @[FUNZIONE COINVOLTA]).

## Formule e script


In BPM una formula è codice VB.NET valutato con il ruolo previsto dal punto di configurazione. Il termine **script** è usato naturalmente per le logiche procedurali più articolate, ma il meccanismo e l'editor sono gli stessi.

Le variabili BPM si richiamano con la sintassi `@[nome_variabile]`.

#### Editor

L'editor mette a disposizione funzioni contestuali tramite il menu del tasto destro, facilita la navigazione nelle strutture di variabili e compila immediatamente il codice per evidenziare gli errori.

#### Ruolo della formula

Ogni punto di configurazione assegna alla formula una semantica precisa. Una formula può, per esempio, calcolare un valore, inizializzare dati, validare un valore restituendo `True` o `False`, oppure impostare più variabili.

Il catalogo completo dei ruoli verrà costruito usando lo studio dettagliato dei modelli reali. Ogni pagina di configurazione deve descrivere il momento di valutazione, i dati disponibili e il risultato atteso, collegandosi a questo riferimento per la sintassi comune.

## Dashboard


Percorso: **Configurazione > Dashboard**.

Questa sezione è dedicata alla configurazione delle dashboard usate per rappresentare e monitorare dati, attività e processi. Le singole schermate e i componenti disponibili devono ancora essere documentati.

## Report


Percorso: **Configurazione > Report**.

Questa sezione è dedicata alla configurazione dei report. Le singole schermate, le sorgenti dati e le opzioni di pubblicazione devono ancora essere documentate.

## Glossario


Il **_Glossario_** contiene i termini tecnici del BPM e i prestiti linguistici presenti all'interno della documentazione di cui è necessaria la spiegazione del significato.

###### BPM

Business Process Modeler.

###### Modello di processo

Configurazione di un flusso eseguibile, comprendente attività, variabili, assegnazioni, autorizzazioni, regole, integrazioni e rappresentazione grafica.

###### Istanza di processo

Singola esecuzione di un modello di processo.

###### Classe documentale

Configurazione di un tipo di documento, comprendente variabili, azioni, autorizzazioni e interazioni con i processi.

###### Designer di processo

Ambiente di progettazione nel quale si configura un modello di processo.

###### Canvas

Superficie del Designer sulla quale si dispongono e si collegano graficamente gli oggetti.

###### Editor delle variabili

Strumento condiviso con cui si definiscono e si organizzano le variabili usate nelle configurazioni BPM.

###### Formula e script

Codice VB.NET inserito tramite un editor condiviso e valutato con il ruolo previsto dal punto di configurazione. Le variabili BPM sono citate con la sintassi `@[nome_variabile]`.

###### Connettore

Componente tecnico che mette a disposizione integrazioni con sistemi esterni oppure funzioni di utilità interne. Non tutti i connettori realizzano un'integrazione.

###### Todo list

Lista delle task da svolgere. È situata nella homepage.

###### Task

Azione di vario genere che viene svolta dagli utenti di un processo attivo.

**Sinonimi di Task**

* Activity
* Azione
* Attività

###### Allegati

Insieme dei file nei diversi formati allegati alla singola istanza.

###### File System

Spazio su Server condiviso aziendale.

###### Query

Stringa che interroga il database, solitamente scritta in linguaggio SQL.

###### Repository

Prestito dall'inglese per il termine Cartella.

###### Popup

Finestra che si apre, di solito per richiedere all'utente di fornire un informazione o per chiedergli conferma.

**Sinonimi di Popup**

* Dialog
* Modal
