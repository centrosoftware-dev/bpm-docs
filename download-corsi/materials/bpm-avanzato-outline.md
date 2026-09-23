# BPM Avanzato — Thematic Outline

Source: full transcript of the "BPM Avanzato" course (Digit Company BPM Designer), ≈5h17m, follow-up to "BPM Base." This outline is organized by topic (not chronologically) to seed a reference manual. Timestamps in `[HH:MM:SS]` point into the course recording; they mostly match `bpm-avanzato_timestamps.md` but a few extra ones are added here for finer granularity.

---

## 1. Data Grids (Griglia Dati)

**What it is:** A special kind of process variable, distinct from both a simple field and a group (header/detail). A data grid is a *single* object that renders a **read-only** grid bound to a database table — local or external. `[00:15:53]`

**Why/when to use it:** To show the user contextual reference data without leaving BPM — e.g. all orders for the client code entered on the form, the rows of a purchase order being approved, a budget table, etc. It's not a data-entry structure (that's what groups are for); it's a live lookup window. `[00:17:01]`

**How it's configured:**

1. Create a variable and set its type to Data Grid, just like creating any other variable.
2. Open its configuration (same screen used for table-bound fields) and pick a source table (local `P_` table, view, or external connector table).
3. Choose which columns to expose and optionally rename their captions (useful when source column names are cryptic/foreign). `[00:18:07]`
4. Place it in the form/warehouse/"variabili da richiedere" like any variable, giving it enough screen space.
5. Publish and reopen a process instance — the grid appears, populated, filterable and groupable exactly like other grids in the product, but not editable.

**Tip:** A data grid can point to the *same* underlying tables used for field-lookups ("aggancio tabella") — it's the same mapping mechanism, just rendered as a persistent grid instead of a combo/lookup popup.

---

## 2. Group Variables: Filtering, Conditions & VB-Script Formulas

### 2.1 Per-task filtering of group rows

**What it is:** A group (header/detail, 1-to-many) variable can be filtered *differently* per task/screen it appears on, without touching the underlying data. `[00:22:48]`

**Why:** Real example — two parallel review activities (“valutazione preventivi tipo A” / “tipo B”) both use the same “lista preventivi” group, but each reviewer should see only their type. `[00:26:00]`

**How:**

- In "variabili da richiedere," select any variable belonging to the group; local settings let you disable add/delete of rows (read-only browsing) and apply a **filter condition** (e.g. `tipo preventivo = "tipo A"`). `[00:27:06]`
- Repeat on the parallel task with the opposite filter.

**Real anecdote:** A quality-control process routed pieces to two different plants based on piece type using exactly this pattern. `[00:23:01]` (context around 27:00)

### 2.2 Conditionally enabling a path based on group content

**What it is:** Using a VB-script formula on a link's **enabling condition** to prevent the process from taking a path when a group has zero matching rows (e.g. don't open the "type A review" branch if there are no type-A quotes). `[00:28:38]`

**How (worked example):**

- Right-click inside the condition editor to browse variables; picking a group member offers pre-built helper expressions (e.g. `Count(tipo preventivo) > 0`), but a plain count on the whole group isn't precise enough when you need to count only matching rows.
- **Tip — no debugger exists in BPM.** Because there's no way to step through/inspect formulas, the instructor recommends creating throwaway helper variables in the warehouse (e.g. `presenza tipo A`, `presenza tipo B`, string type) just to visualize what a formula computes while building it. `[00:30:43]`
- Write the counting logic as a formula on the helper variable itself (a "formula" on that field, which auto-recalculates whenever data changes):

  ```vb
  Dim i As Integer
  For i = 0 To lista_preventivi.Count - 1
      If tipo_preventivo(i) = "tipo A" Then
          Return "sì"
      End If
  Next
  Return "no"
  ```

  `[00:34:15]`
- **Gotcha:** `Return` exits the formula immediately — unlike some other languages (Delphi was mentioned), execution does not fall through past a `Return`. `[00:38:18]`
- The gateway's enabling condition then simply checks `presenza tipo A = "sì"`.

**Access pattern to remember:** `variabile(i)` is how you index the i-th value of a group-member variable across all rows — this pattern recurs constantly for group-based logic.

### 2.3 Field-level vs. global validation formulas

- **Field-level "formula di validazione":** attached to a single field; checked as soon as that field is edited (e.g. reject an amount > 1000).
- **Global validation formula:** a separate formula for the *whole screen*, evaluated only when the user clicks "completed" on the activity. Used for cross-field business rules, e.g. "at least one quote of any type must exist before continuing":

  ```vb
  If Count(tipo_preventivo) = 0 Then
      MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
      Return False
  End If
  Return True
  ```

  `[00:39:44]` `[00:41:04]`
- Note: `Return True` at the end is technically optional/implied, but adding it explicitly avoids ambiguity.

---

## 3. Gateways & Flow Control

### 3.1 Legacy sync bar ("sbarra di sincronizzazione")

**What it is:** The original/classic BPM object for joining parallel branches — visually a "gate" that only opens once all configured incoming branches have arrived. `[00:43:44]`

**Configuration modes:**

- **ALL:** waits for every branch that was *configured* to feed into it, regardless of whether that branch was actually taken/started this time.
- **ALL PLANNED** ("tutte pianificate" / all-launched): waits only for branches that were *actually started* in this instance — critical when the upstream split is conditional (e.g. an inclusive gateway that might only open one of two paths). Using plain "ALL" in that situation would deadlock the process. `[00:45:34]`
- A sync bar can also carry a **custom activation formula** instead of ALL/ALL PLANNED, for cases needing arbitrary logic (real project: "Veneta Cucine"). `[00:50:45]`

### 3.2 Modern BPMN-style gateway object

Three usages of the *same* diamond-shaped gateway object, distinguished by configuration: `[00:47:00]`

