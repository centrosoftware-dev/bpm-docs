<!-- Generato da tools/genera-connettori.py dal manifesto FileSystemConnector versione 20260511. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [IncomingFile](#incomingfile) | evento | This event is raised for each file added to a configured folder |
| [SaveAttachmentToFileSystem](#saveattachmenttofilesystem) | operazione | Save a File, Report, Attachment or base64 to the FileSystem |

### IncomingFile

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

### SaveAttachmentToFileSystem

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
