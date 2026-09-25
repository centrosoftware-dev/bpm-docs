<!-- Generato da tools/genera-connettori.py dal manifesto UtilityConnector versione 20260903. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [CreateOrUpdateDocument](#createorupdatedocument) | operazione | Creazione/aggiornamento di un documento |
| [UpdateDocument](#updatedocument) | operazione | Aggiornamento documento esistente |
| [UpdateDocumentContent](#updatedocumentcontent) | operazione | Aggiornamento della parte file di un documento |
| [RouteByBarcode](#routebybarcode) | operazione | Smista i file in documenti esistenti in base alla presenza di barcode conosciuti |
| [ExtractBarcodes](#extractbarcodes) | operazione | Estrai i barcode trovati in un file |
| [AddDocumentToDossier](#adddocumenttodossier) | operazione | Aggiunge un documento ad un dossier |
| [AddLink](#addlink) | operazione | — |
| [OpenDocument](#opendocument) | azione client | Apertura contestuale di un documento |
| [AddAttachment](#addattachment) | operazione | Aggiunge allegato |
| [SplitByBarcode](#splitbybarcode) | operazione | Divisione pagine di un PDF in base ai Barcode al suo interno |
| [CreateOrUpdateDocument [Client]](#createorupdatedocument-client) | azione client | Create or Update a document on button click |
| [AddAttachment [Client]](#addattachment-client) | azione client | Add an attachment on button click |
| [AddLinkedDocument](#addlinkeddocument) | operazione | — |
| [DeleteAttachment](#deleteattachment) | operazione | — |
| [DeleteDocument](#deletedocument) | operazione | — |

### CreateOrUpdateDocument

*Operazione.* Creazione/aggiornamento di un documento

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf, docx, xlsx |
| `DestinationType` | ingresso | sì | self, document |
| `Doc.Model` | ingresso |  | — |
| `Doc.StartObject` | ingresso |  | optional |
| `Doc.Barcode` | ingresso |  | * |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.NewVersion.Number` | ingresso |  | — |
| `Doc.NewVersion.Description` | ingresso |  | — |
| `Doc.NewVersion.Date` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.JSONVariables` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita |  | — |
| `DocumentName` | uscita |  | — |
| `DocumentDescription` | uscita |  | — |

### UpdateDocument

*Operazione.* Aggiornamento documento esistente

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf, docx, xlsx |
| `DestinationType` | ingresso | sì | self, document |
| `Doc.Model` | ingresso |  | — |
| `Doc.DocumentName` | ingresso |  | — |
| `Doc.InstanceId` | ingresso |  | — |
| `Doc.Barcode` | ingresso |  | * |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.JSONVariables` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita |  | — |
| `DocumentName` | uscita |  | — |
| `DocumentDescription` | uscita |  | — |

### UpdateDocumentContent

*Operazione.* Aggiornamento della parte file di un documento

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf, docx, xlsx |
| `DestinationType` | ingresso | sì | self, document |
| `Doc.Model` | ingresso |  | — |
| `Doc.DocumentName` | ingresso |  | — |
| `Doc.InstanceId` | ingresso |  | — |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita |  | — |
| `DocumentName` | uscita |  | — |
| `DocumentDescription` | uscita |  | — |

### RouteByBarcode

*Operazione.* Smista i file in documenti esistenti in base alla presenza di barcode conosciuti

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf mandatory |
| `Barcode.Format` | ingresso | sì | — |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita (righe) |  | — |
| `DocumentName` | uscita (righe) |  | — |
| `DocumentDescription` | uscita (righe) |  | — |
| `Barcode.RotateFile` | ingresso |  | Rotate the output file based on the QR Code orientation |

### ExtractBarcodes

*Operazione.* Estrai i barcode trovati in un file

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf mandatory |
| `Barcode.Format` | ingresso | sì | — |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita (righe) |  | — |
| `DocumentName` | uscita (righe) |  | — |
| `DocumentDescription` | uscita (righe) |  | — |

### AddDocumentToDossier

*Operazione.* Aggiunge un documento ad un dossier

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `InstanceId` | ingresso |  | — |
| `DossierId` | ingresso |  | — |
| `DossierName` | ingresso |  | — |
| `DossierType` | ingresso |  | — |
| `DossierDescription` | ingresso |  | — |
| `DossierContact` | ingresso |  | — |
| `DossierCompany` | ingresso |  | — |

### AddLink

*Operazione.* —

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `InstanceId` | ingresso |  | — |
| `Model` | ingresso |  | — |
| `InstanceName` | ingresso |  | — |
| `LinkedInstanceId` | ingresso |  | — |
| `LinkedModel` | ingresso |  | — |
| `LinkedInstanceName` | ingresso |  | — |

### OpenDocument

*Azione client.* Apertura contestuale di un documento

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `InstanceId` | ingresso |  | — |
| `Doc.Model` | ingresso |  | — |
| `DocumentName` | ingresso |  | — |

### AddAttachment

*Operazione.* Aggiunge allegato

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | — |
| `Source.FilePath.DeleteAfter` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `Source.Model` | ingresso |  | — |
| `Source.DocumentName` | ingresso |  | — |
| `Source.InstanceId` | ingresso |  | — |
| `Doc.JSONVariables` | ingresso |  | — |
| `DestinationType` | ingresso |  | — |
| `Dest.Model` | ingresso |  | — |
| `Dest.DocumentName` | ingresso |  | — |
| `Dest.InstanceId` | ingresso |  | — |
| `Dest.Attachment.Group` | ingresso |  | — |
| `Dest.Attachment.Type` | ingresso |  | — |
| `Dest.Attachment.FileNameInternal` | ingresso | sì | (unique per instance) |
| `Dest.Attachment.FileNameDisplay` | ingresso |  | (view) |
| `Dest.Attachment.Description` | ingresso |  | — |
| `Dest.Attachment.Root` | ingresso |  | — |
| `Dest.Attachment.Folder` | ingresso |  | — |

### SplitByBarcode

*Operazione.* Divisione pagine di un PDF in base ai Barcode al suo interno

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.FilePath` | ingresso |  | — |
| `Source.FilePath.DeleteAfter` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Barcode.Format` | ingresso | sì | — |
| `Dest.Attachment.Group` | ingresso | sì | Gruppo allegati in cui vengono inseriti i file splittati |
| `Dest.Attachment.Root` | ingresso |  | Root allegati in cui vengono inseriti i file splittati |
| `Dest.Attachment.Folder` | ingresso |  | Folder allegati in cui vengono inseriti i file splittati |
| `Dest.Document.Group` | ingresso |  | Gruppo Documenti in cui vengono inseriti i file splittati |
| `Dest.Document.Root` | ingresso |  | Root Documenti in cui vengono inseriti i file splittati |
| `Dest.Document.Folder` | ingresso |  | Folder Documenti in cui vengono inseriti i file splittati |
| `Dest.NoRIF.Group` | ingresso |  | Gruppo allegati in cui vengono inseriti i file splittati senza RIF |
| `Dest.NoRIF.Root` | ingresso |  | Root allegati in cui vengono inseriti i file splittati senza RIF |
| `Dest.NoRIF.Folder` | ingresso |  | Folder allegati in cui vengono inseriti i file splittati senza RIF |
| `Var.Root` | ingresso |  | Variabile allegato per la root ricavata dai riferimenti barcode |
| `Var.Folder` | ingresso |  | Variabile allegato per la cartella attachment  ricavata dai riferimenti barcode |
| `Var.Barcode` | ingresso | sì | Variabile allegato per il nome Barcode ricavata dai riferimenti barcode |
| `Var.InstanceID` | ingresso | sì | Variabile allegato per l'instanceID ricavata dai riferimenti barcode |
| `Var.Model` | ingresso | sì | Variabile allegato per modello ricavata dai riferimenti barcode |
| `Var.Name` | ingresso | sì | Variabile allegato per il nome ricavata dai riferimenti barcode |
| `AllThingsFound` | uscita |  | — |
| `AnyBarcodesFound` | uscita |  | Se ha trovato dei barcode il valore è true altrimenti false |
| `AnyRiferimentiFound` | uscita |  | Se ha trovato tutti i Riferimenti il valore è true altrimenti false e viene valorizzata RiferimentiNotFound |
| `RiferimentiNotFound` | uscita |  | Lista dei riferimenti non trovati. Se valorizzato, ricontrolla se i riferimenti dentro questa variabile sono collegati a SAM/BPM WEB |
| `Anomalia` | uscita |  | Motivazione dell'anomalia rilevata |
| `Barcode.Filter` | ingresso |  | Scansiona solo i barcode che iniziano per il valore inserito |

### CreateOrUpdateDocument [Client]

*Azione client.* Create or Update a document on button click

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | * |
| `Source.FilePath.DeleteAfter` | ingresso |  | * |
| `Source.Base64.Content` | ingresso |  | * |
| `Source.Attachment.Group` | ingresso |  | * |
| `Source.Attachment.DeleteAfter` | ingresso |  | * |
| `Source.Report` | ingresso |  | * |
| `Source.ReportFormat` | ingresso |  | pdf, docx, xlsx |
| `DestinationType` | ingresso | sì | self, document |
| `Doc.Model` | ingresso |  | — |
| `Doc.StartObject` | ingresso |  | optional |
| `Doc.Barcode` | ingresso |  | * |
| `Doc.NewVersion` | ingresso |  | — |
| `Doc.NewVersion.Number` | ingresso |  | — |
| `Doc.NewVersion.Description` | ingresso |  | — |
| `Doc.NewVersion.Date` | ingresso |  | — |
| `Doc.SignedCopy` | ingresso |  | — |
| `Doc.JSONVariables` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `InstanceId` | uscita |  | — |
| `DocumentName` | uscita |  | — |
| `DocumentDescription` | uscita |  | — |

### AddAttachment [Client]

*Azione client.* Add an attachment on button click

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `SourceType` | ingresso | sì | filePath, base64, attachment, report |
| `Source.Extension` | ingresso |  | file extension (not needed for filePath) |
| `Source.FilePath` | ingresso |  | — |
| `Source.FilePath.DeleteAfter` | ingresso |  | — |
| `Source.Base64.Content` | ingresso |  | — |
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Report` | ingresso |  | — |
| `Source.ReportFormat` | ingresso |  | — |
| `DestinationType` | ingresso |  | — |
| `Dest.Model` | ingresso |  | — |
| `Dest.DocumentName` | ingresso |  | — |
| `Dest.InstanceId` | ingresso |  | — |
| `Dest.Attachment.Group` | ingresso |  | — |
| `Dest.Attachment.Type` | ingresso |  | — |
| `Dest.Attachment.FileNameInternal` | ingresso | sì | (unique per instance) |
| `Dest.Attachment.FileNameDisplay` | ingresso |  | (view) |
| `Dest.Attachment.Description` | ingresso |  | — |
| `Dest.Attachment.Root` | ingresso |  | — |
| `Dest.Attachment.Folder` | ingresso |  | — |

### AddLinkedDocument

*Operazione.* —

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `InstanceId` | ingresso |  | — |
| `Model` | ingresso |  | — |
| `InstanceName` | ingresso |  | — |
| `Linked.InstanceId` | ingresso |  | — |
| `Linked.Model` | ingresso |  | — |
| `Linked.InstanceName` | ingresso |  | — |
| `Dest.AttachmentRoot` | ingresso |  | — |
| `Dest.AttachmentFolder` | ingresso |  | — |

### DeleteAttachment

*Operazione.* —

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso |  | — |
| `Source.Attachment.FileName` | ingresso |  | — |
| `DeletedCount` | uscita |  | — |

### DeleteDocument

*Operazione.* —

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Doc.InstanceId` | ingresso |  | — |
| `Doc.Model` | ingresso |  | — |
| `Doc.DocumentName` | ingresso |  | — |
| `Doc.UserName` | ingresso |  | — |
| `DeletedDocumentsCount` | uscita |  | — |
| `DeletedLinksCount` | uscita |  | — |
