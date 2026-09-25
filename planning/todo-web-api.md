# To do — Web API

Punti aperti nelle pagine `docs/integrazione-e-ai/integrazione/web-api/`. Nel sito sono segnati come *da verificare* o *da dettagliare*.

Fonti usate: Swagger della demo 2026.7.3, documento Word "BPM Web Service Standard" (2022), risposte di Riccardo del 25/9, codice del controller `ext` (`D:\BPM\Application\Core\API\SERVER_WEB_STD\ApiControllers`) e delle classi `ApiClasses`.

## Risolti il 25/9

- [x] DeleteProcess: diritti dell'utente della chiamata; elimina tutto (To-Do List, allegati, variabili).
- [x] AddLink: collega processi; i parametri `attachment…` sono un errore dello Swagger (arriverà `AddLinkedDocument`). Dal codice: serve il diritto "aggiunta istanze collegate" o essere amministratore.
- [x] ProcessModels / DocumentSets: elenco di `Name`, `Description` dei modelli attivi.
- [x] CreateNewDocument: duplicato = stesso nome documento (composto dalle variabili); CreateOrUpdateDocument aggiorna e crea una nuova versione.
- [x] GetDocument: come GetProcess, più `documentDate`, `documentDueDate`, `documentBarcode`, `versions`.
- [x] SearchDocuments: `dossierType`; filtri su variabili e campi `FIX_…`.
- [x] sourceType (`filePath`, `base64`), versioni, `signedCopy`.
- [x] AddDocumentToDossier: il dossier viene creato; `Type` obbligatorio.
- [x] `parameters`, `sourceReference`: uso interno. `choice`: obsoleto. `includeGraph`: PNG base64 del diagramma. `attachments`: `folder`, `isEmail`.
- [x] GetPageTodoList: la risposta aggiunge `page`, `size`, `totalRecords`, `totalPages`; la prima pagina è `1` (OFFSET (Page-1)*Size).
- [x] `<tipo>Company` confermato.
- [x] `newVersion`: `new_draft` / `new_active`; `newVersionNumber` è il numero.
- [x] Campi generali `fix_…`: elenco per processi e documenti (pagina Web API, sezione "Campi generali").
- [x] Regola editoriale: nel sito niente "da verificare", niente riferimenti a bug, niente campi interni o obsoleti. Restano tracciati solo in questo file.

## Ancora aperti

- [ ] **SearchDocuments**: struttura esatta della risposta.
- [ ] **Variabili senza valore nelle risposte** (GetProcess/GetDocument): stringa vuota per stringhe, memo, liste valori; per numeri e date da approfondire. Indizi dall'esempio RECLAMO: numerico vuoto `"TEMPO DI RISPOSTA": 0.0`, data vuota `"DATA_VALUTAZIONE": ""`; nel controller i valori `Nothing` diventano `""`. Tolta per ora la frase dal sito.
- [ ] **DocumentVersions**: campi di ciascuna versione (`DocumentHistoryVersion`, definita fuori dal controller).
- [ ] **CreateOrUpdateUser**: non è nello Swagger della demo 2026.7.3. Da quale versione è disponibile? In aggiornamento i gruppi vengono sostituiti o aggiunti? Va documentata pubblicamente?
- [ ] **Coda delle chiamate** (`coda-chiamate.md`): struttura della tabella `chiamateapi`, stored procedure di inserimento, frequenza, tentativi, pulizia.
- [ ] **Chiavi di accesso**: colonna **Data** (creazione o scadenza? le chiavi scadono?).

## Da nascondere nello Swagger (campi interni o obsoleti, non citati nel sito)

- [ ] `parameters` (CreateNewProcessInput, CreateDocumentInput): uso interno.
- [ ] `sourceReference` (CreateDocumentInput, UpdateDocumentInput, UpdateDocumentContentInput, AddAttachInput): uso interno.
- [ ] `choice` (EseguiTaskInput): obsoleto.
- [ ] `scope` (UpdateTaskInput): obsoleto (nel codice imposta `task.ModuleText`).
- [ ] `attachmentGroup`, `attachmentType`, `attachmentRoot`, `attachmentPath` (LinkedProcessInput): errati, da togliere (arriverà `AddLinkedDocument`).

Nota: `tasks` e `processState` (GetProcess/GetDocument) restano documentati, senza struttura: sono lo stato JSON di task e processo prodotto da `TaskSerialization_SalvaStatoTaskSuClasse` e `WkfSerialization_SalvaStatoWkfSuClasse`, lo stesso salvato in alcune tabelle di BPM.

- [ ] Variabili Memo nelle risposte: oltre a `Text` e `HTML` compare `Testo`, duplicato legacy di `Text`, da togliere. Nel sito è documentato solo `Text`.

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
