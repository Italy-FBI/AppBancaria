import flet as ft

def aggiungiAccredito(page):

    def slider_changed(e):
        textField.value = e.control.value
        page.update()
    def textField_changed(e):
        slider.value = e.control.value
        page.update()

    def aggiungiImporto(e):
        importo = textField.value
        print(importo)
        return importo
    
    textField = ft.TextField("", border_color="white", on_change=textField_changed, autofocus=True)
    bottoneAggiungi = ft.ElevatedButton("Aggiungi", on_click=aggiungiImporto)

    slider = ft.Slider(min=0, max=100000,divisions=100000,label="{value}",on_change=slider_changed)
    page.add(
        ft.Text("Inserisci l'importo da aggiungere: "),
        slider,
        textField, bottoneAggiungi),
        
    page.title ="Aggiungi Accredito"
    page.window.width = 400
    page.window.height = 600
    page.window.always_on_top = False
    page.window.maximizable = False
    page.window.minimizable = False
    page.window.resizable = False
    page.update()