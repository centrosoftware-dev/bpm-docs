<!-- Generato da tools/genera-connettori.py dal manifesto CreditSafeConnector versione 20260225. Non modificare a mano. -->

### Funzioni disponibili

| Funzione | Tipo | Descrizione |
|---|---|---|
| [GetDataByPartitaIVA](#getdatabypartitaiva) | operazione | Ottiene i dati specificando la partita IVA |
| [GetDataByCodiceFiscale](#getdatabycodicefiscale) | operazione | Ottiene i dati specificando il codice fiscale |
| [GetDataByPartitaIVA_CA](#getdatabypartitaiva-ca) | azione client | Ottiene i dati specificando la partita IVA |
| [GetDataByCodiceFiscale_CA](#getdatabycodicefiscale-ca) | azione client | Ottiene i dati specificando il codice fiscale |

### GetDataByPartitaIVA

*Operazione.* Ottiene i dati specificando la partita IVA

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `PartitaIVA` | ingresso | sì | — |
| `CorrelationId` | uscita |  | — |
| `CompanyId` | uscita |  | — |
| `DateOfOrder` | uscita |  | — |
| `Report.CompanyId` | uscita |  | — |
| `Report.Language` | uscita |  | — |
| `Report.AlternateSummary.Province` | uscita |  | — |
| `Report.AlternateSummary.VatRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.Address` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.SimpleValue` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Street` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.HouseNumber` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.City` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.PostalCode` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Province` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Country` | uscita |  | — |
| `Report.AlternateSummary.BusinessName` | uscita |  | — |
| `Report.AlternateSummary.LegalForm` | uscita |  | — |
| `Report.AlternateSummary.TaxCode` | uscita |  | — |
| `Report.AlternateSummary.Country` | uscita |  | — |
| `Report.AlternateSummary.CompanyNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Status` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Description` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Code` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Description` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Currency` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Value` | uscita |  | — |
| `Report.AlternateSummary.NumberOfEmployees` | uscita |  | — |
| `Report.AlternateSummary.Telephone` | uscita |  | — |
| `Report.AlternateSummary.PublicRegisterSection` | uscita |  | — |
| `Report.AlternateSummary.ShareCapital` | uscita |  | — |
| `Report.AlternateSummary.IncorporationDate` | uscita |  | — |
| `Report.AlternateSummary.ReaInscriptionDate` | uscita |  | — |
| `Report.AlternateSummary.HqType` | uscita |  | — |
| `Report.AlternateSummary.RegisterStatus` | uscita |  | — |
| `Report.AlternateSummary.EmailAddresses` | uscita |  | — |

### GetDataByCodiceFiscale

*Operazione.* Ottiene i dati specificando il codice fiscale

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `CodiceFiscale` | ingresso | sì | — |
| `CorrelationId` | uscita |  | — |
| `CompanyId` | uscita |  | — |
| `DateOfOrder` | uscita |  | — |
| `Report.CompanyId` | uscita |  | — |
| `Report.Language` | uscita |  | — |
| `Report.AlternateSummary.Province` | uscita |  | — |
| `Report.AlternateSummary.VatRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.Address` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.SimpleValue` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Street` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.HouseNumber` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.City` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.PostalCode` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Province` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Country` | uscita |  | — |
| `Report.AlternateSummary.BusinessName` | uscita |  | — |
| `Report.AlternateSummary.LegalForm` | uscita |  | — |
| `Report.AlternateSummary.TaxCode` | uscita |  | — |
| `Report.AlternateSummary.Country` | uscita |  | — |
| `Report.AlternateSummary.CompanyNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Status` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Description` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Code` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Description` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Currency` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Value` | uscita |  | — |
| `Report.AlternateSummary.NumberOfEmployees` | uscita |  | — |
| `Report.AlternateSummary.Telephone` | uscita |  | — |
| `Report.AlternateSummary.PublicRegisterSection` | uscita |  | — |
| `Report.AlternateSummary.ShareCapital` | uscita |  | — |
| `Report.AlternateSummary.IncorporationDate` | uscita |  | — |
| `Report.AlternateSummary.ReaInscriptionDate` | uscita |  | — |
| `Report.AlternateSummary.HqType` | uscita |  | — |
| `Report.AlternateSummary.RegisterStatus` | uscita |  | — |
| `Report.AlternateSummary.EmailAddresses` | uscita |  | — |

### GetDataByPartitaIVA_CA

*Azione client.* Ottiene i dati specificando la partita IVA

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `PartitaIVA` | ingresso | sì | — |
| `CorrelationId` | uscita |  | — |
| `CompanyId` | uscita |  | — |
| `DateOfOrder` | uscita |  | — |
| `Report.CompanyId` | uscita |  | — |
| `Report.Language` | uscita |  | — |
| `Report.AlternateSummary.Province` | uscita |  | — |
| `Report.AlternateSummary.VatRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.Address` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.SimpleValue` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Street` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.HouseNumber` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.City` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.PostalCode` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Province` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Country` | uscita |  | — |
| `Report.AlternateSummary.BusinessName` | uscita |  | — |
| `Report.AlternateSummary.LegalForm` | uscita |  | — |
| `Report.AlternateSummary.TaxCode` | uscita |  | — |
| `Report.AlternateSummary.Country` | uscita |  | — |
| `Report.AlternateSummary.CompanyNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Status` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Description` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Code` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Description` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Currency` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Value` | uscita |  | — |
| `Report.AlternateSummary.NumberOfEmployees` | uscita |  | — |
| `Report.AlternateSummary.Telephone` | uscita |  | — |
| `Report.AlternateSummary.PublicRegisterSection` | uscita |  | — |
| `Report.AlternateSummary.ShareCapital` | uscita |  | — |
| `Report.AlternateSummary.IncorporationDate` | uscita |  | — |
| `Report.AlternateSummary.ReaInscriptionDate` | uscita |  | — |
| `Report.AlternateSummary.HqType` | uscita |  | — |
| `Report.AlternateSummary.RegisterStatus` | uscita |  | — |
| `Report.AlternateSummary.EmailAddresses` | uscita |  | — |

### GetDataByCodiceFiscale_CA

*Azione client.* Ottiene i dati specificando il codice fiscale

| Parametro | Direzione | Obbligatorio | Descrizione |
|---|---|---|---|
| `CodiceFiscale` | ingresso | sì | — |
| `CorrelationId` | uscita |  | — |
| `CompanyId` | uscita |  | — |
| `DateOfOrder` | uscita |  | — |
| `Report.CompanyId` | uscita |  | — |
| `Report.Language` | uscita |  | — |
| `Report.AlternateSummary.Province` | uscita |  | — |
| `Report.AlternateSummary.VatRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.Address` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.SimpleValue` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Street` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.HouseNumber` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.City` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.PostalCode` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Province` | uscita |  | — |
| `Report.AlternateSummary.ContactAddress.Country` | uscita |  | — |
| `Report.AlternateSummary.BusinessName` | uscita |  | — |
| `Report.AlternateSummary.LegalForm` | uscita |  | — |
| `Report.AlternateSummary.TaxCode` | uscita |  | — |
| `Report.AlternateSummary.Country` | uscita |  | — |
| `Report.AlternateSummary.CompanyNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyRegistrationNumber` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Status` | uscita |  | — |
| `Report.AlternateSummary.CompanyStatus.Description` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Code` | uscita |  | — |
| `Report.AlternateSummary.MainActivity.Description` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Currency` | uscita |  | — |
| `Report.AlternateSummary.LatestTurnoverFigure.Value` | uscita |  | — |
| `Report.AlternateSummary.NumberOfEmployees` | uscita |  | — |
| `Report.AlternateSummary.Telephone` | uscita |  | — |
| `Report.AlternateSummary.PublicRegisterSection` | uscita |  | — |
| `Report.AlternateSummary.ShareCapital` | uscita |  | — |
| `Report.AlternateSummary.IncorporationDate` | uscita |  | — |
| `Report.AlternateSummary.ReaInscriptionDate` | uscita |  | — |
| `Report.AlternateSummary.HqType` | uscita |  | — |
| `Report.AlternateSummary.RegisterStatus` | uscita |  | — |
| `Report.AlternateSummary.EmailAddresses` | uscita |  | — |
