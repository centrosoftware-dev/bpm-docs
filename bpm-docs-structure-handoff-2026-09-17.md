# BPM Docs Restructuring Handoff

## Goal

Restructure the old BPM product documentation into a durable, collaborator-friendly, searchable product reference. The user wants a well-thought-out starting structure before substantial content work begins. Do not begin restructuring or migrating files until the remaining design questions are settled and the user confirms shared understanding.

## Interaction Mode

The `grilling` skill was loaded and governs the discussion. Work as a design tree in rounds: ask every currently independent decision in the frontier, include a recommendation, then wait. Do not ask the user for repository facts; inspect them or delegate exploration. The `domain-modeling` skill was also loaded: challenge fuzzy terminology and update `CONTEXT.md` immediately when a term is resolved.

## Settled Decisions

- The immediate outcome is a new information architecture for the entire documentation site. This is a rebuild of the shape, not a small cleanup of the present navigation.
- The site is primarily a searchable product reference. It must eventually cover relevant clicks, objects, and fields.
- Introductory content, tutorials, guides, and reference implementations are important supporting material, but the product reference is the current priority.
- Primary readers are external business partners, followed by customer configurators. Internal delivery consultants and support staff also use the documentation. Instance administrators need a dedicated natural capability area.
- Main navigation is by product capability, then by screen or component. It is not by reader role. Page content should say where the UI is found and search should index it.
- The initial content priority is configuration and monitoring.
- General process-execution documentation is deferred: customers normally receive user guides tailored to their individual processes. Later, add only general execution basics such as login, search, and grids if useful.
- Italian is the canonical site language. English is desirable later.
- Preserve current Italian URLs at the site root. When English begins, publish it under `/en/`, with its own navigation, search index, and MkDocs build. This is recorded in `docs/adr/0001-future-english-urls.md`.

## Canonical Vocabulary

The authoritative vocabulary added or corrected during this session is in `CONTEXT.md`. In particular:

- A business partner is an external reseller that also provides BPM consultancy and delivery services. It is the primary external documentation audience.
- A delivery consultant is a company employee who delivers BPM, including integration work. Do not call this role an integration engineer.
- A customer is an organization using BPM; its process designers and instance administrators may configure the instance.
- An end user is anyone interacting with BPM, including process designers, instance administrators, and process actors.
- An `attore del processo` performs tasks in an active process. Do not use `partecipante al processo`.

## Repository Facts

- The site uses MkDocs Material and `mkdocs-awesome-pages-plugin`. Navigation is driven by `.pages` files.
- Existing top-level content is `Iniziare`, `Designer e Configurazione`, `Menu`, and `Glossario`; it mixes UI-location navigation with conceptual documentation.
- `docs/getting-started/index.md` is empty. The user opened `docs/getting-started/.pages` near the end of this session, but did not provide an instruction about it.
- There are many empty or missing content pages referenced by navigation, particularly document classes, shared configuration, variable/process coverage, connectors, automation operation details, dashboards, and reports.
- The working tree was clean at the start of the session. This session added `CONTEXT.md` and `docs/adr/0001-future-english-urls.md`; do not undo those files.

## Evidence-Based Capability Inventory

An exploration pass found these source-backed product domains. This is a provisional proposed top-level map, pending the user's decision:

1. `Progettare processi`: models, canvas, activities, events, gateways, transitions, forms, task design, publishing.
2. `Gestire dati e documenti`: variables, document classes, archives, attachments, dossiers, tables, formulas, queries.
3. `Automatizzare e integrare`: operations, connectors, scheduled/event-driven behavior, email, templates, external calls.
4. `Monitorare e gestire processi`: process search, instance state, deadlines, recurring processes, audit history, dashboards, reports.
5. `Amministrare l'istanza`: users, groups, permissions, security policies, shared settings, custom menus, system operations.

The strongest existing content is workflow design, variables/forms, attachments, identity/permissions, email/engine settings, and audit history. Large documentation gaps include connectors, operation-specific automation, gateway/event details, linked processes, document-class fields, dossiers, Excel model options, barcode/QR, dashboards, and reports.

## Current Frontier

The user has not yet answered the following two questions. These are the next questions to ask; do not introduce dependent decisions until they are resolved.

### Q11: Capability Map

Should the five provisional domains above become the top-level product-reference structure? Ask the user to confirm, rename, regroup, or add missing capabilities.

Recommendation: use those five as the stable top-level map. Keep user process execution as a future sixth area only when there is enough general product material to justify it.

### Q12: Reference Page Unit

For a reference covering every click, object, and field, confirm this fixed depth:

1. Capability overview
2. Screen or component
3. Object type, where a screen contains distinct configurable objects
4. Field, command, and behavior as searchable headings within that page

Create a separate field page only when its configuration or behavior is substantial enough to stand alone.

Recommendation: confirm this model. It is atomic enough for parallel collaborators while avoiding thousands of tiny pages.

## Expected Later Decisions

After Q11 and Q12, recompute the frontier. Likely subsequent topics are the top-level landing/entry pages, cross-cutting reference material (glossary, search, expressions), naming and URL conventions, migration/redirect policy, contribution/page templates, coverage tracking, and how to prepare the MkDocs configuration and CI for a future English build. Ask only decisions unblocked by prior answers.

## Suggested Skills

- `grilling`: continue the design-tree interview until the frontier is empty and the user confirms shared understanding.
- `domain-modeling`: preserve and refine the product vocabulary in `CONTEXT.md` as decisions crystallize.
- `implement` or `implement-spec`: only after a confirmed information architecture is turned into an implementation specification.
- `research`: if later decisions require current MkDocs Material or plugin behavior beyond the established English URL decision.
