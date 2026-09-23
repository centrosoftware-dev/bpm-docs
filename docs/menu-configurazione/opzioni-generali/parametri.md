# Parametri

Dalla sezione **_Parametri_** è possibile configurare l'Engine e gli Automatismi, la configurazione generale, e il logo cliente.

## Engine/automatismi

In **_Engine/automatismi_** sono presenti la configurazione per l'invio della **_Email riepilogo attività_** e la **_Configurazione Engine_**.

L'**_Email riepilogo attività_**, invia agli utenti l'elenco delle attività da svolgere che hanno in sospeso.  
Il riepilogo può essere inviato quotidianamente, settimanalmente e mensilmente, dove è anche possibile scegliere il giorno della settimana e il giorno del mese in cui verrà inviata la mail, scegliendo l'orario, il periodo di riferimento e decidendo se includere cc e le attività ancora aperte.

Tramite la **_Configurazione Engine_** è possibile modificare alcuni dei funzionamenti endogeni del BPM.  
Tramite 4 checkbox è possibile scegliere:

* Se e quando effettuare la ricostruzione indici, se sì, il giorno e l'ora e se effettuare o meno l'update stats.
* Se salvare o meno la tabella pianificazione.
* Se salvare o meno la tabella pianificazione lato server.
* Attivare esecuzione chiamate API da tabella "ChiamateAPI", scegliendo l'URL API e l'URL Base Link Email.

## Configurazione

La tab di **_Configurazione_** presenta delle impostazioni generali del funzionamento del BPM.

### Edit esclusivo istanze

Se spuntato, solo un utente alla volta può modificare un determinato processo o documento.  
La stessa cosa vale per le attività in to-do list.  
L'utente che accede alla task per primo è l'unico che può agire al suo interno.

Una volta salvato il documento o completata l'attività, l'istanza ritorna disponibile.

### Nega login con stesso utente da più postazioni contemporaneamente

Se spuntato, un utente non può accedere da più postazioni contemporaneamente.

### Utilizza password policies su nuovi utenti

L'utilizzo delle **_Password policies_** fa sì che i nuovi utenti debbano cambiare la password dopo il numero di giorni impostato.   

!!! danger "Locazione obsoleta"
    La tab di **_Configurazione_** si trova all'interno della sezione parametri per cause di obsolescenza.  
    In futuro potrebbe essere spostata e non trovarsi più qui.

## Logo Cliente

Nell'ultima tab è possibile impostare il logo del cliente.
