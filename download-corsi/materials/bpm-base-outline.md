# BPM Base — Thematic Course Outline

Source: full transcript of Digit Company's "BPM Base" training course. This outline distills the course thematically (not strictly in recording order) as a seed for a reference-manual/tutorial document. Timestamps reference the recorded course; most correspond to entries in `bpm-base_timestamps.md`.

---

## 1. What is BPM

**BPM** = Business Process Modeler (Digit Company product). It is a graphical workflow/process modeling tool used to digitize activities that would otherwise be handled through unstructured means (email chains, spreadsheets, ad-hoc system customizations). [00:02:10]

- Core idea: everything starts from **the process** — the sequence of operations needed to manage a real-world case ("pratica"), e.g. the course's running example, an **investment-authorization request** process (from request submission to final "collaudo"/testing of the purchase).
- BPM is a standalone product: it can run independently, but in practice it is almost always connected to something else (an ERP/gestionale for master data, SAP, a document-management system). Pre-built connectors exist for SAP ("SAM"); generic ERPs require more custom integration work. [00:00:00]
- Digit Company maintains reference material for consultants: a website BPM section, a YouTube channel with overview/scenario videos, and an internally-shared Excel/PowerPoint of real-world application scenarios by business area (kept on SharePoint, and the instructor invites consultants to help keep it updated). [00:33:00]

### 1.1 Three architectural pillars

Every BPM solution is built from three things that recur throughout the whole course:

1. **The process** — the diagram of activities/tasks/gateways/events (Section 2).
2. **Users and groups** — who does what (Section 3).
3. **Process variables** ("magazzino delle variabili") — the data the process carries (Section 4).

[00:04:16], [00:08:48], [00:11:17]

### 1.2 Client vs. Web application

- **Desktop Client**: covers process modeling/design, configuration (users, dashboards, reports, structures, attachments, mail options), and operational use (start/search processes, To-Do List). This is where a consultant spends design time.
- **Web application**: operational-only (To-Do List, start new process, search, history) — no configuration/design surface. Recently rewritten to match the "Portale 6.0" visual theme and, per the instructor, intended to reach full functional parity with the client and become the **recommended client for end users** (used internally at Digit too). Historically the web lagged on some features (e.g. attachment management used to differ functionally, not just visually) — near-parity as of this recording, one remaining quarter of work mentioned. [00:28:35], [03:12:45], [03:29:29]
- The web app uses a **window/panel stacking model**: navigating from the To-Do List into a process detail keeps the To-Do List "behind" (recoverable via a stacking icon) rather than a full page navigation, so multiple records can be open at once. [03:24:00]
- Layout caveat: client and web use different fonts/spacing (web is more spacious/Bootstrap-based); a screen designed in one should be previewed in the other before rollout. Column/grid layout preferences (e.g. To-Do List columns) are stored **per user but separately** between client and web. [03:17:00], [03:14:00]
- The desktop client remains primarily for **design/configuration** and quick local testing while building a process. [03:29:29]

---

## 2. The Process Diagram (Designer)

### 2.1 Designer layout and workflow

The Designer has three panels: the **objects/tools palette** (grouped into Activities, Events, Gateways, Operations/automations, and other support objects), a **properties panel** (contextual to whatever is selected — clicking blank canvas shows process-level properties, clicking Start shows Start properties), and the canvas itself. A ribbon at the top holds drawing/alignment commands. [00:40:00]

- Objects can be opened, multiple processes can be worked on in parallel tabs, and tabs can even be split into a side-by-side view (useful for comparing/copying between two process models). [00:36:29]
- **Best practice**: sketch ("abbozzare") a rough version of the process quickly — even live with the client/business user — before refining names, rules and details. This is normal iterative practice, not a failure to plan ahead: draft → test → correct the course. [00:41:16], [00:53:00]
- **Terminology**: "Modello di processo" (Process Model) is the reusable template/design; "Processo" is a running execution/instance of that template. [00:39:42]

### 2.2 Core shapes

| Shape | Meaning |
| --- | --- |
| Green circle | **Start** event — where a process instance begins |
| Rectangle | **Task** — work to be done by a user/group |
| Round "state" shape | **Stato** — a milestone/checkpoint label (not work; a status marker, e.g. "Inserito", "Approvata") |
| Diamond | Implicit branch marker on a bare arrow's condition, or the dedicated **Gateway** object |
| Distinct box shape | **Sub-process** — a nested, separately-designed mini diagram |
| "Fine" circle | Optional, purely cosmetic end marker |

The notation used is a **subset of the BPMN standard** — not every BPMN shape is implemented, only those with functionality relevant to BPM. [00:48:41]

#### Activities (Tasks)

