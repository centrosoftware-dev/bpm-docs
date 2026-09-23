# Tutorial 2 — Filtrare un gruppo diversamente su due attività parallele e condizionare il gateway

Obiettivo: due attività parallele di valutazione preventivi (tipo A / tipo B) devono mostrare, dello stesso gruppo "lista preventivi", solo le righe pertinenti al proprio tipo; inoltre il ramo verso ciascuna attività deve aprirsi solo se esistono righe di quel tipo. –

1. Nel diagramma di processo, individua le due attività parallele (es. "valutazione preventivi tipo A" e "valutazione preventivi tipo B"), entrambe collegate allo stesso gruppo "lista preventivi".
2. Sulla prima attività, apri "variabili da richiedere" e seleziona una qualunque variabile appartenente al gruppo "lista preventivi".
3. Nelle impostazioni locali di quella variabile, disabilita l'aggiunta e la cancellazione righe (per rendere la vista di sola consultazione su questa attività) e imposta una **condizione di filtro**, ad esempio `tipo_preventivo = "tipo A"`.
4. Ripeti i passi 2–3 sulla seconda attività, con la condizione opposta (`tipo_preventivo = "tipo B"`).
5. Nel magazzino delle variabili, crea due variabili helper di tipo stringa (es. `presenza_tipo_A`, `presenza_tipo_B`) — servono solo per verificare visivamente il risultato della formula mentre la costruisci, dato che BPM non ha un debugger.
6. Su `presenza_tipo_A`, apri l'editor di formula e scrivi:

    ```vb
    Dim i As Integer
    For i = 0 To lista_preventivi.Count - 1
    If tipo_preventivo(i) = "tipo A" Then
    Return "sì"
    End If
    Next
    Return "no"
    ```

7. Ripeti lo stesso schema per `presenza_tipo_B`, sostituendo la condizione con `"tipo B"`.
8. Sul gateway (o link) che porta verso l'attività "valutazione preventivi tipo A", apri la condizione di abilitazione e imposta `presenza_tipo_A = "sì"`. Ripeti analogamente per il ramo tipo B.
9. Facoltativo — validazione globale: sull'attività di inserimento preventivi, aggiungi una formula di validazione globale che impedisca di proseguire se non è stato inserito alcun preventivo:

    ```vb
    If Count(tipo_preventivo) = 0 Then
    MessageBox("Errore di validazione: necessario almeno un preventivo per proseguire")
    Return False
    End If
    Return True
    ```

10. Pubblica e collauda con dati di test: inserisci solo preventivi di tipo A e verifica che si apra solo il ramo corrispondente; ripeti con tipo B e con entrambi.
