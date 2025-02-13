# Menù di Configurazione

Il **_Menù di Configurazione_** si trova all'interno del menù principale alla voce **Configurazione**.
All'interno sono presenti le opzioni generali, necessarie per il set-up del BPM, opzioni modelli, per manipolare i modelli e configurarli, una serie di impostazioni in base alla propria necessità durante la creazione di un modello di processo.

## Opzioni generali

Da **_Opzioni generali_** è possibile settare varie impostazioni del BPM.

### Parametri

Dalla sezione **_Parametri_** è possibile configurare l'Engine e gli Automatismi, la configurazione generale, e il logo cliente.

#### Engine/automatismi

In **_Engine/automatismi_** sono presenti la configurazione per l'invio della **_Email riepilogo attività_** e la **_Configurazione Engine_**.

L'**_Email riepilogo attività_**, invia agli utenti l'elenco delle attività da svolgere che hanno in sospeso.  
Il riepilogo può essere inviato quotidianamente, settimanalmente e mensilmente, dove è anche possibile scegliere il giorno della settimana e il giorno del mese in cui verrà inviata la mail, scegliendo l'orario, il periodo di riferimento e decidendo se includere cc e le attività ancora aperte.

Tramite la **_Configurazione Engine_** è possibile modificare alcuni dei funzionamenti endogeni del BPM.  
Tramite 4 checkbox è possibile scegliere:

* Se e quando effettuare la ricostruzione indici, se sì, il giorno e l'ora e se effettuare o meno l'update stats.
* Se salvare o meno la tabella pianificazione.
* Se salvare o meno la tabella pianificazione lato server.
* Attivare esecuzione chiamate API da tabella "ChiamateAPI", scegliendo l'URL API e l'URL Base Link Email.

#### Configurazione

La tab di **_Configurazione_** presenta delle impostazioni generali del funzionamento del BPM.

!!! danger "Locazione obsoleta"
    Questa tab si trova all'interno della sezione parametri per cause di obsolescenza.  
    In futuro potrebbe essere spostata e non trovarsi più qui.

Esse sono:

##### Edit esclusivo istanze

Se spuntato, solo un utente alla volta può modificare un determinato processo o documento.  
La stessa cosa vale per le attività in to-do list.  
L'utente che accede alla task per primo è l'unico che può agire al suo interno.

Una volta salvato il documento o completata l'attività, l'istanza ritorna disponibile.

##### Nega login con stesso utente da più postazioni contemporaneamente

Se spuntato, un utente non può accedere da più postazioni contemporaneamente.

#### Logo Cliente

Nell'ultima tab è possibile impostare il logo del cliente.

### Menu personalizzati

La sezione **_Menù personalizzati_** apre una schermata dedicata alla creazione di Menù.  

#### Barra degli strumenti
La barra superiore degli strumenti contiene una serie di pulsanti che permettono di gestire e configurare i Menù.  

##### Modifica

Consente di modificare un elemento selezionato.
##### Salva

Salva le modifiche apportate.
##### Annulla

Annulla le modifiche non salvate.
##### Nuova Radice

Crea una nuova radice del menù.
##### Nuovo submenù

Aggiunge un sottomenù all'elemento selezionato.
##### Nuovo menù

Crea un nuovo elemento di menù.
##### Elimina

Rimuove l'elemento selezionato.
##### Esporta

Esporta la configurazione del menù.
##### Importa

Importa una configurazione di menù esistente.
##### Stampa

Stampa la configurazione attuale del menù.

#### Sezione di struttura del menù

Il pannello a sinistra mostra la gerarchia ad albero che rappresenta il menù configurato.  
È possibile espandere o contrarre gli elementi per visualizzare i sottomenù associati.

#### Pannello delle impostazioni
Nella parte destra dello schermo si trovano le impostazioni dettagliate per l'elemento di menù selezionato:

##### Modello/tabella

Specifica il modello o tabella associato.
##### Tipo di workflow

Indica il tipo di workflow (in questo caso "NESSUNO").
##### Tipo di menù

Definisce il tipo di menù (ad esempio, "MODELLO").
##### Azione

L'azione associata all'elemento (ad esempio, "NUOVO").
##### Posizione

Indica la posizione dell'elemento nel menù (qui è "0").
##### Configurazione

Specifica ulteriori dettagli di configurazione.
##### Punto di avvio

Può definire un trigger o un punto di inizio.
##### Custom data

 Campi aggiuntivi personalizzati.
##### Radice

Nome della radice a cui appartiene l'elemento (es. "Nuova Radice").
##### Sottomenù

Indica se l'elemento è un sottomenù.
##### Descrizione

Descrizione del menù (es. "Nuovo menù").

##### Variabili

Permette di associare variabili per la configurazione dinamica.

### Contatori

In questa sezione sono elencate le variabili presenti nei processi ed impostate come **_Contatori_**.
Nella tabella sono presenti:

* Ciclovita, ovvero il nome del processo a cui appartiene il contatore.
* Chiave, raggruppamento del contatore.
* Variabile, nome della variabile contatore.
* Contatore, valore del contatore.

Tramite Modifica nella barra degli strumenti è possibile settare il valore del **_Contatore_** a quanto si preferisce.

### Configurazioni Mail

La sezione **_Configurazioni Mail_** apre la pagina di gestione dei profili di posta inseriti.

