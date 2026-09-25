<!-- Generato da tools/genera-connettori.py dal manifesto Mail Connector versione 20260902. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [IncomingMail](#incomingmail) | evento | Evento che si scatena con l'arrivo di una nuova mail |
| [ExtractMail](#extractmail) | operazione | Extract Mail data from .MSG or .EML files |

### IncomingMail

*Evento.* Evento che si scatena con l'arrivo di una nuova mail

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `ConfigEmail` | ingresso | sì | Configurazione IMAP da utilizzare per la ricezione mail |
| `ConfigFolder` | ingresso | sì | Folder mail da monitorare |
| `MailAttachmentsGroup` | ingresso |  | Gruppo allegati in cui archiviare il file .EML della mail |
| `Destination.Attachment.Root` | ingresso |  | Root in cui inserire gli allegati alla mail |
| `Destination.Attachment.Folder` | ingresso |  | Folder in cui inserire gli allegati alla mail |
| `Destination.Attachment.FileName` | ingresso |  | Nome allegato da forzare (se lasciato vuoto rimane nome originale dell'allegato da mail) |
| `Destination.Attachment.Filter` | ingresso |  | Filtro per scegliere quali allegati mail prendere (es. *.pdf) |
| `AttachmentsGroup` | ingresso |  | Gruppo allegati in cui inserire gli allegati alla mail |
| `Action` | ingresso |  | Azione da implementare dopo la ricezione della mail (elimina, sposta..) |
| `MoveToMailFolder` | ingresso |  | Folder mail di destinazione per lo spostamento |
| `FromName` | uscita |  | Nome mittente |
| `FromAddress` | uscita |  | Indirizzo mittente |
| `Cc` | uscita |  | — |
| `Bcc` | uscita |  | — |
| `Subject` | uscita |  | Oggetto mail |
| `Text` | uscita |  | Testo mail (plain text) |
| `HtmlText` | uscita |  | Testo mail (html formatted text) |
| `ReferenceInstanceId` | uscita |  | Riferimento a istanza processo/documento BPM (BPM Ref) |
| `AttachmentsData` | uscita |  | — |
| `To` | uscita |  | — |
| `MessageId` | uscita |  | Identificatore univoco messaggio |
| `Date` | uscita |  | Data mail |

### ExtractMail

*Operazione.* Extract Mail data from .MSG or .EML files

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Source.Attachment.Group` | ingresso | sì | Gruppo allegati in cui trovare il file .EML oppure .MSG da elaborare |
| `Destination.Attachment.Group` | ingresso |  | Gruppo allegati in cui inserire gli allegati alla mail |
| `Destination.Attachment.Root` | ingresso |  | Root in cui inserire gli allegati alla mail |
| `Destination.Attachment.Folder` | ingresso |  | Folder in cui inserire gli allegati alla mail |
| `Destination.Attachment.FileName` | ingresso |  | Nome allegato da forzare (se lasciato vuoto rimane nome originale dell'allegato da mail) |
| `Destination.Attachment.Filter` | ingresso |  | Filtro per scegliere quali allegati mail prendere (es. *.pdf) |
| `FromName` | uscita |  | Nome mittente |
| `FromAddress` | uscita |  | Indirizzo mittente |
| `To` | uscita |  | — |
| `Cc` | uscita |  | — |
| `Bcc` | uscita |  | — |
| `Subject` | uscita |  | Oggetto mail |
| `Text` | uscita |  | Testo mail (plain text) |
| `HtmlText` | uscita |  | Testo mail (html formatted text) |
| `ReferenceInstanceId` | uscita |  | Riferimento a istanza processo/documento BPM (BPM Ref) |
| `MessageId` | uscita |  | Identificatore univoco messaggio |
| `Date` | uscita |  | Data messaggio |
