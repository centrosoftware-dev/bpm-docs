# Visualizza storico generale

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