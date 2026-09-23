# Contribuire alla documentazione BPM

## Dove inserire un contenuto

- `docs/modelli-di-processo/`: configurazione dei modelli e del Designer di processo.
- `docs/classi-documentali/`: configurazione delle classi documentali e delle loro regole specifiche.
- `docs/strumenti-condivisi/`: strumenti descritti una volta sola e collegati dai contesti che li usano.
- `docs/menu-configurazione/`: riferimento aderente alle sezioni del menu Configurazione.
- `docs/sistema/`: gestione e monitoraggio tecnico.

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

Documenta il funzionamento comune una sola volta sotto `strumenti-condivisi`. Nelle aree specifiche descrivi differenze e vincoli, quindi collega il riferimento comune.

Usa i termini definiti in `CONTEXT.md`. Mantieni nelle pagine i nomi esatti mostrati dall'interfaccia.

## File e immagini

Usa nomi di cartelle e file in minuscolo ASCII, con parole separate da trattini. Conserva gli screenshot sotto `docs/assets/` nell'area corrispondente, ritagliali sulla parte rilevante, usa testo alternativo e non mostrare dati reali o sensibili. Lo screenshot non sostituisce la descrizione testuale.

## Controlli

Esegui:

```console
python tools/check-docs.py
mkdocs build --strict
```

Correggi gli errori prima di considerare completo il contributo.
