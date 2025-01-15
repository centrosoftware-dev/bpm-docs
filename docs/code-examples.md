Codice:
:melting_face_flat:
```vb.net title="FrmEditorGruppo.vb" linenums="1" hl_lines="12-16"
Private Sub btnNuovo_Click(sender As Object, e As EventArgs) Handles btnNuovo.Click
    Dim nm = IBPMInputBox.Show_NoTrad(Vocabulary.Translate("Codice") & ":", "")
    If nm.Trim <> "" Then
        If ElencoGruppiDict.ContainsKey(nm.Trim.ToUpper) = False Then
            Dim d As New GruppoTmp(nm, nm, False, False, "", False, True, True, True, "", 0)
            ElencoGruppiDict.Add(nm.Trim.ToUpper, d)
            ElencoGruppi.Add(d)
            Me.cmbGruppoCodice.Properties.Items.Clear()
            Me.cmbGruppoCodice.Properties.Items.AddRange(ElencoGruppi)
            'HERE Me.cmbGruppoCodice.DisplayMember = "Codice"
            Me.cmbGruppoCodice.Refresh()
            Try
                Me.cmbGruppoCodice.SelectedItem = d
            Catch ex As Exception
                Logger.LogError(ex, "")
            End Try
        End If
    End If
End Sub
```