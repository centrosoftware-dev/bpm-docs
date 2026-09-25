# Roadmap

## Ristrutturazione del riferimento

- Acquisire lo studio dettagliato in corso sui tipi di formula, sulle proprieta e sui punti di configurazione, basato su oltre 300 modelli di processo usati in casi reali.
- Trasformarlo in una checklist di copertura per verificare che il nuovo riferimento non ometta configurazioni esistenti.
- Costruire prima della riscrittura un inventario di aree, schermate, oggetti, comandi, proprieta e formule, collegando ogni voce alla pagina prevista e al suo stato di verifica.
- Basare i contenuti sulle indicazioni scritte degli esperti di prodotto: consulenti applicativi, sviluppatori, tester e responsabili del prodotto.
- Usare lo studio empirico per interrogare gli autori, individuare omissioni e verificare i casi reali.
- Ripassare e verificare i contenuti precedenti: il vecchio manuale puo suggerire argomenti, ma non certifica il comportamento corrente.
- Consentire contributi incrementali durante sviluppo, test e consulenza, offrendo a ogni informazione una collocazione prevedibile nella struttura.
- Collegare issue e modifiche del prodotto alla scrittura o all'aggiornamento della documentazione pertinente.
- Tracciare la copertura con tre stati: Da documentare, Da verificare e Verificato. Una modifica del prodotto riporta a Da verificare i contenuti interessati.
- Inizialmente non richiedere una seconda revisione obbligatoria: chi assegna lo stato Verificato assume la responsabilita tecnica del contenuto.
- Abbozzare la navigazione completa con pagine introduttive utili per le cinque macroaree e per le dieci sezioni del Menu Configurazione, senza pubblicare pagine di dettaglio vuote.
- Usare lo stato editoriale come traccia libera per il team, non come processo formale di approvazione.
- Per i nuovi contenuti usare titoli italiani coerenti con l'interfaccia e percorsi in minuscolo, ASCII, con parole separate da trattini e senza spazi o accenti.
- Non mantenere redirect per i percorsi attuali: il vecchio sito non e mai stato pubblicato.
- Conservare e migrare le informazioni esistenti come materiale attendibile ma da verificare, perche possono essere cambiate dall'ultima stesura.
- Conservare l'inventario in file strutturati separati per macroarea, usandolo anche come traccia dello stato di copertura.
- Affidare anche agli agenti AI l'aggiornamento dell'inventario e sottoporlo comunque a verifica periodica: non dipendere dal suo aggiornamento manuale perfetto.
- Scrivere una guida sintetica per collaboratori e agenti AI con struttura, collocazione dei contenuti, convenzioni, modelli di pagina, screenshot e gestione dell'inventario.
- Migrare direttamente alla nuova struttura: classificare e recuperare i contenuti utili, poi rimuovere la vecchia organizzazione senza mantenerla in parallelo.
- Usare l'inventario come unica fonte dello stato editoriale, senza duplicarlo nei metadati delle pagine.
- Aggiungere controlli automatici per validita degli inventari, identificatori duplicati, percorsi mancanti, pagine non inventariate e stati non ammessi.












## Decisioni del 23/9

- Tutorial e riferimento possono ripetere gli stessi concetti. Il tutorial non copre tutto: il riferimento resta la fonte completa.
- Navigazione principale: Inizia (home e tutorial) · Processi · Documenti · Integrazione e AI · Amministrazione. La scheda Tutorial scompare: i percorsi di apprendimento stanno sotto Inizia.
- Amministrazione unisce Menu Configurazione e Sistema. Connettori passano a Integrazione e AI; dashboard e report alle Parti comuni.
- Parti comuni (variabili, formule e script, dashboard, report, glossario): nessuna scheda in alto; ci si arriva dai link di processi, documenti e homepage. La sezione resta nella navigazione per avere la barra laterale, ma la sua scheda è nascosta via CSS.
- Ogni informazione si documenta dove si configura. Dashboard e report si configurano nei loro menu ma si consultano da menu personalizzati e schermate dei processi: le pagine di configurazione lo dicono subito, e i modelli di processo e di documento rimandano a esse.
- La parte operativa, piccola, sta nell'area a cui appartiene: To-Do List e ricerca processi in Processi; ricerca documenti e dossier in Documenti.
- Integrazione e AI: la pagina d'ingresso riassume e rimanda a due sezioni nettamente separate, Integrazione (Web API, coda delle chiamate, SQL, fonti dati, script, acquisizione documenti, connettori) e Intelligenza artificiale.
- Nei contenuti non insistere sul client desktop: il Designer passerà al web nei prossimi mesi.

## Da fare — Riccardo

- [ ] Scrivere a mano la lista di tutto quello che il riferimento deve coprire, distinguendo le cose del prodotto (schermate, oggetti, campi, comandi) dai temi trasversali (permessi, formule, allegati…).
- [ ] Portare avanti lo studio sui 300 modelli di processo e usarlo per verificare la lista.
- [ ] Autenticazione del sito: parlare con chi gestisce l'accesso di `portali.centrosoftware.com` (OAuth 2.0 custom, non OpenID Connect) per registrare un nuovo client per la documentazione e capire quali dati utente restituisce (nome, azienda, ruolo).
- [ ] Pubblicazione su Azure dietro una piccola app ASP.NET che fa login con lo stesso flusso di ERP Connect (`/account/signin`) e serve il sito statico generato da MkDocs.
- [ ] Da capire: integrare la pipeline CI attuale (build MkDocs) con la costruzione e il rilascio del contenitore ASP.NET, al posto di GitHub Pages. Ipotesi: un solo repository, con l'app ASP.NET in una cartella `host/` e un Dockerfile multi-stage (build MkDocs, poi build .NET, poi immagine finale con il sito in `wwwroot`).

# Appunti sparsi

analisi dati cancellare

Tagliare pagine troppo lunghe

Attributi variabili - tabella per tipi var

Pagine tematiche - 