- Dragging a Task onto the canvas gives it a permanent internal code (Activity1, Activity2, ...) used as its immutable ID; the human-readable **display name** is set separately via right-click > "Modifica testo" (e.g. "Presa in carico da ufficio sicurezza"). [00:42:19]
- Tip: keep names clear but not overly long. Right-click > "Sposta testo" can detach a label visually from its shape (still logically linked) — occasionally useful for the Start event (e.g. relabeling it "Inserimento richiesta"). [00:43:00]
- The **Link** tool draws connections between shapes, creating anchor points; the ribbon offers alignment/same-size tools to keep large diagrams tidy (diagrams are seen by end users, so legibility matters). [00:44:44]

#### States (milestones)

A "Stato" object marks an important point in the process's overall lifecycle, independent of which specific task is active (e.g. "Inserito" at the start, "Approvata" at the end, "Annullata" on cancellation). States are purely labels with no special system meaning beyond being consultable/searchable later (e.g. querying "all cancelled requests"). [00:46:48]

#### End vs. Terminate

- **No explicit end object needed**: the general BPM rule is "when there are no more activities to do, the process is concluded" — automatically, with no special configuration.
- **Fine** (End): optional, purely visual/documentation marker with zero functional effect.
- **Termina processo** (Terminate process): functionally different — reaching this object forcibly kills/stops any other still-running branches of that process instance. [00:47:57], [00:48:30]

#### Sub-processes

A Sub-process shape hides a nested, independently-designed mini-flow behind a single box in the parent diagram (double-click to enter/design it). Uses:

- Keeping the top-level diagram clean/readable while still modeling detail underneath.
- **Evolving** a design: an existing simple Task can later be converted into a Sub-process if it turns out to need internal breakdown (e.g. splitting one "Approvazione" task into pre-approval/quality/technical steps) without redesigning the parent flow. [04:38:56]

**Recurring sub-process**: a sub-process can be bound to a **group** (master-detail variable set, Section 4.6) and flagged "ricorrente" — at runtime it spawns one full instance of its inner flow **per row** of that group (e.g. one evaluation mini-flow per supplier quote received). Configurable as:

- **Parallel** (all spawned instances open at once; assignee executes them in any order) — icon shows extra parallel bars.
- **Sequential** (one at a time; requires nominating the variable that determines execution order) — icon shows sequential lines.
- An optional "formula per condizione" can filter which rows actually spawn an instance.
The parent flow only proceeds past the sub-process once **all** spawned branches finish (synchronization/join). This pattern is valuable whenever the number of parallel sub-activities is only known at runtime, not design time — e.g. quality corrective/improvement actions, inspection/collaudo steps, or (as demoed) N supplier quotes to evaluate. Inside a group-bound recurring sub-process, that group's variables appear as **single-value** fields (you're conceptually "inside one row"); other groups' and header variables remain accessible as usual. [04:41:46], [04:43:00], [04:48:00]

### 2.3 Branching: conditions and gateways

Two equivalent-but-different-clarity ways to express branching logic in BPM, both built on the **formula engine** (Section 4.7):

1. **Bare conditioned arrows** ("il baffetto"/mustache-marked arrow): right-click an outgoing arrow > "Condizione di abilitazione" and write a formula (e.g. `esito approvazione CDG = "Approvata"`). Compact, but the engine does **not** enforce mutual exclusivity — outgoing conditions might overlap or leave gaps; it's the designer's responsibility to write complementary conditions. [02:33:44]
2. **Gateway object** (diamond in the palette): double-click/right-click > "Configurazione" shows *all* outgoing paths and their conditions in one screen; it evaluates them in order and takes the first true match, with one branch flaggable as the **default/"else"** (so N branches need only N−1 explicit conditions). More BPMN-"professional" and self-explanatory in the diagram, especially valuable once there are 3+ branches, at the cost of a bit more diagram real estate. [02:35:29]

Gateway variants:

- **Exclusive** (the default diamond): exactly one outgoing path fires — a strict if/else.
- **Parallel**: forks into simultaneous branches (e.g. "Collaudo" and "Parte amministrativa" both start together after approval); the same Gateway shape is reused downstream to **join**/wait for all forked branches to finish before the flow continues. Note: you *can* draw multiple unconditioned arrows out of a plain task to the same effect, but this isn't strict BPMN and the Gateway object is the clean way to express it. [02:43:27]
- **Inclusive**: a middle ground — any subset (0, 1, or several) of multiple outgoing branches can activate based on conditions, useful when branches are neither purely alternative (exclusive) nor purely mandatory-together (parallel). [02:45:43]

### 2.4 Runtime visualization

When consulting a running process instance, the diagram color-codes progress:

- **Grey** = activity already executed
- **Yellow** = activity currently in progress ("has the token")
- **Green** = active state (a Stato object currently in effect)
- **Light green** = "planned" — activities the engine already knows it will eventually reach (drives the **Gantt/planning view**); this set updates dynamically as data is collected, since the future path can depend on not-yet-known conditions.
- White/blank = not yet visited. [02:21:16], [02:24:00]

