# Integrazione

BPM non lavora mai da solo. Nella quasi totalità delle installazioni legge almeno le anagrafiche dal gestionale, e spesso scambia dati in entrambe le direzioni con ERP, CRM, sistemi di produzione e servizi web.

Questa sezione risponde alle domande di chi deve collegare BPM ai sistemi dell'azienda: *come leggo i dati del mio ERP? come ci scrivo? come avvio un processo quando nel gestionale succede qualcosa? come chiamo un servizio esterno quando un'attività viene approvata?*

## Due modi di integrare BPM

Le integrazioni con BPM ricadono in due famiglie, diverse per chi prende l'iniziativa.

### Dall'esterno: le API standard

Un'applicazione esterna **pilota attivamente BPM**: avvia processi, esegue le attività, legge la To-Do List di un utente, consulta lo stato di un processo, carica documenti, ne cerca, ne scarica il contenuto e le versioni. È BPM a offrire un servizio, e l'applicazione esterna a decidere quando usarlo.

È la strada per portare BPM dentro un altro software: un portale che mostra ai propri utenti le attività BPM, un ERP che avvia un'approvazione, un'applicazione che archivia documenti nel documentale.

- [API standard](api-standard/index.md): le chiamate disponibili, l'autenticazione, gli esempi.
- [Coda delle chiamate](coda-chiamate.md): la stessa possibilità per i sistemi che lavorano solo sul database, con richieste scritte in una tabella ed eseguite in modo asincrono.

### Dal processo: gli strumenti del workflow

È **BPM a prendere l'iniziativa**, nei punti del processo in cui serve. Essendo un motore di workflow, BPM permette di inserire nelle procedure i momenti di lettura e di scrittura dei dati, secondo l'organizzazione scelta: all'avvio, all'attivazione o alla conclusione di un'attività, su un ramo del flusso, all'arrivo di un file o di una mail.

| Esigenza | Strumento |
|---|---|
| Proporre nei campi i dati del gestionale (clienti, fornitori, articoli…) | [Dati esterni nelle variabili](dati-esterni.md) |
| Leggere dati esterni durante il processo e copiarli nelle variabili | [Carica Dati](carica-dati.md) |
| Scrivere sul database di un altro sistema, o eseguire query e stored procedure | [Esegui SQL](esegui-sql.md) |
| Chiamare un servizio web (REST) di un altro sistema | [Web Service](connettori/web-service.md) |
| Avviare un processo quando arriva un file in una cartella o una mail | [File System](connettori/file-system.md), [Mail](connettori/mail.md) |
| Salvare allegati e documenti su file system | [File System](connettori/file-system.md) |

Tutti gli strumenti che accedono a un database usano le [connessioni esterne](connessioni-esterne.md), configurate una volta sola.

## Un'integrazione ordinata

Gli strumenti permettono di fare quasi tutto, ma non tutto conviene. Un'integrazione ben fatta è quella che si riesce ancora a capire e a modificare dopo un anno. Alcuni principi:

