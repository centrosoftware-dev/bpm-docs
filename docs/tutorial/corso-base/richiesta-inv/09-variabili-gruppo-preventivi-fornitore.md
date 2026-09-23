# Fase 9 — Variabili di gruppo: i preventivi fornitore

41. **Tornare nel magazzino delle variabili** e creare una nuova pagina "Preventivi".
42. **Creare la variabile "Codice Fornitore"** (Stringa), trascinarla sul form, poi cliccare sui "..." di configurazione e assegnarla a un nuovo **Gruppo**, "Lista Preventivi" — diventa così la prima colonna di una griglia di dettaglio virtuale.
43. **Aggiungere le colonne successive trascinandole direttamente sulla griglia**: "Ragione Sociale", "Numero Preventivo", "Importo Preventivo" (Numerico) — ogni variabile trascinata dentro la griglia si unisce automaticamente allo stesso gruppo.
44. **Creare una nuova attività "Ricezione preventivi"**, assegnata come Esecutore all'ufficio acquisti, posizionata dopo l'approvazione. Nelle sue "Variabili da richiedere" trascinare l'intestazione e le variabili del gruppo "Lista Preventivi".
45. **Riutilizzare il layout della pagina "Preventivi"** esportando la categoria corrente e importandola/sostituendola nella schermata "Variabili da richiedere" di "Ricezione preventivi", per non dover ritrascinare manualmente ogni colonna.
46. **Testare**: avviare una nuova istanza, arrivare al task "Ricezione preventivi" ed eseguirlo. A runtime il gruppo appare come una griglia editabile in cui aggiungere/rimuovere righe liberamente.
47. **Rendere obbligatori i campi per riga**: tornare nelle "Variabili da richiedere" di "Ricezione preventivi" e marcare Codice Fornitore, Ragione Sociale, Numero Preventivo e Importo Preventivo come obbligatori — vincolo che si applica a ogni riga inserita, non al numero minimo di righe.
48. **Aggiungere un campo Note per riga**: creare nel magazzino la variabile "Note Preventivo" (Memo) trascinandola direttamente nella griglia del gruppo "Lista Preventivi" (viene automaticamente assegnata al gruppo), poi trascinarla anche nelle "Variabili da richiedere" di "Ricezione preventivi".
49. (Facoltativo, per righe con molti campi) **Aggiungere un bottone "Dettagli..."** stateless dentro la griglia, configurato con una propria sotto-form "Variabili da richiedere", per aprire un pop-up a schermo intero sulla singola riga.