### 2.5 Publishing and versioning

- **Publish** ("pubblicare") makes a model live/usable by the users cited in it. It runs validation (shows warnings, but generally still allows publishing) and creates a new numbered version (R00, R01, ...); **all versions are retained** — both for technical reasons (in-flight instances reference older versions) and organizational/audit reasons. [00:15:36]
- A process model requires a **Nome modello** (model name — the key used to find/overwrite it) before it can be published or saved. Set via clicking blank canvas > process properties. [01:02:05]
- Two additional **process-level formulas** are required for a clean publish (validation warns if missing):
  - **Formula per il calcolo del nome del processo** — builds each instance's business-key title, typically from a counter/date variable, e.g. `[numero richiesta] & "/" & [anno]`.
  - **Formula per la descrizione del processo** — builds a free-form header string, e.g. `"Richiesta numero " & [numero] & " " & [stabilimento]`.
  These names/descriptions are what show up throughout the To-Do List, search grids and headers instead of raw internal IDs. [02:48:11]
- **Save to file**: a process (its entire design — diagram, variables, forms, formulas) can be exported to a single local **JSON file** (`.jbkf` extension) instead of/in addition to publishing — the standard way to move a configuration between environments (e.g. laptop → client environment). Reports and dashboards are the exception: they live independently since they can span multiple processes. [01:01:44]
- **Versioning behavior for running instances**: republishing does **not** retroactively change already-running instances — each instance stays pinned to whatever model version was active when it started. A process-level **"Aggiornamento processo"** button lets you manually catch up a specific running instance to a newer version (e.g. "Aggiorna dalla versione 16 alla 17"). Some changes (warehouse edits, new table bindings) are picked up automatically by running instances; UI/layout additions to an already-executed task's screen typically need this explicit upgrade action. If the version gap is too large/incompatible, the only fix is restarting the instance and manually replaying its progress. [04:02:24], [04:04:00]
- **Admin-only overrides** exist for exceptional cases:
  - **Force-edit warehouse values** on a running instance from its process-detail screen, outside normal flow ("forzatura extra processo") — requires confirm/discard on close, and is fully logged in Storico. [03:25:44]
  - **Force process advancement**: right-click a task in edit mode > "Imposta oggetto attivo" to skip/jump the engine to a given step — explicitly called "cheating" by the instructor, but useful during development (steps forgotten) or to unstick a real stuck process without a database update from a developer. [03:42:15]

---

## 3. Users, Groups and Task Assignment

### 3.1 Roles per activity

For each activity, BPM lets you name:

- **Esecutore** (executor) — the person/group who finds the task in their To-Do List. Used in ~90% of real cases. [00:08:48]
- **Responsabile** (responsible) — can dispatch the task to a specific member of their group.
- **In conoscenza** (CC/aware) — just needs to know the activity happened.

### 3.2 Two assignment patterns

1. **Direct group assignment** (the common case): assign a **group** (e.g. "Controllo di gestione") as Esecutore. All group members see the task in their To-Do List; the first one to act completes it and the process moves on. Groups are used instead of individuals because "people change but roles/groups remain," and groups are typically **purpose-built per process** rather than imported wholesale from Active Directory (AD groups rarely map to the granularity actually needed). [00:56:37], [00:54:11]
2. **Assign-then-execute**: flag "Task deve essere assegnato prima di poter essere eseguito" — adds an explicit dispatch step where a Responsabile first hand-picks a specific person from the group, and only that person then sees the task. More bureaucratic; used selectively (e.g. project/commessa scenarios with a technical-office triage step). [00:58:15]
3. **Dynamic assignment via a User-type variable**: the "Utenti e responsabili" dialog also lists the process's own **User-type variables** (e.g. "richiedente") as assignable executors — pick the variable and the task routes to whoever that variable currently holds. Classic use: sending a task back to whoever originally submitted the request. [02:42:35]

### 3.3 Development-time note

An activity temporarily left with no assigned user is visible only to the admin — this is fine during process design/testing but should be fixed before go-live (every activity should end up with a real owner). [00:58:15], [00:59:00]

---

## 4. Process Variables (the "Magazzino")

The **variable warehouse** ("magazzino delle variabili") is the single design surface holding every data field a process carries — accessed via Strumenti > "Inserimento modifica variabili", shown as an extra tab/page of the process. [01:05:43]

Mental model when designing: sketch the process → think through what data must flow in/out at each point → create the corresponding variables in the warehouse → then, per activity, pull in the relevant subset via **"Variabili da richiedere"** (Section 4.2). Variables auto-generate the underlying database fields — no manual SQL/table design required. [01:06:00], [01:10:00]

