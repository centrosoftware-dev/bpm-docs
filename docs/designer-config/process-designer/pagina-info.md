# Pagina Info processo

La sezione **_Pagina Info_** permette di configurare le **impostazioni** principali di un **modello di processo**.  
Da qui è possibile gestire le informazioni di base, le regole di gestione, i contatti associati, i permessi di utilizzo e altro ancora.

Questa sezione è suddivisa in quattro blocchi principali, ciascuno dei quali contiene campi specifici che permettono di definire in modo preciso il comportamento e le proprietà del modello:

### **Impostazioni base**

In questa parte si impostano le informazioni fondamentali per identificare e organizzare il modello di processo.

##### Nome modello
Nome identificativo univoco del modello di processo. È il titolo con cui verrà visualizzato all’interno dell’applicativo. 

##### Descrizione modello
Campo testuale per inserire una breve descrizione esplicativa del modello.

##### Cartella
Specifica la cartella logica in cui il modello verrà salvato.  

##### Gruppi di modelli
Permette di assegnare il modello a uno o più gruppi di modelli per facilitarne l’organizzazione. 

##### Modello Principale
Indica se il modello rappresenta o meno il processo principale (_True_ / _False_).

##### Tabella variabili
Campo che definisce la tabella delle variabili associate al modello, utile per la gestione delle informazioni interne al processo.

---

### **Gestione**

Questa sezione include campi che permettono di controllare il comportamento automatico e la modalità di duplicazione del modello.

##### Formula nome 
Campo per definire una formula automatica che costruisce automaticamente il nome univoco delle varie instanze del processo in base a regole o variabili.

!!! info "Automazione Formula Nome"
    Sebbene questo campo sia opzionale, è sempre consigliabile definire una _Formula Nome_ per i modelli di processo che creiamo, evitando di dover ogni volta compilare questo valore alla creazione del processo. Un modo semplice per rendere univoci i nomi creati con questa formula è quello di inserire al suo interno un **Progressivo**, ossia una variabile numerica che funge da contatore e che viene incrementata ogni volta che viene creata una nuova istanza di questo processo (è necessario prima definirla nel [Magazzino delle variabili](../variables/warehouse.md)) 

##### Formula descrizione
Campo per definire una formula automatica che costruisce automaticamente la descrizione del processo in base a regole o variabili.

##### Formula testo
Campo per definire una formula automatica che genera automaticamente testi personalizzati in base a regole o variabili.

##### Schemi di duplicazione
Indica quali schemi di duplicazione utilizzare per la duplicazione del modello.  

##### BPMN
Opzione booleana che specifica se il modello utilizza o meno la notazione BPMN (_True_ / _False_).  

---

### **Contatti e utenti**

In questo blocco si configurano i riferimenti a utenti, aziende e contatti legati al modello.

##### Contatti
Campo per associare uno o più contatti esterni al modello.

##### Azienda
Campo per specificare l’azienda o l’ente a cui il modello è collegato.

##### Proprietari
Indica gli utenti proprietari del modello. Solo questi avranno diritti completi di modifica e gestione.

##### Persone messe a conoscenza
Utenti che possono visualizzare il modello, ma senza diritti di modifica.

##### Responsabili programmazione
Utenti incaricati di gestire gli aspetti tecnici o di pianificazione del modello.

---

### **Permessi**

L’ultima sezione è dedicata alla definizione delle autorizzazioni e delle opzioni di sicurezza applicate al modello. Sono tutti valori _True_ / _False_.

##### Autorizzazioni allegati per root
Determina se gli allegati root ereditano o meno le autorizzazioni specifiche del modello.

##### Autorizzazioni per pagina
Stabilisce se le autorizzazioni sono gestite a livello di singola pagina del processo.

##### Abilitazione note salvataggio
Se impostato su _True_, richiede all’utente di inserire una nota ogni volta che vengono salvate modifiche al modello.  