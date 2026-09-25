# Integrazione

BPM non lavora mai da solo. Nella quasi totalità delle installazioni legge almeno le anagrafiche dal gestionale, e spesso scambia dati in entrambe le direzioni con ERP, CRM, sistemi di produzione e servizi web.

Questa sezione risponde alle domande di chi deve collegare BPM ai sistemi dell'azienda: *come leggo i dati del mio ERP? come ci scrivo? come avvio un processo quando nel gestionale succede qualcosa? come chiamo un servizio esterno quando un'attività viene approvata?*

## Le modalità di integrazione

| Esigenza | Strumento |
|---|---|
| Proporre nei campi i dati del gestionale (clienti, fornitori, articoli…) | [Dati esterni nelle variabili](dati-esterni.md) |
| Leggere dati esterni durante il processo e copiarli nelle variabili | [Carica Dati](carica-dati.md) |
| Scrivere sul database di un altro sistema, o eseguire query e stored procedure | [Esegui SQL](esegui-sql.md) |
| Chiamare un servizio web (REST) di un altro sistema | [Web Service](connettori/web-service.md) |
| Avviare un processo quando arriva un file in una cartella o una mail | [File System](connettori/file-system.md), [Mail](connettori/mail.md) |
| Salvare allegati e documenti su file system | [File System](connettori/file-system.md) |
| Far pilotare BPM da un'applicazione esterna | [API standard](api-standard/index.md) |
| Far avviare o avanzare processi da un sistema che lavora solo sul database | [Coda delle chiamate](coda-chiamate.md) |

Tutte le modalità che accedono a un database usano le [connessioni esterne](connessioni-esterne.md), configurate una volta sola.

## Gli strumenti: operazioni, eventi e connettori

Nel Designer, l'integrazione passa da due famiglie di oggetti.

<div class="grid" markdown>

![Operazioni](../assets/modelli-di-processo/designer/palette-operazioni.png){ width=200 }

![Eventi](../assets/modelli-di-processo/designer/palette-eventi.png){ width=160 }

</div>

Le **[operazioni](../modelli-di-processo/elementi/operazioni/index.md)** sono le attività automatiche del processo: si inseriscono nel flusso oppure si agganciano a un momento del ciclo di vita di un'attività. Alcune servono alla logica del processo (Decision Table, Imposta variabili, Invia email, Aggiorna altro processo); per l'integrazione contano soprattutto:

- **Carica dati** ed **Esegui sql**, operazioni native per leggere e scrivere su database;
- **Connettore attivo**, che esegue una funzione di un connettore: chiamare un servizio web, salvare un file, e molto altro.

Gli **[eventi](../modelli-di-processo/elementi/eventi.md)** avviano, sospendono o concludono il flusso. Per l'integrazione conta **Start su evento**: il processo non viene avviato da un utente o da un'applicazione, ma dal motore di BPM stesso, in ascolto, quando si verifica l'evento di un connettore (l'arrivo di un file, di una mail).

I **[connettori](connettori/index.md)** sono i moduli che forniscono queste funzioni: le loro operazioni si usano tramite Connettore attivo, i loro eventi tramite Start su evento.

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
