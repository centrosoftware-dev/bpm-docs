# Attributi di una variabile
Nel Pannello Attributi sulla destra sono elencati tutti gli **_Attributi di una variabile_** suddivisi in 3 sezioni.

## Impostazioni base

### Nome variabile

Il **_Nome della variabile_** è il nome tecnico con cui ci si riferisce alla variabile.  
Esso Non può essere modificato dopo l'inizializzazione.

### Descrizione

La Descrizione di una variabile definisce la label che appare nel canvas.  
Serve ad un utente per capire che genere di dato inserire in un input.

### Descrizione su interrogazioni

Utilizzando la ricerca processi, la **_Descrizione su interrogazioni_** è l'attributo che viene ricercato e mostrato in caso combaciasse coi filtri di ricerca.

!!! note
    Si consiglia di impostare la **_Descrizione su interrogazioni_** in modo che sia più accurata e specifica rispetto alla Descrizione normale, in quanto la **_Descrizione su interrogazioni_** viene letta in una pagina dove l'utente non vede il flusso disegnato.

### Gruppo
Definisce il gruppo logico o categoria a cui appartiene la variabile.

### Obbligatoria
Booleano (True/False) che indica se il valore della variabile è obbligatorio.

### Readonly
Booleano (True/False) che determina se la variabile è di sola lettura.

### Senza salvataggio
Specifica se la variabile non deve essere salvata nei dati.

### Sezione/sottocategoria
Permette di organizzare la variabile in una sezione o sottocategoria.

### Tabella di origine
Indica se la variabile deriva da una tabella di dati specifica.

### Tipo impostazioni di base
Indica il tipo di impostazioni predefinite (ad esempio, Testo).

### Tipo variabile
Determina il tipo specifico della variabile (es. StringType, NumericType, ecc.).
Ogni **_Tipo variabile_** viene approfondito nella sezione Tipo di variabili [qui](#tipi-di-variabili).

## Altre impostazioni
### Attività collegate
Indica se ci sono attività o azioni associate alla variabile.

### Autocomplete
Booleano che definisce se il campo deve supportare il completamento automatico.

### Campo chiave
Specifica se la variabile rappresenta un campo chiave.

### Formula
Formula personalizzata per calcolare il valore della variabile.

### Formula di validazione
Formula per convalidare il valore della variabile.

### Formula formattazione
Formula per definire il formato del valore della variabile.

### Formula default
Formula per impostare il valore predefinito della variabile.

### Formula per visibilità
Specifica una condizione per mostrare o nascondere la variabile.

### Formula readonly
Formula che determina se la variabile è di sola lettura.

### Help text
Testo di aiuto visualizzato all'utente per spiegare l'uso della variabile.

### Imposta variabili
Opzione per configurare o modificare dinamicamente altre variabili in base al valore corrente.

### Valore di default
Il valore iniziale o predefinito della variabile.

### Variabile di intestazione
Booleano che indica se la variabile è utilizzata come intestazione.

### Formula intestazione (p.)
Permette di definire una formula per le intestazioni.

### Variabili da richiedere
Numero o elenco di variabili che devono essere richieste quando questa è utilizzata.

## Altro

### Dimensione carattere
Lo stile o dimensione del carattere associato.

### Location
Coordinate X, Y che indicano la posizione dell'elemento.

### Nascosta su mobile device
Indica se la variabile è nascosta sui dispositivi mobili.

### Pagina/categoria
La pagina o categoria a cui appartiene la variabile.

### TAG
Tag o etichette per identificare ulteriormente la variabile.

## Tipi di variabili

### StringType
Una variabile di tipo testo semplice.

### NumericType
Una variabile numerica (interi o decimali).

### BooleanType
Una variabile booleana (valori True/False).

### DataType
Una variabile per rappresentare una data (senza ora).

### CurrencyType
Una variabile per valori monetari.

### MemoType
Una variabile per testi lunghi, simile a un campo memo.

### ValueListType
Una variabile che offre una lista di valori selezionabili.

### UserType
Una variabile che rappresenta un utente (es. ID o nome utente).

### LABEL
Una variabile di tipo etichetta (non modificabile, solo visualizzazione).

### DateTimeType
Una variabile per rappresentare una data e un'ora.

### SignType
Una variabile per firme (es. digitali o grafiche).

### LINK
Una variabile per memorizzare o gestire collegamenti ipertestuali.

### DataGrid
Una variabile che rappresenta una griglia o tabella di dati.
