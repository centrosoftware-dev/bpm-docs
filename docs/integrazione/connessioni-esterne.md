# Connessioni esterne

Percorso: **Configurazione > Configurazione > Connessioni esterne**.

Una connessione esterna descrive come raggiungere il database di un altro sistema: server, database, credenziali. Si configura una volta sola, con un nome, e si riusa ovunque serva:

- nei [dati esterni delle variabili](dati-esterni.md) e nelle griglie dati;
- nell'operazione [Carica Dati](carica-dati.md);
- nell'operazione [Esegui SQL](esegui-sql.md).

Sono supportati SQL Server e le fonti dati raggiungibili via **ODBC**.

## Buone pratiche

- **Una connessione per sistema e per ambiente**, con un nome chiaro (per esempio `ERP A1`, `ERP B`): quando il processo passa da un ambiente di prova a quello reale, si cambia la connessione e non i modelli.
- **Evita le viste "ponte"** create nel database di BPM che puntano, a loro volta, al database esterno: funzionano, ma si rompono quando si sposta l'installazione su un altro ambiente. Una connessione esterna è sempre preferibile.
- **ODBC** funziona, ma con alcuni sistemi legacy può dare problemi: in quei casi un servizio web o un connettore dedicato sono spesso la scelta migliore.
- Usa per la connessione un utente del database con i **soli diritti necessari**: lettura per le anagrafiche, scrittura solo dove BPM deve davvero scrivere.

## Configurazione dei connettori

I [connettori](connettori/index.md) non usano le connessioni esterne: hanno una propria configurazione, in **Configurazione > Connettori**. Lì si attiva il connettore, si aggiungono le aziende e, per ciascuna, si compilano i parametri richiesti (indirizzi di servizi web, credenziali, database).
