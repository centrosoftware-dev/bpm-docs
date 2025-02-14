# Configurazioni Mail

La sezione **_Configurazioni Mail_** apre la pagina di gestione dei profili di posta inseriti.

Cliccando Nuovo o andando a modificare un profilo già esistente si aprirà un popup con tutte le specifiche.

Nella parte superiore della finestra è presente la barra degli strumenti con quattro pulsanti:

* Modifica: Permette di modificare i dettagli della configurazione.
* Salva: Consente di salvare le modifiche apportate.
* Annulla: Annulla le modifiche effettuate.
* Elimina: Elimina la configurazione attualmente selezionata.

## Configurazione Base

Questa sezione consente di configurare le informazioni generali dell'account email.  

I campi e le opzioni disponibili includono:

* Nome, campo di testo che definisce un nome descrittivo per questa configurazione .
* Email, indirizzo email associato all'account.
* Tipo Server, un menu a tendina da cui è selezionabile il tipo di server tra GMAIL, OUTLOOK e CUSTOM.
* Autenticazione, un altro menu a tendina che consente di scegliere il metodo di autenticazione tra USER_PASSWORD, OAUTH2 e NO_AUTHENTICATION.
* Configurazione di default, una casella di spunta per indicare se questa configurazione è quella predefinita.

## Sezione SMTP

Questa sezione è dedicata ai parametri del server SMTP (Simple Mail Transfer Protocol) per l'invio delle email:

* Server SMTP, campo di testo con l'indirizzo del server SMTP.
* SSL, una casella di spunta per abilitare la connessione protetta tramite SSL.
* STARTTLS, una casella di spunta per abilitare STARTTLS.
* Porta SMTP, campo numerico per specificare la porta utilizzata per il server SMTP.

## Sezione IMAP
Questa sezione è dedicata ai parametri del server IMAP (Internet Message Access Protocol) per la ricezione delle email:

* Server IMAP: Campo di testo con l'indirizzo del server IMAP, configurato come "imap.gmail.com".
* SSL: Una casella di spunta per abilitare la connessione protetta tramite SSL (attualmente selezionata).
* STARTTLS: Una casella di spunta per abilitare STARTTLS (attualmente non selezionata).
* Accetta certificati invalidi: Una casella di spunta che consente di accettare certificati non validi (non selezionata).
* Porta IMAP: Campo numerico per specificare la porta utilizzata per il server IMAP. Il valore configurato è "993".

## Sezione Autenticazione
Sul lato destro, una sezione separata permette di configurare le credenziali dell'account in base al tipo di autenticazione scelta.

Nel caso di USER_PASSWORD:

* Utente: Campo di testo che mostra l'indirizzo email dell'utente (lo stesso configurato in "Email").
* Password: Campo mascherato (con asterischi) per inserire la password associata all'account.

Nel caso di OAUTH2:

* TENANT ID
* CLIENT ID
* CLIENT SECRET

## Pulsante Inferiore
Nella parte inferiore della finestra, troviamo il pulsante **_Configura gestione risposte email_**, che permette di scegliere quale cartella, all'interno della mail inserita, utilizzare per la gestione delle risposte.