Cliccando Nuovo o andando a modificare un profilo già esistente si aprirà un popup con tutte le specifiche.

Nella parte superiore della finestra è presente la barra degli strumenti con quattro pulsanti:

* Modifica: Permette di modificare i dettagli della configurazione.
* Salva: Consente di salvare le modifiche apportate.
* Annulla: Annulla le modifiche effettuate.
* Elimina: Elimina la configurazione attualmente selezionata.

#### Configurazione Base

Questa sezione consente di configurare le informazioni generali dell'account email.  

I campi e le opzioni disponibili includono:

* Nome, campo di testo che definisce un nome descrittivo per questa configurazione .
* Email, indirizzo email associato all'account.
* Tipo Server, un menu a tendina da cui è selezionabile il tipo di server tra GMAIL, OUTLOOK e CUSTOM.
* Autenticazione, un altro menu a tendina che consente di scegliere il metodo di autenticazione tra USER_PASSWORD, OAUTH2 e NO_AUTHENTICATION.
* Configurazione di default, una casella di spunta per indicare se questa configurazione è quella predefinita.

#### Sezione SMTP

Questa sezione è dedicata ai parametri del server SMTP (Simple Mail Transfer Protocol) per l'invio delle email:

* Server SMTP, campo di testo con l'indirizzo del server SMTP.
* SSL, una casella di spunta per abilitare la connessione protetta tramite SSL.
* STARTTLS, una casella di spunta per abilitare STARTTLS.
* Porta SMTP, campo numerico per specificare la porta utilizzata per il server SMTP.

#### Sezione IMAP
Questa sezione è dedicata ai parametri del server IMAP (Internet Message Access Protocol) per la ricezione delle email:

* Server IMAP: Campo di testo con l'indirizzo del server IMAP, configurato come "imap.gmail.com".
* SSL: Una casella di spunta per abilitare la connessione protetta tramite SSL (attualmente selezionata).
* STARTTLS: Una casella di spunta per abilitare STARTTLS (attualmente non selezionata).
* Accetta certificati invalidi: Una casella di spunta che consente di accettare certificati non validi (non selezionata).
* Porta IMAP: Campo numerico per specificare la porta utilizzata per il server IMAP. Il valore configurato è "993".

#### Sezione Autenticazione
Sul lato destro, una sezione separata permette di configurare le credenziali dell'account in base al tipo di autenticazione scelta.

Nel caso di USER_PASSWORD:

* Utente: Campo di testo che mostra l'indirizzo email dell'utente (lo stesso configurato in "Email").
* Password: Campo mascherato (con asterischi) per inserire la password associata all'account.

Nel caso di OAUTH2:

* TENANT ID
* CLIENT ID
* CLIENT SECRET

#### Pulsante Inferiore
Nella parte inferiore della finestra, troviamo il pulsante **_Configura gestione risposte email_**, che permette di scegliere quale cartella, all'interno della mail inserita, utilizzare per la gestione delle risposte.

### Processi con avvio ricorrente

La sezione **_Processi con avvio ricorrente_** elenca tutti i processi che hanno come inizio uno Start a tempo.

Nella tabella sono presenti:

* Nome del modello.
* Descrizione del timer.
* Stato del modello, attivo o non attivo.

### Aggiornamento massivo processi

**_Aggiornamento massivo processi_** consente di aggiornare in massa i processi di un modello.

Sarà richiesto all'utente di decidere se mantenere l'avanzamento del processo, *dove possibile*, oppure azzerarli tutti e ripartire dallo start.  
Inoltre è necessario scegliere se non variare le cartelle allegati o aggiornare la struttura allegati in sola aggiunta. 

Dopo aver scelto, si aprirà una tab analoga a quella della ricerca processi.  
Da qui è possibile filtrare tutti i processi di quel modello e, dopo aver spuntato quelli scelti, è possibile cliccare su aggiorna ultima versione.  

Dopo qualche istante i processi selezionati saranno aggiornati all'ultima versione del modello.

### Attiva/Disattiva processi

Cliccando su **_Attiva/Disattiva processi_** si aprirà un popup che elenca tutti i processi.

Facendo doppio click su un processo, esso verrà attivato/disattivato.

### Visualizza storico generale

**_Visualizza storico generale_** apre la pagina del **Log operazione** ovvero tutte le azioni svolte dall'utente all'interno del BPM.

Nella tabella dei log sono presenti: Nome del modello, Data del log, Utente da cui è stata loggata l'azione, Nome del processo, Descrizione del Processo, Evento e Oggetto evento.

Gli Eventi possono essere:

* Aggiornamento processo da modello
* Creazione processo
* Eliminazione processo
* Esecuzione task
* Modifica ai dati di processo
* Modifica dati task
* Visualizzazione allegato
* Visualizzazione task

Nome e descrizione del processo vengono loggati solo quando l'evento ha come soggetto un processo.  
Oggetto evento quando l'evento parte appunto da un oggetto, come una task, un attributo o un elemento.

La tabella è filtrabile in alto per: Data da/a, Tipologia, Modello, Utente.  

Inoltre, se si dovesse scegliere **Visualizza dettaglio modifiche** appariranno nella tabella altre 7 colonne: Azione, Descrizione oggetto, Variabile, Valore Precedente, Valore nuovo, Gruppo e Riga.

Tramite il bottone esporta si aprirà un nuovo file excel con i dati dei log al suo interno.