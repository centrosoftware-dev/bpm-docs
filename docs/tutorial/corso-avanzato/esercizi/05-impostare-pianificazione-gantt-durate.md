# Tutorial 5 — Impostare la pianificazione/Gantt di un processo con durate standard e scadenza dinamica

Obiettivo: dotare un processo di stime di durata per ogni attività, in modo che all'avvio di ogni istanza venga generato automaticamente un Gantt, con una scadenza agganciata a una variabile data. –

1. Verifica i permessi di processo: sotto Utenti e Gruppi, assicurati che "visualizza pianificazione" (e, se necessario, "modifica pianificazione") siano abilitati per i gruppi che dovranno vedere/gestire il Gantt.
2. Per ciascuna attività del processo, apri la scheda **Pianificazione e Scadenze** e imposta una durata standard in giorni (es. 5, 7, 15, 2 a seconda dell'attività).
3. Se un'attività deve avere un vincolo di scadenza esterno (non derivato dalla durata), sulla stessa scheda seleziona l'opzione per agganciare la **data scadenza** a una variabile data del processo (es. `data_consegna_prevista`), invece di lasciarla come valore fisso o come "N giorni dopo l'inizio".
4. Facoltativo — durata dinamica: se la durata standard deve dipendere da un dato del processo (es. una variabile lista di valori "difficoltà" A/B/C), crea una formula o decision table che calcoli la durata in giorni e agganciala al campo durata dell'attività:

    ```vb
    If difficolta = "A" Then
    Return 5
    Else
    Return 10
    End If
    ```

5. Se un'attività rappresenta lavoro che può restare "disponibile" prima di essere effettivamente iniziato (es. attività di progettazione), abilita il flag **Rileva Inizio** su quell'attività.
6. Se il processo richiede che il proprietario possa aggiustare la pianificazione iniziale di ogni singola istanza prima che diventi baseline definitiva, abilita il flag **Da Confermare** sulle attività pertinenti.
7. Verifica, per le attività il cui ritmo di lavoro non segue la settimana lavorativa standard, se disabilitare il flag "Utilizza Calendario" (per contare giorni solari grezzi invece che giorni di calendario aziendale con weekend/festività).
8. Pubblica il processo.
9. Avvia una nuova istanza: verifica, nella scheda **Pianificazione** del magazzino delle variabili, che il Gantt dell'intero processo sia stato generato automaticamente a partire dalle durate standard.
10. Completa la prima attività e osserva che la sua barra passa da tratteggiata (baseline) a piena (reale), e che tutte le attività a valle si aggiornano di conseguenza nella pianificazione "aggiornata".
11. Se un'attività è marcata "Da Confermare", verifica che al momento della sua attivazione il proprietario possa trascinare/aggiustare le date proposte e poi cliccare **Conferma** (o "conferma tutto") per congelarle come nuova baseline dell'istanza.
