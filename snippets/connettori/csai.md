<!-- Generato da tools/genera-connettori.py dal manifesto Cs AI Connector versione 20251216. Non modificare a mano. -->

### Configurazione del connettore

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `ApiKey` | ingresso |  | — |
| `AiAgentEndpoint` | ingresso |  | (opzionale) normalmente viene lasciato vuoto |
| `Partita IVA Attivazione` | ingresso |  | — |

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [AI Agent](#ai-agent) | operazione | Esegue un comando descritto in linguaggio naturale, prendendo come contesto le informazioni presenti all'interno del processo |
| [AI Document Intelligence (Read)](#ai-document-intelligence-read) | operazione | Estrae il testo dal documento |
| [AI Document Intelligence (Layout)](#ai-document-intelligence-layout) | operazione | Estrae testo strutturato dal documento |
| [AI Document Intelligence (Invoice)](#ai-document-intelligence-invoice) | operazione | Estrae informazioni da un documento tipo fattura/ddt/ordine (testata, righe) |
| [Update Index](#update-index) | operazione | Aggiorna indice per ricerca full text |
| [AI Agent [Client]](#ai-agent-client) | azione client | agent disponibile in modalità immediata nel client |
| [AI Document Intelligence (IDDocuments)](#ai-document-intelligence-iddocuments) | operazione | Estrae informazioni da un documento di tipo identificativo (Carta d'identità, Patente, Passaporto) |
| [AI Document Intelligence (Contract)](#ai-document-intelligence-contract) | operazione | Estrae informazioni da un documento contrattuale |

### AI Agent

*Operazione.* Esegue un comando descritto in linguaggio naturale, prendendo come contesto le informazioni presenti all'interno del processo

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Agent Exception` | uscita |  | Id dell'eccezione che l'agent ha eventualmente trovato |
| `Agent Comment` | uscita |  | Eventuale risposta testuale dell'agent |
| `Agent Model` | ingresso |  | Modello AI dell'agente |

### AI Document Intelligence (Read)

*Operazione.* Estrae il testo dal documento

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `AttachmentsGroup` | ingresso | sì | — |
| `FromPage` | ingresso |  | — |
| `ToPage` | ingresso |  | — |
| `ContentFormat` | ingresso |  | — |
| `Content` | uscita |  | — |
| `FullJsonResult` | uscita |  | — |
| `Marked.Attachments.FileName` | ingresso |  | — |
| `Marked.Attachments.Root` | ingresso |  | — |
| `Marked.Attachments.Folder` | ingresso |  | — |
| `AnalyzeStructure` | ingresso |  | — |

### AI Document Intelligence (Layout)

*Operazione.* Estrae testo strutturato dal documento

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `AttachmentsGroup` | ingresso | sì | — |
| `ContentFormat` | ingresso | sì | — |
| `FullJsonResult` | uscita |  | — |
| `Content` | uscita |  | — |
| `AnalyzeStructure` | ingresso |  | — |
| `Marked.Attachments.FileName` | ingresso |  | — |
| `Marked.Attachments.Root` | ingresso |  | — |
| `Marked.Attachments.Folder` | ingresso |  | — |

### AI Document Intelligence (Invoice)

*Operazione.* Estrae informazioni da un documento tipo fattura/ddt/ordine (testata, righe)

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Agent Model` | ingresso | sì | Modello dell'agente AI |
| `AttachmentsGroup` | ingresso | sì | Gruppo allegati di provenienza |
| `FullJsonResult` | uscita |  | Json completo della chiamata API |
| `AnalyzeStructure` | ingresso |  | — |
| `CustomerAddress` | uscita |  | Indirizzo controparte |
| `CustomerName` | uscita |  | Nome controparte |
| `CustomerTaxID` | uscita |  | Partita iva / Codice fiscale |
| `InvoiceDate` | uscita |  | Data documento |
| `InvoiceId` | uscita |  | Numero documento |
| `Items.Content` | uscita (righe) |  | Contenuto Riga |
| `Items.Amount` | uscita (righe) |  | Importo Riga |
| `Items.Date` | uscita (righe) |  | Data Riga |
| `Items.Description` | uscita (righe) |  | Descrizione Riga |
| `Items.ProductCode` | uscita (righe) |  | Codice Articolo Riga |
| `Items.PurchaseOrder` | uscita (righe) |  | Numero ordine Riga |
| `Items.Quantity` | uscita (righe) |  | Quantità Riga |
| `Items.Tax` | uscita (righe) |  | — |
| `Items.Unit` | uscita (righe) |  | Unità di misura Riga |
| `Items.UnitPrice` | uscita (righe) |  | Prezzo unitario Riga |
| `PaymentDetails.IBAN` | uscita |  | IBAN pagamento |
| `PaymentDetails.SWIFT` | uscita |  | SWIFT pagamento |
| `PaymentTerms` | uscita |  | Condizioni di pagamento |
| `ShippingAddress` | uscita |  | Indirizzo di consegna |
| `VendorName` | uscita |  | Nome fornitore |
| `AmountDue` | uscita |  | Importo dovuto |
| `InvoiceTotal` | uscita |  | Totale documento |
| `Subtotal` | uscita |  | Subtotale |
| `TaxDetails` | uscita |  | Dettaglio IVA |
| `TotalTax` | uscita |  | IVA |
| `Marked.Attachments.Root` | ingresso |  | — |
| `Marked.Attachments.Folder` | ingresso |  | — |
| `Marked.Attachments.FileName` | ingresso |  | — |

### Update Index

*Operazione.* Aggiorna indice per ricerca full text

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Index.Name` | ingresso | sì | — |
| `Index.Type` | ingresso | sì | BM25, EMBEDDINGS |
| `Language` | ingresso |  | — |
| `Doc.Model` | ingresso | sì | — |
| `Variable` | ingresso | sì | — |
| `Metadata` | ingresso |  | — |

### AI Agent [Client]

*Azione client.* agent disponibile in modalità immediata nel client

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `Agent Exception` | uscita |  | Eccezione dall'agent |
| `Agent Comment` | uscita |  | Eventuale risposta testuale dall'agent |
| `Agent Model` | ingresso |  | Modello AI utilizzato per la richiesta |

### AI Document Intelligence (IDDocuments)

*Operazione.* Estrae informazioni da un documento di tipo identificativo (Carta d'identità, Patente, Passaporto)

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `AttachmentsGroup` | ingresso | sì | — |
| `FullJsonResult` | ingresso |  | — |
| `AnalyzeStructure` | ingresso |  | — |
| `Address` | uscita |  | — |
| `DateOfBirth` | uscita |  | — |
| `DateOfExpiration` | uscita |  | — |
| `DateOfIssue` | uscita |  | — |
| `DocumentDiscriminator` | uscita |  | — |
| `DocumentNumber` | uscita |  | — |
| `FirstName` | uscita |  | — |
| `LastName` | uscita |  | — |
| `Height` | uscita |  | — |
| `PersonalNumber` | uscita |  | — |
| `PlaceOfBirth` | uscita |  | — |
| `Sex` | uscita |  | — |
| `Marked.Attachments.Root` | ingresso |  | — |
| `Marked.Attachments.Folder` | ingresso |  | — |
| `Marked.Attachments.FileName` | ingresso |  | — |

### AI Document Intelligence (Contract)

*Operazione.* Estrae informazioni da un documento contrattuale

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `AttachmentsGroup` | ingresso | sì | — |
| `FullJsonResult` | uscita |  | — |
| `AnalyzeStructure` | ingresso | sì | — |
| `Marked.Attachments.Root` | ingresso |  | — |
| `Marked.Attachments.Folder` | ingresso |  | — |
| `Marked.Attachments.FileName` | ingresso |  | — |
| `Title` | uscita |  | — |
| `ContractId` | uscita |  | — |
| `ExecutionDate` | uscita |  | — |
| `EffectiveDate` | uscita |  | — |
| `RenewalDate` | uscita |  | — |
| `TerminationDate` | uscita |  | — |
| `Parties.Name` | uscita (righe) |  | — |
| `Parties.Address` | uscita (righe) |  | — |
| `Parties.ReferenceName` | uscita (righe) |  | — |
| `Parties.Clause` | uscita (righe) |  | — |
