<!-- Generato da tools/genera-connettori.py dal manifesto Pdf Connector versione 20260809. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [ExtractTextArea](#extracttextarea) | operazione | Extract text from a PDF in the chosen area |
| [ExtractMarkdown](#extractmarkdown) | operazione | Extract text as Markdown from PDF |
| [ExtractTextReadingOrder](#extracttextreadingorder) | operazione | Extract the text based on the reading order in the specified pages |
| [ExtractTextAreaImage](#extracttextareaimage) | operazione | Extract text from PDF that is a scan of a document or an image with no highlightable text |
| [ExtractTableStructures](#extracttablestructures) | operazione | Extract Tables in a pdf file as an array |
| [SplitEachPage](#spliteachpage) | operazione | Split each page of a PDF into a different PDF. The output files will be stored in the selected folder. |
| [MergePDFs](#mergepdfs) | operazione | Merge multiple PDF files into a single PDF. You must declare the Filename with .PDF extension. |
| [WriteOnPDF](#writeonpdf) | operazione | WriteOnPDF allows the user to define areas on a sample PDF. For each Area, the user can define the text to write in it by using the Rich text editor. |
| [SplitByGroups](#splitbygroups) | operazione | Split the initial PDF file based on the FromPage and ToPage detail parameters |
| [MergePDFs [Client]](#mergepdfs-client) | azione client | Merge multiple PDF files into a single PDF as a client action |
| [ZIPPDFs](#zippdfs) | operazione | ZIP selected files and documents into a folder |

### ExtractTextArea

*Operazione.* Extract text from a PDF in the chosen area

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Extension` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `TextAreas` | ingresso | sì | Area selector to define the areas from where the text is extracted |
| `ExtractedText` | uscita |  | The whole extracted text. Each area output is divided by new line. |

### ExtractMarkdown

*Operazione.* Extract text as Markdown from PDF

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso |  | — |
| `Source.Extension` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `ExtractedText` | uscita |  | The whole extracted text |
| `FromPage` | ingresso |  | — |
| `ToPage` | ingresso |  | — |

### ExtractTextReadingOrder

*Operazione.* Extract the text based on the reading order in the specified pages

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.ReportFormat` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Extension` | ingresso |  | — |
| `SourceType` | ingresso |  | — |
| `ExtractedText` | uscita |  | The whole extracted text |
| `FromPage` | ingresso |  | — |
| `ToPage` | ingresso |  | — |

### ExtractTextAreaImage

*Operazione.* Extract text from PDF that is a scan of a document or an image with no highlightable text

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Extension` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `TextAreas` | ingresso | sì | Area selector to define the areas from where the text is extracted |
| `ExtractedText` | uscita |  | The whole extracted text. Each area output is divided by new line. |

### ExtractTableStructures

*Operazione.* Extract Tables in a pdf file as an array

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso |  | — |
| `Source.Extension` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `ExtractedTables` | uscita |  | — |
| `FromPage` | ingresso |  | — |
| `ToPage` | ingresso |  | — |

### SplitEachPage

*Operazione.* Split each page of a PDF into a different PDF. The output files will be stored in the selected folder.

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso | sì | Attachment group of the input files |
| `Destination.Attachment.Root` | ingresso | sì | Root of the destination Folder |
| `Destination.Attachment.Folder` | ingresso |  | Folder for the output file to be saved into |

### MergePDFs

*Operazione.* Merge multiple PDF files into a single PDF. You must declare the Filename with .PDF extension.

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Destination.Attachment.Root` | ingresso | sì | Root of the destination Folder |
| `Destination.Attachment.Folder` | ingresso |  | Folder for the output file to be saved into |
| `Destination.Attachment.FileName` | ingresso | sì | Filename for the output file. It MUST contain .PDF |

### WriteOnPDF

*Operazione.* WriteOnPDF allows the user to define areas on a sample PDF. For each Area, the user can define the text to write in it by using the Rich text editor.

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso | sì | Attachment group where the process will find the input PDF file |
| `Destination.Attachment.Root` | ingresso | sì | Root of the destination Folder |
| `Destination.Attachment.Folder` | ingresso |  | Destination folder for the output file |
| `Destination.Attachment.FileName` | ingresso | sì | Filename of the output file. It MUST contain .PDF |
| `WritingSettings` | ingresso | sì | Area selector where the user can define Areas, text to write, type of writing. |

### SplitByGroups

*Operazione.* Split the initial PDF file based on the FromPage and ToPage detail parameters

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso | sì | — |
| `Destination.Attachment.Root` | ingresso |  | — |
| `Destination.Attachment.Folder` | ingresso |  | — |
| `FromPage` | ingresso (righe) |  | — |
| `ToPage` | ingresso (righe) |  | — |

### MergePDFs [Client]

*Azione client.* Merge multiple PDF files into a single PDF as a client action

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso |  | Attachment group of the input files |
| `Source.LinkedDocuments` | ingresso |  | List of Document Classes from which the files will be merged |
| `Destination.Attachment.Root` | ingresso |  | Root of the destination Folder |
| `Destination.Attachment.Folder` | ingresso |  | Folder for the output file to be saved into |
| `Destination.Attachment.FileName` | ingresso | sì | Filename for the output file. It MUST contain .PDF |
| `IndexVariable.Name` | ingresso |  | Name of the index variable. The index variable is used to define the order in which the PDF are going to be merged together |

### ZIPPDFs

*Operazione.* ZIP selected files and documents into a folder

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Destination.Attachment.Root` | uscita | sì | — |
| `Destination.Attachment.Folder` | uscita |  | — |
| `Destination.Attachment.Filename` | uscita | sì | — |
