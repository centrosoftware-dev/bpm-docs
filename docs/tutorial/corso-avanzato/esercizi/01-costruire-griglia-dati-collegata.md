# Tutorial 1 — Costruire una griglia dati collegata a una tabella fornitori

Obiettivo: aggiungere alla form di un processo una griglia in sola lettura che mostri i dati anagrafici dei fornitori, consultabile senza uscire dal processo. –

1. Nel magazzino delle variabili, crea una nuova variabile e imposta il suo tipo su **Griglia Dati**.
2. Apri la configurazione della variabile (la stessa schermata usata per l'aggancio tabella dei campi semplici).
3. Scegli come tabella sorgente la tabella (locale, vista o tabella esposta da connettore) desiderata — nell'esempio del corso, la tabella "fornitori".
4. Nell'elenco delle colonne disponibili, seleziona quelle da esporre nella griglia (nell'esempio: codice, descrizione).
5. Per ciascuna colonna selezionata, se il nome originale non è chiaro per l'utente finale, assegna un'intestazione (caption) più leggibile.
6. Salva la configurazione della variabile.
7. Trascina la variabile griglia dati nella form del processo (pagina del magazzino) e anche nelle "variabili da richiedere" dell'attività/start dove deve comparire, dandole spazio a schermo sufficiente.
8. Pubblica il processo.
9. Avvia (o riapri) un'istanza: la griglia appare popolata con i dati della tabella, filtrabile e raggruppabile come le altre griglie del prodotto, ma non modificabile.

Nota: lo stesso identico meccanismo di aggancio è usato per i campi con lookup su tabella (combo/popup di ricerca) — la differenza è solo nella resa a video.
