# To do — API standard

Punti aperti nelle pagine `docs/integrazione/api-standard/`. Nel sito sono segnati come *da verificare* o *da dettagliare*.

Fonti usate: Swagger della demo 2026.7.3, documento Word "BPM Web Service Standard" (2022), risposte di Riccardo del 25/9, codice del controller `ext` (`D:\BPM\Application\Core\API\SERVER_WEB_STD\ApiControllers`) e delle classi `ApiClasses`.

## Risolti il 25/9

- [x] DeleteProcess: diritti dell'utente della chiamata; elimina tutto (To-Do List, allegati, variabili).
- [x] AddLink: collega processi; i parametri `attachment…` sono un errore dello Swagger (arriverà `AddLinkedDocument`). Dal codice: serve il diritto "aggiunta istanze collegate" o essere amministratore.
- [x] ProcessModels / DocumentSets: elenco di `Name`, `Description` dei modelli attivi.
- [x] CreateNewDocument: duplicato = stesso nome documento (composto dalle variabili); CreateOrUpdateDocument aggiorna e crea una nuova versione.
- [x] GetDocument: come GetProcess, più `documentDate`, `documentDueDate`, `documentBarcode`, `versions`.
- [x] SearchDocuments: `dossierType`; filtri su variabili e campi `FIX_…`; risposta = array di record con variabili della classe + campi FIX_ (in maiuscolo) + `ID`/`instanceid`.
- [x] sourceType (`filePath`, `base64`), versioni, `signedCopy`.
- [x] AddDocumentToDossier: il dossier viene creato; `Type` obbligatorio.
- [x] `parameters`, `sourceReference`: uso interno. `choice`: obsoleto. `includeGraph`: PNG base64 del diagramma. `attachments`: `folder`, `isEmail`.
- [x] GetPageTodoList: la risposta aggiunge `page`, `size`, `totalRecords`, `totalPages`; la prima pagina è `1` (OFFSET (Page-1)*Size).
- [x] `<tipo>Company` confermato.
- [x] `newVersion`: `new_draft` / `new_active`; `newVersionNumber` è il numero.
- [x] DocumentVersions: campi della risposta; `State` = `ACTIVE`, `HISTORY`, `DRAFT`.
- [x] Campi generali `fix_…`: elenco per processi e documenti (pagina Web API, sezione "Campi generali").
- [x] Regola editoriale: nel sito niente "da verificare", niente riferimenti a bug, niente campi interni o obsoleti. Restano tracciati solo in questo file.

## Ancora aperti

- [ ] **Variabili senza valore nelle risposte** (GetProcess/GetDocument): stringa vuota per stringhe, memo, liste valori; per numeri e date da approfondire. Indizi dall'esempio RECLAMO: numerico vuoto `"TEMPO DI RISPOSTA": 0.0`, data vuota `"DATA_VALUTAZIONE": ""`; nel controller i valori `Nothing` diventano `""`. Tolta per ora la frase dal sito.
- [ ] **CreateOrUpdateUser**: non è nello Swagger della demo 2026.7.3. Da quale versione è disponibile? In aggiornamento i gruppi vengono sostituiti o aggiunti? Va documentata pubblicamente?
- [ ] **Coda delle chiamate**: altre stored procedure (ExecTask, UpdateProcess, …) da documentare; gestione dei tentativi e pulizia delle righe elaborate. (Frequenza: pochi secondi, documentata.)
- [ ] **Chiavi di accesso**: colonna **Data** (creazione o scadenza? le chiavi scadono?).

## Da nascondere nello Swagger (campi interni o obsoleti, non citati nel sito)

- [ ] `parameters` (CreateNewProcessInput, CreateDocumentInput): uso interno.
- [ ] `sourceReference` (CreateDocumentInput, UpdateDocumentInput, UpdateDocumentContentInput, AddAttachInput): uso interno.
- [ ] `choice` (EseguiTaskInput): obsoleto.
- [ ] `scope` (UpdateTaskInput): obsoleto (nel codice imposta `task.ModuleText`).
- [ ] `attachmentGroup`, `attachmentType`, `attachmentRoot`, `attachmentPath` (LinkedProcessInput): errati, da togliere (arriverà `AddLinkedDocument`).

Nota: `tasks` e `processState` (GetProcess/GetDocument) restano documentati, senza struttura: sono lo stato JSON di task e processo prodotto da `TaskSerialization_SalvaStatoTaskSuClasse` e `WkfSerialization_SalvaStatoWkfSuClasse`, lo stesso salvato in alcune tabelle di BPM.

