# Connettori

Un **connettore** è un modulo che aggiunge a BPM funzioni pronte all'uso. Un connettore non è un oggetto del Designer: le sue funzioni si usano attraverso tre "porte", ciascuna con il proprio oggetto.

| Tipo di funzione | Si usa tramite | Cosa succede | Esempi |
|---|---|---|---|
| **Operazione** | l'operazione [Connettore attivo](../../modelli-di-processo/elementi/operazioni/index.md#connettore-attivo) | Il motore esegue la funzione quando il flusso la raggiunge, o nel momento del ciclo di vita a cui è agganciata | Web API, SaveAttachmentToFileSystem |
| **Evento** | l'evento di avvio [Start su evento](../../modelli-di-processo/elementi/eventi.md#start-su-evento) | Il motore resta in ascolto e avvia un processo quando si verifica l'evento | IncomingFile, IncomingMail |
| **Azione client** | un pulsante nell'interfaccia di un processo o di un documento | La funzione viene eseguita quando l'utente preme il pulsante | MergePDFs [Client] |

In tutti i casi, nella configurazione dell'oggetto si sceglie il connettore e la funzione; BPM presenta i **parametri** della funzione, da valorizzare con valori fissi o da collegare alle variabili: in **ingresso** per dire alla funzione cosa fare, in **uscita** per scriverne i risultati nelle variabili.

## Configurazione

Percorso: **Configurazione > Connettori**.

Qui si attiva il connettore e, se richiede una configurazione (indirizzi, credenziali, chiavi), si aggiungono le aziende e si compilano i parametri per ciascuna.

## Connettori per l'integrazione

| Connettore | Funzioni |
|---|---|
| [File System](file-system.md) | Evento all'arrivo di un file in una cartella; salvataggio di file, allegati e report su file system |
| [Mail](mail.md) | Evento all'arrivo di una mail; estrazione dei dati da file `.eml` e `.msg` |
| [Web Service](web-service.md) | Chiamata a un'API REST, configurata o descritta da uno script |

Altri connettori riguardano la gestione dei documenti, l'intelligenza artificiale o sistemi specifici, e sono descritti nelle rispettive sezioni.

!!! note "Nomi e descrizioni"
    Nelle tabelle di riferimento dei connettori, i nomi di funzioni e parametri sono quelli usati in BPM. Le descrizioni riportano il testo del connettore, talvolta in inglese.
