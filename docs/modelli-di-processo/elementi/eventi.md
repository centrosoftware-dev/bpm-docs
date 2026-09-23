# Eventi

Gli eventi rappresentano punti di avvio, attesa o conclusione del flusso. Gli eventi che avviano un modello possono richiedere variabili, allegati e operazioni secondo la propria configurazione.

## Start

**Start** e il punto di inizio di un flusso avviato manualmente. Un modello puo contenere piu Start; in questo caso, all'avvio viene richiesto quale utilizzare.

Lo Start puo configurare variabili e allegati da richiedere, utenti e responsabili, e operazioni eseguite durante o al termine dell'esecuzione.

## Start su evento

**Start su evento** avvia un'istanza di processo quando riceve un evento esterno definito da un connettore. I connettori disponibili sono configurati nel [Menu Configurazione](../../menu-configurazione/connettori/index.md).

## Start a tempo

**Start a tempo** avvia periodicamente un'istanza di processo. La configurazione definisce descrizione, frequenza giornaliera, settimanale o mensile e orario di avvio.

## Attesa

**Attesa** sospende l'avanzamento fino al momento configurato. È possibile indicare un numero di giorni, un giorno della settimana o del mese e un orario.

## Fine e Termina processo

**Fine** conclude il percorso corrente. **Termina processo** conclude anche gli altri rami paralleli e i sottoprocessi ancora attivi.

Le singole configurazioni degli eventi devono essere completate e verificate sul prodotto corrente.
