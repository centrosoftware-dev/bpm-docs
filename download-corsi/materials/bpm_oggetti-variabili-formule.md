# BPM — Catalogo di riferimento: oggetti, variabili, formule

Catalogo tecnico unificato compilato dai transcript integrali dei corsi bpm-base e bpm-avanzato. Raccoglie in un unico riferimento tutti gli oggetti trascinabili nel Designer, tutti i tipi di variabile di processo con le relative caratteristiche, e tutte le formule/espressioni citate nei due corsi, indipendentemente da quale dei due corsi le abbia introdotte.

---

## 1. Oggetti

### 1.1 Eventi di avvio

**Start (evento di inizio)** — forma a pallino verde, indica il punto di partenza esplicito del processo.

- Ha proprie Variabili da richiedere (il sottoinsieme di campi necessari per avviare il processo).
- Può essere rinominato/etichettato con "Sposta testo" (es. "Inserimento richiesta").
- Supporta formule di default (es. valorizzare l'utente corrente, la data corrente) e formule di validazione locali.
- Un processo può avere **più oggetti Start** (es. "richiesta normale" e "richiesta sicurezza"): ciascuno con proprie variabili da richiedere e proprie regole di validazione, propri valori di default (es. campo precompilato e in sola lettura).
- Se non specificato, all'avvio il sistema chiede quale start utilizzare; si può fissare uno start specifico su una voce di menu personalizzato per evitare il prompt.
- Permessi differenziati per start: si può limitare quale gruppo/utente può avviare un determinato start ("utenti responsabili" sullo start).

**Start a tempo (timer start)** — avvia il processo secondo una schedulazione anziché un evento/utente.

- Ricorrenza configurabile: ogni giorno, ogni settimana di lunedì, ogni primo del mese, ogni primo lunedì del mese, con orario specifico (es. alle 8:00).
- Il processo parte "orfano" di variabili (nessun dato iniziale): serve una prima attività per raccogliere dati e un eventuale contatore/data.
- Utile per attività periodiche/amministrative (es. chiusure mensili).

### 1.2 Attività

**Attività (Task)** — elemento base del disegno di processo, rappresenta un lavoro da svolgere da un utente/gruppo.

- Nome interno immutabile assegnato automaticamente alla creazione (es. Activity1, Activity2...), è l'ID dell'attività e non cambia più.
- Nome visualizzato (testo) modificabile con tasto destro > Modifica testo, visto da tutti gli utenti; modalità "Sposta testo" per staccare graficamente l'etichetta dal box mantenendo il collegamento logico.
- Utenti/gruppi assegnati con tre ruoli: **Esecutore** (la trova in To Do List), **Responsabile** (può smistare/assegnare l'attività a membri del proprio gruppo), **Per conoscenza** (deve solo sapere che è stata svolta).
- Flag "Task deve essere assegnato prima di poter essere eseguito" (richiede un passaggio di assegnazione da parte del responsabile prima che un singolo esecutore la veda in To Do List).
- Possibilità di lasciare un'attività senza utenti intestatari in fase di sviluppo (visibile solo all'amministratore) — a regime deve sempre avere un utente/gruppo assegnato.
- Esecutore/responsabile impostabile anche come variabile di processo di tipo utente (es. "il richiedente"), per instradare dinamicamente l'attività.
- **Variabili da richiedere**: sottoinsieme di variabili del magazzino mostrate/richieste in quell'attività, con proprietà locali (obbligatorio, sola lettura, formula di validazione, default, filtro — vedi §2.3).
- **Allegati da richiedere**: analogo alle variabili da richiedere ma per la gestione documentale; possibilità di puntare a una cartella specifica (sola visualizzazione o inserimento).
- Icona "chiocciola" quando sono configurate variabili da richiedere; icona "graffetta" quando sono configurati allegati da richiedere; icona a forma di "bidone/database" quando ha operazioni agganciate.
- Colorazione di stato nel disegno: grigio = eseguita, giallo = in corso, verde chiaro = pianificata (prevista ma non ancora raggiunta), nero = non ancora vista.
- Colonne/attributi visibili in To Do List: utente, attività, modello, nome processo, data di inizio prevista, priorità (indicatore libero senza logica), scadenza, percentuale di completamento.
- Condizione di abilitazione applicabile sulle frecce (link) in uscita, con comparsa di un "diamantino"/baffetto se presenti condizioni.
- Può essere trasformata in **Sottoprocesso** mantenendo i collegamenti.
- Operazioni agganciabili sul ciclo di vita del task (vedi §1.4): attivazione, inizio, esecuzione, esecuzione terminata.
- Proprietà di pianificazione/scadenze avanzate — vedi §1.6.

**Sottoprocesso** — doppio clic apre un disegno annidato indipendente (con propri task, eventuali fine, ecc.), per incapsulare/dettagliare una parte di processo senza appesantire il disegno principale.

- Un'attività (task) esistente può essere trasformata in sottoprocesso.
- **Sottoprocesso ricorrente**: il contenuto viene istanziato n volte, una per ogni riga di un gruppo di variabili collegato (es. una valutazione per ogni preventivo ricevuto, numero non prevedibile a priori).
  - Modalità di esecuzione: **parallela** (icona righe verticali, tutte le istanze generate insieme) o **sequenziale** (icona righe orizzontali, un'istanza alla volta secondo un ordine).
  - Possibilità di impostare una "formula per condizione" che seleziona solo alcune righe del gruppo per cui generare l'istanza.
  - Le variabili del gruppo collegato, dentro le variabili da richiedere del sottoprocesso, sono viste come valore singolo di riga (non come griglia).
  - Le variabili sono condivise in tempo reale col processo padre (a differenza del "processo collegato", che ha variabili proprie) — alternativa più recente e più snella al processo collegato quando il numero di istanze non è noto a priori.
  - Graficamente in esecuzione assume colore giallo e mostra la struttura espansa con le singole istanze quando aperto.

### 1.3 Eventi di fine

**Fine (End)** — oggetto puramente grafico che identifica il punto di terminazione di un ramo del disegno.

- Nessuna funzione operativa: il processo si considera comunque concluso quando non ci sono più attività da fare, con o senza questo oggetto; non termina eventuali altri rami ancora attivi.
- Si possono inserire più "Fine" diverse nello stesso processo per chiarezza grafica (es. una normale e una "per annullamento"), ciascuna etichettabile con testo descrittivo.

**Termina processo** — a differenza di "Fine", ha un effetto operativo reale: se il flusso arriva qui, le eventuali altre attività ancora aperte del processo (anche su rami paralleli) vengono troncate/interrotte forzatamente e l'intera istanza viene terminata. Usato tipicamente su rami di eccezione.

**Escalation / Time out (evento boundary su attività)** — collegato al bordo di un'attività (non è un evento libero nel flusso); non è in toolbox come oggetto autonomo, si crea trascinando dal bordo dell'attività.

- Si attiva dopo un certo numero di giorni dalla data di attivazione o dalla scadenza dell'attività.
- Porta a un percorso alternativo (es. attività di sollecito, escalation a un altro utente).
- "Escalation" e "time out" sono la stessa funzionalità, differiscono solo nell'etichetta grafica.
- Corrisponde al "boundary event" dello standard BPMN.

### 1.4 Stati e milestone

**Stato (evento intermedio / milestone)** — forma tonda, rappresenta una milestone/punto importante del processo (non un task da eseguire).

- Si collega trascinando un punto di ancoraggio da un'attività/link esistente.
- Etichetta libera e puramente descrittiva (es. "Inserito", "Approvata", "Annullata"), senza significato applicativo vincolante.
- Quando è lo stato attivo del processo compare in verde acceso nel disegno; se non più attivo resta bianco.
- Viene mostrato anche nella schermata di sintesi/anagrafica del processo come "stato" corrente.

### 1.5 Gateway e sincronizzazione

**Gateway esclusivo** (diamante, "if secco" / percorsi alternativi) — un solo percorso in uscita possibile (scelta secca, uscite mutuamente esclusive).

- Configurazione centralizzata delle uscite (doppio clic/tasto destro > Configurazione): mostra tutte le condizioni in un'unica schermata.
- Ogni uscita ha una condizione (formula); una delle uscite può essere marcata come "else" (default, se nessun'altra condizione è vera).
- Compatibile con lo standard BPMN, più esplicito visivamente del semplice "baffetto" sulle frecce; può essere rinominato (es. "Scelta approvazione").
- Alternativa equivalente: mettere le condizioni direttamente sui link in uscita da un task (vedi §1.6) — con quell'approccio più link in uscita non sono automaticamente mutuamente esclusivi, vanno scritti in modo che si controbilancino.

**Gateway parallelo** (percorsi paralleli) — apre più percorsi contemporaneamente senza condizioni (tutti i rami partono).

- Va usato in coppia: un gateway che "apre" i percorsi e un gateway analogo che li "richiude" aspettando che tutti i rami siano completati (sincronizzazione).

**Gateway inclusivo** (percorsi liberi) — consente di attivare da zero a n percorsi in uscita in base a condizioni (anche impostabili con variabili booleane), utile quando più rami possono essere attivati insieme, uno solo, o nessuno.

- Lo stesso oggetto si usa in configurazione "diramazione" (1 entrata, n uscite) oppure "ricongiungimento" (n entrate, 1 uscita); non si possono configurare n entrate e n uscite contemporaneamente (il sistema lo impedisce con una riga rossa).
- In modalità ricongiungimento non richiede configurazione: attende che tutte le attività partite siano concluse.
- Presentato come alternativa più "moderna"/espressiva alla sbarra di sincronizzazione.

**Sbarra di sincronizzazione** (sincronizzatore, notazione legacy) — cancello che si apre solo quando tutti i rami collegati sono arrivati.

- Le frecce hanno sempre direzione dall'origine alla destinazione (non conta se l'aggancio è sopra o sotto).
- Modalità **ALL**: aspetta sempre tutti i rami collegati anche se non tutti sono partiti (rischio di blocco se un ramo non parte mai).
- Modalità **ALL PLANNED**: aspetta solo i rami effettivamente partiti — da preferire quando i rami a monte sono condizionati.
- Possibilità di impostare una formula di apertura personalizzata, oltre a "tutte pianificate".

### 1.6 Link

**Link (freccia di collegamento)** — strumento per disegnare le transizioni tra oggetti del processo, tramite punti di ancoraggio (pallini gialli) che permettono collegamenti flessibili.

- Può avere una **Condizione di abilitazione** (formula VBScript) che determina quando il flusso passa di là.
- Quando ha una condizione compare un piccolo "baffetto"/etichetta sul link.
- Più link in uscita da uno stesso task non sono automaticamente mutuamente esclusivi: le condizioni vanno scritte in modo che si controbilancino a vicenda.
- L'editor della formula propone/aiuta con riferimenti a variabili e formule già pronte (es. Count su variabile di gruppo).
- Usata anche per impedire che il processo prenda una strada se una condizione sui dati non è soddisfatta (es. nessuna riga di un certo tipo in un gruppo).
- Serve anche per i percorsi di ritorno/alternativi (es. rifiuto/riapprovazione).
- Strumenti di allineamento disponibili (stessa larghezza, allinea al centro, ecc.), applicabili anche ai link.

### 1.7 Operazioni (automatismi)

Categoria di oggetti che rappresentano azioni di sistema senza intervento umano diretto: trascinabili direttamente nel flusso del processo, oppure agganciabili a un task (tasto destro > operazioni) su uno dei quattro momenti del suo ciclo di vita — **attivazione** (il task diventa disponibile/visibile, giallo nel disegno), **inizio** (l'utente dichiara di aver iniziato, richiede il flag "rileva inizio"), **esecuzione** (subito prima del completamento effettivo) ed **esecuzione terminata** (dopo il completamento, prima di attivare il task successivo). Possono anche essere agganciate come azione a un pulsante (variabile booleana di tipo bottone).

- **Invio Mail**: richiede un modello mail (nome/descrizione, oggetto con variabili, destinatari — utente fisso, gruppo o variabile che contiene un indirizzo/utente —, eventuali "in copia conoscenza", body con testo libero e variabili). Sezione allegati per documenti del processo e/o report generati. Variabili generiche disponibili: "utente esecutore attività", "attività corrente", "link web al task" (link diretto all'esecuzione nell'app web, equivalente al tasto Esegui), "link al processo", "allegati". Dipende dal parametro di sistema "url base link email" (altrimenti i link generano localhost). Un modello è riutilizzabile su più attività diverse (parametrico).
- **Creazione nuovo processo collegato**: unica operazione non disponibile nell'ambito di un task (solo nel flusso principale). Scelta del modello e dello start (se il modello ne ha più di uno); opzione "attendi ritorno"/"non attendere ritorno" (sincrono vs fire-and-forget); formula per decidere se creare veramente il processo; comportamento in caso di riciclo (di default non ricrea il processo già creato, spuntabile per crearne un altro in parallelo); mappatura "variabili a copiare" tra processo padre e figlio (manuale o con "automap" per nome/tipo uguale) e "variabili da impostare" come valori fissi; allegati da copiare (anche di un gruppo specifico); formula/script per impostare variabili di destinazione da variabili di origine. Il processo figlio ha variabili proprie, indipendenti da quelle del padre. Alternativa più recente e spesso preferibile: il sottoprocesso ricorrente.
- **Ritorno al processo chiamante**: obbligatoria nel processo figlio quando il padre usa "attendi ritorno"; va posizionata alla fine del processo figlio; segnala il completamento e sblocca il padre; permette di passare indietro variabili di ritorno e allegati, con formula per impostare le variabili al ritorno.
- **Set Variables** (imposta/pulisci variabili): imposta o azzera ("blank") una o più variabili tramite script, con più righe di logica possibili. Casi d'uso: ripulire un campo esito quando il processo torna indietro (evita loop dovuti a obbligatorietà del campo); instradamento dinamico dell'esecutore in base a un valore (es. importo). Suggerito di mettere le operazioni "tecniche" dentro al task (non nel flusso visibile) per mantenere il disegno leggibile.
- **Decision Table** (tabella di decisione): modo dichiarativo, alternativo alla formula/script, per esprimere logiche if/else su combinazioni di condizioni. Colonne di Input e di Output (anche multiple); righe/regole riordinabili tramite frecce su/giù (l'ordine conta); input impostabile a "qualsiasi" (nessuna condizione su quella colonna in quella riga). Genera codice/formula "dietro le quinte" ma resta mostrata come tabella; convertibile in formula testuale (perdendo il legame con la tabella) e, in alcuni contesti, viceversa. Disponibile ovunque ci sia una formula (anche come validazione di un campo, proponendo automaticamente l'output vero/falso; se l'input è una variabile utente, propone automaticamente utenti/gruppi possibili). Adatta solo a combinazioni relativamente semplici, non a iterazioni su righe di un gruppo.
- **SQL libero**: esegue una query SQL libera su una connessione esterna configurata (stringa di connessione). Supporta update, insert, select, chiamata a stored procedure. Parametri mappabili a variabili del processo sia in ingresso sia in uscita. Responsabilità della query interamente del configuratore (BPM non ne valida sintassi/esito).
- **Aggiorna un altro processo** (update process): aggiorna variabili di un altro processo (collegato o no) in qualunque punto del flusso. Richiede una regola di identificazione del processo target: per nome, per uguaglianza di variabile, o per Instance ID. Possibilità di impostare variabili di origine/destinazione, variabili da impostare, formula di passaggio, e di aggiornare allegati. Un uso troppo frequente può indicare forte duplicazione di dati tra processi.
- **Get Data** (recupera dati da tabella esterna): configurazione analoga alla scelta tabella su un campo (tabella, colonna chiave valorizzata da una variabile, colonne da riportare). Esegue automaticamente la selezione/aggiornamento del record senza intervento manuale. Adatta a un caso lineare (un solo record); per join/group by si usa SQL libero. Tipicamente usata a inizio processo per arricchire i dati partendo da un solo codice.
- **Operazioni a livello di processo** (non legate a un task specifico): eseguite automaticamente ogni volta che il processo avanza (comportamento simile a un trigger) — es. query di aggiornamento verso un sistema esterno o invio documenti a un sistema documentale a ogni avanzamento.
- **Connettore attivo (SAM)**: basata sul web import; richiede la scelta di un'interfaccia/template XML predefinito. Parametri di input (testata) mappabili a variabili o a valore fisso, con possibilità di aggiungere campi extra suggeriti dal sistema. Parametri di output (es. ID, numero documento) mappabili su variabili. Parametri di dettaglio per gruppi/righe, con mappatura riga per riga. L'insieme dei parametri disponibili per connettore è finito e predefinito da sviluppo.

### 1.8 Oggetti grafici e di documentazione (senza funzionalità di processo)

- **Casella di testo**: testo libero; colore font, colore/trasparenza bordo, dimensione font personalizzabili (da tasto destro o pannello proprietà). Puramente grafico, utile in vista stampa/PDF.
- **Immagine**: inserimento di immagine/logo nel disegno; nessuna funzionalità di sistema.
- **Memo / Post-it**: testo libero collegabile a un'attività, solo annotazione, nessuna funzionalità nel sistema.
- **Marker** (collegamento tra pagine): fa proseguire il disegno da una pagina all'altra ("tunnel spazio-temporale"), numerato (marker 0, marker 1, ...); si collega a un marker esistente o se ne crea uno nuovo. Utile per processi lunghi su più pagine stampabili.
- **Swim lane**: corsie sempre adiacenti tra loro (non posizionabili liberamente), nome libero (tipicamente ufficio/ruolo/ente). Tasto destro > Utenti responsabili: eredità verso tutte le attività della lane, sovrascrivibile a livello di singola attività. Colore della testata configurabile; lane riordinabili; orientamento orizzontale/verticale per pagina. Obbligatorie nel BPMN classico, opzionali nel prodotto.
- **Gruppo** (oggetto grafico di raggruppamento attività — diverso dal "Gruppo" variabile, vedi §2.2): alternativa alla swim lane per raggruppare graficamente le attività; possibilità di impostare Utenti responsabili sul gruppo; si comprime/espande; utilizzabile anche solo a fini grafici per etichettare visivamente una parte del processo.
- **Pagine e margini** (formato pagina, menu Strumenti > Pagina): dimensione impostabile (A0, A1, A2, A4...), di default formato grande (~A3); possibilità di stampare/esportare in PDF; il processo funziona comunque anche se il disegno sconfina fuori dai margini.

### 1.9 Componenti e configurazioni di sistema

- **Definizione di Connettore** (Configurazione > Connettori): installato tramite DLL/plugin esterno. Espone interfacce di tipo **Azione** (scrittura da BPM verso il sistema esterno) e di tipo **Tabella** (viste in lettura sui dati esterni). Parametri generali (es. indirizzo web service) e parametri per azienda (server database, utente, password, database di configurazione/azienda/marketing, indirizzo web service), con possibilità di gestire più aziende nello stesso connettore. Flag di attivazione. L'aggiornamento del database del connettore genera automaticamente viste SQL con prefisso `vvbpm`. Mappatura utenti tra BPM e sistema esterno (alias) per gestire to-do list/permessi incrociati. Esempi citati: connettore SAM, connettore GLOBE.
- **Tabella locale personalizzata** (Configurazione > Tabelle > Nuova tabella): non è un oggetto trascinato nel canvas ma configurazione di sistema. Editor di struttura analogo a quello delle variabili di processo ma con funzionalità limitate (niente gruppo testata/dettaglio, niente formula di validazione). Nome tabella SQL generato con prefisso `P_` (spazi sostituiti da underscore). Gestione record direttamente da BPM (menu Tabelle); permessi di visualizzazione/modifica per utente/gruppo; "gruppo menu" per raggrupparla nella vista menu, aggiungibile ai menu personalizzati. Tabelle create via script SQL esterno con prefisso `P_` vengono individuate ma non sono editabili da interfaccia. Usata al posto di una value list quando servono più colonne, filtri, o manutenzione indipendente dal designer.
- **Report** (designer PDF, componente terze parti): modello sempre basato su output PDF con "buchi" da riempire con valori delle variabili (raggruppate per pagina/nome, trascinabili sul modello); possibilità di inserire etichette/testi fissi e sezioni mostrabili/nascondibili in base a condizioni sui campi. Supporto a report testata-dettaglio per stampare righe di un gruppo. Salvato nel database del processo; richiamabile/stampabile dall'interno di un'istanza (es. bottone "stampa modulo").
- **Dashboard / Cruscotto** (componente terze parti, stessa famiglia del report designer): richiede una fonte dati collegata a un processo (variabili esposte + nome fonte dati). Oggetti disponibili: **Griglia** (colonne trascinate dalle variabili, formattazione numerica configurabile), **Grafico a torta** (campo valore con aggregazione — conteggio/media — e campo argomenti di raggruppamento), **Casella combinata** (filtro interattivo, es. per anno/mese/giorno). Campi calcolati definibili (es. differenza tra due date), utilizzabili come base per aggregazioni. Raggruppamento automatico delle date per anno di default (configurabile per giorno/mese/anno). Salvato e disponibile in area dedicata ("analisi dati") sia client sia web, senza strumenti di editing. Non è BI vero e proprio: dati sempre "in diretta" dal database del processo, nessun cubo.
- **Pianificazione e scadenze del task** (proprietà avanzate del Task): durata prevista in giorni di calendario (non ore/UOM, nessun concetto di capacità), collegabile a una variabile numerica anche calcolata con formula. Data scadenza collegabile a una variabile di tipo data (consigliato, più robusto di "a giorni dall'inizio"). Flag **"rileva inizio"** (disaccoppia data di inizio effettiva da fine del task precedente, introduce il comando "Inizia" oltre a "Esegui"). Flag **"da confermare"** (l'owner può modificare la pianificazione iniziale prima di "congelarla" come versione 0, singolarmente o con "conferma tutto"). Flag **"utilizza calendario"** (tiene conto di sabati/domeniche/festivi, altrimenti giorni solari continui). Permessi dedicati "visualizza pianificazione" e "modifica pianificazione" (disattivabili per nascondere il Gantt). Gestisce tre serie di date per task: programmazione (pianificazione iniziale), aggiornamento (pianificazione corrente), effettiva (valorizzata solo per task iniziati/conclusi).
- **Diagramma di Gantt del processo**: sequenza logica dei task sull'asse dei tempi; task paralleli rappresentati come tali con ricongiungimento automatico. Pianificazione iniziale tratteggiata, pianificazione aggiornata si sposta man mano (sempre verso destra, mai a sinistra). Bordo del task "spesso" quando la data di inizio effettiva è valorizzata. Puntino rosso = data di scadenza collegata. Spostare un task dalla propria agenda personale sposta anche il Gantt. Giorni non lavorativi mostrati in grigio (se "utilizza calendario" attivo).
- **Calendario di sistema**: gestisce sabati, domeniche e festivi; usato dal calcolo delle durate solo se il task ha "utilizza calendario" attivo; non facilmente personalizzabile.
- **Storico versioni processo** (pubblicazione): ogni pubblicazione crea una riga nello storico con numero progressivo, campo "versione" e "note di pubblicazione" liberi; possibile tornare a una versione precedente e ripubblicare (diventa N+1); traccia utente e data di pubblicazione; possibilità di pulizia dei dati storici (il sistema la impedisce se ci sono processi ancora in esecuzione su quella versione).
- **Undo/Redo del designer**: storico limitato al momento in cui il processo è aperto (circa una decina di passaggi); esiste anche Redo; diverso dallo storico delle versioni pubblicate (persistito nel database).

---

## 2. Variabili

### 2.1 Tipi base

- **Stringa**: tipo di default alla creazione; limite di 250 caratteri (pensato per campi brevi tipo codici/ragioni sociali). Opzione **multilinea** (consente andare a capo, non cambia il limite di lunghezza). Opzione **autocomplete** (propone in combo libera i valori già usati in precedenza sui processi esistenti, senza vincolare a una tabella). Può essere collegata a una tabella di origine (locale o esterna) diventando tendina anziché testo libero.
- **Numero** (campo numerico): opzione **contatore** (valore generato automaticamente come progressivo), modalità *perpetual* (senza reset) oppure raggruppato per un altro campo numerico (es. per Anno). Usato tipicamente per numeratori di processo. Usato anche per durata prevista di un task (solo variabili numeriche sono proponibili per il collegamento alla durata) e come base di logiche di instradamento (es. importo).
- **Valuta**: variante del campo numerico dedicata a importi monetari.
- **Data**: formattazione configurabile; può essere calcolata tramite formula; supporta formule di validazione (es. maggiore/uguale a oggi) e formule di default (es. data corrente). Usata per registrare momenti significativi del processo (valorizzata tramite Set Variables = Today) e per calcoli di durata/tempi di risposta (differenza tra due date) in formule e campi calcolati del dashboard.
- **Booleano**: di default checkbox; in alternativa impostabile come **Bottone/Pulsante** nelle impostazioni di base. Il bottone può essere "con stato" (memorizza vero/falso, resta spuntato) o "senza stato" (comando puro). Al bottone si possono agganciare: "Variabili da impostare" (assegna valori ad altre variabili al click, alternativa manuale a una formula automatica), aggiunta allegati (cartella di destinazione, estensioni ammesse, dimensione massima), invio mail, visualizzazione report, esecuzione connettori.
- **Memo** (testo lungo): senza limiti pratici di lunghezza, supporta formattazione del testo, editor allargabile a piacere nella form.
- **Lista valori (Value List)**: elenco di opzioni configurabile nelle impostazioni di base; distinzione tra codice di iscrizione (interno, stabile) e descrizione/etichetta visualizzata (rinominabile senza rompere i dati salvati); genera una tendina invece di un campo libero. Solitamente definita "su misura" del processo perché deve coincidere con le condizioni scritte nelle formule collegate — se la lista cambia senza aggiornare le formule, queste smettono di funzionare. Alternativa più semplice/rigida della tabella locale quando bastano poche opzioni fisse.
- **User type** (utente): consente di scegliere tra utenti e gruppi dell'anagrafica BPM; limitabile a un gruppo specifico nelle impostazioni di base. Valorizzabile con formula di default "Utente corrente" (`UserName()`). Usata per assegnazione/instradamento dinamico dell'esecutore di un'attività (in alternativa a gruppo fisso o assegnazione manuale), anche tramite Set Variables o Decision Table in base ad altre variabili; può contenere sia un utente singolo sia un gruppo.
- **Label** (etichetta): variabile di sola visualizzazione, non un vero campo del database. Proprietà principale "Testo": editor in cui si scrive testo libero, si inseriscono riferimenti ad altre variabili (tasto destro > Variabili, ricerca per pagina/nome) e si incollano immagini/loghi. Usata per riepiloghi/intestazioni leggibili o per un logo aziendale.

### 2.2 Strutture complesse

- **Gruppo** (struttura testata/dettaglio, relazione 1-a-molti): si crea assegnando una variabile a un gruppo tramite i tre puntini nelle proprietà; una variabile appartiene a un solo gruppo; livello unico (nessun sottolivello/gruppo annidato). Visualizzato come griglia (tabella virtuale) con aggiunta/cancellazione righe.
  - Variabili da richiedere legate a un gruppo: obbligatorietà per colonna, disattivazione aggiunta/eliminazione riga per attività, filtro sulle righe visibili per attività (es. solo "tipo A" in un'attività, solo "tipo B" in un'altra), sola lettura per campo/attività.
  - Una variabile del gruppo può avere proprie "Variabili da richiedere" che aprono una form di dettaglio per singola riga (utile per campi larghi, es. note).
  - Può essere collegato a un **Sottoprocesso ricorrente** per generare n istanze, una per riga.
  - Può fare da "tabella di origine locale" per un altro campo (pescare la scelta dalle righe del gruppo invece che da una tabella esterna).
  - **Count** disponibile su qualunque variabile del gruppo (calcolato sempre sull'intero gruppo, non distingue sottotipi/filtri).
  - Accesso programmatico alle righe tramite ciclo (loop) sulla collection/"elenco indici" del gruppo e accesso all'i-esimo valore di una variabile.
  - Esportazione/importazione di pagine di variabili (categoria) per copiare rapidamente la struttura da un task all'altro.
- **Griglia dati (Data Grid)**: variabile di processo di tipo particolare (creata come una variabile qualunque, specificata come "data grid"); non corrisponde a un vero campo del database.
  - Due usi tipici: **(a)** vista in sola lettura su tabella locale/esterna, con aggancio analogo ai campi a tendina, selezione delle colonne da mostrare (non mappatura di variabili di destinazione) e descrizione di colonna personalizzabile; **(b)** vista filtrata su un gruppo (testata-dettaglio) già presente nel magazzino.
  - Risultato non modificabile ma filtrabile e raggruppabile (funzionalità standard di griglia) a runtime.
  - Va inserita nel magazzino e nelle variabili da richiedere, con dimensionamento dello spazio.
  - Se collegata a un gruppo: nelle variabili da richiedere si possono disattivare per singola attività l'aggiunta e l'eliminazione di righe, e filtrare le righe visibili (es. solo "tipo B").
  - Campi della griglia impostabili in sola lettura a livello di singola attività.

### 2.3 Caratteristiche trasversali ("variabili da richiedere") e altre proprietà notevoli

Ogni variabile, quando inserita nelle "variabili da richiedere" di un'attività o di uno Start, può ricevere personalizzazioni **locali a quell'attività**, indipendenti da come la variabile è definita nel magazzino:

- obbligatorietà per attività;
- sola lettura per attività;
- formula di validazione sul singolo campo;
- formula di validazione globale della form (valutata al completamento dell'attività — "Completato" — diversa da quella di singolo campo, tipicamente usata per vincoli che coinvolgono un gruppo/griglia, es. "almeno una riga presente");
- valore di default configurabile per attività/start;
- filtro impostabile per attività (in particolare su gruppi/griglie dati);
- disattivazione aggiungi/elimina riga per attività (su gruppi/griglie).

Altri tipi/usi di variabile notevoli, non riconducibili a un "tipo" a sé ma a un pattern d'uso:

- **Variabile "senza salvataggio"**: flag che impedisce la memorizzazione reale del valore nel database del processo; tipico per campi calcolati via formula che servono solo a video, non da conservare.
- **Variabile "di intestazione"**: flag con numero progressivo che ne stabilisce l'ordine; le variabili di intestazione emergono più facilmente nell'applicativo (es. in To Do List) oltre che nel singolo processo.
- **Campo collegato ad allegato** (colonna custom della griglia allegati): campo aggiuntivo associabile alla griglia allegati, agganciabile al valore di una variabile di processo per classificare/etichettare l'allegato. Attributi standard dell'allegato: Revisione, Stato (Attivo/Obsoleto, gestione manuale).
- **Campo stringa di appoggio** (variabile "scaffolding" tecnica): usata per semplificare una formula complessa (es. "presenza tipo A" sì/no), valorizzata da una formula che scorre le righe di un gruppo; utile anche per debug manuale (il BPM non ha un ambiente di debug integrato); resta sempre aggiornata automaticamente grazie alla formula collegata.
- **External ID**: variabile usata per convenzione come unico parametro passato da una stored procedure/trigger esterno all'avvio del processo (contiene l'ID del documento/ordine esterno); usata subito dopo lo start (con Get Data o SQL) per recuperare le altre informazioni accessorie dal sistema esterno, così da non appesantire il trigger con troppi parametri ("trigger super semplice, poi tutto il recupero dati lo fa BPM").

---

## 3. Formule

Le formule in BPM sono scritte in VBScript (o come espressione singola equivalente) e compaiono in diversi punti del prodotto: formule di validazione, formule di default, campi calcolati, condizioni di abilitazione su link/gateway, operazioni Set Variables, Decision Table, query SQL libere, formule di pianificazione, mapping dei connettori. Di seguito gli esempi concreti citati nei due corsi, raggruppati per contesto d'uso.

### 3.1 Formule di validazione (campo)

- `data_richiesta >= Today()` — impedisce di inserire una data antecedente a oggi.
- `If data_richiesta < Today() Then Return False` — stessa validazione, forma estesa in Visual Basic.
- `If data_richiesta < AddDays(Today(), -2) Then Return False` — la data non può essere antecedente a "oggi meno due giorni" (uso della funzione `AddDays`).
- `Error = "Data è antecedente a due giorni fa"` — possibilità di restituire un messaggio d'errore personalizzato insieme al blocco del campo.
- Formula per **readonly condizionale**: rende una variabile in sola lettura solo in certi casi/condizioni (utilizzo più avanzato, tipicamente sulle variabili da richiedere di un task).
- La **Decision Table** (§1.7) è utilizzabile come alternativa dichiarativa alla formula di validazione: propone automaticamente l'output atteso vero/falso.

### 3.2 Formula di validazione globale della form

- `If Count(TipoPreventivo) = 0 Then (Error = "Necessario almeno un preventivo per proseguire"; Return False) Else Return True` — valutata quando l'utente preme "Completato" su un'attività (non sul singolo campo), per obbligare la presenza di almeno un elemento in un gruppo prima di proseguire. Il `Return True` finale viene aggiunto d'ufficio dal sistema se omesso.

### 3.3 Formule di default

- `Richiedente = Utente corrente (UserName())` — sullo Start, valorizza automaticamente il campo con l'utente che apre la schermata (resta modificabile).
- `Data richiesta = Data corrente` — sullo Start, valorizza automaticamente il campo con la data odierna.
- Snippet/funzioni richiamabili da tasto destro nell'editor formule (aiuti contestuali al tipo di campo): anno corrente, data corrente, utente corrente, ecc.

### 3.4 Campi calcolati ("a cascata", stile Excel)

- `Year(data_richiesta)` — calcola l'anno dalla data richiesta; formula generale nel magazzino, si ricalcola automaticamente quando cambia la variabile da cui dipende.
- `Totale costi = importo_richiesta + costi_accessori` — formula semplice su una riga.
- `If conteggia_costi_accessori Then Return importo_richiesta + costi_accessori Else Return importo_richiesta` — formula multi-riga con condizione su una variabile booleana (richiede `Return` esplicito quando la formula è su più righe).
- `campo calcolato "Tempo di Risposta" = differenza tra Data Risposta e Data Apertura` — usato sia come campo di processo sia come campo calcolato nel Dashboard, base per un'aggregazione di tipo media.
- `If Difficolta = valore Then Return N (giorni) ...` (es. A/B/C mappati rispettivamente a 5, 7, 10, 12 giorni) — formula collegata alla variabile numerica "durata prevista" di un task, per rendere la pianificazione dinamica invece che a durata fissa.

### 3.5 Impostazione manuale al click ("Variabili da impostare" su un bottone)

- `Imposta Totale costi = importo_richiesta + costi_accessori` — a differenza della formula generale (calcolo automatico), qui il calcolo avviene solo quando l'utente preme il pulsante (es. "Ricalcola totali").

### 3.6 Condizioni di abilitazione (link e gateway)

- `esito_approvazione_CDG = "Approvata"` / `esito_approvazione_CDG = "Non approvata"` — condizioni sui due link in uscita da un task di approvazione, scritte in modo da controbilanciarsi a vicenda.
- Stessa logica riproposta come configurazione di un **Gateway esclusivo**: un'uscita con condizione esplicita, l'altra marcata come "else"/default.
- `Presenza Tipo A = sì` / `Presenza Tipo B = sì` — condizione basata su una variabile di appoggio calcolata (vedi §3.7), per far partire un'attività parallela solo se esiste almeno una riga del tipo corrispondente in un gruppo.
- Prima ipotesi **scartata** perché imprecisa: `If Count(VariabileGruppo) > 0 Then Return True` — il Count su una variabile di un gruppo viene comunque calcolato sull'intero gruppo, non distingue i sottotipi; da qui la necessità della formula a ciclo di §3.7.
- Formula personalizzata di apertura di una sbarra di sincronizzazione, alternativa alla condizione standard "tutte pianificate" (testo non mostrato nel transcript, ma il meccanismo è lo stesso: una formula VBScript che restituisce vero/falso).

### 3.7 Formule con ciclo su un gruppo

- ```vb
  Dim i As Integer
  For i = 0 To Count(ListaPreventivi) - 1
      If TipoPreventivo(i) = "TipoA" Then Return True
  Next
  ' se il ciclo finisce senza trovare nulla, il risultato resta/diventa False
  ```
  
  Formula (su una variabile di appoggio tipo "presenza tipo A", sì/no) che scorre le righe di un gruppo per determinare se esiste almeno una riga di un certo tipo; ricalcolata automaticamente ogni volta che cambia il gruppo. `Return` esce immediatamente dalla formula (comportamento diverso da un ciclo Delphi). Versione analoga creata per "presenza tipo B".

### 3.8 Set Variables (script di impostazione/pulizia)

- Impostazione di `Esito Approvazione CDG` a blank — agganciata al task su "esecuzione terminata", per ripulire un campo obbligatorio quando il processo torna indietro ed evitare loop nel flusso.
- `If ImportoRichiesta < 1000 Then UtenteApprovazioneTecnica = DirTec Else UtenteApprovazioneTecnica = DirGen` — instradamento dinamico dell'esecutore di un'attività di approvazione in base all'importo.
- Impostazione di `Data Presa a Visione = Today` — agganciata al task "presa in carico" (esecuzione terminata), per registrare automaticamente il momento ai fini del calcolo dei tempi di risposta.
- Impostazione di `Data Risposta = Today` — agganciata al task "chiusura reclamo" (esecuzione terminata), stesso pattern.
- `If TipoRichiesta_origine = "RichiestaSicurezza" Then Note_destinazione = "Attenzione richiesta sicurezza"` — formula nell'operazione "Creazione nuovo processo collegato", per impostare variabili sul processo figlio in base a variabili del padre (logica distinta tra "variabili di origine" e "variabili di destinazione").

### 3.9 Decision Table (equivalente dichiarativo)

- Tabella equivalente alla formula Set Variables di §3.8: `(Importo < 1000, Tipo Richiesta = normale) → DirTec` · `(Importo >= 1000, Tipo Richiesta = normale) → DirGen` · `(qualsiasi importo, Tipo Richiesta = sicurezza) → Sicurezza`. L'ordine delle regole è significativo.

### 3.10 SQL libero

- `UPDATE tabella SET valore = 1 WHERE campo_numeric = @n` — esempio illustrativo, con `@n` mappato a una variabile del processo tra i parametri del comando; usato per aggiornare un sistema esterno (es. segnalare un ordine come firmato).
- `SELECT ... FROM tabella WHERE campo_numeric = @n` con parametro di output `@p` mappato alla variabile "importo richiesta" — uso in lettura, per valorizzare una variabile con un dato letto da un sistema esterno.

### 3.11 Identificazione del processo target ("Aggiorna un altro processo")

- Regola di ricerca: **per nome** (processo il cui nome è uguale al valore di una variabile, es. "numero richiesta"), **per uguaglianza di variabile** (es. numero richiesta del processo corrente = numero richiesta del processo target), oppure **per Instance ID** (codice interno univoco del processo).

### 3.12 Formule per nome/descrizione del processo

- `variabili.numero_richiesta & "/" & variabili.anno` — formula per il "Nome processo" (proprietà generali, selezionando l'area bianca del designer): definisce la chiave/etichetta con cui è identificata ogni istanza.
- `"Richiesta numero " & variabili.numero & " stabilimento: " & variabili.codice_stabilimento` — formula per la "Descrizione del processo", usata come intestazione descrittiva della pratica.

### 3.13 Formule per percorsi allegati su file system

- `\\server\allegati\[stabilimento]\[numero_richiesta]` — percorso di una root allegati su file system, composto dinamicamente concatenando variabili di processo.
- `\\[srvfs01]\allegati\...` — variante che usa una **variabile d'ambiente** (es. `srvfs01`, contenente il nome del server) al posto del nome server hardcoded: buona pratica suggerita per evitare di "hard-codare" il server nel percorso.

### 3.14 Formule e mapping per i connettori (SAM)

- `csx:testovi` con attributo cliente = valore della variabile "codice cliente" (mappatura tipo `csx:testovi.punto.code_cliente`) — mapping tra parametri XML del connettore attivo (template "XML commessa") e variabili di processo, per generare l'XML passato al web import di SAM.
- `csx:riga.ov.codarticolo = CodiceArticolo`, `qta1 = QtaArticolo` — parametri di dettaglio del connettore attivo, mappatura riga per riga tra le righe di un gruppo/griglia del processo e le righe di dettaglio del documento creato su SAM.
- Chiamata web service REST-like `POST` verso l'endpoint `create-new-process`, con body JSON contenente token di autenticazione, utente, nome del modello di processo, start da utilizzare, elenco delle variabili da valorizzare — avvio di un nuovo processo BPM da un sistema esterno (dimostrato con Postman); risponde con esito (vero/falso), messaggio, nome/numero del processo creato.
- Chiamata a **stored procedure** con parametro unico "external ID" (es. utente=2, modello="richieste inv", start=1, external_id=1), che scrive su una tabella di confine ("chiamate API") letta poi in modo asincrono da un motore interno che esegue la vera chiamata web service `create-new-process` — pattern di avvio asincrono da un trigger SQL quando non è comodo chiamare direttamente il web service in modo sincrono.

### 3.15 Funzioni e riferimenti VBScript ricorrenti (cheat-sheet)

- `Today()` — data odierna.
- `AddDays(data, n)` — somma/sottrae n giorni a una data.
- `Year(data)` — estrae l'anno da una data.
- `UserName()` — utente corrente.
- `Count(variabile_di_gruppo)` — numero di righe di un gruppo (calcolato sempre sull'intero gruppo, non su un sottoinsieme filtrato).
- `Return` — esce immediatamente dalla formula con il valore indicato (comportamento diverso da un semplice assegnamento a fine ciclo).
- `variabili.nome_variabile` — sintassi di riferimento a una variabile di processo nelle formule di nome/descrizione del processo.
