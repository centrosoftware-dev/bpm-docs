# Collection delle API standard di BPM

Collection con tutte le chiamate di `/api/ext`, per Postman e per Bruno.

I file Postman sono pubblicati nel sito e si trovano in `docs/integrazione/api-standard/postman/`: sono loro la versione di riferimento. Questa cartella contiene la versione nativa per Bruno. Gli esempi usano i parametri descritti in `docs/integrazione/api-standard/`.

## Variabili d'ambiente

| Variabile | Contenuto |
|---|---|
| `bpmUrl` | Indirizzo dell'applicazione web, senza `/api` finale (es. `https://bpm.azienda.it/BPM`). |
| `apiKey` | Chiave API generata in BPM (Configurazione > Configurazione > Chiavi di accesso Web API). **Segreta.** |
| `userName` | Utente BPM per conto del quale si opera. |
| `processModel`, `documentModel` | Modello di processo e classe documentale usati negli esempi. |
| `startObject`, `activityName` | Nome interno dello start e dell'attività (es. `start1`, `activity4`). |
| `instanceId`, `documentName` | Impostati automaticamente da CreateNewProcess. |
| `documentInstanceId`, `documentNameDoc` | Impostati automaticamente da CreateNewDocument / CreateOrUpdateDocument. |
| `linkedInstanceId` | Istanza da collegare con AddLink. |
| `aliasType`, `aliasUser`, `aliasCompany` | Utente esterno per provare il mapping con gli alias (GetUser utente esterno). |

## Postman

Importa i due file di `docs/integrazione/api-standard/postman/` (scaricabili anche dalla pagina API standard del sito): la collection e l'ambiente **BPM**. Seleziona l'ambiente e inserisci `bpmUrl`, `apiKey` e `userName`.

## Bruno

Apri la cartella `bruno/BPM API standard` con **Open Collection**, seleziona l'ambiente **BPM** e inserisci i valori. `apiKey` è una variabile segreta: Bruno la conserva solo in locale e non la scrive nei file.

In alternativa, Bruno può importare direttamente la collection Postman.

## Attenzione

- Non salvare nel repository file d'ambiente con una chiave API reale.
- DeleteProcess e DeleteDocument eliminano davvero i dati: usali solo su un ambiente di prova.