- Variables can be organized into multiple **pages** (tabs), conventionally prefixed `01`, `02`, `03`... since pages sort alphabetically. Good practice: loosely follow the process's chronological flow when organizing pages, for the sake of readability (not mandatory). [01:19:00], [00:25:00]
- Fields can be aligned/resized (multi-select with Ctrl) for a tidy end-user-facing layout — the design surface is literally what users will see. [01:11:00]

### 4.1 Variable types

| Type | Notes |
| --- | --- |
| String | Free text, default 250-character limit (suited to codes/short fields typically sourced from an ERP); can be flagged multiline |
| Numeric | Can be flagged as an auto-incrementing **Counter** (Perpetual, or grouped/reset by another field, e.g. reset per "anno"/year) [01:48:32] |
| Boolean | Renders as a checkbox by default, or as a stateful/stateless **Button** — see 4.8 |
| Date | Basic-settings mainly control formatting |
| Currency | A specialized numeric type |
| Memo | Long text/blob, effectively unlimited length, supports formatted/long notes |
| Value List | A fixed, small set of choices (a dropdown); supports separate internal **codice di iscrizione** (registration code) vs. display label, so relabeling doesn't break stored codes [01:19:07] |
| User type | Restricted to BPM users/groups registry; can be scoped to a specific group via "Tipo impostazioni di base" [01:09:00], [00:13:00] |
| Label | Read-only, non-persisted display text with a rich-text editor — see 4.4 |

### 4.2 "Variabili da richiedere" (per-task variable subset)

This is the counterpart, at the level of each Task/Start/button, of the global warehouse: right-click a task (or a variable, for its own sub-form) > "Variabili da richiedere" and drag in exactly the fields relevant there. [01:20:35]

Key relationship: the warehouse and every task's "variabili da richiedere" screen are **linked by variable name** (single source of truth per variable, one value per process instance) but **independent in layout/placement** — removing a variable from one task's screen doesn't delete it from the warehouse or reset its value elsewhere. [01:23:00]

Per-task/local settings on a placed variable (independent from its warehouse-level defaults):

- **Obbligatorio** (mandatory) — can be set globally in the warehouse or, better practice, locally per task (since a field might be required at one point in the process but not another). [01:42:00]
- **Sola lettura / Ridolli** (read-only) — e.g. to show upstream context data to a later task's user without letting them edit it (common pattern: reshow requester/date/type as read-only on a downstream task). [01:32:00]
- Local **Formula di validazione** (Section 4.7).

