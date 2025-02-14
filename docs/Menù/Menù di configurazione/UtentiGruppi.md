# Utenti e Gruppi

Dalla sezione **_Utenti e Gruppi_** è possibile gestire gli utenti e i gruppi.

## Nuovo utente

Cliccando su **Nuovo utente**, verrà aperta una nuova pagina dove inserire le seguenti informazioni necessarie:

* Nome e iniziali
* Descrizione
* Lingua

Tramite il bottone **Imposta password utente** è possibile impostare la password del profilo che si sta creando.  
Il checkbox *Utilizza password policy*, se spuntato, farà sì che le policy impostate nei parametri di gestione del BPM, documentate [qui](Parametri.md#utilizza-password-policies-su-nuovi-utenti), verranno attuate.

Se si sta modificando un profilo, il pulsante **Azzera password utente** reimposta la password dell'utente selezionato con una temporanea. L'utente riceverà un'email con la nuova password, che potrà sostituire al prossimo accesso.

Spuntando il checkbox **È un gruppo**, il profilo creato sarà un gruppo invece che un utente.

Cliccando il bottone **Visualizza storico** verranno mostrati tutti i log delle azioni relative agli utenti e gruppi.  
Collassando ogni riga, è possibile visualizzare tutti i dettagli interno, di cui:

* Info modificate
* Permessi aggiunti/rimossi
* Gruppi aggiunti/rimossi
* Filtri aggiunti/rimossi

Cliccando il bottone **Copia autorizzazioni da** tramite il popup specifico, si potranno importare le autorizzazioni di un account a quello che si sta creando.

## Lista utenti

Dalla lista utenti, tramite la barra degli strumenti, è possibile creare, eliminare, esportare o importare profili, come descritto nella sezione precedente. 

Facendo doppio clic su un profilo nella tabella principale, si accede alle sue informazioni avanzate. 

Il popup visualizzato è simile a quello per la creazione di un profilo, con i dati iniziali nella parte superiore e 11 tab centrali che contengono tutte le informazioni avanzate.

Le 11 tab sono:

| **Tab**                    | **Descrizione**                                                                                      |
|----------------------------|------------------------------------------------------------------------------------------------------|
| **Dati**                   | Contiene le informazioni anagrafiche e di configurazione dell’utente o gruppo (es. email, recapiti, firma email). |
| **Gruppo**                 | Gestisce l’appartenenza a gruppi o ruoli, utile per organizzare gli utenti in categorie con permessi specifici. |
| **Permessi menù**          | Definisce quali voci di menù l’utente o il gruppo può visualizzare e utilizzare.                     |
| **Permessi processi**      | Specifica i processi o workflow ai quali l’utente o il gruppo può accedere e con quali diritti.      |
| **Permessi Classi Documentali** | Stabilisce le classi di documenti a cui l’utente o il gruppo può accedere e in che modo.                 |
| **Permessi tabelle**       | Determina quali tabelle di dati l’utente o il gruppo può consultare o modificare.                    |
| **Permessi dashboard**     | Regola l’accesso e le autorizzazioni alle dashboard o report visuali.                               |
| **Permessi reports**       | Controlla quali report l’utente o il gruppo può generare o visualizzare.                            |
| **Permessi Dossier**       | Imposta le autorizzazioni di consultazione o modifica sui dossier, ossia raccolte di documenti o pratiche. |
| **Prefiltri**              | Permette di definire e applicare filtri preconfigurati ai dati, facilitando la ricerca e la consultazione. |
| **Aliases**                | Gestisce eventuali alias o nomi alternativi associati all’utente o al gruppo, ad esempio indirizzi email aggiuntivi. |


### Dati

* Utente non attivo: Casella da selezionare per disattivare l’utente.
* Non avviare con home page: Se spuntata la home page non verrà caricata all'avvio.
* Utente amministratore: Casella selezionata per indicare che l'utente ha privilegi amministrativi.  
#
* Carica Firma: Permette di caricare una firma personalizzata per l'utente.
* Impostazioni notifiche utente: Pulsante che apre la configurazione specifica per gestire le notifiche assegnate all'utente.  
Questo popup consente di configurare in modo dettagliato le notifiche relative alle attività, stabilendo sia come che quando l’utente riceve avvisi via email o all’interno del sistema. Di seguito una panoramica dei principali elementi:

1. Invio riepilogo attività via email

    Casella di spunta per abilitare l’invio di un riepilogo (ad esempio giornaliero o periodico) delle attività via email.

2. Modalità Notifiche

    Opzione per selezionare il canale di notifica (in questo caso “Via email”).

3. Notifiche Scatenate Immediatamente da Azioni

    * Notifica nuova attività (assegnata, delegata): Attiva un avviso non appena viene assegnata o delegata una nuova attività.
    * Notifica spostamento attività: Invia un avviso quando la data di un’attività viene modificata.
    * Notifica cambio data scadenza attività: Avvisa in caso di variazione della data di scadenza di un’attività.

4. Per attività che riguardano

    * Selezioni multiple (checkbox) per definire su quali attività ricevere notifiche, ad esempio:
        * Me (l’utente stesso)
        * Me in CC
        * Il mio gruppo
        * Il mio gruppo in CC
        * Il gruppo che amministro
        * Il gruppo che amministro in CC
5. Notifica X giorni prima della data inizio/scadenza attività
    
    Permette di impostare quanti giorni prima dell’inizio o della scadenza di un’attività deve essere inviata la notifica.

6. Silenzia Notifiche su Processi di Tipo

    Sezione per escludere alcuni tipi di processi (o workflow) dall’invio delle notifiche, riducendo il numero di avvisi non rilevanti.

7. Salva e esci

    Pulsante per confermare le impostazioni e chiudere la finestra di configurazione.
