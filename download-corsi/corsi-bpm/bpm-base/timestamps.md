# BPM Base — Course Timestamps

Source: full transcript of the "BPM Base" training course (Digit Company BPM product). Timestamps refer to the course recording. Descriptions are translated/paraphrased from the original Italian audio.

| Timestamp | Category | Title | Description |
|---|---|---|---|
| [00:02:10] | definition | What BPM stands for | Instructor defines BPM = Business Process Modeler: a graphical modeler used to design a workflow/flow diagram that digitizes activities otherwise handled by email, Excel, or ad hoc customizations. |
| [00:04:16] | concept-intro | Process = activities, drawn in the Designer | Introduces the process as the central BPM concept, built from activities placed via drag-and-drop in the graphical Designer. |
| [00:04:58] | concept-intro | Task and Start shapes | The rectangle represents a Task (user activity); the green circle represents the process Start event. |
| [00:05:11] | concept-intro | Gateway (diamond) for branching | The diamond shape marks a branch point/condition where the process can take alternative or parallel paths. |
| [00:07:07] | concept-intro | Operations = automations | "Operazioni" are automation objects (send mail, call a web service, query an external system) since a process rarely lives in isolation from other systems. |
| [00:08:48] | concept-intro | Users & roles: executor, responsible, CC | Second BPM pillar: for each activity you assign an Executor (gets the task in their To-Do List), a Responsible (can dispatch within their group), and users kept "in conoscenza" (aware/CC only). |
| [00:09:52] | concept | To-Do List is the execution mechanism | The BPM engine surfaces work to users purely through the To-Do List; activities move forward as users complete their tasks. |
| [00:11:17] | concept-intro | Process variables ("magazzino") | Third pillar: process variables are the information fields a process carries (requester, date, request type, etc.), defined via a form designer, not hard SQL tables. |
| [00:15:36] | definition | Publishing a process | "Pubblicare" makes a process model live/usable; each publish creates a new version (R00, etc.) and full version history is retained. |
| [00:17:14] | demo-start | Starting a process instance | Demo of "Avvia processo": picks the model, shows the Start form with default values and mandatory-field validation. |
| [00:19:06] | concept-intro | Watching the token move | Clicking a running process shows a graphical view of "who has the token", the current state (green dot), and the active task. |
| [00:24:41] | demo | Searching and filtering process instances | Search grid returns one row per process instance (open or closed); columns can be added from variables and filtered (e.g. by requester, plant, date). |
| [00:28:35] | concept-intro | Client vs. architecture overview | BPM ships as a desktop Client (design/config + operational use) and a separate Web app (operational only: To-Do List, start/search process). |
| [00:36:29] | demo-start | Designer menu tour | Tour of the hamburger menu: "Modelli di processo" (design), "Configurazione" (settings/users), "Sistema" (system/debug tools). |
| [00:39:42] | definition | Model vs. process instance | "Modello di processo" = the template; "processo" = a running execution/instance of that template. |
| [00:41:16] | tip | Sketch first, refine later | Best practice: rough out ("abbozzare") the process diagram quickly, even together with the client, before refining details. |
| [00:42:19] | tutorial-step | Creating and naming activities | Dragging an activity gives it an immutable internal code (Activity1, Activity2...); the display name is set via right-click > "Modifica testo". |
| [00:44:44] | tutorial-step | Connecting activities with the Link tool | Using the Link tool creates connectors between shapes; alignment/resize tools help keep the diagram tidy. |
| [00:46:48] | concept-intro | State objects (milestones) | "Stato" objects mark important checkpoints (e.g. "Inserito", "Approvata") distinct from Tasks, which represent work to be done. |
| [00:47:57] | tip | End is optional, cosmetic | A process concludes automatically once no activities remain; the explicit "Fine" object has no functional effect, only visual clarity. |
| [00:48:30] | concept-intro | Fine vs. Termina processo | "Termina processo" forcibly kills any other still-running branches of the process, unlike "Fine" which does nothing functionally. |
| [00:49:37] | tutorial-step | Sketching loop-back / rejection paths | Adds a "back to requester" path and an "Annullata" (cancelled) state as example alternative outcomes. |
| [00:54:11] | tutorial-step | Creating users and groups | In Configurazione > Utenti e Gruppi, creates groups (e.g. "AM", "Direzione Tecnica") — groups are usually purpose-built per process rather than reused from Active Directory. |
| [00:56:37] | tutorial-step | Assigning a group as task executor | Sets group "AM" as Esecutore on "Approvazione controllo di gestione" — all group members receive the task, first to act completes it. |
| [00:58:15] | concept-intro | "Must be assigned before execution" flag | Alternative assignment mode: a responsible person must first dispatch the task to a specific group member before it can be executed. |
| [01:01:44] | tutorial-step | Save process to file | A process can be exported to a local JSON file (portable between environments) instead of/alongside publishing to the BPM database. |
| [01:02:05] | tutorial-step | Naming and publishing the model | Sets "Nome modello" (e.g. "Richiesta INV") in process properties, a prerequisite for publishing; publish yields version R00. |
| [01:05:43] | demo-start | Opening the variable warehouse | Strumenti > "Inserimento modifica variabili" opens the "magazzino delle variabili", the design surface for all process data fields. |
| [01:07:11] | tutorial-step | Creating the first variable | Creates variable "richiedente" (default String type), drags it onto the form canvas. |
| [01:08:50] | concept-intro | Variable type catalogue | Overview of variable types: String, Numeric, Boolean, Date, Currency, Memo, Value List, User type. |
| [01:20:35] | concept-intro | "Variabili da richiedere" per task | Right-click a task/Start > "Variabili da richiedere" defines which warehouse fields are shown/collected at that specific point in the process. |
| [01:22:54] | tip | Export/import variable layouts | A page of variables can be exported to a local file and imported into another task's form to avoid manually re-dragging fields. |
| [01:33:19] | concept-intro | Label-type variable | A Label is a read-only display element (not a real DB field) with a rich-text editor that can embed variable placeholders and images (e.g. a logo/summary header). |
| [01:39:29] | definition | Variable name is immutable | The variable's internal name (DB key) can never change once created; only its Description/label text can be edited (and localized). |
| [01:43:00] | concept-intro | "Variabile senza salvataggio" | A variable can be flagged to not persist to the database — pure UI value, typically paired with formula-calculated fields. |
| [01:45:03] | concept-intro | Tabella di origine (source table) | Any string variable can be bound to a lookup source — a local BPM table, a SQL view, or an external database — instead of free text entry. |
| [01:48:32] | concept-intro | Numeric field as a counter | A numeric variable (e.g. "numero richiesta") can be set as an auto-incrementing counter, optionally grouped/reset by another field like "anno" (year). |
| [01:51:23] | concept-intro | Autocomplete on string fields | "Autocomplete" proposes previously-used distinct values for a field as a free-typed suggestion combo — a lightweight alternative to a full lookup table. |
| [01:52:58] | concept-intro | The formula editor (Visual Basic) | Introduces the Formula concept: per-variable calculated logic written in Visual Basic syntax, with a right-click helper menu (current year/user/date, variable search). |
| [01:55:38] | concept-intro | Formula di validazione | A per-task validation formula returns true/false to validate a field beyond simple mandatory, and can set a custom error message shown to the user. |
| [02:00:00] | concept-intro | Formula di visibilità | A formula that dynamically shows/hides a field based on a condition. |
| [02:01:33] | concept-intro | Formula per default vs. Valore di default | Default-value formula sets a field's initial value only (e.g. current user, current date), unlike the fixed constant "Valore di default". |
| [02:06:07] | example | Calculated total via formula | Worked example: "totale costi" = "importo richiesta" + "costi accessori", auto-recalculating whenever the dependencies change, Excel-style. |
| [02:13:22] | concept-intro | Variabili da impostare (button actions) | A stateless Button-type variable can trigger an imperative action list ("variabili da impostare") that sets other variables on click, as an alternative to a reactive formula. |
| [02:21:16] | tip | Diagram color coding | Grey = executed, yellow = in progress (has the token), green = active state, light green = planned (feeds the Gantt view). |
| [02:29:14] | concept-intro | Conditions drive approval branching | Approval flows are built from ValueList outcome variables (e.g. "esito approvazione CDG") referenced in transition conditions. |
| [02:33:44] | tutorial-step | Condition on a transition arrow | Right-click an outgoing arrow > "Condizione di abilitazione" to attach a formula-based enabling condition to that specific path. |
| [02:35:29] | concept-intro | Exclusive Gateway object | The dedicated Gateway shape lists all outgoing conditions in one screen, guarantees exactly one branch fires, and supports a default/"else" branch. |
| [02:42:35] | tip | Dynamic assignment to a process-variable user | A task can be routed to whoever a User-type variable (e.g. "richiedente") currently holds — classic pattern for sending work back to the request originator. |
| [02:43:27] | concept-intro | Parallel gateways (fork/join) | Gateway objects can fork a process into simultaneous branches and later rejoin/wait for all branches to complete before proceeding. |
| [02:45:43] | concept-intro | Inclusive gateway | A third gateway variant allows any subset (0..N) of branches to activate based on conditions, between strict AND (parallel) and strict XOR (exclusive). |
| [02:48:11] | tutorial-step | Process name & description formulas | Process-level "Formula per il calcolo del nome/descrizione del processo" builds a human-readable instance title (e.g. numero/anno), required before publish. |
| [02:55:52] | concept-intro | Three activity states | Every BPM activity exists as Eseguita (completed), In corso (available now), or Pianificata (planned/future) — visible in the diagram and as To-Do List filters. |
| [02:58:06] | tutorial-step | Customizing the To-Do List grid | Right-click column headers to group (e.g. by process model) and reorder columns; layout is persisted per user automatically. |
| [03:03:22] | demo-start | Process detail / inspection screen | Opens the full process record from the To-Do List: Variabili (warehouse), Intestazione (header/anagrafica), Allegati, Processi collegati, Pianificazione, Storico tabs. |
| [03:06:14] | concept-intro | Storico: full audit log | Every view, edit and task execution is timestamped per user; double-clicking a log entry shows a field-level before/after value diff. |
| [03:08:53] | tutorial-step | Custom search views | "Modifica visualizzazione" lets you pick relevant columns for a search grid, save multiple named views, and mark one "Pubblicato" so all users see it. |
| [03:12:45] | demo-start | Web client walkthrough | Tour of the web app (Portale 6.0 styling): To-Do List, Dashboard, Avvia processo, Ricerca processo, Storico — same engine/rules as the desktop client. |
| [03:20:17] | concept-intro | Custom menu entries | Configurazione > Opzioni generali > Menu personalizzati adds direct shortcuts (up to 3 levels) to start or search a specific process, bypassing the generic menus. |
| [03:25:44] | tip | Admin force-edit outside the process flow | A user with rights can open a running process in "Modifica" mode and directly overwrite warehouse variable values; every such change is logged in Storico. |
| [03:32:36] | concept-intro | Group (master-detail) variables | A variable assigned to a "Gruppo" becomes a column of a virtual detail/grid table (e.g. one row per supplier quote) — 1-to-many data inside a single process record. |
| [03:42:15] | tip | Admin-only force process advancement | Right-click a task in Modifica mode > "Imposta oggetto attivo" lets an admin manually skip/force the process to a given step — explicitly framed as "cheating", useful in development and stuck-process fixes. |
| [03:48:41] | concept-intro | Detail pop-up form for a grid row | A Button-type variable inside a group grid can open its own "Variabili da richiedere" sub-form, giving a larger single-record view of one detail row. |
| [03:53:52] | concept-intro | Source table lookup: local vs. external | Configuring "Tabella di origine" for a group column: local BPM table/SQL view, or an external DB via a connection string (server/database/user/password, SQL or ODBC). |
| [04:01:10] | concept-intro | Preview: Connectors (e.g. SAM) | Brief preview of pre-built connectors (e.g. to SAM) as an alternative, company-scoped way to read — and in some cases the only way to write back — external data. |
| [04:02:24] | concept-intro | Versioning: running instances pin to their version | Republishing a process does not affect already-running instances, which stay on their original version until explicitly upgraded via "Aggiornamento processo". |
| [04:07:16] | concept-intro | Attachments overview | The BPM has its own document-attachment system: documents live inside a process's "dossier", organized into virtual folders, stored in DB and/or file system. |
| [04:09:24] | concept-intro | Allegati da richiedere | The per-task counterpart of "Variabili da richiedere" for files: enables attachment management on a task and can pin its default target folder. |
| [04:13:00] | concept-intro | Storage roots: Database vs. File System | New attachment "root" folders can be DB-backed or FS-backed (with a path built dynamically from process variables); the two can be freely mixed. |
| [04:22:44] | tutorial-step | Mandatory attachment via a button | A stateless Button variable configured as "Aggiunta allegati" (target folder + allowed extensions) can be made mandatory to force a required document upload. |
| [04:38:56] | concept-intro | Sub-processes | The Sub-process shape encapsulates a nested, separately-designed mini-diagram, used to keep the top-level flow clean or to later expand a simple task into detail. |
| [04:41:46] | concept-intro | Recurring sub-process | A sub-process bound to a group spawns one instance of its whole inner flow per row of that group (parallel or sequential), for an a-priori-unknown activity count. |
| [04:54:39] | concept-intro | Lookup from local group data | "Tabella di origine" > "Variabili locali" lets a field pick one row from the process's own group data (e.g. choosing the winning quote) and auto-fill denormalized columns. |
| [05:05:25] | concept-intro | Permission baseline: citation is enough | A user/group merely cited in a process (as executor/responsible/CC) needs no extra permission grant to see and act on that activity. |
| [05:07:05] | concept-intro | Domain-linked users & single sign-on | A BPM user can optionally be linked to a Windows domain account, giving automatic SSO on the desktop client (web still prompts for the domain password). |
| [05:12:06] | concept-intro | Permission categories overview | Users have Menu permissions (app-wide), Processi permissions (per model: create/view/edit/delete/duplicate/force-state), plus separate Tabelle/Dashboard/Report permissions. |
| [05:26:05] | tip | Enable vs. Deny override semantics | A user-level "Nega" (Deny) overrides a group-granted permission, letting you exclude one specific member from an otherwise group-wide grant. |
