# Fase 2 — Utenti e gruppi

9. **Spostarsi in Configurazione > Utenti e Gruppi.** Utenti e gruppi condividono la stessa griglia, filtrabile per tipo.
10. **Creare i gruppi necessari al processo**, ad esempio "AM" (controllo di gestione/amministrazione) e "Direzione Tecnica" — in questa fase basta dare loro un nome, senza preoccuparsi ancora dei permessi. I gruppi vengono tipicamente creati ad hoc per il processo, non importati da Active Directory, perché la granularità richiesta raramente coincide con i gruppi già esistenti nel dominio aziendale.
11. **Tornare al Designer** sull'attività "Approvazione controllo di gestione" e aprire "Utenti e responsabili". Impostare il gruppo "AM" come **Esecutore**: tutti i membri del gruppo (quando ci saranno) troveranno il task nella propria To-Do List; il primo che lo esegue fa avanzare il processo.
12. Ripetere per "Approvazione direzione industriale", assegnando il gruppo "Direzione Tecnica" come Esecutore.
13. In fase di progettazione è ammesso lasciare temporaneamente un'attività priva di utente assegnato (resta visibile solo all'amministratore); va però sistemata prima del go-live.
14. (Nota a margine, non obbligatoria per l'esercizio base) Per un flusso più controllato, è possibile marcare un'attività "Task deve essere assegnato prima di poter essere eseguito", introducendo un passaggio di smistamento esplicito da parte di un Responsabile.
