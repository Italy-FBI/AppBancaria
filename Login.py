import flet as ft
from VerificaUtente import verificaUtente

from log import *

def login(page: ft.Page):
    page.clean()
    def acceso(e):
        credenzialiErrate.visible=False
        if verificaUtente(username.value, password.value):
            logging.info(f'Accesso effettuato come: {username.value}')
            from Home import homepage
            homepage(page)  # Chiama direttamente la funzione homepage
        else:
            credenzialiErrate.visible=True
            logging.error('Credenziali errate / Account non trovato')
            page.update()

    def registrati(e):
        from NewAccount import newAccount
        newAccount(page)
    a = ft.Text("Salve...")
    b = ft.Text("Esegui l'Accesso", color="lightblue")
    credenzialiErrate = ft.Text("*Credenziali non valide", color="red", visible=False)
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True)
    invio = ft.ElevatedButton("Invio", on_click=acceso)

    #registrazione
    g = ft.Text("Non hai un account... Creane uno!!!")
    passaRegistrazione = ft.ElevatedButton("Registrati", on_click=registrati)

    alignLabel = ft.Row(
       controls=[a, b],
       alignment=ft.MainAxisAlignment.CENTER
   )

    alignText = ft.Row(
        controls=[username, password],
        alignment=ft.MainAxisAlignment.CENTER
    )

    alignBottone = ft.Row(
        controls=[invio],
        alignment=ft.MainAxisAlignment.CENTER
    )
    #impostazioni pagina
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "Login"
    page.add(alignLabel, alignText, alignBottone,g,passaRegistrazione,credenzialiErrate)
    page.update()


