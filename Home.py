import flet as ft
from PrendiInfo import *
def homepage(page: ft.Page):
    page.clean()  # Pulisci la pagina attuale

    def apriUser(e):
        from PaginaUser import paginaUtente
        paginaUtente(page)

    def apriAggiungiImporto(e):
        from AggiungiAccredito import aggiungiAccredito
        aggiungiAccredito(page)

    saluto = ft.Text(f" Salve, {getNome()}")
    contoDisponibile = ft.Text(f"Saldo Disponibile: {getSaldo()} €")
    bottoneTransazioni = ft.ElevatedButton("Visualizza le transazioni")
    bottoneAggiungi = ft.ElevatedButton("Aggiungi accredito", on_click=apriAggiungiImporto)
    bottoneSpesa = ft.ElevatedButton("Aggiungi spesa")
    
    bottoneUser = ft.IconButton(
                    icon=ft.icons.ACCOUNT_CIRCLE,
                    icon_color="blue400",
                    icon_size=70,
                    tooltip="Pause record",
                    on_click=apriUser
                )
   
    page.add(saluto,contoDisponibile,bottoneTransazioni,bottoneAggiungi,bottoneSpesa,bottoneUser)

    page.title = "Home"
    page.update()
ft.app(target=homepage)