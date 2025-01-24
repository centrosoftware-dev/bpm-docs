# Magazzino delle variabili

Con **_Magazzino delle variabili_** si intende la pagina di un processo dove sono contenuti tutti i dati.

In questa pagina ci sono 2 colonne laterali: la sidebar di sinistra contiene tutte le variabili ed è infatti chiamata **_Variable List_**, mentre la sidebar di destra contiene i loro attributi.

In alto è presente la barra degli strumenti che, sotto la sezione **_Variabili_**, presenta tutti i comandi utili nel contesto del Magazzino.

## Barra degli strumenti - Variabili

La sezione variabili della barra degli strumenti è divisa in 6 colonne la cui ultima presenta solo il bottone di chiusura della pagina del Magazzino delle variabili.

### Operatività

La colonna **_Operatività_** contiene i comandi più comuni utilizzabili nel Magazzino.

#### Nuova variabile, Duplica variabile e Rimuovi variabile

**_Nuova variabile_** serve ad aggiungere nuove variabili al Magazzino.  
Cliccando il comando, un dialog si aprirà chiedendo all'utente di inserire il Nome variabile.  
Dopo aver confermato, si aprirà un secondo dialog dove è possibile personalizzare tutti gli attributi di una variabile.

!!! note

    Il **_Nome variabile_** non è reimpostabile né dal dialog degli attributi né dal pannello degli attributi.  
    Gli attributi del secondo dialog sono situae nel pannello degli attributi.  

**_Duplica variabile_**, selezionando una variabile all'interno del canvas, duplica la variabile selezionata, chiedendo all'utente di inserire solamente il nome della variabile duplicata.  

**_Rimuovi variabile_** serve a rimuovere una variabile dal canvas.

#### Trova riferimenti

Selezionando una variabile nel canvas, **_Trova riferimenti_** cercherà nel processo tutte i riferimenti alla variabile selezionata.

### Pagina

Per **_Pagina_** non si intendono nel pagine del progetto, bensì quelle del Magazzino delle variabili, simili a delle schede.

#### Nuova pagina, Rinomina pagina e Refresh

##### Nuova pagina
Crea una nuova scheda all'interno del Magazzino delle variabili.  

##### Rinomina pagina

Rinomina la pagina in cui si sta lavorando.  

##### Refresh 

Aggiorna la pagina corrente.

### Gestione

La colonna **_Gestione_** raggruppa i comandi e le impostazioni per gestire la portabilità e la validazione.

#### Formule

Le **_Formule_** sono 3: **_Validazione, Inizializzazione e Formattazione ricerche_**.

##### Validazione

Formula che valida la fine di un processo.

##### Inizializzazione

##### Formattazione ricerche

#### Sqlview

L'**_Sqlview_** semplifica la scrittura delle query sul database del BPM.
Sul click, si aprirà un file di testo con all'interno una query relative a tutte le variabili nel Magazzino.
Dalla query di default verrà selezionato l'InstanceID del workflow.


``` title="Default query" linenums="1"
-- Verranno riportate nella selezione soltanto le variabili di testata (non di gruppo)

Select WKF.InstanceID, v1.aaa
from WKF
left join (Select StringValue As aaa, InstanceID,VariableName  from VAR_FGWTFEFWE ) v1 On  v1.VariableName ='aaa' and v1.InstanceID = wkf.InstanceID
where wkf.Name like 'fgwtfefwe' 
```

#### Importa/Esporta

**_Importa/Esporta_** è un dropdown con 6 possibili scelte.



#### Esporta variabili
