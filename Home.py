import flet as ft
from PrendiInfo import *
def homepage(page: ft.Page):
    page.clean()  # Pulisci la pagina attuale
    saluto = ft.Text(f" Salve, {getNome()}")
    contoDisponibile = ft.Text(f"Saldo Disponibile: {getSaldo()} €")
    imgProfilo = ft.Image(
        src=f"C:/Users/zonzi/Desktop/Python/AppBancaria/img/user.png",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN,
        )
    
    images = ft.Row(expand=1, wrap=False, scroll="always")

    alignSaluto = ft.Column([
        ft.Row(
                controls=[saluto],
                alignment=[ft.MainAxisAlignment.CENTER]
            )])
    ft.Column([
        ft.Row(
            controls=[contoDisponibile]
        )
    ])
    page.add(alignSaluto)

    page.title = "Home"
    page.update()
