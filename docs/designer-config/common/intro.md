# Parti comuni

La sezione **_Parti comuni_** del BPM raccoglie tutti gli **elementi e le impostazioni condivise** tra le diverse aree del sistema, come processi, classi documentali e variabili.  
Qui vengono configurati componenti trasversali che possono essere **riutilizzati in più modelli**, consentendo una gestione centralizzata, coerente e semplificata delle risorse del BPM.

L’obiettivo principale di questa sezione è quello di ridurre le duplicazioni, migliorare la coerenza dei dati e fornire un punto unico di configurazione per elementi comuni a più processi o moduli.

![IMG1]  
_Descrizione immagine: schermata iniziale della sezione “Parti comuni” con l’elenco dei moduli e componenti configurabili._

## Scopo della sezione

La sezione **_Parti comuni_** è pensata per amministratori e configuratori che devono mantenere **uniformità e standardizzazione** all’interno della piattaforma BPM.  
Da qui è possibile:
- Definire regole e parametri generali condivisi  
- Configurare componenti riutilizzabili in diversi modelli di processo  
- Gestire template, dizionari e impostazioni di sistema comuni  
- Centralizzare la manutenzione delle risorse per semplificare gli aggiornamenti  

![IMG2]  
_Descrizione immagine: esempio di elenco parametri comuni e opzioni globali configurabili nel sistema._

## Componenti principali

Le **Parti comuni** possono includere diversi tipi di elementi, a seconda della configurazione del BPM.  
Tra i più utilizzati troviamo:

1. **Parametri generali**  
   Impostazioni che influenzano il comportamento dell’intero sistema o di più processi (es. formati data, percorsi di archiviazione, regole di sicurezza, ecc.).

2. **Template condivisi**  
   Modelli predefiniti di documenti, email o notifiche che possono essere riutilizzati in più processi per garantire coerenza comunicativa e grafica.

3. **Dizionari e liste di valori**  
   Elenchi di valori standard (dropdown, categorie, stati, ecc.) gestiti centralmente e richiamabili da vari processi o classi documentali.

4. **Script e funzioni comuni**  
   Blocchi di codice o logiche riutilizzabili che possono essere richiamati da più modelli di processo, evitando di doverli riscrivere più volte.

5. **Regole di visibilità e permessi comuni**  
   Configurazioni condivise che regolano l’accesso e la visualizzazione di dati o componenti del sistema per gruppi di utenti.

![IMG3]  
_Descrizione immagine: schermata che mostra una lista di template e dizionari configurabili nella sezione Parti comuni._

## Vantaggi dell’utilizzo delle Parti comuni

L’utilizzo delle **Parti comuni** offre numerosi benefici nella gestione dei progetti BPM:

- **Uniformità**: garantisce che tutti i processi seguano le stesse regole e impostazioni di base.  
- **Efficienza**: evita di dover ricreare da zero componenti già esistenti.  
- **Manutenibilità**: centralizza gli aggiornamenti, riducendo errori e tempi di intervento.  
- **Scalabilità**: semplifica la creazione di nuovi processi che possono subito riutilizzare elementi già configurati.  

![IMG4]  
_Descrizione immagine: diagramma o schema che rappresenta come le parti comuni vengono condivise tra più processi BPM._

## Esempi di applicazione

Alcuni esempi pratici di utilizzo delle Parti comuni includono:
- Un **template di email** condiviso per tutte le notifiche di avanzamento processo  
- Una **lista di stati standard** utilizzata in più modelli di processo (es. “In corso”, “Completato”, “Annullato”)  
- Una **funzione di calcolo o controllo** utilizzata in diverse attività automatiche  
- Un **parametro globale di configurazione** per definire limiti o soglie comuni a tutti i flussi  

![IMG5]  
_Descrizione immagine: esempio di schermata che mostra un template di notifica riutilizzato in più processi._

## Buone pratiche

Per sfruttare al meglio le potenzialità della sezione **_Parti comuni_**, si consiglia di:
- Centralizzare tutti gli elementi ricorrenti (template, regole, script, parametri, ecc.)  
- Documentare accuratamente ogni componente comune per facilitarne il riutilizzo  
- Utilizzare convenzioni di naming coerenti (es. prefissi “COMMON_” o “SHARED_”)  
- Aggiornare regolarmente i componenti condivisi per garantire l’allineamento con le modifiche dei processi  

![IMG6]  
_Descrizione immagine: schermata di esempio che mostra l’organizzazione dei componenti comuni con naming coerente e descrizioni._

## Approfondimenti

Nei capitoli successivi verranno trattati nel dettaglio i principali elementi che compongono le **Parti comuni**, con esempi pratici e casi d’uso, tra cui:
- Configurazione dei parametri globali  
- Creazione e gestione di template condivisi  
- Implementazione di dizionari e liste di valori  
- Gestione delle regole comuni di sicurezza e visibilità  

??? info "Suggerimento"
    Le **Parti comuni** sono la base per un ambiente BPM scalabile e coerente.  
    Prima di creare nuovi elementi all’interno dei processi, verifica sempre se esiste già un componente condiviso riutilizzabile.  
    In questo modo potrai ridurre i tempi di sviluppo e mantenere una maggiore uniformità all’interno del sistema.