- **Ognuno fa il suo mestiere.** L'ERP resta il padrone dei dati (anagrafiche, ordini, articoli); BPM è il padrone del processo: chi deve fare cosa, in che ordine, con quali regole, e lo storico di ciò che è successo.
- **Pochi punti di contatto, ben scelti.** Di solito bastano un momento in cui BPM legge i dati di cui ha bisogno (all'avvio) e uno in cui restituisce l'esito (alla conclusione o a un'approvazione). Ogni scambio in più è un punto da mantenere.
- **Passare riferimenti, non dati.** Per avviare un processo basta l'identificativo del record esterno, per esempio l'ID dell'ordine (la convenzione *EXTERNAL ID*): è poi il processo a leggere ciò che gli serve. Così il sistema esterno non deve conoscere le variabili del processo, e il processo può cambiare senza toccarlo.
- **Lo stato si chiede, non si spinge.** Non serve che BPM notifichi al sistema esterno ogni passaggio: in qualunque momento il sistema esterno può chiedere lo stato di avanzamento con [GetProcess](api-standard/processi.md#getprocess) o le attività aperte con [GetTodolist](api-standard/attivita.md#gettodolist).
- **Il disegno del processo resta libero.** Se l'integrazione è concentrata in pochi punti, il flusso si può ridisegnare (aggiungere un'approvazione, cambiare un percorso) senza preoccuparsi dei dettagli dell'ERP. Un'orchestrazione in cui ogni attività scambia dati con l'esterno diventa invece fragile e poco produttiva: ogni modifica al processo è anche una modifica all'integrazione.
- **Preferire le API alle scritture dirette.** Se il sistema esterno espone API, usarle: applicano le regole di quel sistema. Una scrittura diretta sul suo database no.

Lo scenario dell'ERP qui sotto segue questi principi.

## Gli strumenti nel processo: operazioni, eventi e connettori

Nel Designer, gli strumenti del workflow sono due famiglie di oggetti.

<div class="grid" markdown>

![Operazioni](../assets/modelli-di-processo/designer/palette-operazioni.png){ width=200 }

![Eventi](../assets/modelli-di-processo/designer/palette-eventi.png){ width=160 }

</div>

Le **[operazioni](../modelli-di-processo/elementi/operazioni/index.md)** sono le attività automatiche del processo: si inseriscono nel flusso oppure si agganciano a un momento del ciclo di vita di un'attività. Alcune servono alla logica del processo (Decision Table, Imposta variabili, Invia email, Aggiorna altro processo); per l'integrazione contano soprattutto:

- **Carica dati** ed **Esegui sql**, operazioni native per leggere e scrivere su database;
- **Connettore attivo**, che esegue una funzione di un connettore: chiamare un servizio web, salvare un file, e molto altro.

Gli **[eventi](../modelli-di-processo/elementi/eventi.md)** avviano, sospendono o concludono il flusso. Per l'integrazione conta **Start su evento**: il processo non viene avviato da un utente o da un'applicazione, ma dal motore di BPM stesso, in ascolto, quando si verifica l'evento di un connettore (l'arrivo di un file, di una mail).

I **[connettori](connettori/index.md)** sono i moduli che forniscono queste funzioni: le loro operazioni si usano tramite Connettore attivo, i loro eventi tramite Start su evento.

### Il collegamento con le variabili

Tutti questi strumenti comunicano con il processo attraverso le **variabili**. Nella configurazione di un'operazione o di un evento, ogni parametro si valorizza in uno di due modi:

- con un **valore fisso**, uguale per ogni istanza (per esempio la cartella da monitorare);
- **collegandolo a una variabile** del processo, il cui valore cambia da un'istanza all'altra.

I parametri di **ingresso** leggono le variabili: il codice cliente da cercare, l'importo da scrivere nell'ERP, il corpo della chiamata a un servizio web. I parametri di **uscita** scrivono nelle variabili: la ragione sociale letta, l'identificativo restituito dal CRM, il mittente della mail arrivata. Le attività successive del processo trovano così i dati già pronti, e li vedono anche gli utenti nelle loro maschere.

## Due scenari tipici

### Integrare BPM con l'ERP

Un processo di approvazione degli ordini d'acquisto:

1. **Le anagrafiche restano nell'ERP.** Il campo *Fornitore* propone i fornitori leggendoli dal database dell'ERP ([dati esterni nelle variabili](dati-esterni.md)): nessuna copia dei dati in BPM.
2. **L'ERP avvia il processo.** Quando un ordine viene inserito, un trigger nell'ERP accoda l'avvio con la [coda delle chiamate](coda-chiamate.md), passando solo l'ID dell'ordine (convenzione *EXTERNAL ID*). Se l'ERP può fare chiamate HTTP, può usare direttamente le [API standard](api-standard/processi.md#createnewprocess).
3. **BPM recupera i dati.** All'avvio, un'operazione [Carica Dati](carica-dati.md) legge dall'ERP fornitore, importo e righe dell'ordine e valorizza le variabili.
4. **BPM scrive l'esito.** Alla fine dell'approvazione, un'operazione [Esegui SQL](esegui-sql.md) aggiorna lo stato dell'ordine nell'ERP, oppure lo fa una chiamata alle API dell'ERP con il connettore [Web Service](connettori/web-service.md).

### Chiamare un servizio esterno quando un'offerta viene approvata

Un processo di approvazione delle offerte deve creare l'opportunità nel CRM (per esempio Salesforce) quando l'offerta viene approvata:

1. Dopo l'attività di approvazione, sul ramo *approvata*, si inserisce un'operazione del connettore [Web Service](connettori/web-service.md), oppure la si aggancia alla conclusione dell'attività.
2. L'operazione chiama l'API del CRM con i dati dell'offerta presi dalle variabili del processo.
3. La risposta del CRM, per esempio l'ID dell'opportunità creata, viene scritta in una variabile e resta nello storico del processo.

Per chiamate che richiedono logica (autenticazione a più passaggi, trasformazione dei dati, più chiamate in sequenza) si usa la variante **Web API [Script]**, che descrive la chiamata con uno script.
