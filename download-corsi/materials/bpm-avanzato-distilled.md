# BPM Avanzato

## Introduzione

Il corso BPM Avanzato prosegue il percorso formativo iniziato con il corso BPM Base e approfondisce le funzionalità del Designer BPM (Digit Company) destinate a chi deve modellare processi complessi, integrare BPM con sistemi esterni e presidiare l'avanzamento operativo dei processi nel tempo. I macro-argomenti trattati sono: variabili avanzate (griglie dati, filtri su gruppi, formule VB-script e validazione), gateway e sincronizzazione dei rami paralleli, oggetti puramente grafici e swim lane, start multipli ed eventi (attesa, timeout/escalation), operazioni automatiche (mail, processo collegato, set variable, decision table, SQL, get data), tabelle locali personalizzate (tabelle P_), report e dashboard, integrazione con il gestionale esterno SAM (in entrambe le direzioni) e infine pianificazione/Gantt dei processi.

---

## Concetti

### Variabili avanzate: data grid e filtri su gruppo

#### Griglia dati (data grid)

La griglia dati è un tipo di variabile di processo a sé stante, distinto sia dal campo semplice sia dal gruppo (testata/dettaglio). È un oggetto singolo che visualizza una griglia **in sola lettura**, agganciata a una tabella — locale o esterna.

Si usa per mostrare all'utente dati di contesto senza uscire dal processo: tutti gli ordini di un certo cliente, le righe di un ordine in approvazione, una tabella di budget, ecc. Non è una struttura di inserimento dati (per quello ci sono i gruppi): è una finestra di consultazione dal vivo.

Configurazione:

1. Si crea una variabile e se ne imposta il tipo su Griglia Dati, come per qualunque altra variabile.
2. Si apre la sua configurazione (la stessa schermata usata per l'aggancio tabella dei campi) e si sceglie la tabella sorgente (tabella locale P_, vista, o tabella esposta da un connettore esterno).
3. Si scelgono le colonne da esporre e, opzionalmente, se ne rinominano le intestazioni (utile quando i nomi colonna della sorgente sono criptici o in lingua straniera).
4. Si posiziona nella form/magazzino/variabili da richiedere come qualunque altra variabile, dandole spazio a schermo sufficiente.
5. Dopo la pubblicazione, aprendo un'istanza di processo la griglia appare popolata, filtrabile e raggruppabile come le altre griglie del prodotto, ma non editabile.

L'aggancio di una griglia dati usa lo stesso meccanismo di mappatura dell'aggancio tabella sui campi ("aggancio del tipo di quelle che si fanno per puntare una tabella") — cambia solo la resa a video (griglia persistente anziché combo/popup di ricerca).

#### Filtro per attività su un gruppo

Un gruppo (testata/dettaglio, relazione 1-a-molti) può essere filtrato in modo **diverso per ogni attività/schermata** in cui compare, senza toccare i dati sottostanti.

Esempio reale citato dal docente: due attività parallele di revisione ("valutazione preventivi tipo A" / "tipo B") usano lo stesso gruppo "lista preventivi", ma ogni revisore deve vedere solo il proprio tipo. Un'altra applicazione concreta menzionata è un processo di controllo qualità che smistava i pezzi verso due reparti diversi in base al tipo di pezzo, con esattamente questo schema.

Configurazione, in "variabili da richiedere" (frames/003_002706_configure-a-per-task-filter-on-a-group-variable.jpg):

- Si seleziona una qualunque variabile appartenente al gruppo; le impostazioni locali permettono di disabilitare l'aggiunta/cancellazione righe (navigazione in sola lettura) e di applicare una **condizione di filtro** (es. `tipo preventivo = "tipo A"`).
- Si ripete l'operazione sull'attività parallela con il filtro opposto.

#### Condizionare un percorso in base al contenuto di un gruppo

Si può usare una formula VB-script sulla **condizione di abilitazione** di un link per impedire al processo di percorrere un ramo quando un gruppo non contiene righe corrispondenti (es. non aprire il ramo "revisione tipo A" se non ci sono preventivi di tipo A).

Esempio guidato:

- Tasto destro dentro l'editor della condizione per navigare le variabili disponibili; selezionando un membro del gruppo vengono proposte espressioni helper preconfezionate (es. `Count(tipo preventivo) > 0`), ma un semplice conteggio sull'intero gruppo non è sufficiente quando serve contare solo le righe che soddisfano una condizione specifica.
- **Suggerimento — in BPM non esiste un debugger.** Non essendoci modo di eseguire passo-passo una formula, il docente consiglia di creare variabili helper "usa e getta" nel magazzino (es. `presenza tipo A`, `presenza tipo B`, di tipo stringa) solo per visualizzare cosa calcola una formula mentre la si scrive (frames/004_003043_helper-variable-workaround-for-debugging-formulas.jpg).
- La logica di conteggio va scritta come formula sulla stessa variabile helper (una "formula" sul campo, che si ricalcola automaticamente a ogni variazione dei dati):

```vb
Dim i As Integer
For i = 0 To lista_preventivi.Count - 1
 If tipo_preventivo(i) = "tipo A" Then
 Return "sì"
 End If
Next
Return "no"
```

 (frames/005_003415_vb-script-loop-over-group-rows-worked-example.jpg)

- **Attenzione:** `Return` esce immediatamente dalla formula — a differenza di altri linguaggi (il docente cita Delphi come esempio), l'esecuzione non prosegue oltre un `Return`.
- La condizione di abilitazione del gateway a valle controlla poi semplicemente `presenza tipo A = "sì"`.

Pattern di accesso da ricordare: `variabile(i)` è il modo per indicare l'i-esimo valore di una variabile membro di un gruppo su tutte le righe — questo pattern ricorre costantemente nella logica basata su gruppi.

#### Formula di validazione: a livello di campo vs. globale

- **Formula di validazione a livello di campo:** è agganciata a un singolo campo; viene verificata non appena quel campo viene modificato (es. rifiutare un importo > 1000). Il tasto per attivarla in genere si chiama "formula di attivazione" o "formula di validazione".
- **Formula di validazione globale:** è una formula separata per l'intera schermata, valutata solo quando l'utente clicca "completato" sull'attività. Si usa per regole di business trasversali a più campi, ad esempio "deve esistere almeno un preventivo di qualunque tipo prima di poter proseguire":

```vb
If Count(tipo_preventivo) = 0 Then
 MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
 Return False
End If
Return True
```

 (frames/006_003944_global-validation-formula-vs-field-level-validatio.jpg)

Nota: `Return True` in fondo è tecnicamente opzionale/implicito, ma scriverlo esplicitamente evita ambiguità.

### Gateway e sincronizzazione dei rami

#### Sbarra di sincronizzazione (oggetto storico)

È l'oggetto storico di BPM per ricongiungere rami paralleli — visivamente un "cancello" che si apre solo quando tutti i rami entranti configurati sono arrivati (frames/007_004344_legacy-sync-bar-object-sbarra-di-sincronizzazione.jpg).

Modalità di configurazione:

- **TUTTE:** attende ogni ramo che è stato *configurato* come entrante, indipendentemente dal fatto che sia stato effettivamente avviato in quella istanza.
- **TUTTE PIANIFICATE** (tutte lanciate): attende solo i rami effettivamente avviati in quell'istanza — fondamentale quando il gateway di diramazione a monte è condizionale (es. un gateway inclusivo che potrebbe aprire solo uno dei due percorsi). Usare "TUTTE" in quel caso porterebbe il processo in stallo (deadlock) (frames/008_004534_all-vs-all-planned-gotcha-on-sync-bars.jpg).
- La sbarra di sincronizzazione può inoltre portare una **formula di attivazione personalizzata** al posto di TUTTE/TUTTE PIANIFICATE, per i casi che richiedono una logica arbitraria: esempio reale citato, progetto "Veneta Cucine".

#### Gateway in stile BPMN moderno

Lo stesso oggetto a forma di rombo assume tre significati diversi a seconda della configurazione (frames/009_004700_three-modern-gateway-types-exclusive-parallel-incl.jpg):

- **Percorsi alternativi (esclusivo):** viene percorso esattamente un ramo in uscita; gli esiti sono mutuamente esclusivi.
- **Percorsi paralleli (parallelo/AND):** tutti i rami in uscita vengono sempre percorsi, senza condizioni.
- **Percorsi liberi (inclusivo/OR):** uno, alcuni o tutti i rami in uscita possono essere percorsi, in base alla condizione di ciascuno.

Configurazione: doppio clic (oppure tasto destro → Configurazione) per impostare una condizione su ciascun ramo in uscita. È possibile usare direttamente variabili booleane come condizione, oltre a espressioni più articolate.

Vincolo: un oggetto gateway è **o** una diramazione (1 ingresso → n uscite) **o** un ricongiungimento (n ingressi → 1 uscita) — il designer blocca (disegna in rosso il collegamento) qualunque tentativo di dargli entrambe le funzioni contemporaneamente. La stessa forma diventa automaticamente un "ricongiungimento" quando vi si collegano più link entranti verso un'unica uscita; usato come ricongiungimento non richiede alcuna configurazione (attende semplicemente il completamento dei rami che sono stati effettivamente avviati).

Richiamo — percorso di default ("diamantino"): il rombo nero indica il percorso predefinito/di fallback preso quando nessuna condizione esplicita risulta vera, in modo che il processo non resti mai bloccato.

### Oggetti grafici, pagine multiple e swim lane

#### Oggetti puramente grafici

- **Casella di testo:** testo libero personalizzabile (font, colore, bordo trasparente), es. un titolo del processo — puramente estetico (frames/010_005239_purely-graphical-objects-text-box-image-page-setup.jpg).
- **Immagine:** es. il logo aziendale.
- **Pagina e margini:** Configurazione → Strumenti → pagina permette di impostare formato carta (A0–A4) e margini; la maggior parte dei processi viene disegnata su una pagina sovradimensionata ignorando i margini, ma se si vuole un diagramma di processo **stampabile** (es. come documentazione, esportabile in PDF con "stampa su PDF"), lo si impagina per rientrare in pagine reali.
- **Memo/post-it:** una nota libera agganciata vicino a un'attività per annotazioni in fase di progettazione; nessun effetto a runtime.

#### Processi multi-pagina e oggetto Marker

Per processi molto lunghi/complessi, il canvas può essere suddiviso in più pagine (Nuova Pagina). L'oggetto **Marker** funge da "goto"/teletrasporto tra pagine: si posiziona un marker numerato nel punto in cui il flusso lascia la pagina 1 e un marker corrispondente nel punto in cui rientra sulla pagina 2. Non c'è limite al numero di marker/pagine. Utile soprattutto quando il diagramma deve restare leggibile/stampabile come documentazione.

#### Swim lane

Corsie adiacenti e ordinate (come i "pool/lane" BPMN) usate per organizzare visivamente un processo per ruolo/reparto. Trascinando l'oggetto swim lane si crea un insieme di corsie contigue, rinominabili (es. "Inseritore," "Sicurezza," "Controllo di Gestione," "Dirtec").

Comportamento funzionale, non solo cosmetico: impostare gli **"utenti responsabili"** a livello di corsia (tasto destro) assegna automaticamente quell'utente/gruppo a qualunque attività posizionata nella corsia che non abbia già un'assegnazione esplicita propria; un'assegnazione esplicita a livello di attività prevale sempre su quella di corsia.

Configurazione:

- Colore dell'intestazione della corsia, ordine (sposta corsie su/giù).
- Orientamento: verticale (dall'alto in basso, la convenzione preferita dal docente) oppure orizzontale (la convenzione BPMN standard, usata quando i diagrammi devono avere un aspetto "da manuale").

Esempio di progetto reale: un processo multi-reparto (commerciale → tecnico → acquisti → qualità → produzione) impaginato con swim lane — molto leggibile su "chi fa cosa" a colpo d'occhio, ma il docente segnala che questo stile di diagramma è visivamente più disordinato ("a zig-zag") da disegnare e mantenere rispetto a un flusso lineare dall'alto in basso (frames/014_010728_real-project-zig-zag-swim-lane-process.jpg).

#### Oggetto Gruppo (attività)

Un'alternativa alle swim lane per raggruppare/etichettare: supporta anch'esso l'assegnazione di "utenti responsabili" a tutto ciò che contiene, oppure può essere usato puramente come etichetta visiva/riquadro attorno a una sezione del diagramma (es. "ufficio tecnico").

#### Undo vs. storico versioni

- L'**Undo** (~10 passi) è transitorio: copre solo la sessione di editing corrente, dall'apertura alla chiusura del designer.
- Lo storico di **pubblicazione/versioni** è permanente, salvato a database: ogni volta che si "Pubblica," BPM crea una nuova riga di versione numerata. Si può tornare a qualunque versione pubblicata precedente.
- Suggerimento: in fase di pubblicazione, BPM propone un campo libero **"Versione" / note di pubblicazione** dove annotare cosa è cambiato (es. "R01 dev — modificata attività 2"); utile come changelog informale, anche se il contatore di versione sottostante si incrementa comunque.
- Esiste anche uno strumento di pulizia dello storico (per installazioni grandi/datate) per eliminare vecchie versioni, con un controllo di sicurezza che impedisce di cancellare una versione su cui sono ancora attive istanze in esecuzione.

### Start multipli ed eventi

#### Start multipli

Un processo può avere due o più oggetti Start distinti, ciascuno configurato in modo indipendente (proprie variabili richieste, valori di default, regole di validazione, permessi).

Esempio: "Inserimento richiesta normale" vs. "Inserimento richiesta sicurezza" — lo start sicurezza precompila/snellisce i campi in modo diverso (es. salta un passaggio di revisione, aggiunge un campo note dedicato) (frames/016_011600_building-two-start-events-normal-vs-security.jpg).

All'avvio di un processo con start multipli:

- Comportamento di default: all'utente viene chiesto quale punto di partenza usare.
- **Restrizione per permesso:** si impostano gli "utenti responsabili" su ciascuno Start individualmente, così che solo il gruppo giusto possa usare quel punto di ingresso.
- **Associazione tramite menu personalizzato:** una voce di menu personalizzato ("menu personalizzati") può essere precablata su uno start specifico, dando a ogni punto di ingresso la propria voce di menu dedicata invece di una richiesta generica.
- **Via API/web service:** la chiamata `create-new-process` richiede un parametro esplicito di punto di partenza; ometterlo quando esistono start multipli restituisce un errore invece di sceglierne uno silenziosamente.

#### Start a tempo (avvio schedulato)

Avvia un processo automaticamente secondo una pianificazione, invece che tramite un'azione utente (es. "ogni primo lunedì del mese alle 08:00"). Adatto a processi periodici/amministrativi (chiusure di fine periodo, controlli ricorrenti). Poiché non porta con sé variabili, la prima attività reale del processo deve comunque raccogliere i dati di lavoro effettivi.

#### Evento Attesa (Wait)

Sospende il processo per una durata configurata (es. "attendi 5 giorni", oppure il pattern "il primo lunedì") e poi prosegue automaticamente — durante l'attesa **non esiste alcuna voce in to-do list** (a differenza della semplice pianificazione di un'attività fra 10 giorni, che invece resterebbe comunque nella to-do list di qualcuno per tutto il tempo) (frames/018_012344_attesa-wait-event.jpg).

Esempio reale: il processo interno di "welcome kit" (inserimento di un nuovo dipendente) usa l'evento attesa in più punti per scaglionare i passaggi di un certo numero di giorni.

#### Fine vs. Termina Processo

- **Fine:** un semplice marcatore grafico di chiusura di un ramo — segnala visivamente "questo ramo del diagramma finisce qui", nessun effetto a runtime oltre a questo.
- **Termina Processo:** **uccide** effettivamente l'intera istanza di processo — qualunque attività parallela ancora aperta altrove nel processo viene chiusa forzatamente. Tipicamente usato su rami di eccezione/errore quando si decide che l'intera istanza vada interrotta (frames/019_012600_fine-vs-termina-processo-distinction.jpg).

#### Eventi boundary: timeout ed escalation

Un evento agganciato al **bordo di un'attività** (non alla linea di flusso principale) — attiva un percorso alternativo dopo N giorni dalla data di attivazione dell'attività o da una scadenza, es. per attivare un promemoria o un passaggio di mano a un altro utente. Funzionalmente "timeout" ed "escalation" sono lo **stesso** meccanismo; le due icone differiscono solo per convenzione semantica (timeout = "questa attività sta impiegando troppo tempo, sollecita"; escalation = "passa di mano/alza il livello"). Corrisponde al concetto BPMN di "evento di confine" ("boundary event") — l'evento esiste perché l'attività è attiva, non perché il flusso principale l'ha raggiunto (frames/020_012810_timeout-escalation-boundary-event.jpg).

### Operazioni automatiche

Concetto chiave: a differenza delle attività utente (rettangoli, che richiedono un intervento umano) e degli eventi (punti che semplicemente accadono), le **operazioni** sono cose che il motore BPM fa da sé, automaticamente. Possono essere trascinate direttamente nel flusso di processo come qualunque altro oggetto, oppure agganciate a un momento specifico del ciclo di vita di un'attività, oppure agganciate a livello dell'intero processo (frames/021_013034_operations-automatic-system-activities.jpg).

#### Operazione Invio Mail

- Si trascina l'operazione mail nel flusso, poi la si configura selezionando (o creando) un **template di mail**.
- I template di mail sono oggetti che vivono dentro il processo (da Configurazione, oppure direttamente dall'operazione) e sono riutilizzabili su più punti di invio (frames/022_013406_building-an-email-notification-template.jpg).
- Costruzione del template: oggetto e corpo supportano l'inserimento di variabili di processo tramite tasto destro (il menu "generic" espone anche placeholder speciali — vedi sotto).
- **Destinatari:** possono essere un utente BPM fisso, un gruppo fisso, una variabile che contiene un indirizzo email grezzo (es. il campo email di un fornitore), oppure una variabile che contiene un riferimento a utente/gruppo BPM. I destinatari possono anche essere messi in copia conoscenza ("in propria conoscenza").
- **Allegati:** si possono allegare documenti di processo e/o report generati.
- **Placeholder generici utili nei template:**
 - `mia mail` (my own email) — l'email di chi è attualmente assegnatario dell'*attività* (permette di riusare lo stesso template su tante attività/assegnatari diversi).
 - `mia attività` (my activity) — il nome visualizzato dell'attività corrente.
 - **`link web al task`** — inserisce un URL cliccabile che porta direttamente alla schermata di esecuzione di quella specifica attività nel client web (bypassando del tutto la to-do list). Funziona anche per collegarsi all'intero processo o alla sua pagina allegati (frames/024_014614_link-web-al-task-generic-field.jpg).
- **Insidia comune:** il link diretto funziona solo se **Configurazione → parametri → "URL base link email"** è impostato sul vero hostname visibile esternamente del server; se lasciato a `localhost` (il default facile da dimenticare), ogni link nelle mail si rompe silenziosamente — particolarmente importante quando il server è esposto su un IP pubblico.
- In genere si consiglia di abilitare sempre il modulo web (non serve licenza aggiuntiva, solo un'attività di setup IIS per i sistemisti), perché è necessario affinché questi link diretti funzionino fuori dal client desktop.

#### Operazioni agganciate al ciclo di vita di un'attività

Tasto destro su un'attività → **Operazioni** permette di agganciare qualunque operazione (stesso catalogo delle operazioni di flusso) a uno di quattro momenti:

- **Attivazione:** l'attività è appena diventata disponibile (compare nella to-do list di qualcuno — buon momento per una notifica "hai qualcosa da fare").
- **Inizio:** l'utente ha dichiarato esplicitamente di aver *iniziato* l'attività (scatta solo se "rileva inizio" è abilitato su quell'attività — vedi la sezione sulla pianificazione).
- **Esecuzione:** scatta appena prima che l'attività venga segnata come effettivamente completata (cioè "sta per completarsi").
- **Esecuzione terminata:** scatta subito dopo il completamento, appena prima che l'attività successiva si attivi.

Attivazione vs. Inizio, con precisione: attivazione = l'attività è *pronta*; inizio = l'attività è stata effettivamente *iniziata*. Sono deliberatamente due concetti separati, usati insieme al sistema di pianificazione.

Suggerimento pratico: posizionare operazioni puramente tecniche/di servizio (es. azzerare una variabile obsoleta) direttamente sull'attività, invece che come oggetto visibile nel flusso, mantiene il diagramma di processo focalizzato sulla logica di business invece di affollarlo di passaggi tecnici di "idraulica" interna.

#### Set Variable / operazione formula inline ("un pezzo di scritto")

Un'operazione leggera che esegue un breve script per impostare una o più variabili — distinta da una formula di validazione (che restituisce solo vero/falso) (frames/029_021020_set-variable-formula-operation-inserire-un-pezzo-d.jpg).

Esempio guidato — azzerare un esito obsoleto in caso di rilavorazione: se un campo "esito approvazione" è impostato a "non approvato" e l'attività viene rimandata indietro al richiedente per revisione e poi torna all'approvatore, il campo mantiene silenziosamente il vecchio valore "non approvato" (fonte comune di confusione: molti si aspettano che torni vuoto). Un'operazione Set Variable agganciata a **Esecuzione Terminata** dell'attività azzera di nuovo il campo, costringendo l'utente a ridecidere consapevolmente, ed evita che il ciclo si ripeta all'infinito perché il controllo "campo obbligatorio" era già banalmente soddisfatto dal valore obsoleto (frames/030_021119_clearing-a-stale-variable-on-a-rework-loop.jpg):

```vb
' agganciata sull'attività "controllo di gestione", su esecuzione terminata
esito_approvazione = Blank
```

Esempio guidato — assegnazione automatica dell'approvatore in base all'importo (frames/031_021517_auto-assign-an-approver-by-amount-threshold.jpg):

```vb
If importo_richiesta < 1000 Then
 utente_approvazione_tecnica = "Dir Tech" ' può essere anche un gruppo
Else
 utente_approvazione_tecnica = "Dir Gen"
End If
```

Gli "utenti responsabili" dell'attività vengono poi associati alla variabile `utente_approvazione_tecnica` (variabile di tipo Utente) invece che a un gruppo fisso — una terza modalità di assegnazione, oltre a "assegna a gruppo" e "scegli manualmente una persona": l'**assegnazione guidata da regola**.

#### Decision table

Un'alternativa più recente e dichiarativa alla scrittura manuale di una formula. Si definiscono colonne di input e colonne di output e un insieme di righe-regola; BPM genera il codice VB sottostante in automatico. Disponibile ovunque sia utilizzabile una formula/formula di validazione (frames/032_021905_decision-table-object-introduced.jpg).

Esempio guidato — stessa logica di assegnazione approvatore per importo, come tabella (frames/033_022039_decision-table-demo-amount-approver.jpg):

| Importo Richiesta | → | Utente Approvazione |
|---|---|---|
| < 1000 | | Dir Tech |
| ≥ 1000 | | Dir Gen |

Estesa con una seconda colonna di input (Tipo Richiesta) per regole più complesse:

| Importo Richiesta | Tipo Richiesta | → | Utente Approvazione |
|---|---|---|---|
| < 1000 | Normale | | Dir Tech |
| ≥ 1000 | Normale | | Dir Gen |
| (qualunque) | Sicurezza | | Sicurezza |

- L'ordine delle righe conta e può essere modificato con le frecce su/giù (vince la prima riga che soddisfa le condizioni).
- Lo strumento è consapevole del tipo di variabile: per un campo a lista di valori propone i valori noti; per un campo di tipo Utente propone l'elenco di utenti/gruppi; in un contesto di formula di validazione sa già che l'output deve essere vero/falso.
- **Limite:** la decision table esprime solo condizioni semplici di confronto tra campi — non può esprimere logica procedurale come "scorri un gruppo e conta le righe corrispondenti" (vedi l'esempio della condizione di abilitazione sopra). Per quello serve ancora una formula.
- **Conversione bidirezionale:** un campo formula può essere convertito in decision table (come punto di partenza, se ci si blocca davanti a una formula vuota) e una tabella può essere riconvertita in formula quando la sua logica supera ciò che la tabella può esprimere. Il docente paragona questo utilizzo a partire da codice generato con ChatGPT: mai una risposta finita e affidabile, ma un utile sblocco iniziale (frames/034_022747_convert-between-decision-table-and-formula-code.jpg).

#### Operazione SQL ("SQL libero")

Un'operazione che esegue un'istruzione SQL arbitraria su una stringa di connessione esterna — non limitata al CRUD di una singola tabella, può eseguire stored procedure, join, qualunque cosa consenta l'SQL (frames/035_022908_sql-operation-object-introduced.jpg).

Esempio guidato (frames/036_023018_sql-update-query-demo-with-in-out-parameters.jpg):

```sql
UPDATE fornitori SET valore = 1 WHERE ID_numeric = @n
```

con `@n` legato come parametro di input a una variabile di processo; separatamente, una `SELECT` con un parametro di output (`@p`) scrive un valore restituito in una variabile di processo (es. `importo_richiesta`).

Caso d'uso: scrivere in un ERP esterno che un documento è stato firmato/approvato da un certo utente in un certo passaggio (es. "UPDATE ordine SET firmato_da =... WHERE ordine_id =..."), usato come alternativa più leggera al connettore dedicato quando non esiste un'interfaccia di connettore preconfezionata per quella scrittura.

Configurazione: la stringa di connessione si imposta una volta sola sotto **Configurazione → Connessione Esterna** (supporta target SQL Server/tipo ODBC), e viene riusata sia dall'operazione SQL sia da qualunque aggancio tabella sui campi.

#### Aggiorna un altro processo

Permette di scrivere aggiornamenti di variabili su un'istanza di un *altro* processo in esecuzione, in qualunque punto del flusso — non solo al lancio (processo collegato) o al ritorno. Non richiede nemmeno che i due processi siano stati formalmente collegati. Si fornisce una regola di ricerca per trovare l'istanza target: per codice istanza interno BPM, oppure facendo corrispondere il valore di una variabile (es. "trova il processo il cui `numero_richiesta` = il mio"). Si mappano poi variabile sorgente → variabile destinazione, si impostano valori fissi, oppure si usa una formula di passaggio, come nella mappatura del processo collegato. **Attenzione:** se ci si accorge di dover ricorrere a questa operazione troppo spesso, è di solito il segnale di una duplicazione eccessiva di dati fra processi che andrebbe ripensata architetturalmente.

#### Operazioni a livello di processo

Le operazioni possono essere agganciate non solo a una singola attività ma all'**intero processo** — vengono quindi eseguite automaticamente ogni volta che *qualunque* passaggio avanza, senza doverle cablare su ogni singola attività. Uso comune: aggiornare sempre lo stato su un CRM/ERP esterno, oppure sincronizzare sempre i nuovi allegati verso un repository documentale esterno ("documentale Globe"), a ogni avanzamento, senza chiedere conferma all'utente.

#### Operazione Get Data

Un'alternativa strutturata e guidata a una query SQL grezza, per ricerche in sola lettura: si sceglie una tabella/vista sorgente, si fornisce il valore chiave, e si mappano le colonne restituite direttamente su variabili di processo — lo stesso identico meccanismo/interfaccia usato per l'aggancio tabella su un campo, ma invocato come operazione autonoma (frames/039_024119_get-data-operation-introduced.jpg).

Esempio guidato: dato un codice fornitore, si consulta la tabella fornitori e si precompila automaticamente la ragione sociale in una variabile `ragione_sociale` — comunemente usato proprio all'**inizio** di un processo, quando l'utente inserisce solo un codice e il resto dei campi anagrafici deve autopopolarsi.

Get Data vs. query SQL grezza: Get Data è più guidato (conosce i tipi di colonne/tabelle, meno soggetto a errori) ma limitato a una semplice ricerca puntuale per chiave; qualunque cosa richieda join, GROUP BY, più righe restituite o logica arbitraria richiede l'operazione SQL.

### Tabelle locali personalizzate (tabelle P_)

Oltre alle viste e liste di valori predefinite, BPM permette di definire tabelle di lookup completamente personalizzate direttamente nel designer. Salvandone una si genera automaticamente una vera tabella SQL con prefisso `P_` (es. `P_area_geografiche`) (frames/040_024602_custom-local-tables-tabelle-p-introduced.jpg).

Quando usarle:

- Una lista di valori non basta (servono più colonne, non solo codice+descrizione).
- I dati devono essere mantenuti da qualcuno diverso dal progettista del processo, o indipendentemente dal ciclo di pubblicazione di uno specifico processo.
- Serve filtro/ricerca su un elenco troppo lungo per una comoda dropdown.

Caso d'uso reale: usate frequentemente per tabelle di riferimento del reparto qualità (definizioni/standard non presenti nell'ERP principale).

Configurazione:

1. Configurazione → Tabelle → Nuova Tabella; le si dà un nome (gli spazi si convertono automaticamente in underscore per mantenere pulito l'identificatore SQL generato) (frames/041_024744_demo-creating-a-custom-table-aree-geografiche.jpg).
2. Si progettano le colonne con un editor molto simile a quello delle variabili di processo — ma con limiti reali: **niente gruppi/testata-dettaglio**, **niente formula di validazione**, meno funzionalità avanzate rispetto a una vera variabile di processo.
3. Salvando si crea la tabella SQL. Si popolano le righe direttamente da BPM (Tabelle → la tua tabella → Nuovo).
4. Si usa ovunque sia previsto un aggancio a "tabella locale" (aggancio campo, sorgente di una griglia dati, sorgente Get Data) — comparirà con il prefisso `P_`.
5. Se una tabella `P_...` esiste in SQL ma non è stata creata tramite il designer tabelle di BPM, BPM la elencherà comunque come sorgente di lookup, ma non se ne possono gestire i dati riga da BPM (nessun menu di inserimento valori) — utile se è popolata da un import esterno.

Permessi: le tabelle personalizzate sono soggette a permessi per utente/gruppo (visualizza/modifica), lo stesso meccanismo dei permessi di processo, configurato sotto Utenti e Gruppi.

Menu personalizzati: una tabella personalizzata può essere esposta come propria voce di menu (Configurazione → menu personalizzati → "visualizza tabella"), così l'utente finale può consultarla/mantenerla direttamente senza passare da un processo.

Guida alla scelta — lista di valori vs. tabella personalizzata:

- Usare una **lista di valori** *dentro il processo* quando logica/condizioni altrove nel processo dipendono dai suoi valori esatti — modificare la lista in seguito potrebbe altrimenti rompere silenziosamente quelle condizioni.
- Usare una **tabella personalizzata** quando le opzioni sono numerose, devono essere filtrabili/ricercabili, o chi le mantiene non deve avere il permesso di modificare il processo.

### Report e dashboard (analisi dati)

Due modalità complementari per estrarre/presentare i dati raccolti in un processo BPM, entrambe basate sulle **variabili di processo** come sorgente dati (nessuna estrazione dati separata necessaria) (frames/043_025737_reports-dashboards-two-ways-to-extract-data.jpg).

#### Report (documenti pixel-perfect)

Un designer di report di terze parti integrato (stessa famiglia di prodotto di Crystal Reports / dei generatori PDF usati in RGT e "Globe" di SAM) che permette di impaginare un documento in stile PDF e trascinare variabili di processo in segnaposto etichettati (frames/045_030227_report-designer-embedded-3rd-party-tool.jpg).

Caso di studio reale — "scheda commessa": prima di BPM, i commerciali di un'azienda compilavano a mano un modulo PDF/Word vuoto per ogni nuovo ordine/commessa, poi lo inviavano via mail in giro e inseguivano manualmente i colleghi ("hai inserito il numero di serie? hai fatto l'ordine?"). Il processo BPM ora replica e migliora questo flusso: la prima attività cattura ~70-80 campi direttamente in BPM (molti commerciali, anche via client web/mobile in trasferta), con molti campi trasformati da testo libero a **selezioni guidate da tabella** (vedi tabelle P_) — pur mantenendo testo libero dove serviva la flessibilità richiesta dal cliente (frames/044_025834_real-case-study-scheda-commessa-work-order-form.jpg).

Costruzione di un report:

- I campi presentati nel designer sono raggruppati per pagina/nome variabile, rispecchiando l'organizzazione delle variabili nel processo stesso.
- Trascinando una variabile sul canvas si crea un segnaposto agganciato; si aggiungono etichette statiche intorno.
- **Sezioni condizionali:** intere sezioni possono essere mostrate/nascoste in base a una condizione (es. mostrare una sotto-sezione "Gas1/Gas2" solo se quelle caselle sono selezionate) — utile per moduli con molti sotto-blocchi opzionali.
- **Report testata/dettaglio (gruppo):** con un po' di attenzione, un report può rendere una variabile di gruppo (es. elenco preventivi) come blocco "dettaglio" ripetuto, producendo più righe per pagina stampata.
- I report sono salvati nel database BPM (non nel filesystem) come parte del processo; un comando "Stampa" sull'istanza di processo in esecuzione rende i valori correnti nel template.
- Il docente precisa che questo non vuole competere con un vero strumento di reporting/BI — è una comodità integrata, dato che i dati sono già modellati dentro il processo.

#### Dashboard (cruscotti)

Un altro componente analitico di terze parti integrato (basato su DevExpress) per costruire dashboard visive interattive sui dati di processo — distinto dai report PDF pixel-perfect visti sopra (frames/073_044836_dashboard-tool-introduced.jpg).

Costruzione passo-passo, punto per punto:

1. Si crea una nuova dashboard, si aggiunge una **sorgente dati** agganciata a un processo scelto (es. un processo "reclamo"), la si nomina (es. "elenco reclami") e si importano le variabili che si vogliono avere disponibili come campi (frames/074_045008_demo-create-a-dashboard-and-add-a-data-source.jpg).
2. Si trascinano widget sul canvas — es. una **Griglia** e un **Grafico a torta**; ogni widget, una volta selezionato, mostra delle zone di aggancio (colonne per la griglia; valori/argomenti per il grafico) da popolare trascinandovi i campi.
3. **Formattazione numerica:** opzioni integrate per abbreviazione unità K/M, separatore delle migliaia, cifre decimali.
4. **Grafico a torta:** si trascina un campo univoco (es. `ID`) su "valore" per ottenere un'aggregazione Count di default, e un campo categorico (es. "marca") su "argomenti" per suddividere per categoria.
5. **Elementi filtro:** un widget "casella combinata" agganciato a un campo (es. una data, raggruppata per giorno/mese/anno) funge da filtro incrociato per tutti gli altri widget della dashboard quando l'utente sceglie un valore (frames/075_045518_demo-combo-box-filter-element.jpg).
6. **Campi calcolati:** es. un campo "tempo di risposta" calcolato come `data_risposta − data_apertura`, poi usato con un'aggregazione **Media** per mostrare il tempo di risposta medio.

Prerequisito per KPI significativi — catturare esplicitamente le date chiave: i timestamp grezzi di esecuzione delle attività non sono sempre la metrica che serve (es. "giorni per rispondere a un reclamo" andrebbe misurato da "preso in carico" a "risposto", non da creazione a chiusura del ticket). Il pattern usato: agganciare operazioni **Set Variable** (vedi sopra) a specifiche transizioni di attività che scrivono `Oggi` in variabili data dedicate (`data_presa_in_carico`, `data_risposta`) automaticamente, senza alcun input utente — queste alimentano poi i campi calcolati della dashboard (frames/078_045913_set-variable-operations-capture-today-at-key-trans.jpg).

Disponibilità: una volta salvata, una dashboard è disponibile agli utenti finali (senza la barra degli strumenti di progettazione) sotto il menu **"Analisi Dati"** (compare solo quando esiste almeno una dashboard/tabella, come per il menu delle tabelle personalizzate) — e la stessa identica dashboard è automaticamente disponibile anche nel **client web**, senza bisogno di ricostruirla.

Posizionamento: esplicitamente *non* un sostituto della BI (nessun cubo, tutto calcolato al volo) — il suo valore è la comodità, dato che i dati sono già connessi dentro BPM.

### Integrazione con SAM (ERP)

L'integrazione è articolata attorno a **quattro aspetti distinti**, trattati in sequenza:

1. BPM → SAM: scrittura di documenti/anagrafiche (connettore attivo).
2. BPM → SAM: lettura di tabelle (viste-tabella del connettore / SQL grezzo).
3. SAM → BPM: avvio di un processo da un evento lato SAM (web service/stored procedure/trigger).
4. SAM ↔ BPM: la to-do list di SAM che mostra le attività BPM.

#### Architettura del connettore (generale)

Un "connettore" (es. "SAM v5", o il connettore separato "Globe") è modellato come un **plugin** installabile:

- **Definizione** (metadati che vivono nella configurazione BPM): quali aziende esistono, quali interfacce espone il connettore, e i parametri di connessione generali (URL del web service, dettagli di connessione al DB per ciascuna azienda — i connettori SAM usano un approccio *misto*: alcune operazioni via web service, altre via lettura diretta del DB).
- **DLL/plugin esterno**, che deve essere effettivamente installato sull'ambiente (normalmente incluso nell'installazione standard; altrimenti va richiesto come attività di setup) e che fa il lavoro reale dietro la definizione.
- Il connettore espone due tipi di interfaccia:
 - **Interfacce azione** — usate come *operazioni* trascinate nel flusso di processo; *scrivono* su SAM.
 - **Interfacce tabella** — usate come sorgenti di lookup in sola lettura su campi/griglie dati; espongono i dati SAM come se fossero una tabella/vista locale.
- Configurazione azienda/ambiente: Configurazione → connettori → spuntare **Attivo**, aggiungere un'azienda ("nuova azienda") e compilare i parametri per azienda (server DB, credenziali, DB marketing se rilevante, e l'endpoint web service di quell'azienda).

#### Connettore attivo — BPM scrive su SAM

Un tipo di operazione, associata a uno specifico connettore, che scrive un documento o un'anagrafica in SAM (creare un cliente, creare una "commessa", registrare un "intervento", ecc.), inserita nel flusso come qualunque altra operazione. Per **SAM 5**, questa funzionalità è costruita sopra la funzione XML **Web Import** di SAM; per SAM 6 è previsto un supporto più ricco tramite web service JSON (frames/047_031052_connettore-attivo-active-connector-operation.jpg).

Configurazione guidata (es. "creazione commessa") (frames/048_031324_xml-template-variable-mapping-demo.jpg):

1. Si trascina l'operazione connettore-attivo nel processo, si fa doppio clic, e si sceglie un'interfaccia XML preconfezionata (es. "xml commessa").
2. L'interfaccia arriva con un template preconfigurato e un insieme finito e fisso di **parametri di input** ("testata", raccomandati dalla documentazione tecnica di SAM stessa) — ciascuno si mappa su una variabile di processo, o si lascia come valore fisso letterale. Un campo obbligatorio mancante causa semplicemente il rifiuto della chiamata da parte del web import di SAM con un errore (BPM stesso non sa cosa l'XML "dovrebbe" contenere — è solo un pass-through).
3. Campi di testata aggiuntivi non presenti nell'elenco di default possono essere aggiunti tramite un piccolo helper (che conosce le colonne della tabella target) e mappati allo stesso modo.
4. **Parametri di output:** se l'interfaccia restituisce dei valori (non tutte lo fanno), possono essere mappati indietro su variabili di processo, es. catturando l'ID interno del nuovo documento / il numero documento in `numero_commessa`.
5. **Parametri di riga/dettaglio:** se il processo ha un gruppo corrispondente (es. "lista codici"), ogni riga del gruppo viene mappata automaticamente su un nodo di dettaglio XML ripetuto — permettendo di inviare in una sola chiamata un intero elenco di righe ordine/distinta (es. mappando `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`). Tutto ciò che non è esplicitamente presente in BPM (es. logica dei prezzi) è lasciato interamente alla configurazione di SAM (frames/049_031849_detail-row-parameters-mapping-a-group-to-xml-rows.jpg).

Estensibilità: le interfacce preconfezionate coprono un insieme deliberatamente finito di casi comuni (cliente, commessa, intervento, ecc.) — un nuovo template XML genuinamente diverso richiede una richiesta di sviluppo, non è qualcosa che un consulente/cliente possa cablare liberamente dall'interfaccia.

Requisito di attivazione: il **modulo Web Import** di SAM deve essere installato e raggiungibile — tipicamente un ticket sistemistico di routine, nessuna licenza aggiuntiva richiesta.

Alternativa/quando non usarlo: se non esiste un'interfaccia di connettore preconfezionata per ciò che serve, una semplice attività manuale che ricorda a un utente di inserire il record in SAM è un'alternativa legittima — automatizzarla solo per il gusto di farlo può essere in realtà peggio, se significa duplicare logica anagrafica (es. tutte le regole di onboarding cliente) che già vive correttamente dentro SAM. È più appropriato quando serve solo un record segnaposto leggero (es. uno stub cliente con un codice, per poter agganciare documenti contro di esso).

#### Lettura dei dati SAM in BPM (connettori tabella)

Due opzioni per un campo/griglia dati agganciato a una tabella per leggere dati SAM:

- **Vista locale/accesso diretto a tabella esterna** — si costruisce una propria vista SQL con esattamente le colonne desiderate (un certo sforzo iniziale una tantum, ma piena flessibilità).
- **Connettore Dati (interfaccia tabella del connettore)** — si sceglie da un catalogo finito di viste preconfezionate incluse nel connettore; se manca una colonna necessaria, occorre richiederne l'aggiunta a monte, oppure **copiare la vista generata e personalizzare la copia** (modificare l'originale non è sicuro — vedi sotto).

Come vengono generate le viste preconfezionate: eseguire l'"aggiornamento database" del connettore genera automaticamente un insieme di viste SQL con prefisso `vvbpm...` dentro il database SAM (una per ogni interfaccia tabella esposta, es. la vista clienti).

Insidia critica: queste viste auto-generate vengono **rigenerate/sovrascritte** ogni volta che la definizione del connettore viene aggiornata — qualunque modifica manuale alla vista originale va persa. Il pattern sicuro è duplicare la vista sotto un proprio nome e puntare la propria personalizzazione alla copia.

#### La to-do list di SAM mostra le attività BPM

Un modulo di SAM permette alle voci della to-do list BPM ("eventi BPM") di comparire integrate nella to-do list nativa di SAM, per gli utenti che lavorano su entrambi i sistemi e non vogliono cambiare applicazione.

- Doppio clic su un evento BPM dentro SAM mostra un popup di dettaglio dal vivo (nome processo/modello, attività corrente) recuperato **in tempo reale tramite un web service BPM** — nulla riguardo alle attività BPM è cache/salvato nel database di SAM, viene letto fresco ogni volta che si apre la schermata.
- Include lo stesso meccanismo di deep-link usato nelle mail per saltare direttamente a quell'attività nel client web BPM.
- **Sincronizzazione bidirezionale dal vivo:** avanzare un'attività in BPM (es. passare da "firma1" a "firma2") si riflette immediatamente come la stessa attività che compare nella to-do list di SAM — sono la stessa attività sottostante, non due copie mantenute separatamente (frames/053_034238_bidirectional-sync-firma1-firma2-mirrored-in-both-.jpg).
- Lo stesso meccanismo/modulo è disponibile anche dentro la to-do list di **CRM1**.

Configurazione (lato SAM): Opzioni → cerca "BPM" → impostare il **percorso server BPM** (di nuovo: deve essere il vero hostname raggiungibile esternamente, non localhost) e una **chiave API generata da BPM**.

Generazione della chiave API (lato BPM): Configurazione → **Chiave Web API** — creare una nuova chiave (opzionalmente con data di scadenza); è la credenziale che ogni chiamante esterno (SAM, Postman, codice custom) deve presentare.

Mapping utenti: Configurazione → Utenti e Gruppi → ogni utente ha una sezione **"Alias"** che mappa la sua identità per ciascun connettore esterno (es. `css-admin` di SAM ↔ `admin` di BPM) — ogni connettore può avere il proprio mapping utenti indipendente (frames/054_034451_user-alias-mapping-between-bpm-and-sam.jpg).

#### Pilotare BPM da SAM (SAM → BPM)

**Web service standard di BPM:** un insieme deliberatamente **piccolo** di endpoint HTTP che accettano body JSON in POST (descritti come "REST-ish" più che strettamente REST). Tenuto piccolo perché una singola chiamata generica `create-new-process`, parametrizzata sul nome del modello, copre già l'avvio di *qualunque* processo.

Endpoint principali:

- `create-new-process` — avvia una nuova istanza di processo (specifica modello, punto di partenza, variabili iniziali).
- `exec-task` — avanza/esegue un'attività attualmente presente nella to-do list di un utente (simula il clic su "Esegui").
- Caricamento di un allegato su un processo.
- Forzare l'avanzamento di un processo.
- Lettura dei dati variabili di un processo.
- Lettura della to-do list di un utente.

Prova pratica: non serve installare nulla — basta generare una chiave API e qualunque server BPM può essere chiamato. Dimostrato dal vivo con **Postman** (frames/057_035206_postman-demo-create-a-new-process-via-web-service.jpg):

```
POST {bpm-server}/api-ext-create-new-process
Body (JSON): { auth_token, user, model, start, variables{...} }
```

La risposta restituisce successo/fallimento più il nome del processo generato (secondo la regola di naming) ed eventuali messaggi di validazione.

Insidie confermate dal vivo:

- Omettere il punto di partenza su un modello multi-start restituisce un errore esplicito invece di sceglierne uno silenziosamente.
- Campi obbligatori/formule di validazione sono applicati esattamente come lo sarebbero dall'interfaccia utente — un payload incompleto/non valido restituisce `false` senza effetti collaterali.
- `exec-task` è funzionalmente equivalente a cliccare "Esegui" nella to-do list — usato ad es. per far avanzare un processo BPM quando avviene un evento corrispondente lato SAM, anche se il docente è cauto sull'affidarsi troppo a questo meccanismo perché *identificare correttamente* l'evento SAM scatenante è spesso la parte difficile.

Raccomandazione: le chiamate dirette ai web service sono il metodo **ufficiale e più robusto** per qualunque integrazione custom/plugin — restituiscono un vero risultato sincrono di successo/fallimento.

#### Wrapper a stored procedure e trigger (percorso asincrono)

Perché esiste: SAM non ha un meccanismo nativo di evento/webhook in uscita, quindi l'*unico* strumento disponibile per intercettare un evento lato SAM (nuovo ordine, cambio di stato, ecc.) e far partire un processo BPM è un classico **trigger SQL**.

Meccanismo del wrapper a stored procedure: la stessa capacità di "creare processo" è esposta anche come semplice **stored procedure SQL** — ma invece di chiamare il web service in modo sincrono, scrive semplicemente una riga in una tabella di staging (`chiamate API`); un motore in background interno a BPM legge periodicamente quella tabella ed esegue esso stesso la vera chiamata al web service:

```sql
EXEC dbo.usp_bpm_create_process
 @user = 2, @model = 'richieste inv', @start = 1, @external_id = 1
```

Pattern d'uso dei trigger (progetti reali citati: un cliente del settore alimentare, e "Calzavara"): un trigger richiama la stored procedure quando accade un evento di business in SAM (es. un ordine viene approvato); il processo BPM risultante procede e, a ogni passo, usa l'**operazione SQL** per scrivere aggiornamenti di firma/stato indietro su SAM man mano che avanza.

Insidia chiave dell'asincronia: a differenza della chiamata diretta al web service, i trigger e il wrapper a stored procedure sono **fire-and-forget/asincroni** — non c'è un risultato immediato di successo/fallimento, la consegna tipicamente si completa in pochi secondi tramite il motore della tabella di staging, ma questo percorso richiede un **collaudo approfondito**, e la logica del trigger stesso può essere fragile (un bug nel trigger può "mandare in crash" la transazione SAM sottostante).

Convenzione — mantenere il trigger minimale ("External ID"): per evitare di riversare decine di campi in un trigger fragile, il team ha adottato una convenzione rigida: la stored procedure accetta **un solo parametro** — l'ID del documento sorgente — mappato in una variabile di processo BPM chiamata letteralmente **`external_id`**.

BPM si arricchisce da sé dopo l'avvio minimale via trigger, tramite un callback: come primissimo passo del processo (sullo Start, nelle operazioni), BPM richiama subito indietro SAM — usando **Get Data** oppure una **vista-tabella del connettore**, con chiave `external_id` — per recuperare tutti gli altri campi che il processo realmente necessita (ragione sociale del fornitore, indirizzo, termini di pagamento, righe ordine, ecc.). Questo sposta deliberatamente tutta la complessità dal trigger fragile verso gli strumenti BPM, più robusti e testabili.

Via di fuga per casi complessi: se il pattern standard trigger/SP/Get Data non è davvero sufficiente, il codice custom che chiama direttamente i web service è sempre disponibile come alternativa (un collega — Filippo Curati — ne aveva prototipato esattamente una).

#### Buone pratiche e aneddoti reali sull'integrazione

- **Aneddoto — inseguire un evento di business "sfumato":** un cliente voleva un'attività avanzata automaticamente "quando viene inserita la distinta base" in SAM. Il docente spiega che si tratta di un obiettivo di automazione genuinamente difficile: non esiste un singolo evento di database inequivocabile che significhi affidabilmente "la distinta base è davvero finita", e le richieste dei clienti di "automazione totale" portano spesso aspettative poco realistiche che vanno gestite/ridimensionate a monte — meglio promettere meno che costruire qualcosa di fragile che si rompe silenziosamente su casi limite (articolo sbagliato, inserimento duplicato, lotto/partita sbagliati, ecc.) (frames/063_041304_anecdote-a-trigger-event-too-fuzzy-to-automate-rel.jpg).
- **Buona pratica — minimizzare l'accoppiamento:** evitare di progettare un'integrazione in cui i due sistemi interagiscono continuamente avanti e indietro per tutto il processo (ogni modifica al processo rischia allora di rompere anche il lato SAM). La forma ideale prevede che i due sistemi si parlino solo **all'inizio e alla fine** del processo (es. un trigger per lanciare, una scrittura finale di stato tipo "approvato"/"non approvato" invece di molti micro-stati intermedi sincronizzati avanti e indietro).
- SAM 6 dovrebbe supportare questa integrazione in modo più nativo/flessibile tramite veri web service JSON, riducendo la dipendenza dai workaround dell'era trigger/Web Import descritti sopra.

### Pianificazione e Gantt

#### Concetto di base

Oltre a tracciare le date/orari effettivi di inizio/fine di ogni attività (cosa che BPM registra sempre di default), BPM offre un livello opzionale di **pianificazione/stima**: durate standard attese per attività, riepilogate automaticamente in un Gantt dal vivo che si aggiorna man mano che il processo procede realmente.

Caratteristiche importanti:

- Le durate sono espresse in **giorni di calendario** (tempo solare), *non* in unità di sforzo/capacità — non esiste in BPM un concetto di capacità/allocazione risorse.
- L'intera funzionalità è opzionale per ogni processo; può essere disattivata interamente tramite permessi quando non è utile per un dato processo (vedi Calendario e permessi, sotto).

#### Impostare durate standard e Gantt auto-generato

1. Su ogni attività, si apre **Pianificazione e Scadenze** e si imposta una durata standard in giorni (es. 5, 7, 15, 2) (frames/065_042229_demo-setting-standard-task-durations-on-the-model.jpg).
2. Non appena un'istanza di processo parte, BPM calcola immediatamente una stima Gantt dell'intero processo a partire da queste durate standard, visibile sotto la scheda **Pianificazione** del magazzino delle variabili.
3. Il motore del Gantt modella correttamente la struttura delle dipendenze — inclusi i rami paralleli (due attività affiancate, con logica finish-to-start che alimenta l'attività di ricongiungimento a valle solo dopo la conclusione del ramo parallelo *più lungo*) — "proprio come in Project".

#### Aggiornamenti dal vivo mentre il processo procede

- Man mano che ogni attività viene effettivamente completata, la sua barra Gantt passa dalla durata pianificata originale (mostrata tratteggiata, come "baseline") alla durata compattata/reale, e **tutto ciò che sta a valle si sposta di conseguenza**.
- **Comportamento chiave — il piano spinge solo a destra, mai a sinistra:** se l'avanzamento reale va più tardi del previsto, la pianificazione "aggiornata" slitta più avanti; ma procedere *in anticipo* su un'attività non comprime automaticamente la stima al di sotto delle durate standard per le attività non ancora iniziate.
- Riprogrammare un'attività dalla vista to-do list/calendario (es. trascinando un'attività a una data successiva) rimodella immediatamente anche il Gantt a valle — perché le date della to-do list e le date del Gantt sono letteralmente lo stesso dato sottostante, non due sistemi separati.

#### I tre insiemi di date

Per ogni attività, BPM traccia tre copie parallele dell'intervallo di date:

1. **Programmazione (iniziale/baseline):** il piano originale, punto zero.
2. **Aggiornamento:** la stima corrente, ricalcolata continuamente dal vivo.
3. **Effettiva:** popolata solo una volta che un'attività è realmente iniziata e/o terminata.

#### Data scadenza — separata dalla durata

Concetto: un vincolo di scadenza rigido, imposto dall'esterno (mostrato come un pallino rosso sulla barra del Gantt), impostabile su **qualunque** attività — non solo l'ultima — usato per confrontare la pianificazione aggiornata dal vivo con una data promessa.

Indicazione emersa in sede di Q&A: il modo *corretto* di impostare una scadenza è agganciarla a una vera **variabile data** (qualcosa che l'utente inserisce, o che arriva da un sistema esterno come SAM) piuttosto che a una durata relativa del tipo "N giorni dopo l'inizio" — perché le durate rispondono a "quanto tempo richiede", mentre una scadenza è un vincolo esterno che va catturato come un proprio dato autonomo.

Caso d'uso: scadenze di milestone intermedie a metà processo — es. date di checkpoint del cliente dentro un progetto più lungo, non solo una singola data di fine.

#### Rileva inizio (disaccoppiare inizio attività da attivazione)

Comportamento di default: senza questo flag, l'"inizio" di un'attività si assume coincidente con il momento in cui l'attività precedente è terminata (cioè attivazione = inizio).

Con "rileva inizio" abilitato su un'attività:

- La to-do list mostra un pulsante **"Inizia"** invece di saltare direttamente a "Esegui".
- Finché l'utente non clicca esplicitamente Inizia, la barra Gantt dell'attività ha un contorno sottile/non marcato e nessuna data di inizio effettiva.
- Una volta iniziata, la barra ottiene un bordo marcato e viene registrata una vera data di inizio effettiva.
- Caso d'uso: lavoro che è *pronto ma non ancora iniziato* — es. attività di progettazione/ingegneria che restano "disponibili" per un po' prima che qualcuno le prenda in carico — distingue "in coda" da "in corso".
- Questo si ricollega direttamente ai punti di aggancio delle operazioni Attivazione vs. Inizio: l'aggancio "Inizio" scatta in modo significativo solo su attività con rileva inizio abilitato.

#### Agganciare date/durate a variabili di processo

Sia la **scadenza** sia la **durata pianificata** di un'attività possono essere agganciate a una variabile di processo invece che a un valore fisso di configurazione, rendendo il piano dinamico in base ai dati del processo invece che a un numero statico a livello di modello.

Esempi guidati:

- Scadenza: agganciare "data scadenza" (calendario) a una variabile "data consegna prevista" che il commerciale compila al momento dell'inserimento.
- Durata: un cliente reale aveva una variabile a lista di valori "difficoltà" (A/B/C), e una formula/decision table calcolava la durata standard a partire da essa (es. 5/7/10/12 giorni), che pilotava poi la durata pianificata dell'attività:

```vb
If difficolta = "A" Then
 Return 5
Else
 Return 10
End If
```

#### Da confermare — aggiustamento della baseline iniziale

Concetto: un flag per attività che dà al **proprietario** del processo una finestra una tantum, proprio nel momento in cui l'attività diventa disponibile, per aggiustare manualmente le date pianificate di quella specifica istanza (trascinandole) prima di bloccarle definitivamente.

Flusso operativo:

1. L'attività diventa disponibile con stato "da confermare"; il proprietario può liberamente trascinare/aggiustare le sue date pianificate (e ogni effetto a valle) — questo tocca ancora la baseline *iniziale*, ma solo per questa istanza, non per il modello.
2. Il proprietario clicca **Conferma** (per singola attività, o "conferma tutto"): questo **congela** il piano aggiustato come baseline permanente dell'istanza ("versione 0" / punto di confronto) (frames/082_051243_demo-confirming-freezes-the-baseline-plan.jpg).
3. Da quel momento in poi, ogni ulteriore scostamento viene tracciato solo nella pianificazione "aggiornata", relativamente a quella baseline congelata — la baseline confermata in sé non cambia mai più.

- Se un'attività non è marcata "da confermare", nasce già confermata, e il piano derivato dalla durata standard originale è semplicemente, fin dall'inizio, la baseline permanente.

#### Calendario e permessi

- BPM ha un **calendario interno integrato** che tiene conto di weekend e festività; quando viene calcolata una durata attività di "12 giorni", questa copre di default 12 giorni *di calendario* (i weekend sono mostrati in grigio nel Gantt). Un flag per attività ("Utilizza Calendario") permette a un'attività di ignorare il calendario e contare i giorni trascorsi grezzi (es. un passaggio di processo genuinamente attivo 24/7). Il calendario in sé non è facilmente personalizzabile dall'utente finale — lo si usa o non lo si usa.
- L'intera vista di pianificazione/Gantt (visualizzazione e/o modifica) è vincolata da **permessi a livello di processo** ("visualizza pianificazione" / "modifica pianificazione") per utente/gruppo — per i processi in cui il Gantt non ha significato, è meglio nasconderlo del tutto piuttosto che mostrare un grafico confuso o irrilevante.

---

## Tutorial passo-passo

### Tutorial 1 — Costruire una griglia dati collegata a una tabella fornitori

Obiettivo: aggiungere alla form di un processo una griglia in sola lettura che mostri i dati anagrafici dei fornitori, consultabile senza uscire dal processo. –

1. Nel magazzino delle variabili, crea una nuova variabile e imposta il suo tipo su **Griglia Dati**.
2. Apri la configurazione della variabile (la stessa schermata usata per l'aggancio tabella dei campi semplici).
3. Scegli come tabella sorgente la tabella (locale, vista o tabella esposta da connettore) desiderata — nell'esempio del corso, la tabella "fornitori".
4. Nell'elenco delle colonne disponibili, seleziona quelle da esporre nella griglia (nell'esempio: codice, descrizione).
5. Per ciascuna colonna selezionata, se il nome originale non è chiaro per l'utente finale, assegna un'intestazione (caption) più leggibile.
6. Salva la configurazione della variabile.
7. Trascina la variabile griglia dati nella form del processo (pagina del magazzino) e anche nelle "variabili da richiedere" dell'attività/start dove deve comparire, dandole spazio a schermo sufficiente.
8. Pubblica il processo.
9. Avvia (o riapri) un'istanza: la griglia appare popolata con i dati della tabella, filtrabile e raggruppabile come le altre griglie del prodotto, ma non modificabile.

Nota: lo stesso identico meccanismo di aggancio è usato per i campi con lookup su tabella (combo/popup di ricerca) — la differenza è solo nella resa a video.

### Tutorial 2 — Filtrare un gruppo diversamente su due attività parallele e condizionare il gateway

Obiettivo: due attività parallele di valutazione preventivi (tipo A / tipo B) devono mostrare, dello stesso gruppo "lista preventivi", solo le righe pertinenti al proprio tipo; inoltre il ramo verso ciascuna attività deve aprirsi solo se esistono righe di quel tipo. –

1. Nel diagramma di processo, individua le due attività parallele (es. "valutazione preventivi tipo A" e "valutazione preventivi tipo B"), entrambe collegate allo stesso gruppo "lista preventivi".
2. Sulla prima attività, apri "variabili da richiedere" e seleziona una qualunque variabile appartenente al gruppo "lista preventivi".
3. Nelle impostazioni locali di quella variabile, disabilita l'aggiunta e la cancellazione righe (per rendere la vista di sola consultazione su questa attività) e imposta una **condizione di filtro**, ad esempio `tipo_preventivo = "tipo A"`.
4. Ripeti i passi 2–3 sulla seconda attività, con la condizione opposta (`tipo_preventivo = "tipo B"`).
5. Nel magazzino delle variabili, crea due variabili helper di tipo stringa (es. `presenza_tipo_A`, `presenza_tipo_B`) — servono solo per verificare visivamente il risultato della formula mentre la costruisci, dato che BPM non ha un debugger.
6. Su `presenza_tipo_A`, apri l'editor di formula e scrivi:

 ```vb
 Dim i As Integer
 For i = 0 To lista_preventivi.Count - 1
 If tipo_preventivo(i) = "tipo A" Then
 Return "sì"
 End If
 Next
 Return "no"
 ```

7. Ripeti lo stesso schema per `presenza_tipo_B`, sostituendo la condizione con `"tipo B"`.
8. Sul gateway (o link) che porta verso l'attività "valutazione preventivi tipo A", apri la condizione di abilitazione e imposta `presenza_tipo_A = "sì"`. Ripeti analogamente per il ramo tipo B.
9. Facoltativo — validazione globale: sull'attività di inserimento preventivi, aggiungi una formula di validazione globale che impedisca di proseguire se non è stato inserito alcun preventivo:

 ```vb
 If Count(tipo_preventivo) = 0 Then
 MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
 Return False
 End If
 Return True
 ```

10. Pubblica e collauda con dati di test: inserisci solo preventivi di tipo A e verifica che si apra solo il ramo corrispondente; ripeti con tipo B e con entrambi.

### Tutorial 3 — Costruire una decision table per l'assegnazione automatica dell'approvatore in base all'importo

Obiettivo: sostituire una formula scritta a mano con una decision table che assegna l'approvatore tecnico in base all'importo della richiesta (ed eventualmente al tipo di richiesta). –

1. Individua il punto del processo dove serve calcolare l'utente approvatore — tipicamente una formula agganciata a una variabile di tipo Utente (es. `utente_approvazione_tecnica`), oppure una decisione da prendere in un'operazione Set Variable.
2. Apri l'editor della formula/valore su quella variabile e scegli l'opzione per convertirla in **decision table** (o creane una nuova direttamente come decision table, se disponibile).
3. Aggiungi una colonna di input: `Importo Richiesta`.
4. Aggiungi una colonna di output: `Utente Approvazione` — essendo di tipo Utente, la tabella propone automaticamente l'elenco di utenti/gruppi disponibili come valori possibili.
5. Inserisci le righe-regola:

 - Riga 1: `Importo Richiesta < 1000` → `Dir Tech`
 - Riga 2: `Importo Richiesta ≥ 1000` → `Dir Gen`

6. Verifica/aggiusta l'ordine delle righe con le frecce su/giù, ricordando che vince la prima riga che soddisfa la condizione.
7. Estendi la tabella con una seconda colonna di input, `Tipo Richiesta` (lista di valori — la tabella ne conosce automaticamente i valori ammessi), e aggiungi/riordina le righe:

 - `< 1000` / `Normale` → `Dir Tech`
 - `≥ 1000` / `Normale` → `Dir Gen`
 - `(qualunque)` / `Sicurezza` → `Sicurezza`

8. Salva la decision table.
9. Sull'attività di approvazione, imposta gli "utenti responsabili" sulla variabile `utente_approvazione_tecnica` (assegnazione guidata da regola) invece che su un gruppo fisso.
10. Pubblica e collauda con richieste di importo/tipo diversi, verificando che l'attività venga assegnata correttamente.
11. Se in seguito la logica dovesse superare ciò che la tabella può esprimere (es. serve scorrere un gruppo e contare righe), converti la tabella in formula e completa la logica a mano in VB.

### Tutorial 4 — Configurare un connettore attivo verso SAM per la creazione di una commessa

Obiettivo: da un'attività del processo, generare automaticamente una nuova commessa in SAM tramite il connettore attivo, mappando testata, dettaglio righe e recuperando il numero commessa generato. –

1. Verifica preliminare (lato ambiente): il connettore "SAM v5" deve essere configurato in Configurazione → connettori, marcato **Attivo**, con almeno un'azienda ("nuova azienda") configurata con i parametri di connessione (server DB, credenziali, endpoint web service dell'azienda). Il modulo **Web Import** di SAM deve essere installato e raggiungibile.
2. Nel diagramma di processo, trascina l'operazione **Connettore Attivo** nel punto del flusso dove deve avvenire la creazione della commessa.
3. Fai doppio clic sull'operazione appena inserita.
4. Scegli l'interfaccia XML preconfezionata pertinente (es. "xml commessa").
5. Nella schermata dei parametri di input (testata), mappa ciascun campo richiesto su una variabile di processo corrispondente (es. codice cliente, descrizione commessa) oppure lascialo come valore fisso quando appropriato.
6. Se serve un campo di testata non presente nell'elenco default, usa l'helper di aggiunta campo (che conosce le colonne della tabella target in SAM) per aggiungerlo e mappalo a sua volta.
7. Se l'interfaccia prevede parametri di output (es. l'ID/numero della commessa creata), mappali su una variabile di processo dedicata (es. `numero_commessa`).
8. Se il processo include un gruppo di dettaglio corrispondente (es. "lista codici" articoli), apri la sezione parametri di dettaglio/riga e mappa ciascuna colonna del gruppo sul nodo XML di dettaglio ripetuto corrispondente (es. `codice_articolo` → `csx riga OV / codice articolo`, `qta` → `qta1`).
9. Salva la configurazione dell'operazione.
10. Pubblica il processo e collauda l'esecuzione dell'attività: verifica in SAM che la commessa sia stata effettivamente creata con i dati attesi, e che `numero_commessa` sia stato valorizzato correttamente nell'istanza di processo.
11. In caso di errore, ricorda che BPM è un semplice pass-through verso il web import di SAM: un campo obbligatorio mancante o non valido produce un errore restituito da SAM, non da BPM.

### Tutorial 5 — Impostare la pianificazione/Gantt di un processo con durate standard e scadenza dinamica

Obiettivo: dotare un processo di stime di durata per ogni attività, in modo che all'avvio di ogni istanza venga generato automaticamente un Gantt, con una scadenza agganciata a una variabile data. –

1. Verifica i permessi di processo: sotto Utenti e Gruppi, assicurati che "visualizza pianificazione" (e, se necessario, "modifica pianificazione") siano abilitati per i gruppi che dovranno vedere/gestire il Gantt.
2. Per ciascuna attività del processo, apri la scheda **Pianificazione e Scadenze** e imposta una durata standard in giorni (es. 5, 7, 15, 2 a seconda dell'attività).
3. Se un'attività deve avere un vincolo di scadenza esterno (non derivato dalla durata), sulla stessa scheda seleziona l'opzione per agganciare la **data scadenza** a una variabile data del processo (es. `data_consegna_prevista`), invece di lasciarla come valore fisso o come "N giorni dopo l'inizio".
4. Facoltativo — durata dinamica: se la durata standard deve dipendere da un dato del processo (es. una variabile lista di valori "difficoltà" A/B/C), crea una formula o decision table che calcoli la durata in giorni e agganciala al campo durata dell'attività:

 ```vb
 If difficolta = "A" Then
 Return 5
 Else
 Return 10
 End If
 ```

5. Se un'attività rappresenta lavoro che può restare "disponibile" prima di essere effettivamente iniziato (es. attività di progettazione), abilita il flag **Rileva Inizio** su quell'attività.
6. Se il processo richiede che il proprietario possa aggiustare la pianificazione iniziale di ogni singola istanza prima che diventi baseline definitiva, abilita il flag **Da Confermare** sulle attività pertinenti.
7. Verifica, per le attività il cui ritmo di lavoro non segue la settimana lavorativa standard, se disabilitare il flag "Utilizza Calendario" (per contare giorni solari grezzi invece che giorni di calendario aziendale con weekend/festività).
8. Pubblica il processo.
9. Avvia una nuova istanza: verifica, nella scheda **Pianificazione** del magazzino delle variabili, che il Gantt dell'intero processo sia stato generato automaticamente a partire dalle durate standard.
10. Completa la prima attività e osserva che la sua barra passa da tratteggiata (baseline) a piena (reale), e che tutte le attività a valle si aggiornano di conseguenza nella pianificazione "aggiornata".
11. Se un'attività è marcata "Da Confermare", verifica che al momento della sua attivazione il proprietario possa trascinare/aggiustare le date proposte e poi cliccare **Conferma** (o "conferma tutto") per congelarle come nuova baseline dell'istanza.