**Export/Import shortcut**: a page (or a task's whole "variabili da richiedere" layout) can be exported to a local file and imported into another task to avoid manually re-dragging many fields — heavily used when reusing a layout (e.g. copying the Start form into a later "Revisione da parte del richiedente" task). [01:22:54], [02:40:00]

### 4.3 Core variable properties

- **Name** — the internal/DB key; **immutable** once created.
- **Descrizione** (Description/label) — freely editable, localizable, shown next to the field; can be abbreviated ("Rich.") independently of the underlying name.
- **Descrizione su interrogazioni** — a separate label used specifically in search-grid columns, which can be more verbose/context-free than the in-form label.
- **Obbligatorio / Ridolli (read-only)** — as above, settable globally or locally.
- **Variabile senza salvataggio** — value not persisted to the DB, pure UI/interface state, typically paired with a formula-calculated display field you don't want stored. [01:43:00]
- **Sottocategoria** — assigning the same subcategory label to a Ctrl-selected group of variables draws a full-width grouping divider bar above them in the form, for visual organization of dense forms; the topmost variable's subcategory wins the bar position. [01:43:00]
- **Help text** — tooltip text shown on hover, useful for user guidance (e.g. "enter the amount per form XXXX"). [02:10:00]
- **Valore di default** vs. **Formula per default** — a fixed constant vs. logic-driven initial value (current user, current date, etc.) — see 4.7. [02:11:00]
- **Variabili di intestazione** (header/summary variables) — flag and number (1, 2, 3...) a handful of the most important variables (e.g. numero richiesta, codice stabilimento) so they surface prominently across the app (To-Do List columns, headers), beyond just the single process detail view. [02:12:00]
- **Tag**, hide-on-mobile flag, font size (small/medium/large — minor visual difference). [02:17:22]
- **Gruppo** — assigns a variable to a master-detail group (Section 4.6).

### 4.4 Label variables (read-only summary headers)

A Label-type variable is not a real DB field; it holds a rich-text "Testo" that can embed **variable placeholders** (via right-click > insert variable, e.g. "Richiesta numero {numero richiesta}") and even images (a pasted logo). A common pattern: replace several separately-dragged read-only fields on a task's form with a single label that composes them into a nicer, branded summary header — reused across multiple task screens. [01:33:19]

### 4.5 Source tables (lookups) — single value

"Tabella di origine" turns a String variable from free text into a **choice bound to a data source**:

- **Tabella locale** — a table created directly inside the BPM database (prefixed `P_...`), or a SQL **view** created there.
- **Dati esterni** — requires a connection string (server, database, user, password; SQL or ODBC) to an external system's database (e.g. a database also used by SAP/SAM). Named/reusable connection strings can be set up per company/environment (e.g. "SAM A1", "SAM B") rather than hardcoding a raw string per field.
- A discouraged-but-sometimes-used shortcut: create a **view inside the BPM DB that itself cross-database-points to the external system** — fragile (breaks when moved to a different client's environment) versus a clean external connection. [03:53:52]
- ODBC works but can be painful for some legacy systems (e.g. AS400); web services or dedicated connectors are often better for those. [03:57:00]
- Configuration requires mapping the **key column** (source table column → the driving variable, mandatory) and then arbitrary additional **column mappings** (other source columns → other target variables), so selecting one value auto-fills related denormalized fields (e.g. selecting a supplier code auto-fills its ragione sociale/company name). [03:58:00]
- **Lookup from the process's own group data** ("Variabili locali" source): instead of an external table, a field can look up a row from one of the process's own groups (e.g. letting the user "choose the winning quote" from the "Lista Preventivi" group already entered earlier in the same process, auto-filling a "Codice fornitore scelto"/"Ragione sociale scelta" pair). [04:54:39]
- **Pre-built connectors** (e.g. a SAM/SAP connector) are a related but distinct mechanism: configured per company (not a raw connection string) and, notably, sometimes the *only* supported way to **write** data back into the external system (vs. read-only via a plain connection). Deep dive reserved for later in the course. [04:01:10]

### 4.6 Group variables — master-detail (1-to-many) data

BPM's mechanism for 1-to-many data (e.g. N supplier quotes on one investment request):

1. Create a variable (e.g. "Codice Fornitore") normally in the warehouse.
2. Instead of leaving it single-valued, click the "..." config button and assign it to a new/existing **Gruppo** (e.g. "Lista Preventivi") — this turns it into the first column of a virtual detail/grid table.
3. Add more columns simply by **dragging additional variables directly onto the grid** — the fastest, most common way (99% of cases). Each additional variable dropped inside the grid auto-joins the same group. [03:32:36], [03:35:00]

Constraints and notes:

- A variable belongs to **exactly one** group.
- Groups are a **flat/single-level** structure — BPM deliberately does **not** support nested sub-groups, a usability tradeoff since end users/configurers are typically consultants, not programmers.
- A process can have multiple, independent groups (e.g. "Lista Preventivi" and a separate "Team utenti" group). [03:36:00]
- At runtime, the group renders as an **editable grid** where the user can add/remove rows freely (unless mandatory rules are added on the per-row fields, e.g. marking fornitore/importo mandatory *within* each row — a separate concern from "at least one row required"). [03:41:00], [03:45:00]
- A **stateless Button variable dropped into the grid** ("Dettagli...") can open a larger single-row pop-up form (via its own "Variabili da richiedere") — solves the problem of narrow grid columns cramping fields like long notes. [03:48:41]
- Group columns support the same **Tabella di origine** lookups as ordinary variables (Section 4.5), including looking up from another group's/the group's own local data.

### 4.7 Formulas

Formulas are BPM's built-in scripting layer, written in **Visual Basic** syntax, edited through a formula editor with a right-click helper menu (current year/user/date, and a searchable tree of all process variables by page). Excel-style one-liners work directly (e.g. `Year([data richiesta])`); multi-line logic requires an explicit `Return` statement and supports `If/Then/Else`. Formulas **recalculate automatically** whenever a variable they depend on changes (dependency tracking, like a spreadsheet). [01:52:58]

Formula types, and where they live:

- **Formula** (warehouse-level, "the" formula) — a globally-always-true calculated value, e.g. `anno = Year(data_richiesta)`, or a running total `totale_costi = importo_richiesta + costi_accessori`. [01:53:00], [02:06:07]
- **Formula di validazione** — set per-task on "variabili da richiedere" (not global); returns pass/fail to validate a field beyond a simple mandatory flag (e.g. `data_richiesta >= Today()`), and can set a custom error message shown to the user (`Errore = "..."`). Also usable to express "mandatory *if* [condition]", which a plain mandatory flag cannot do. [01:55:38]
- **Formula di visibilità** — dynamically shows/hides a field based on a condition. [02:00:00]
- **Formula per default** — sets a variable's *initial* value only, the first time it's opened while still unset (e.g. requester = current user, date = today); distinct from a fixed **Valore di default** constant. [02:01:33]
- **Formula per ridolli** — makes a field conditionally read-only under certain circumstances; considered a more advanced/specific technique. [02:03:00]
- **Condizione di abilitazione** — the formula attached to a transition arrow or gateway branch to control routing (Section 2.3).

Instructor's guidance: the engine is powerful enough for arbitrary complexity, but the recommendation is to keep formulas as simple as the business logic genuinely requires and not over-engineer. [02:09:00]

### 4.8 Buttons and "Variabili da impostare"

A Boolean variable can render either as a checkbox or as a **Button** (stateful — behaves like a toggle that stays "pressed" — or stateless, a pure command). Buttons are more powerful than a plain checkbox because actions can be attached to them:

- **Variabili da impostare**: an imperative alternative to a reactive Formula — attach an action list to a button that sets target variables only when clicked (e.g. a "Ricalcola totali" button explicitly setting `totale_costi`), as opposed to a Formula which recalculates automatically on every dependency change. Two variants of the same underlying goal, chosen based on whether "always live" or "only on demand" behavior is wanted. [02:13:22]
- **Aggiunta allegati** (add-attachment) button behavior — Section 5.2.
- A button can also carry its own **"Variabili da richiedere"** sub-form (Section 4.2), used both for standalone pop-up detail entry and for the group-row "Dettagli" pattern (Section 4.6).

---

## 5. Attachments

### 5.1 Concept

BPM has its own document/attachment management, always scoped **inside a process** (a document never lives standalone in BPM — it's always part of a process's "dossier"/"plico"). Documents can be organized into **virtual folders** created inside the process's Allegati tab ("Visualizza elenco" list view / "Visualizza struttura" tree view), e.g. "Preventivi", "Scheda Investimento". [04:07:16], [04:08:00]

Built-in **document viewer**: PDFs, Word, Excel, emails (.msg) and images preview directly inside BPM; other file types open via double-click in the OS-associated application. Emails/attachments can be **drag-and-dropped directly from Outlook**, useful when a process is triggered by an email exchange. [04:11:00], [04:32:00]

### 5.2 Enabling attachments per task

**"Allegati da richiedere"** is the file-management counterpart of "Variabili da richiedere":

- Toggles attachment support on/off for a given task.
- Can pin the task's default target folder (e.g. Start pins to "Scheda Investimento").
- Can be set **read-only** on a task purely to expose visibility of already-collected documents without allowing edits (e.g. showing all attachments, read-only, on a later review step). [04:09:24], [04:10:00]

A **mandatory required-attachment pattern**: create a stateless Button variable (e.g. "Inserisci scheda richiesta"), configure it in "Tipo impostazioni di base" as **Aggiunta allegati** (add-attachment), pick a target folder and optionally restrict allowed file extensions, then drag it into a task's "variabili da richiedere" and mark it mandatory — pure configuration, no scripting, to force a specific required document upload before the process can advance. Applied at the process level (e.g. a required "scheda investimento" PDF at Start) and at the group-row level (e.g. an "Allega preventivo" button inside each quote row of a detail grid). [04:22:44]

### 5.3 Storage: Database vs. File System

A new process is born with a default **DB-backed** attachment root ("Attachments" — the file's stream stored as a table inside BPM's own database). Additional **root folders** can be created:

- **On database**, or
- **On file system**, given a base path (typically a network share reachable by everyone) that can be **built dynamically from process variables** (e.g. a path pattern combining stabilimento + numero richiesta), so BPM auto-creates a real per-instance subfolder on disk at runtime — matching how many clients already organize shared-drive documents by plant/request number. [04:13:00]

Roots of both kinds can be **freely mixed** within one process; visually, file-system folders get a distinct (blue-tinted) folder icon in the tree, but functionally, from inside BPM, drag-and-drop upload works identically either way. Right-click on a folder offers different admin capabilities depending on storage type. [04:16:00]

**Caveats**:

- DB-stored attachments are fully governed by BPM (delete in BPM = gone; BPM permissions apply).
- FS-stored attachments remain independently accessible/editable/deletable **directly on the share, outside BPM** — a real gap, since BPM's permission model does not govern file-system-level permissions (two permission systems to maintain in parallel). Instructor's personal opinion: FS-based storage is conceptually the "wrong" choice for a proper document-management approach (security/logging/access should live in SQL), but it's pragmatically supported and used in practice, especially for a lighter initial rollout when a client already has FS-organized documents (deferring the "proper" DB migration to a later project phase). [04:19:00], [05:02:00]
- BPM can also **pre-generate a whole folder-tree template** on process creation (mimicking a typical commessa/project folder structure — preventivi/disegni/schede tecniche/...), useful for clients already working with such conventions. [04:19:00]
- Best practice for FS root paths: store the server name in an **environment variable** rather than hardcoding it in every path formula (rarely actually done in the field); some clients instead keep a SQL table mapping each process to its root folder paths. [05:01:00]

### 5.4 Attachment-level metadata & versioning

- An attachment can carry **custom metadata columns** (distinct from process variables) that get bound to the value of a process variable at upload time (e.g. adding a "Ragione Sociale" column to the attachment grid, bound to that quote row's supplier name) — a denormalized snapshot captured on the file itself. [04:33:00]
- Standard attachment attributes include **Revisione** (revision) and **Stato** (Attivo/Obsoleto). Versioning today is **manual only**: an attachment can be marked "Obsoleto" and the view toggled to show/hide obsolete ones (e.g. reattaching a revised document when a process loops back) — there is no automatic version-chaining. [05:03:00]
- Attachment uploads are tracked in **Storico** (Section 7) just like variable changes.
- No hard file-size limit is enforced by BPM itself (very large files just risk timing out/being slow); a **maximum size** can be explicitly configured on an "Aggiunta allegati" button. [05:00:00]
- Attachments can (topic reserved for a later session) be integrated with Digit's document-management product ("Globo") so files live there instead of in BPM. [04:21:00]

---

## 6. Running Processes: To-Do List, Search & Execution

### 6.1 To-Do List

The concrete, day-to-day interface for participating in processes. Opens by default on login. [00:19:06]

- **Filters**: user scope ("Tutti gli utenti visibili" = admin sees everyone; "Tutto" = my own + my groups' tasks — the normal filter for regular users), date range (day/week/month/all open), and **activity state**.
- **Three activity states**, visible both here and in the diagram: **Eseguita** (completed), **In corso** (available now), **Pianificata** (planned/future — light green). [02:55:52]
- Grid supports right-click **grouping** (e.g. by process model) and column reordering; layout preferences are **saved per user automatically**. Default columns include Utente, Attività, Modello, Nome processo, Data inizio prevista, Priorità (a free label with no functional meaning beyond sorting/reminders), Scadenza, % completamento. [02:58:06]
- **Executing a task**: click "Esegui" to fill fields (validated against mandatory/formula rules — a red indicator blocks submission until satisfied); **Completato** submits and advances the process; **Salva/Salva e chiudi** persists a draft without advancing (data is kept for later). [03:00:00]

### 6.2 Process detail / inspection screen

Accessed from the To-Do List (subject to view/edit permissions — Section 8). Tabs:

- **Variabili** — the full warehouse, laid out per the same page/tab structure designed earlier.
- **Intestazione** (header/anagrafica) — fixed system fields: process name, description, source model, current activity, creation date, owner (who started it).
- **Allegati** — the document dossier (Section 5).
- **Processi collegati** — links to other related process instances.
- **Pianificazione** — time-axis/Gantt-style scheduling info.
- **Storico** — the full audit log (Section 7). [03:03:22]

This screen is often used by a process **owner** to monitor progress/timing/status across instances; access can be granted read-only or read-write depending on audience. [03:07:00]

### 6.3 Search

"Ricerca processi" returns **one row per process instance** (not per task), covering both open and closed/archived instances (nothing is deleted unless an explicit archiving policy is applied). [00:24:41], [02:56:00]

- Default view ships with many generic system columns of limited interest; **"Modifica visualizzazione"** lets you pick the relevant ones (e.g. anno, codice stabilimento, richiedente, tipo richiesta, importo, note).
- Multiple named views can be saved; marking one **"Pubblicato"** makes it visible to all users, not just its creator — a typical admin task is building good default search views for end users, since the out-of-the-box default is not very useful. [03:08:53]
- Grids throughout BPM (To-Do List, search, warehouse-linked grids) support both dropdown-style and free-text column filters. [03:11:00]

### 6.4 Custom menu entries

Configurazione > Opzioni generali > **Menu personalizzati** lets an admin add direct shortcuts (up to 3 levels: root menu / submenu / description) bound to a specific process action (e.g. "start Richiesta INV" or "search Richiesta INV requests"), letting end users bypass the generic "Nuovo processo"/"Ricerca processi" menus. Custom menus only refresh on next login/app restart. [03:20:17]

---

## 7. History / Audit Log (Storico)

Every view, edit, and task execution against a process instance is logged with **timestamp + user** (e.g. created 14:38, viewed 14:41, modified fields 14:45/14:47, executed task X at 14:47...). Double-clicking a log entry shows a **field-level before/after diff** of exactly what changed. [03:06:14]

Purpose: besides plain traceability, this is explicitly called out as valuable for **quality/compliance certification** — proving that a designed procedure was actually followed as specified. Visibility of Storico to end users (vs. just admins/owners) is a configurable choice. [03:07:00]

---

## 8. Permissions & Security

### 8.1 Baseline rule

**A user or group merely cited in a process** (as Esecutore/Responsabile/in conoscenza on some activity) automatically sees and can act on that activity in their To-Do List — **no additional permission grant is required** for that alone. Permissions govern everything *beyond* that baseline (search, general process creation from the menu, admin-style overrides, table/dashboard/report access). [05:05:25]

### 8.2 Users and groups

- Users and Groups share one underlying table/grid, filterable by type. A user has a name (free string, naming convention is a matter of taste), and an **email** (important — used for BPM-triggered notification mails). [05:06:00]
- A BPM user can **optionally** be linked to a Windows/domain account. Effect: the desktop **Client gets automatic single sign-on** when linked; the **Web client still prompts for the domain password** in this version (no web SSO yet) — the "last used username" shown on web login is just a cookie, not true SSO. [05:07:05]
- **Group membership serves two distinct purposes** that often overlap but aren't identical: (a) inheriting that group's *permissions*, and (b) being a participant who receives tasks assigned to that group in one or more processes. A user is typically in multiple groups for these different reasons at once. [05:10:00]

### 8.3 Permission categories

1. **Permessi Menu** (application-wide) — enable/disable whole app areas: change password, access a "page", start new process (generic), view in-progress processes, etc. Split into an **operational** set (home, new process, in-progress, To-Do-on-process-screen, import, attachments, planning) and a **configuration** set (manage process models, tables, config, view/edit users) — ordinary end users typically get none of the configuration-set permissions. [05:12:06]
2. **Permessi Processi** (per specific process model) — fine-grained, off by default (red): **Creazione** (start a new instance of this model — note: also requires the generic "new process" *menu* permission to be on, i.e. AND logic across the two levels), **Visualizzazione** (open/search the process detail read), **Modifica** (force-edit values — the admin-override capability from 2.5), **Eliminazione** (permanently delete a specific instance — distinct from full system-admin rights; can be granted to a non-admin "process owner"), **Copia/Duplica**, **Cambio stato processo** (force-advance, same mechanism as the admin override). [05:12:06], [05:21:00]
3. **Permessi Tabelle** — per local BPM table, separately for Visualizza (browse the standalone table-management area) vs. Modifica (edit records) — distinct from simply using that table as a lookup source inside a process form. [05:28:00]
4. **Permessi Dashboard / Report** — per-dashboard and per-report grant (dashboards especially often restricted, since they can expose sensitive figures like monetary totals). [05:29:00]
5. (Briefly mentioned, not detailed in this course) **Prefiltri/alias** on data access. [05:30:00]

### 8.4 Resolution logic and best practice

- Rights resolve **additively** from two sources: direct **user**-level grant, or **inherited via group** membership (UI marks a right "abilitato da gruppo" when inherited).
- **Best practice: grant via groups, not individuals** — e.g. create a permission-only group "Inserimento richieste INV", grant it Creazione on "Richiesta INV", then add users to that group. Rule of thumb: *"if you end up with as many or more permission-groups than users, something's probably wrong with the design."* [05:12:06]
- **Enable/Deny override semantics**: enabling a permission directly on a user when they already have it via a group makes the grant "sticky" (it survives later removal from the group); removing a redundant user-level grant that's still covered by the group does nothing; a user-level **"Nega" (Deny)** overrides a group-level Enable, letting you exclude one specific member from an otherwise group-wide grant. [05:26:05]
- **What a typical end user actually needs**: for a user who only ever *receives and executes* tasks from the To-Do List, essentially **no extra permissions** are required beyond being cited in the process (attachments and fields they need are already exposed via the task's own "variabili/allegati da richiedere" config). The one commonly-needed addition is **Creazione** (start new process), for whichever users initiate new requests via the generic menu (not needed if they only ever act on assigned tasks). Broader access like Visualizzazione/Modifica/Eliminazione is reserved for process owners/admins, not rank-and-file participants. [05:23:00], [05:26:00]

### 8.5 Instructor's closing framing

At a basic level, the permission system requires relatively little configuration, because most of the access-control "thinking" is expected to happen inside the **process design itself** (who is cited on which task, via which group). The finer-grained permission matrices (menu/process/table/dashboard/report) are an advanced layer that a first "base" course can mostly gloss over — this closing point marks the end of the fundamentals part of the course, with SAP integration, document-management (Globo) integration, connectors, and deeper dashboard/report coverage reserved for later sessions. [05:30:21]

---

## Appendix: Glossary of BPM-specific terms used in the course

- **Magazzino delle variabili** — the variable "warehouse": the full design surface/repository for all of a process's data fields.
- **Variabili da richiedere** — the per-task (or per-button) subset of variables shown/collected at that specific point.
- **Allegati da richiedere** — the file-attachment counterpart of the above.
- **Gruppo** (of variables) — a master-detail/1-to-many grouping of variables into a virtual grid.
- **Tabella di origine** — a lookup/source-table binding for a string field (local table/view, external DB, or local process-group data).
- **Ridolli** — the instructor's term for a read-only field/setting.
- **Pubblicare** — publish a process model, making it usable and versioned.
- **Pallino in mano** — informal phrase ("holding the token") for wherever a process instance currently is in its flow.
- **Plico / dossier** — the accumulated bundle of attachments a process instance collects over its lifetime.
- **Sottoprocesso ricorrente** — a sub-process that spawns one instance per row of a bound group.
