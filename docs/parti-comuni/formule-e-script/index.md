# Formule e script

In BPM una formula è codice VB.NET valutato con il ruolo previsto dal punto di configurazione. Il termine **script** è usato naturalmente per le logiche procedurali più articolate, ma il meccanismo e l'editor sono gli stessi.

Le variabili BPM si richiamano con la sintassi `@[nome_variabile]`.

## Editor

L'editor mette a disposizione funzioni contestuali tramite il menu del tasto destro, facilita la navigazione nelle strutture di variabili e compila immediatamente il codice per evidenziare gli errori.

## Ruolo della formula

Ogni punto di configurazione assegna alla formula una semantica precisa. Una formula può, per esempio, calcolare un valore, inizializzare dati, validare un valore restituendo `True` o `False`, oppure impostare più variabili.

Il catalogo completo dei ruoli verrà costruito usando lo studio dettagliato dei modelli reali. Ogni pagina di configurazione deve descrivere il momento di valutazione, i dati disponibili e il risultato atteso, collegandosi a questo riferimento per la sintassi comune.
