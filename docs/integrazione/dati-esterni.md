# Dati esterni nelle variabili

Una variabile può essere collegata a una **fonte dati**: invece del testo libero, l'utente sceglie un valore da una tabella, e la scelta può valorizzare automaticamente altre variabili. È il modo più semplice per usare in BPM le anagrafiche di un altro sistema senza copiarle.

Per esempio, scegliendo il codice fornitore, BPM compila da solo la ragione sociale, la partita IVA e le condizioni di pagamento lette dall'ERP.

## Fonti dati

| Fonte | Quando usarla |
|---|---|
| **Tabella o vista esterna** | I dati stanno nel database di un altro sistema. Richiede una [connessione esterna](connessioni-esterne.md). |
| **Tabella locale** | I dati sono gestiti in BPM, in una tabella personalizzata (prefisso `P_`) o in una vista del database di BPM. |
| **Tabella di un connettore** | Il connettore espone i dati di un sistema come se fossero una tabella (per esempio i connettori per SAM). |
| **Servizio web (REST)** | I dati arrivano da una chiamata a un'API. Possibilità più limitata rispetto alle tabelle. |
| **Variabili del processo** | I valori si scelgono tra le righe di un gruppo dello stesso processo (per esempio il preventivo vincente tra quelli inseriti). |

## Come si configura

La configurazione avviene nella scheda della variabile, con la stessa finestra usata dall'operazione [Carica Dati](carica-dati.md):

1. si sceglie la fonte (connessione e tabella, oppure la query);
2. si indica la **colonna chiave**, collegata alla variabile che si sta configurando;
3. si collegano, se serve, **altre colonne** ad altre variabili, che si valorizzano con la scelta;
4. si impostano le opzioni di ricerca: campi su cui cercare, filtri, prefiltro sul valore già inserito, caricamento dei dati solo dopo una ricerca per le tabelle molto grandi.

## Griglia dati

La **griglia dati** è un tipo di variabile che mostra in sola lettura una tabella esterna o locale: per esempio tutti gli ordini aperti del cliente del processo. Si configura con la stessa finestra, scegliendo le colonne da mostrare e, se serve, rinominandone le intestazioni.

Non serve a inserire dati, per quello ci sono i gruppi: è una finestra di consultazione sempre aggiornata.
