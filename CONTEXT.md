# BPM Documentation

The documentation context for the BPM product and the people who configure,
operate, support, and deliver it to customers.

## People

**Process designer**:
A user who configures workflow models and document archives in BPM.
_Avoid_: Administrator

**Delivery consultant**:
A company employee who delivers BPM to a customer, including its integration work.
_Avoid_: Integration engineer

**Business partner**:
An external reseller that also provides BPM consultancy and delivery services. Business partners are the primary external audience for product documentation.
_Avoid_: Delivery consultant

**Customer**:
An organization that uses BPM. Its process designers and instance administrators may configure its BPM instance.
_Avoid_: Client

**Instance administrator**:
A user who manages a running customer BPM instance, including users and permissions.
_Avoid_: Process designer

**End user**:
A person who interacts with BPM, including process designers, instance administrators, and process actors.

**Attore del processo**:
An end user who performs tasks in an active process.
_Avoid_: Partecipante al processo

## Configurazione

**Modello di processo**:
La configurazione di un flusso eseguibile, comprendente attività, variabili, assegnazioni, autorizzazioni, regole, integrazioni e rappresentazione grafica. Dall'esecuzione di un modello nasce un'istanza di processo.
_Avoid_: Processo

**Classe documentale**:
La configurazione di un tipo di documento, comprendente variabili, azioni, autorizzazioni e interazioni con i processi.

**Istanza di processo**:
Una singola esecuzione di un modello di processo.
_Avoid_: Modello di processo

**Connettore**:
Un componente tecnico che mette a disposizione integrazioni con sistemi esterni oppure funzioni di utilità interne. Non tutti i connettori realizzano un'integrazione.
_Avoid_: Integrazione

**Designer di processo**:
L'ambiente di progettazione nel quale si configura un modello di processo.
_Avoid_: Canvas

**Canvas**:
La superficie del Designer sulla quale si dispongono e si collegano graficamente gli oggetti.
_Avoid_: Designer di processo

**Editor delle variabili**:
Lo strumento condiviso con cui si definiscono e si organizzano le variabili usate nelle configurazioni BPM.

**Designer di classe documentale**:
L'ambiente di progettazione nel quale si configura una classe documentale. Ha la stessa struttura del Designer di processo, con differenze legate allo scopo e alle regole delle classi documentali.

**Formula / script**:
Codice VB.NET inserito tramite un editor condiviso e valutato con il ruolo previsto dal punto di configurazione, per esempio calcolo, inizializzazione o validazione. Nell'interfaccia e normalmente nel manuale è chiamato formula; script è naturale per logiche procedurali piu articolate. Le variabili BPM sono citate con la sintassi `@[nome_variabile]`.

**Operazione**:
Attività automatica di un processo, eseguita dal motore. Si inserisce nel flusso oppure si aggancia a un momento del ciclo di vita di un altro oggetto. Tipi: Decision Table, Imposta variabili, Invia email, Aggiorna altro processo, Carica dati, Esegui sql, Connettore attivo.
_Avoid_: Azione, Task automatico

**Connettore attivo**:
L'operazione che esegue una funzione di tipo operazione di un connettore. È l'unica porta d'ingresso alle operazioni dei connettori.
_Avoid_: Connettore azione

**Start su evento**:
Evento di avvio legato a un connettore: il motore resta in ascolto e avvia il processo quando si verifica l'evento del connettore (per esempio IncomingMail, IncomingFile).

**Funzione di un connettore**:
Ciò che un connettore espone: operazione (usata tramite Connettore attivo), evento (tramite Start su evento) o azione client (tramite un pulsante nell'interfaccia).
_Avoid_: Interfaccia (termine del manifesto, non dell'interfaccia utente)