- **Percorsi alternativi (exclusive):** exactly one outgoing path is taken; outcomes are mutually exclusive.
- **Percorsi paralleli (parallel/AND):** all outgoing paths are always taken, unconditionally.
- **Percorsi liberi (inclusive/OR):** one, several, or all outgoing paths can be taken depending on each path's condition.

**Configuration:** double-click (or right-click → Configuration) to set a condition per outgoing path. `[00:48:36]`

**Constraint:** a gateway object is strictly **either** a fan-out (1 input → n outputs) **or** a fan-in (n inputs → 1 output) — the designer blocks (draws the connection red) any attempt to give it both. The same shape automatically becomes a "join" when you wire multiple incoming links into a single outgoing link; when used as a join it needs no configuration (it simply waits for whichever branches were actually taken to complete). `[00:50:00]`

**Recap — default path ("diamantino"):** the black diamond marks the default/fallback path taken when no explicit condition matches, so the process never gets stuck. `[03:07:14]`

---

## 4. Diagram / Canvas Objects

### 4.1 Purely graphical objects

- **Text box:** styleable (font, color, transparent border) free text, e.g. a process title — purely cosmetic. `[00:52:39]`
- **Image:** e.g. a company logo.
- **Page & margins:** Configuration → Strumenti → pagina lets you set paper size (A0–A4) and margins; most processes are drawn on an oversized page and margins are ignored, but if you want a **printable** process diagram (e.g. as documentation, exportable to PDF via "print to PDF"), you lay it out to fit real pages. `[00:55:05]`
- **Memo/post-it:** a free-floating note attached near an activity for design-time annotation; has no runtime effect.

### 4.2 Multi-page processes & the Marker object

For very long/complex processes, the canvas can be split into multiple pages (Nuova Pagina). A **Marker** object acts as a "goto"/teleport between pages: you place a numbered marker where the flow leaves page 1, and a matching marker where it re-enters on page 2. There can be any number of markers/pages. Useful mainly when the diagram needs to be readable/printable as documentation. `[00:58:20]`

### 4.3 Swim Lanes

**What it is:** Adjacent, ordered lanes (like BPMN "pools/lanes") used to visually organize a process by role/department. Dragging the swim-lane object in creates a set of contiguous tracks that can be renamed (e.g. "Inseritore," "Sicurezza," "Controllo di Gestione," "Dirtec"). `[01:00:10]`

**Functional behavior — not just cosmetic:** setting **"utenti responsabili"** at the lane level (right-click) auto-assigns that user/group to any task placed inside the lane that doesn't already have its own explicit assignment; an explicit task-level assignment overrides the lane. `[01:06:00]`

**Configuration:**

