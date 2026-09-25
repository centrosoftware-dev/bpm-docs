# Chiavi di accesso Web API

Percorso: **Configurazione > Configurazione > Chiavi di accesso Web API**.

La schermata **Token di accesso per Web API** elenca le chiavi API con cui le applicazioni esterne accedono alle [Web API](../../integrazione-e-ai/integrazione/web-api/index.md) di BPM.

## Comandi

### Crea nuovo token di autenticazione

Genera una nuova chiave casuale e la aggiunge all'elenco.

## Colonne

| Colonna | Descrizione |
|---|---|
| **Chiave di autenticazione** | La chiave da comunicare all'applicazione esterna, che la invierà nel campo `authenticationToken`. |
| **Copy to clipboard** | Copia la chiave negli appunti. |
| **Descrizione** | Descrizione libera: indica quale applicazione usa la chiave. |
| **Data** | Data associata alla chiave. |
| **Edit** | Modifica la chiave. |
| **Delete** | Elimina la chiave: le applicazioni che la usano non potranno più accedere. |

!!! warning "Sicurezza"
    Una chiave consente di operare per conto di qualunque utente. Crea una chiave per ogni applicazione, descrivila con chiarezza ed eliminala quando l'integrazione non è più in uso. Vedi [Autenticazione e utenti](../../integrazione-e-ai/integrazione/web-api/autenticazione.md).
