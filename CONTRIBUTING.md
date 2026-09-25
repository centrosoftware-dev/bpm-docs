# Contribuire alla documentazione BPM

## Dove inserire un contenuto

- `docs/modelli-di-processo/` (scheda **Processi**): configurazione dei modelli, Designer di processo, esecuzione (To-Do List, ricerca processi).
- `docs/classi-documentali/` (scheda **Documenti**): classi documentali, metadati, acquisizione e ricerca dei documenti, dossier.
- `docs/integrazione/` (scheda **Integrazione**): Web API, coda delle chiamate, connettori, database, fonti dati esterne, script, acquisizione documenti.
- `docs/intelligenza-artificiale/` (scheda **Intelligenza artificiale**): strumenti di intelligenza artificiale.
- `docs/amministrazione/` (scheda **Amministrazione**): opzioni generali, utenti e gruppi, contatti, allegati, tabelle, altre opzioni e funzioni di sistema.
- `docs/parti-comuni/` (senza scheda in alto): variabili, formule e script, dashboard, report, glossario. Descritti una volta sola e collegati da processi e documenti.
- `docs/tutorial/` (scheda **Inizia**): percorsi di apprendimento; non fanno parte dell'inventario.

Prima di creare una pagina, cerca la voce in `planning/inventory/`. Se manca, aggiungila nell'inventario della macroarea corretta.

## Stati

L'inventario è l'unica fonte dello stato editoriale:

- `da-documentare`: contenuto assente;
- `da-verificare`: contenuto presente ma da controllare sul prodotto corrente;
- `verificato`: contenuto controllato da un esperto.

Lo stato è una traccia per il team, non un processo formale di approvazione. Una modifica del prodotto riporta a `da-verificare` le voci interessate.

## Struttura di una pagina

Per una schermata semplice usa, quando pertinenti: scopo, percorso nell'interfaccia, prerequisiti e autorizzazioni, screenshot generale, comandi, campi, comportamento e vincoli, differenze contestuali e pagine correlate.

Per Designer ed editor complessi separa: panoramica, anatomia, comandi generali, catalogo degli oggetti, proprieta, regole e interazioni, strumenti collegati e guide introduttive.

Descrivi ogni campo o comando con un titolo ricercabile. Crea una pagina autonoma solo quando il comportamento richiede una spiegazione sostanziale.

## Contenuti condivisi

Documenta il funzionamento comune una sola volta sotto `parti-comuni`. Nelle aree specifiche descrivi differenze e vincoli, quindi collega il riferimento comune.

Usa i termini definiti in `CONTEXT.md`. Mantieni nelle pagine i nomi esatti mostrati dall'interfaccia.

## Esempi di codice

Gli esempi (JSON, SQL, script) devono essere brevi: il sito diventerà anche documentazione stampabile in PDF.

- Mostra solo i campi che servono a capire; l'elenco completo va nella tabella dei campi.
- Abbrevia con `…` gli elementi ripetuti, le liste lunghe e i campi secondari.
- Preferisci oggetti su una riga quando sono piccoli.
- Usa dati di fantasia e segnaposto (`<chiave-api>`, `<id-istanza>`), mai dati reali di clienti.
- Gli esempi completi e funzionanti vanno nella collection `api-collection/`, non nelle pagine.

## Connettori: parti generate

Le tabelle di riferimento dei connettori (funzioni e parametri) non si scrivono a mano: le genera `tools/genera-connettori.py` dai manifesti JSON dei connettori, in `snippets/connettori/`. Le pagine le includono con:

```text
--8<-- "snippets/connettori/<connettore>.md"
```

A ogni rilascio che modifica i connettori, rigenera i file:

```console
python tools/genera-connettori.py <cartella-manifesti> snippets/connettori
```

Le descrizioni si correggono nei manifesti, non nei file generati.

## File e immagini

Usa nomi di cartelle e file in minuscolo ASCII, con parole separate da trattini. Conserva gli screenshot sotto `docs/assets/` nell'area corrispondente, ritagliali sulla parte rilevante, usa testo alternativo e non mostrare dati reali o sensibili. Lo screenshot non sostituisce la descrizione testuale.

## Controlli

Esegui:

```console
python tools/check-docs.py
mkdocs build --strict
```

Correggi gli errori prima di considerare completo il contributo.
