# Web API BPM — sintesi dello Swagger

Fonte: `https://demobpm.centrosoftware.com/api/swagger/docs/v1` (letto il 25/9/2026).
Titolo: "BPM external API - App version: 2026.7.3". Versione v1, base path `/api`, solo HTTPS.

## Note generali

- Nessuna `securityDefinitions` dichiarata nello Swagger: le credenziali viaggiano nel corpo della richiesta.
- Quasi tutte le chiamate sono `POST` con un unico parametro `par` nel corpo JSON.
- Ogni input eredita da `BaseInputClass`: `userName`, `authenticationToken`, `authorization` (oggetto libero).
- Le risposte di scrittura hanno sempre `result` (boolean) e `message`.

## Endpoint (prefisso `/api/ext/`)

### Processi
| Endpoint | Input | Output |
|---|---|---|
| CreateNewProcess | model, startObject, variables, parameters, attachments[] | CreateNewProcessOutput (isDuplicate, duplicateDocumentName, instanceId, documentName, documentDescription) |
| GetProcess | model, documentName, instanceId, includeVariables[], includeGraph | object |
| UpdateProcess | model, documentName, instanceId, resetGroups[], variables, state | CreateNewProcessOutput |
| DeleteProcess | model, documentName, instanceId | GenericResponse |
| AddLink | model, documentName, instanceId, attachmentGroup/Type/Root/Path, linkedModel, linkedDocumentName, linkedInstanceId | LinkedProcessOutput |
| ProcessModels | — | object |
| GetSchema | modelName, activityName | object |
| UploadAttachment | model, documentName, instanceId, fileName, fileDescription, root, path, group, type, revision, state, variables, content, sourceType, filePathSource, base64Source, sourceReference | AddAttachOutput |

### Attività e To-Do List
| Endpoint | Input | Output |
|---|---|---|
| GetTodolist | fromDate, toDate, filterByUser, filterByText, filterByPriority, includeCompleted, includePlanned, includeCC | object |
| GetPageTodoList | come GetTodolist + Page, Size | object |
| ExecTask | model, documentName, activity, variables, choice, comments, instanceId | EseguiTaskOutput |
| UpdateTask | model, documentName, activityName, instanceId, assignedUser, ccUser, respUser, priority, startDate, durationDays, scope, plannedStartDate, updatedStartDate, actualStartDate, durationDaysPlanned, durationDaysUpdated, dueDate, ignoreCalendar | GenericResponse |

### Documenti
| Endpoint | Input | Output |
|---|---|---|
| CreateNewDocument | come CreateNewProcess + sourceType, filePathSource, base64Source, newVersion*, signedCopy, sourceReference, barcode | CreateNewProcessOutput |
| CreateOrUpdateDocument | come CreateNewDocument | CreateOrUpdateDocumentOutput (created, updated) |
| UpdateDocument | model, documentName, instanceId, resetGroups[], variables, state + contenuto e versione | UpdateProcessOutput |
| UpdateDocumentContent | model, documentName, instanceId + contenuto e versione | UpdateProcessOutput |
| GetDocument | InstanceId, Model, Name, IncludeVariables[] | object |
| SearchDocuments | dossierType, Models[], Filters[] (Name, Value, ValueIn[]) | object |
| DownloadDocument / DownloadDocumentJSON | InstanceId, Model, Name, Version | object |
| DocumentVersions | InstanceId, Model, Name | object |
| DeleteDocument | InstanceId, Model, Name | GenericResponse |
| DocumentSets | — | object |
| AddDocumentToDossier | InstanceId, Model, DocumentName, Dossier (ID, Name, Description, Type, Contact, Company) | GenericResponse |

Sorgente del contenuto: `FilePathSource` (extension, filePath, deleteAfter) oppure `Base64Source` (extension, content).

### Utilità
| Endpoint | Metodo | Output |
|---|---|---|
| GetUser | GET/POST | userName, email, isExternal, groups[] |
| GetVersion | GET/POST | object |

## Da chiarire

- Dove va la chiave API: è `authenticationToken`? Un header?
- Cosa contiene l'oggetto `authorization`.
- Come funziona il mapping con gli alias utente (userName dell'app esterna → utente BPM).
- Differenza tra `model` + `documentName` e `instanceId` per identificare un'istanza.
- Significato di `startObject`, `parameters`, `choice`, `scope`, `DocumentSets`, `sourceReference`.
