# Tutorial 3 — Costruire una decision table per l'assegnazione automatica dell'approvatore in base all'importo

Obiettivo: sostituire una formula scritta a mano con una decision table che assegna l'approvatore tecnico in base all'importo della richiesta (ed eventualmente al tipo di richiesta). –

1. Individua il punto del processo dove serve calcolare l'utente approvatore — tipicamente una formula agganciata a una variabile di tipo Utente (es. `utente_approvazione_tecnica`), oppure una decisione da prendere in un'operazione Set Variable.
2. Apri l'editor della formula/valore su quella variabile e scegli l'opzione per convertirla in **decision table** (o creane una nuova direttamente come decision table, se disponibile).
3. Aggiungi una colonna di input: `Importo Richiesta`.
4. Aggiungi una colonna di output: `Utente Approvazione` — essendo di tipo Utente, la tabella propone automaticamente l'elenco di utenti/gruppi disponibili come valori possibili.
5. Inserisci le righe-regola:

 - Riga 1: `Importo Richiesta < 1000` → `Dir Tech`
 - Riga 2: `Importo Richiesta ≥ 1000` → `Dir Gen`

6. Verifica/aggiusta l'ordine delle righe con le frecce su/giù, ricordando che vince la prima riga che soddisfa la condizione.
7. Estendi la tabella con una seconda colonna di input, `Tipo Richiesta` (lista di valori — la tabella ne conosce automaticamente i valori ammessi), e aggiungi/riordina le righe:

 - `< 1000` / `Normale` → `Dir Tech`
 - `≥ 1000` / `Normale` → `Dir Gen`
 - `(qualunque)` / `Sicurezza` → `Sicurezza`

8. Salva la decision table.
9. Sull'attività di approvazione, imposta gli "utenti responsabili" sulla variabile `utente_approvazione_tecnica` (assegnazione guidata da regola) invece che su un gruppo fisso.
10. Pubblica e collauda con richieste di importo/tipo diversi, verificando che l'attività venga assegnata correttamente.
11. Se in seguito la logica dovesse superare ciò che la tabella può esprimere (es. serve scorrere un gruppo e contare righe), converti la tabella in formula e completa la logica a mano in VB.
