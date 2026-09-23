# Fase 4 — Il magazzino delle variabili

18. **Aprire il magazzino delle variabili**: Strumenti > "Inserimento modifica variabili" — appare come una nuova pagina/tab del processo, inizialmente vuota.
19. **Creare la prima variabile**: "Nuova variabile" e assegnarle il nome "richiedente". Di default viene creata come tipo Stringa; cambiarne il tipo in **Utente (User type)**, poiché rappresenta la persona che inoltra la richiesta.
20. **Trascinare la variabile "richiedente" sul canvas del form** — a questo punto compare come campo utente, con possibilità di scegliere tra tutti gli utenti/gruppi registrati in BPM.
21. **Creare le variabili aggiuntive di testata**, tipicamente: "data richiesta" (tipo Data), "tipo richiesta" (tipo Lista Valori), "numero richiesta" (tipo Numerico, poi configurato come contatore), "codice stabilimento" (tipo Stringa, con tabella di origine) e "note richiesta" (tipo Memo). Trascinare ciascuna sul form man mano che viene creata.
22. **Organizzare il layout**: selezionare più campi con Ctrl e usare gli strumenti di allineamento ("Allinea in alto", "Allinea a destra", "Stessa dimensione") per un form ordinato — è la schermata che vedranno gli utenti finali.
23. (Opzionale, buona prassi) **Creare una nuova pagina di variabili** per il gruppo di campi legati alle approvazioni (vedi passo 27), prefissandola numericamente (es. "02 - Approvazioni") per mantenere l'organizzazione allineata al flusso cronologico del processo.
