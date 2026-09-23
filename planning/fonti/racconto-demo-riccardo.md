# Racconto della demo di BPM (Riccardo, 23/9/2026)

Fonte grezza per la homepage e per i "Primi passi". Trascritto così come raccontato.

## Presentazione

BPM (Business Process Modeler) è un'applicazione che serve a gestire processi, documenti, e tutto integrato con AI.

Due tipologie di entità:

- modelli di processo: sono i flussi di lavoro, iniziano e finiscono;
- classi documentali: rappresentano eventuali documenti.

BPM è nato principalmente come gestore di processi, super forte, immediato e produttivo. Ma siccome non esistono processi senza documenti (e i documenti hanno bisogno di processi di gestione), sono implementate anche le classi documentali. I documenti possono vivere anche senza i processi, ma in generale i processi raccolgono, generano, modificano e approvano documenti, e i documenti vengono distribuiti, gestiti ecc. Tutto è flessibile e configurabile.

La parte principale è il Designer: qui si formalizzano i flussi di lavoro. Con BPM si creano applicazioni per gestire i "figli di nessuno": cose che richiedono la collaborazione di più persone e reparti, ma i cui strumenti sono mail, fogli Excel condivisi, "ultima versione (1)(1).doc". BPM cattura questi flussi destrutturati e li struttura in un sistema che ti ricorda cosa devi fare, permette ricerche, dà allarmi e soprattutto certifica con i suoi storici che i flussi sono stati eseguiti secondo le regole aziendali. Human workflow + automation.

La parte documentale completa il quadro: i documenti possono essere il risultato di un flusso oppure derivare dal gestionale (documenti transazionali: bolle, fatture…). Per BPM tutto è processo: anche l'acquisizione automatica dei documenti (senza AI, con l'AI, con accesso al DB) si fa con un piccolo processo senza attività umane.

BPM non vive mai da solo. Il minimo sindacale sono le anagrafiche lette, ma ci sono tutti gli strumenti per integrazioni profonde con ERP, CRM ecc., in lettura e in scrittura.

## Demo processi

- processo di esempio, qualche attività, le variabili;
- accesso ai dati esterni, possibilità di integrazione;
- il processo che gira: si avvia, la To-Do List si muove, il "token" va avanti;
- le variabili si compilano: campi tabellati (record dell'ERP), numerici, date; campi obbligatori, validazione;
- la pianificazione: l'asse dei tempi è importante;
- mail di avvertimento, ritardi, escalation;
- connettori per leggere e scrivere database, web service, AI;
- linguaggio di scripting basato su Visual Basic per logiche più complesse.

## Demo documenti

- esistono le classi documentali: concettualmente diverse dai processi ma strutturalmente condividono molto (le variabili sono le stesse, con la stessa potenza, per creare i metadati);
- come entrano i documenti: a mano (drag and drop dall'applicazione web); acquisizione automatica dall'ERP (un processo che legge i documenti da eventi); da cartelle, da mail, con l'AI; da modelli Word/Excel o generati dal motore di reportistica;
- nei processi ci sono gli oggetti per archiviare un documento, aprirlo, leggerlo, modificarne il contenuto, estrarre il testo, usare l'AI per estrarre metadati o campi;
- novità in sviluppo: chatbot di ricerca nei documenti (non ancora da presentare come disponibile);
- documentale concettualmente separato ma integratissimo con i processi: condividono variabili, strumenti e connettori.

La parte operativa web è responsive. Ci sono API REST con cui si può fare tutto.

## Indicazioni editoriali

- Non citare troppo il client desktop: sta andando a terminare. Oggi il Designer è solo client e la parte operativa è web; nel giro di qualche mese anche il disegno sarà web e modernizzato. Non dire che c'è già, ma non insistere sul desktop.

## Esempi dimostrativi da preparare

1. Approvazione ferie (semplice, anche come tutorial).
2. Classe documentale transazionale (da gestionale).
3. Due esempi con AI: lettura mail; comprensione di un documento con integrazione ERP.
