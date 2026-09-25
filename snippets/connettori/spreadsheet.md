<!-- Generato da tools/genera-connettori.py dal manifesto Spreadsheet Connector versione 20260720. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [LaunchImport](#launchimport) | operazione | Importa dati da un file CSV, XLSX o XLS |
| [ImportConfigurationsFromFile](#importconfigurationsfromfile) | operazione | Importa una configurazione da un file XLSX |
| [ExportDataFromGroups](#exportdatafromgroups) | operazione | Esporta i dati di un gruppo di variabili |
| [ExportExcelToMarkdown](#exportexceltomarkdown) | operazione | Export an XLSX or XLS file to markdown text |
| [ExportExcelToPDF](#exportexceltopdf) | operazione | Export an XLSX or XLS file to PDF |
| [ExportExcelToImage](#exportexceltoimage) | operazione | Export an XLSX or XLS file to Image |
| [LaunchImport [Client]](#launchimport-client) | azione client | Importa dati da un file CSV, XLSX o XLS |

### LaunchImport

*Operazione.* Importa dati da un file CSV, XLSX o XLS

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `ConnectColumnsToGrid` | ingresso | sì | — |
| `SourceType` | ingresso | sì | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Extension` | ingresso | sì | — |

### ImportConfigurationsFromFile

*Operazione.* Importa una configurazione da un file XLSX

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.FileName` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Config` | ingresso | sì | — |

### ExportDataFromGroups

*Operazione.* Esporta i dati di un gruppo di variabili

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Extension` | ingresso | sì | Estensione file di input |
| `ConnectColumnsToGrid` | ingresso | sì | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.FileName` | ingresso | sì | — |

### ExportExcelToMarkdown

*Operazione.* Export an XLSX or XLS file to markdown text

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Extension` | ingresso | sì | — |
| `TargetWorksheet` | ingresso |  | — |
| `ExtractedText` | uscita |  | — |

### ExportExcelToPDF

*Operazione.* Export an XLSX or XLS file to PDF

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Extension` | ingresso | sì | — |
| `Destination.Attachment.Root` | ingresso |  | — |
| `Print.Scaling.Option` | ingresso |  | — |
| `Print.Scaling.Percentage` | ingresso |  | — |
| `Print.Orientation` | ingresso |  | — |
| `Destination.Attachment.Folder` | ingresso |  | — |
| `Destination.Attachment.FileName` | ingresso |  | — |

### ExportExcelToImage

*Operazione.* Export an XLSX or XLS file to Image

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Extension` | ingresso | sì | — |
| `Destination.Attachment.Root` | ingresso |  | — |
| `Print.Scaling.Option` | ingresso |  | — |
| `Print.Scaling.Percentage` | ingresso |  | — |
| `Print.Orientation` | ingresso |  | — |
| `Destination.Attachment.Folder` | ingresso |  | — |
| `Destination.Attachment.FileName` | ingresso |  | — |

### LaunchImport [Client]

*Azione client.* Importa dati da un file CSV, XLSX o XLS

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `ConnectColumnsToGrid` | ingresso | sì | — |
| `SourceType` | ingresso | sì | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Extension` | ingresso | sì | — |