- [ ] Variabili Memo nelle risposte: oltre a `Text` e `HTML` compare `Testo`, duplicato legacy di `Text`, da togliere. Nel sito è documentato solo `Text`.

- [ ] Risposta di SearchDocuments: contiene anche campi interni non documentati nel sito (`FIX_MODIFICATO`, `ID`, `MUST_LifeCycle`, `MUST_CHECKEDOUT`, `ForeColor`, `BackColor`). Valutare se escluderli dalla risposta API.

## Da rivedere nell'implementazione: versioni dei documenti e API

Promemoria per Riccardo: la gestione delle versioni esposta dalle API ha alcuni spigoli.

- [ ] **`FileName` nelle versioni** (DocumentVersions, DownloadDocumentJSON): non è chiaro se serva, perché nel documentale non esiste il concetto di file. Decidere se tenerlo, cosa deve contenere e come documentarlo.
- [ ] **`State` delle versioni**: è un enum (`ACTIVE`, `HISTORY`, `DRAFT`) che in passato veniva serializzato come numero anziché come stringa. Verificare che la serializzazione sia sempre come stringa, in tutte le chiamate che lo restituiscono.
- [ ] Rivedere in generale la coerenza tra `newVersion` / `newVersionNumber` in ingresso e `Version` / `State` in uscita.

- [ ] **BPM_CreateNewProcess**: la chiave API è letta da `TokenValidiApi` con `Descrizione = 'SAM'` e l'utente è sempre passato come `samUser`: la stored procedure è di fatto legata all'integrazione con SAM. Nel sito è descritta in modo generico ("la chiave API viene letta dalla configurazione"). Valutare una versione parametrica.
- [x] **BPM_CreateNewProcess**: il `CATCH` vuoto è voluto (un errore nel trigger bloccherebbe l'elaborazione lato SAM). Documentato come scelta.
- [ ] Nei log reali di `ChiamateAPI` le chiavi API sono in chiaro nella colonna `Parametri`: valutare se mascherarle.

## Differenze tra Word e codice (la documentazione segue il codice)

- [ ] **GetProcess `includeVariables` vuoto**: il Word dice "nessuna variabile", il codice restituisce **tutte** le variabili. Confermare quale sia il comportamento voluto.
- [ ] **`userName` dentro `authorization`**: il Word lo mostra, ma il codice non lo legge (legge solo `authenticationToken`/`apiKey`, `<tipo>User`, `<tipo>Company`). `userName` va messo fuori da `authorization`. Confermare.
- [ ] **Chiave `apiKey`**: il codice accetta nell'oggetto `authorization` sia `authenticationToken` sia `apiKey`. Documentato: va bene?

## Possibili bug trovati nel codice (da girare agli sviluppatori)

- [ ] **DownloadDocument / DownloadDocumentJSON**: con `Model` + `Name` (senza `InstanceId`) il metodo ricava l'id, ma poi usa `par.InstanceId` (vuoto) in `Guid.Parse` → probabile errore 500. In DownloadDocument manca anche il controllo `wk Is Nothing`. Nella documentazione per ora si consiglia di usare `InstanceId`.
- [ ] **AddDocumentToDossier**: con `Model` + `DocumentName` il documento viene trovato, ma alla fine si passa `par.InstanceId` (vuoto) a `InternalEngine.AddDocumentToDossier`. Se il documento non è di tipo documentale, la risposta ha `result = false` con `message` vuoto.
- [ ] **UpdateTask, vincolo di gruppo**: il controllo "il nuovo assegnatario deve appartenere al gruppo dell'attività" verifica i gruppi dell'utente **chiamante** (`ute.GroupList`), non quelli del nuovo assegnatario.
- [ ] **Cache delle chiavi API** (`TestToken`): l'elenco delle chiavi valide viene caricato una sola volta, al primo utilizzo. Una chiave creata dopo potrebbe non essere riconosciuta fino al riavvio dell'applicazione (e una chiave eliminata restare valida). Da verificare.
- [ ] **GetPageTodoList con `Size` o `Page` a 0**: l'engine non pagina e restituisce tutto, ma `totalPages` viene calcolato come `Ceiling(count / Size)`: con `Size = 0` è una divisione per zero. Valutare un controllo sui parametri.
- [ ] **Variabili sconosciute**: una variabile inesistente viene ignorata con un warning nel log del servizio WkfApi. Documentato così; valutare se restituire un errore.