- Lane header color, order (swap lanes up/down).
- Orientation: vertical (top-to-bottom, the instructor's own preferred convention) or horizontal (the standard BPMN convention, used when diagrams need to look "textbook"). `[01:08:42]`

**Real project example:** a multi-department process (commerciale → tecnico → acquisti → qualità → produzione) laid out with swim lanes — very legible about "who does what" at a glance, but the instructor notes this style of diagram is visually messier ("zig-zag") to draw and maintain than a straight top-to-bottom flow. `[01:07:28]`

### 4.4 Activity Group ("gruppo") object

An alternative to swim lanes for grouping/labeling: also supports assigning "utenti responsabili" to everything inside it, or can be used purely as a visual label/box around a section of the diagram (e.g. "ufficio tecnico"). `[01:13:39]`

### 4.5 Undo vs. Version History

- **Undo** (~10 steps) is transient — it only covers the current editing session, from opening the process to closing the designer.
- **Publish/version history** is permanent, stored in the database: every time you "Pubblica," BPM creates a new numbered version row. You can revert to any prior published version. `[01:11:36]`
- **Tip:** on publish, BPM offers a free-text **"Version" / "Publication notes"** field where you can record what changed (e.g. "R01 dev — modified task 2"); useful as an informal changelog even though the underlying version counter increments regardless. `[01:12:00]`
- There is also a history-cleanup tool (for large/old installs) to purge old version history, with a safety check that prevents deleting a version that instances are still actively running on. `[01:13:03]`

---

## 5. Events

### 5.1 Multiple Start events

A process can have two or more distinct **Start** objects, each independently configured (its own required variables, default values, validation rules, permissions). `[01:15:37]`

**Example:** "Inserimento richiesta normale" vs. "Inserimento richiesta sicurezza" — the security start pre-fills/streamlines fields differently (e.g. skips a review step, adds a dedicated notes field). `[01:16:00]`

**When launching a process with multiple starts:**

- Default behavior: the user is prompted to choose which start point.
- **Restrict by permission:** set "utenti responsabili" on each Start individually so only the right group can use that entry point. `[01:19:16]`
- **Bind via custom menu:** a custom menu entry ("menu personalizzati") can be pre-wired to a specific start, giving each entry point its own friendly menu item instead of a generic prompt. `[01:20:22]`
- **Via API/web service:** the `create-new-process` call takes an explicit start-point parameter; omitting it when multiple starts exist returns an error rather than defaulting silently. `[03:53:54]`

### 5.2 Start a tempo (scheduled/timed start)

Fires a process automatically on a schedule instead of a user action (e.g. "every first Monday of the month at 08:00"). Good for periodic/administrative processes (period-end closings, recurring checks). Because it carries no variables, the first real activity of the process must still gather the actual working data. `[01:22:05]`

### 5.3 Attesa (Wait) event

Suspends the process for a configured duration (e.g. "wait 5 days," or "the first Monday" pattern) and then automatically continues — during the wait, there is **no to-do-list entry** (contrast with just planning a task 10 days out, which *would* still sit in someone's to-do list the whole time). `[01:23:44]`

**Real example:** the internal "welcome kit" (employee onboarding) process uses the wait event at several points to space out steps by a number of days. `[01:24:51]`

### 5.4 Fine vs. Termina Processo

- **Fine:** a purely graphical end-of-branch marker — signals visually "this branch of the diagram ends here," no runtime effect beyond that.
- **Termina Processo:** actually **kills** the whole process instance — any still-open parallel activities elsewhere in the process get force-closed. Typically used on exception/error branches when you decide the whole instance should be aborted. `[01:26:00]`

### 5.5 Timeout / Escalation boundary events

An event attached to the **border of a task** (not the main flow line) — fires an alternate path after N days from the task's activation date or a deadline, e.g. to trigger a reminder or hand off to someone else. Functionally "timeout" and "escalation" are the *same* mechanism; the two icons only differ semantically by convention (timeout = "this is taking too long, nudge"; escalation = "hand off / raise the stakes"). This corresponds to BPMN's "boundary event" concept — the event exists because of the task being active, not because the main flow reached it. `[01:28:10]`

---

## 6. Operations (Automatic System Activities)

**Core concept:** unlike user tasks (rectangles, need a human) or events (points that just happen), **operations** are things the BPM engine does *by itself*, automatically. They can be dragged directly into the process flow like any other object, **or** attached to a specific task's lifecycle moment (see §6.2), **or** attached at the whole-process level (see §6.7). `[01:30:34]`

### 6.1 Send Mail operation

- Drag the mail operation into the flow, then configure it to select (or create) a **mail template**.
- Mail templates are objects that live inside the process (Configuration → or directly from the operation) and are reusable across multiple send-points. `[01:34:06]`
- Building a template: subject line and body support inserting process variables via right-click ("generic" menu also exposes special placeholders — see below).
- **Recipients:** can be a fixed BPM user, a fixed group, a variable holding a raw email address (e.g. a supplier's email field), or a variable holding a BPM user/group reference. Recipients can also be CC'd ("in propria conoscenza"). `[01:36:40]`
- **Attachments:** you can attach process documents and/or generated reports to the mail.
- **Special generic placeholders useful in templates:**
  - `my own email` — the email of whoever the *task* is currently assigned to (lets one template be reused across many different tasks/assignees). `[01:43:05]`
  - `my activity` — the current task's display name.
  - **`link web al task`** — inserts a clickable URL that deep-links directly into that specific activity's execution screen in the web client (bypasses the to-do list entirely). Also works for linking to the whole process or its attachments page. `[01:46:14]`
- **Common gotcha:** the deep link only works if **Configuration → parameters → "URL base link email"** is set to the server's real externally-visible hostname; if left at `localhost` (the easy-to-forget default), every emailed link silently breaks — especially important when the server is exposed on a public IP. `[01:49:00]`
- It's usually recommended to always enable the web module (no extra license needed, just an IIS setup task for sysadmins) since it's needed for these deep links to work outside the desktop client.

### 6.2 Attaching operations to a task's lifecycle

Right-click a task → **Operazioni** lets you attach any operation (same catalog as the flow-level ones) to one of four moments: `[01:39:41]`

- **Attivazione (activation):** the task just became available (appears in someone's to-do list — good moment for a "you have something to do" notification).
- **Inizio (start):** the user explicitly declared they've *begun* the task (only fires if "rileva inizio" is enabled on that task — see §9.6).
- **Esecuzione (execution):** fires right before the activity is marked truly complete (i.e. "about to complete").
- **Esecuzione terminata (execution completed):** fires right after completion, just before the next task activates.

**Activation vs. Inizio, precisely:** activation = task is *ready*; inizio = task has actually *begun*. These are deliberately separate concepts, used together with the planning system (§9). `[01:41:00]`

**Design tip:** placing purely technical/plumbing operations (e.g. resetting a stale variable — see §6.3) directly on the task, rather than as a visible object in the flow, keeps the process diagram focused on business logic instead of cluttering it with technical housekeeping steps. `[02:13:06]`

### 6.3 Set Variable / inline-formula operation ("un pezzo di scritto")

A lightweight operation that runs a short script to set one or more variables — distinct from a validation formula (which just returns true/false). `[02:10:20]`

**Worked example — clearing a stale outcome on rework:** if an "esito approvazione" field is set to "not approved," and the activity is sent back to the requester for revision and then returns to the approver, the field silently still holds the old "not approved" value (a common source of confusion — many people expect it to revert to blank). A Set Variable operation attached to the task's **Esecuzione Terminata** blanks the field again, forcing the user to consciously re-decide, and prevents accidentally looping forever because the "required field" check was trivially already satisfied by the stale value. `[02:11:19]`

```vb
' attached on "controllo di gestione" task, on execution-completed
esito_approvazione = Blank
```

**Worked example — auto-assigning an approver by amount:** `[02:15:17]`

```vb
If importo_richiesta < 1000 Then
    utente_approvazione_tecnica = "Dir Tech"   ' can be a group too
Else
    utente_approvazione_tecnica = "Dir Gen"
End If
```

The task's "utenti responsabili" is then bound to the `utente_approvazione_tecnica` variable (a User-type variable) instead of a fixed group — a third addressing mode beyond "assign to group" and "manually pick a person": **rule-driven addressing**.

### 6.4 Decision Table

**What it is:** A newer, more declarative alternative to hand-writing a formula. You define input columns and output columns and a set of rule rows; BPM generates the underlying VB code behind the scenes. Available anywhere a formula/validation formula can be used. `[02:19:05]`

**Worked example — same approver-by-amount logic as a table:** `[02:20:39]`

| Importo Richiesta | → | Utente Approvazione |
| --- | --- | --- |
| < 1000 | | Dir Tech |
| ≥ 1000 | | Dir Gen |

Extended with a second input column (Tipo Richiesta) for more complex rules, e.g.: `[02:22:32]`

| Importo Richiesta | Tipo Richiesta | → | Utente Approvazione |
| --- | --- | --- | --- |
| < 1000 | Normale | | Dir Tech |
| ≥ 1000 | Normale | | Dir Gen |
| (any) | Sicurezza | | Sicurezza |

- Row order matters and can be changed with up/down arrows (the first matching row wins).
- The tool is aware of variable types: for a value-list field it offers the known values; for a User-type field it offers the list of users/groups; for a validation-formula context it already knows the output must be true/false.
- **Limitation:** the decision table only expresses simple field-comparison conditions — it cannot express procedural logic like "loop through a group and count matching rows" (§2.2's example). For that you still need a formula.
- **Convert both ways:** a formula field can be converted to a decision table (as a starting point, if you're stuck facing a blank formula box) and a table can be converted back to a formula when its logic outgrows the table format. The instructor compares this to using ChatGPT-generated code as a starting point — never a finished, trustworthy answer, but a useful unblock. `[02:27:47]`

### 6.5 SQL operation ("SQL libero")

**What it is:** An operation that executes an arbitrary SQL statement against an external connection string — not restricted to a single table's CRUD, can run stored procedures, joins, whatever SQL allows. `[02:29:08]`

**Worked example:** `[02:30:18]`

```sql
UPDATE fornitori SET valore = 1 WHERE ID_numeric = @n
```

with `@n` bound as an input parameter to a process variable; separately, a `SELECT` with an output parameter (`@p`) writes a returned value back into a process variable (e.g. `importo_richiesta`).

**Use case:** stamping back into an external ERP that a document was signed/approved by a certain user at a certain step (e.g. "UPDATE order SET signed_by = ... WHERE order_id = ..."), used as a lighter-weight alternative to the dedicated connector when there isn't a pre-built connector interface for that write. `[02:32:45]`

**Configuration:** the connection string is set up once under **Configuration → Connessione Esterna** (supports SQL Server / ODBC-style targets), and reused by both the SQL operation and any table-bound field lookup. `[02:34:16]`

### 6.6 "Aggiorna un altro processo" (Update another process)

Lets you push variable updates into a *different* running process instance at any arbitrary point mid-flow — not just at launch (linked process) or at return. Doesn't even require the two processes to have been formally linked. You supply a lookup rule to find the target instance: by internal BPM instance code, or by matching a variable's value (e.g. "find the process whose `numero_richiesta` = mine"). Then map source→destination variables, set fixed values, or use a passage-formula, same as linked-process mapping. **Caution:** if you find yourself needing this too often, it's usually a sign of excessive data duplication between processes that should be re-architected. `[02:35:10]`

### 6.7 Process-level operations (trigger-like)

Operations can be attached not just to a single task but to the **whole process** — meaning they fire automatically every time *any* step advances, without needing to be wired onto every individual task. Common use: always push a status update to an external CRM/ERP, or always sync new attachments out to a document repository ("documentale globe") on every advance, without prompting the user. `[02:39:48]`

### 6.8 Get Data operation

**What it is:** A structured, guided alternative to a raw SQL query for read-only lookups: pick a source table/view, supply the key value, and map the returned columns directly into process variables — the exact same UI/mechanism used for a field's table-lookup binding, just invoked as a standalone operation. `[02:41:19]`

**Worked example:** given a supplier code, look up the supplier table and auto-fill company name into a `ragione_sociale` variable — commonly used right at the **start** of a process when the user only enters a code and the rest of the master-data fields should auto-populate.

**Get Data vs. raw SQL query:** Get Data is more guided (aware of columns/table types, less error-prone) but limited to a simple single-record lookup by key; anything requiring joins, GROUP BY, multiple returned rows, or arbitrary logic requires the SQL operation instead. `[02:44:06]`

---

## 7. Custom Local Tables (Tabelle P_)

**What it is:** Beyond built-in views and value-lists, BPM lets you define fully custom lookup tables directly inside the designer. Saving one auto-generates a real SQL table prefixed `P_` (e.g. `P_area_geografiche`). `[02:46:02]`

**Why/when:**

- A value list isn't enough (need multiple columns, not just code+description).
- The data needs to be maintained by someone other than the process designer, or independently of any specific process's publish cycle.
- You want filtering/search over a longer list than a dropdown comfortably supports.

**Real use case:** frequently used for quality-department reference tables (definitions/standards not present in the main ERP). `[02:54:08]`

**How to configure:**

1. Configuration → Tabelle → Nuova Tabella; name it (spaces auto-convert to underscores to keep the generated SQL identifier clean). `[02:47:44]`
2. Design columns with an editor very similar to the process-variable editor — but with real limits: **no groups/header-detail**, **no validation formula**, fewer advanced features than a true process variable. `[02:49:55]`
3. Save → the SQL table is created. Populate rows directly inside BPM (Tabelle → your table → Nuovo).
4. Use it anywhere a "tabella locale" lookup is expected (field binding, data grid source, Get Data source) — it will show up prefixed `P_`.
5. If a `P_...` table exists in SQL but wasn't created through BPM's table designer, BPM will still list it as a lookup source, but you can't manage its row data from inside BPM (no value-entry menu for it) — useful if it's populated by an external import instead.

**Permissions:** custom tables are subject to per-user/group permissions (view / modify), same mechanism as process permissions, configured under Users & Groups. `[02:53:04]`

**Custom menus:** a custom table can be exposed as its own menu entry (Configuration → menu personalizzati → "visualizza tabella"), so end-users can browse/maintain it directly without going through a process. `[02:53:10]`

**Guidance — value list vs. custom table:** `[02:56:08]`

- Use a **value list** *inside the process* when logic/conditions elsewhere in the process depend on its exact values — changing the list later could otherwise silently break those conditions.
- Use a **custom table** when there are many options, they need to be filterable/searchable, or the person maintaining them shouldn't need permission to modify the process itself.

---

## 8. Reports & Dashboards (Analytics)

Two complementary ways to extract/present data collected in a BPM process, both built on **process variables** as the data source (no separate data-extraction step needed). `[02:57:37]`

### 8.1 Reports (pixel-perfect documents)

**What it is:** An embedded third-party report designer (same product family as Crystal Reports / the PDF generators used in SAM's RGT and "Globe") that lets you lay out a PDF-style document and drag process variables into labeled placeholders. `[03:02:27]`

**Real case study — "scheda commessa" (work-order form):** before BPM, a company's sales reps filled a blank PDF/Word form by hand for every new order/commessa, then emailed it around and manually chased colleagues ("did you enter the serial number? did you place the order?"). The BPM process now replicates and improves this: the first activity captures ~70–80 fields directly in BPM (many sales reps, including on the web/mobile client while traveling), with many fields upgraded from free text to **table-driven** selections (§7) — while still allowing free text where the customer needed that flexibility. `[02:58:34]`

**Building a report:**

- Fields presented in the designer are grouped by page/variable name, mirroring the process's own variable organization.
- Drag a variable onto the canvas to create a bound placeholder; add static labels around it.
- **Conditional sections:** whole sections can be shown/hidden based on a condition (e.g. show a "Gas1/Gas2" sub-section only if those checkboxes are set) — useful for forms with many optional sub-blocks. `[03:04:29]`
- **Header/detail (group) reporting:** with a bit of care, a report can render a group variable (e.g. list of quotes) as a repeated "detail" block, producing multiple rows per printed page.
- Reports are saved into the BPM database (not the filesystem) as part of the process; a "Stampa" (print) command on the running process instance renders the current values into the template.
- The instructor notes this is not meant to compete with proper reporting/BI — it's a built-in convenience, since the data is already modeled inside the process.

### 8.2 Dashboards (Cruscotti)

**What it is:** Another embedded third-party (DevExpress-based) analytics component for building interactive visual dashboards over process data — distinct from the pixel-perfect PDF reports above. `[04:48:36]`

**Building one, step by step:**

1. Create a new dashboard, add a **data source** bound to a chosen process (e.g. a "reclamo"/complaint-handling process), name it (e.g. "elenco reclami") and pull in the variables you want available as fields. `[04:50:08]`
2. Drag widgets onto the canvas — e.g. a **Grid** and a **Pie Chart**; each widget, once selected, shows drop-zones (columns for the grid; value/arguments for the chart) that you populate by dragging fields in. `[04:51:31]`
3. **Number formatting:** built-in options for K/M unit abbreviation, thousands separators, decimal places.
4. **Pie chart:** drag a unique field (e.g. `ID`) into "value" to get a default Count aggregation, and a categorical field (e.g. "marca") into "arguments" to break it down by category. `[04:54:31]`
5. **Filter elements:** a "casella combinata" (combo box) widget bound to a field (e.g. a date, grouped by day/month/year) acts as a cross-filter for every other widget on the dashboard when the user picks a value. `[04:55:18]`
6. **Calculated fields:** e.g. a "tempo di risposta" field computed as `data_risposta − data_apertura`, then used with an **Average** aggregation to show mean response time. `[05:03:01]`

**Prerequisite for meaningful KPIs — capture key dates explicitly:** raw task-execution timestamps aren't always the metric you want (e.g. "days to respond to a complaint" should be measured from "taken in charge" to "answered," not from ticket creation to ticket closure). The pattern used: attach **Set Variable operations** (see §6.3) to specific task transitions that stamp `Today` into dedicated date variables (`data_presa_in_carico`, `data_risposta`) automatically, with zero user input — these then feed the dashboard's calculated fields. `[04:58:30]` `[04:59:13]`

**Real project example:** an unusual quality-control project for a coffee roaster used dashboards extensively to visualize tasting/roasting scores collected during the process — described as "very niche" but a good illustration of the tool's flexibility beyond typical business processes. `[05:04:36]`

**Availability:** once saved, a dashboard is available to end users (without the design toolbar) under the **"Analisi Dati"** menu (only appears once at least one dashboard/table exists, same as the custom-table menu) — and the identical dashboard is automatically also available in the **web client**, no separate rebuild needed. `[05:05:11]`

**Positioning:** explicitly *not* a BI replacement (no cubes, everything computed live/on the fly) — its value is convenience, since the data is already connected inside BPM. `[04:57:35]`

---

## 9. Process Planning & Scheduling (Pianificazione / Gantt)

### 9.1 Core concept

Beyond tracking actual start/end timestamps per task (which BPM always records by default), BPM offers an optional **planning/estimation layer**: standard expected durations per task, auto-rolled into a live Gantt chart that updates as the process actually executes. `[04:18:05]` `[04:21:01]`

**Important characteristics:**

- Durations are expressed in **calendar days** (wall-clock time), *not* effort/capacity units — there is no resource-capacity/allocation concept in BPM.
- This whole feature is optional per process; it can be turned off entirely via permissions if not useful for a given process (§9.9).

### 9.2 Setting standard durations & auto-generated Gantt

1. On each task, open **Pianificazione e Scadenze** and set a standard duration in days (e.g. 5, 7, 15, 2). `[04:22:29]`
2. As soon as a process instance starts, BPM immediately computes a full-process Gantt estimate from these standard durations, visible under the variable warehouse's **Pianificazione** tab. `[04:25:01]`
3. The Gantt engine correctly models dependency structure — including parallel branches (two tasks side by side, finish-to-start logic feeding the downstream join task only after the *longer* parallel branch finishes) — "just like Project." `[04:26:44]`... but see note below re: reference removed from timestamp file, concept still applies mid-course around `[04:25:42]`.

### 9.3 Live updates as the process runs

- As each task is actually completed, its Gantt bar switches from the original planned duration (shown dashed, as the "baseline") to the compacted/actual duration, and **everything downstream shifts accordingly**. `[04:27:32]`
- **Key behavior — plans only push right, never pull left:** if actual progress runs later than planned, the "updated" schedule slips later; but running *ahead* of schedule on one task does not auto-compress the estimate below the standard durations for tasks not yet started. `[04:28:42]`
- Rescheduling a task from the to-do-list/calendar view (e.g. dragging an activity to a later date) immediately reshapes the downstream Gantt too — because to-do-list dates and Gantt dates are literally the same underlying data, not two separate systems. `[04:32:55]`

### 9.4 The three date sets

For every task, BPM tracks three parallel copies of the date range: `[04:33:15]`

1. **Programmazione (initial/baseline):** the original plan, point zero.
2. **Aggiornamento (updated):** the live, continuously-recalculated current estimate.
3. **Effettiva (actual):** populated only once a task has actually started and/or finished.

### 9.5 Data scadenza (deadline) — separate from duration

**Concept:** a hard, externally-imposed deadline pin (shown as a red dot on the Gantt bar) that can be set on **any** task — not just the last one — used to compare the live/updated schedule against a promised date. `[04:29:17]`

**Guidance from Q&A:** the *correct* way to set a deadline is to bind it to an actual **date variable** (something the user enters, or that arrives from an external system like SAM) rather than a relative "N days after start" duration — because durations answer "how long does this take," while a deadline is an external constraint that should be captured as its own data point. `[05:09:03]` `[05:10:12]`

**Use case:** intermediate milestone deadlines mid-process — e.g. client checkpoint dates within a longer project, not just a single end-date.

### 9.6 Rileva Inizio (decouple task start from activation)

**Default behavior:** without this flag, a task's "start" is assumed to equal the moment the previous task finished (i.e. activation = start). `[04:36:28]`

**With "rileva inizio" enabled on a task:**

- The to-do-list shows an **"Inizia"** (Start) button instead of jumping straight to "Esegui" (Execute).
- Until the user explicitly clicks Inizia, the task's Gantt bar has a thin/unbordered outline and no "actual start" date.
- Once started, the bar gets a bold border and a real actual-start date is recorded. `[04:37:33]`
- **Use case:** work that is *ready but not yet begun* — e.g. engineering/design tasks that sit "available" for a while before someone picks them up — distinguishes "queued" from "in progress."
- This ties directly back to the **Attivazione vs. Inizio** operation trigger points (§6.2) — the "Inizio" operation hook only fires meaningfully on tasks with rileva inizio enabled.

### 9.7 Binding dates/durations to process variables

Both a task's **deadline** and its **planned duration** can be bound to a process variable instead of a fixed configuration value, making the plan dynamic based on process data instead of a static model-level number. `[04:42:40]`

**Worked examples:**

- Deadline: bind "data scadenza" (calendar) to a "data consegna prevista" variable that the commercial rep fills in at intake. `[04:43:03]`
- Duration: a real client had a "difficoltà" (difficulty) value-list variable (A/B/C), and a formula/decision table computed the standard duration from it (e.g. 5/7/10/12 days), which then drove the task's planned duration. `[04:44:07]`

  ```vb
  If difficolta = "A" Then
      Return 5
  Else
      Return 10
  End If
  ```

### 9.8 Da Confermare (to-be-confirmed) — initial baseline adjustment

**Concept:** a per-task flag that gives the process **owner** a one-time window, right when the task becomes available, to manually adjust that specific instance's planned dates (drag them around) before locking them in. `[05:11:08]`

**Workflow:**

1. Task becomes available with a "da confermare" status; the owner can freely drag/adjust its planned dates (and any downstream effects) — this is still touching the *initial* baseline, only for this one instance, not the model.
2. Owner clicks **Conferma** (either per-task, or "conferma tutto"): this **freezes** the adjusted plan as the instance's permanent baseline ("version 0" / point of comparison). `[05:12:43]`
3. From then on, all further drift is tracked only in the "updated" schedule (§9.4) relative to that frozen baseline — the confirmed baseline itself never changes again.

- If a task is *not* marked "da confermare," it is born already confirmed, and the original standard-duration-derived plan simply *is* the permanent baseline from the start.

### 9.9 Calendar & permissions

- BPM has a **built-in internal calendar** accounting for weekends and public holidays; when a task duration of "12 days" is computed, it spans 12 *calendar* days by default (weekends shown greyed-out in the Gantt). A per-task toggle ("Utilizza Calendario") lets a task ignore the calendar and count raw elapsed days instead (e.g. a genuinely 24/7 process step). The calendar itself isn't easily end-user-customizable — you either use it or don't. `[05:16:09]`
- The entire planning/Gantt view (visualize and/or modify) is gated by **process-level permissions** ("visualizza pianificazione" / "modifica pianificazione") per user/group — for processes where the Gantt isn't meaningful, it's better to hide it entirely than show a confusing or irrelevant chart. `[04:47:11]`

---

## 10. SAM (ERP) Integration / Connectors

Integration is framed around **four distinct aspects**, covered in turn below: `[04:08:46]`

1. BPM → SAM: writing documents/entities (active connector).
2. BPM → SAM: reading tables (connector table-views / raw SQL).
3. SAM → BPM: launching a process from a SAM-side event (web services / stored procedures / triggers).
4. SAM ↔ BPM: SAM's to-do list showing BPM activities.

### 10.1 Connector architecture (general)

A "connector" (e.g. "SAM v5," or the separate "Globe" connector) is modeled as an installable **plugin**: `[03:21:00]`

- **Definition** (metadata living in BPM config): which companies ("aziende") exist, which interfaces the connector exposes, and general connection parameters (web-service URL, DB connection details for each company — SAM connectors use a *mixed* approach: some operations via web service, others via direct DB read).
- **DLL / external plugin**, which must actually be installed on the environment (normally ships with the standard install; otherwise it's a setup task) and does the real work behind the definition. `[03:25:34]`
- Two interface types are exposed by a connector: `[03:26:42]`
  - **Action interfaces** — used as *operations* dragged into a process flow; they *write* to SAM.
  - **Table interfaces** — used as *read-only lookup sources* on fields/data grids; they expose SAM data as if it were a local table/view.
- Company/environment setup: Configuration → connettori → mark **Attivo**, add a company ("nuova azienda"), and fill in per-company parameters (DB server, credentials, marketing DB if relevant, and that company's web-service endpoint). `[03:24:37]`

### 10.2 Connettore Attivo (Active Connector) — BPM writes to SAM

**What it is:** An operation type, tagged to a specific connector, that writes a document or master-data entity into SAM (create a client, create a "commessa"/work order, log an "intervento," etc.), placed into the flow like any other operation. For **SAM 5**, this is built on top of SAM's XML **Web Import** feature; SAM 6 is expected to offer richer JSON web services instead. `[03:10:52]` `[03:12:18]`

**Configuration walkthrough (e.g. "creazione commessa"):** `[03:13:24]`

1. Drag the connector-attivo operation into the process, double-click, and pick a pre-built XML interface (e.g. "xml commessa").
2. The interface comes with a pre-configured template and a fixed, finite set of **input parameters** ("testata"/header fields, as recommended by SAM's own dev documentation) — map each to a process variable, or leave it as a fixed literal value. Missing a required field simply causes SAM's web import to reject the call with an error (BPM itself has no idea what the XML "should" contain — it's a pass-through).
3. Extra header fields not in the default list can be added via a small helper (it knows the target table's columns) and mapped the same way.
4. **Output parameters:** if the interface returns values (not all do), they can be mapped back into process variables, e.g. capturing the new document's internal ID / doc-number into `numero_commessa`. `[03:17:45]`
5. **Detail/row parameters:** if the process has a matching group (e.g. "lista codici"), each group row is automatically mapped to a repeated XML detail node — letting a whole order/BOM line list be sent in a single call (e.g. mapping `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`). Anything not explicitly present in BPM (e.g. pricing logic) is left entirely to SAM's own configuration. `[03:18:49]`

**Extensibility:** the pre-built interfaces cover a deliberately finite set of common cases (client, commessa, intervento, etc.) — a genuinely new XML template requires a development request, it's not something a consultant/customer can wire up freely from the UI. `[03:12:10]`... (see also 03:29:04 for extensibility note.)

**Activation requirement:** SAM's **Web Import module** must be installed and reachable — typically a routine sysadmin ticket, no extra license required. `[03:34:22]`

**Fallback / when not to use it:** if no pre-built connector interface exists for what you need, a plain manual task reminding a user to enter the record in SAM is a legitimate fallback — automating it just for its own sake can actually be *worse* if it means re-duplicating master data logic (e.g. full client onboarding rules) that already lives properly inside SAM. It's more appropriate when you just need a lightweight placeholder record (e.g. a client stub with a code, so documents can be attached against it). `[03:36:54]`

### 10.3 Reading SAM data into BPM (table connectors)

Two options for a table-bound field/data grid to read SAM data: `[03:29:19]`

- **Local view / direct external table access** — build your own SQL view with exactly the columns you want (a modest amount of one-time effort, but fully flexible).
- **Connector Dati (connector table interface)** — pick from a finite catalog of pre-built views the connector ships with; if a needed column is missing, you must either request it added upstream, or **copy the generated view and customize the copy** (editing the original is unsafe — see below). `[03:31:44]`

**How the pre-built views are generated:** running the connector's "database update" auto-generates a set of SQL views prefixed `vvbpm...` inside the SAM database (one per exposed table interface, e.g. the clients view). `[03:32:08]`

**Critical gotcha:** these auto-generated views get **regenerated/overwritten** every time the connector definition is updated — any hand-edits to the original view are lost. The safe pattern is to duplicate the view under your own name and point your customization at the copy. `[03:31:44]`

### 10.4 SAM's to-do list shows BPM activities

A SAM module lets BPM to-do-list items ("eventi BPM") appear inline in SAM's native to-do list, for users who work across both systems and don't want to switch apps. `[03:39:01]`

- Double-clicking a BPM event inside SAM shows a live detail popup (process/model name, current activity) fetched **in real time via a BPM web service** — nothing about BPM tasks is cached/stored in SAM's own database, it's read fresh every time the screen opens. `[03:40:00]` `[03:41:52]`
- It includes the same deep-link mechanism used in emails (§6.1) to jump straight into that task in the BPM web client.
- **Bidirectional live sync:** advancing a task in BPM (e.g. moving from "firma1" to "firma2") is immediately reflected as the same activity showing up in SAM's to-do list — they're the same underlying task, not two separately-maintained copies. `[03:42:38]`
- The same mechanism/module is also available inside **CRM1**'s to-do list.

**Configuration (SAM side):** Options → search "BPM" → set the **BPM server path** (again: must be the real externally-reachable hostname, not localhost) and a **BPM-generated API key**. `[03:42:44]`

**API key generation (BPM side):** Configuration → **Chiave Web API** — create a new key (optionally with an expiry date); this is the credential every external caller (SAM, Postman, custom code) must present. `[03:43:53]`

**User mapping:** Configuration → Users & Groups → each user has an **"Alias"** section mapping their identity per external connector (e.g. SAM's `css-admin` ↔ BPM's `admin`) — each connector can have its own independent user mapping. `[03:44:51]`

### 10.5 Piloting BPM from SAM (SAM → BPM)

**Standard BPM web services:** a deliberately **small** set of HTTP endpoints accepting JSON POST bodies (described as "REST-ish" rather than strictly REST). Kept small because a single generic `create-new-process` call, parameterized by model name, already covers launching *any* process. `[03:48:22]` `[03:49:58]`

**Key endpoints:** `[03:50:25]`

- `create-new-process` — launch a new process instance (specify model, start point, initial variables).
- `exec-task` — advance/execute an activity currently sitting in a user's to-do list (simulates clicking "Esegui").
- Upload an attachment to a process.
- Force a process forward.
- Read a process's variable data.
- Read a user's to-do list.

**Trying it out:** nothing needs to be installed — just generate an API key (§10.4) and any BPM server can be called. Demonstrated live with **Postman**: `[03:52:06]`

```text
POST {bpm-server}/api-ext-create-new-process
Body (JSON): { auth_token, user, model, start, variables{...} }
```

Response returns success/failure plus the generated process name (per the naming rule) and any validation messages.

**Gotchas confirmed live:**

- Omitting the start point on a multi-start model returns an explicit error rather than silently picking one. `[03:53:54]`
- Required fields / validation formulas are enforced exactly as they would be through the UI — an incomplete/invalid payload returns `false` with no side effects.
- `exec-task` is functionally the same as clicking "Esegui" in the to-do list — used e.g. to advance a BPM process when a matching event happens on the SAM side, though the instructor is cautious about relying on this because *correctly identifying* the triggering SAM-side event is often the hard part (see §10.6 anecdote). `[04:12:41]`

**Recommendation:** direct web-service calls are the **official, most robust method** for any custom/plugin integration — they return a real synchronous success/failure result. `[04:08:00]`

### 10.6 Stored Procedure wrapper & Triggers (async path)

**Why this exists:** SAM has no native outbound event/webhook mechanism, so the *only* tool available to catch a SAM-side event (new order, status change, etc.) and kick off a BPM process is a classic **SQL trigger**. `[03:57:06]`

**Stored procedure wrapper mechanism:** the same "create process" capability is also exposed as a plain **SQL stored procedure** — but rather than calling the web service synchronously, it just **writes a row into a staging table** (`chiamate API`); a background engine running inside BPM polls/reads that table and performs the real web-service call itself. `[03:56:01]`

```sql
EXEC dbo.usp_bpm_create_process
     @user = 2, @model = 'richieste inv', @start = 1, @external_id = 1
```

**Trigger usage pattern (real projects: an "alimentari"/food-industry client, and "Calzavara"):** a trigger fires the stored procedure when a business event occurs in SAM (e.g. an order gets approved); the resulting BPM process then progresses and, at each step, uses the **SQL operation (§6.5)** to write firm/signature/status updates back to SAM as it advances. `[04:00:52]`

**Key async gotcha:** unlike the direct web-service call, triggers and the SP wrapper are **fire-and-forget / asynchronous** — there's no immediate success/failure result, delivery typically completes within a few seconds via the staging-table engine, but this path needs **thorough testing**, and trigger logic itself can be fragile (a bug in the trigger can "brick" the underlying SAM transaction). `[03:59:34]`

**Convention — keep the trigger minimal ("External ID"):** to avoid packing dozens of fields into a fragile trigger, the team adopted a strict convention: the stored procedure accepts **only one parameter** — the source document's ID — mapped into a BPM process variable literally named **`external_id`**. `[04:02:34]`

**BPM enriches itself after the minimal trigger-start, via a callback:** as the very first step of the process (on Start, in operations), BPM immediately calls back into SAM — using **Get Data (§6.8)** or a **connector table view (§10.3)**, keyed on `external_id` — to fetch every other field the process actually needs (supplier name, address, payment terms, order lines, etc.). This deliberately shifts all the complexity from the fragile trigger into BPM's own, more robust and testable tooling. `[04:05:17]` `[04:07:32]`

**Escape hatch for complex cases:** if the standard trigger/SP/Get Data pattern genuinely isn't enough, direct custom code calling the web services is always available as a fallback (a colleague — Filippo Curati — had prototyped exactly this). `[04:08:00]`

### 10.7 Integration best practices & real anecdotes

- **Anecdote — chasing a "fuzzy" business event:** a client wanted a task auto-advanced "when the distinta base (BOM) is inserted" in SAM. The instructor explains this is a genuinely hard automation target: there's no single unambiguous database event that reliably means "the BOM is truly finished," and client requests for "full automation" often carry unrealistic expectations that need to be managed/tempered up front — better to under-promise than to build something fragile that quietly breaks on edge cases (wrong article, duplicate entry, wrong batch/lot, etc.). `[04:13:04]`
- **Best practice — minimize coupling:** avoid designing a project where the two systems interact continuously/back-and-forth throughout the whole process (every process change then risks breaking the SAM side too). The ideal shape has the two systems talk only at the **start and the end** of the process (e.g. one trigger to launch, one final status write-back like "approved"/"not approved" rather than many intermediate micro-states synced back and forth). `[04:16:03]`
- SAM 6 is expected to support this integration more natively/flexibly via real JSON web services, reducing reliance on the trigger/Web-Import-era workarounds described above.

---

## Appendix: Quick-reference glossary (Italian → concept)

| Italian term | English concept |
| --- | --- |
| Griglia dati | Data grid (read-only bound grid variable) |
| Magazzino (delle variabili) | Variable warehouse — the process's full variable repository |
| Variabili da richiedere | Per-screen/task variable configuration (requested/visible variables) |
| Sbarra di sincronizzazione | (Legacy) synchronization bar / join gateway |
| Diamantino / diamante | Path condition / default-path marker on a link |
| Percorsi alternativi / paralleli / liberi | Exclusive / parallel / inclusive gateway |
| Swim lane | Swim lane (organizational track) |
| Gruppo (attività) | Activity group object |
| Marker | Cross-page "goto" object |
| Attesa | Wait event |
| Start a tempo | Timed/scheduled start event |
| Termina processo | Kill/terminate the whole process instance |
| Operazioni | Operations (automatic system activities) |
| Connettore attivo | Active connector (BPM→SAM write operation) |
| Web import | SAM's XML import mechanism used by SAM5 active connector |
| Tabelle P_ | Custom local tables created in BPM |
| Cruscotto | Dashboard |
| Pianificazione | Planning/scheduling (Gantt) subsystem |
| Rileva inizio | "Detect start" flag — decouples task start from activation |
| Da confermare | To-be-confirmed baseline adjustment flag |
| Data scadenza | Deadline (as opposed to planned duration) |
