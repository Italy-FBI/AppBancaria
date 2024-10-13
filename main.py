import flet as ft
from VerificaUtente import verificaUtente
from Home import homepage

def main(page: ft.Page):
    def acceso(e):
        if verificaUtente(username.value, password.value):
            homepage(page)  # Chiama direttamente la funzione homepage
        else:
            a.text = "Credenziali non valide"
            page.update()

    a = ft.Text("Salve...")
    b = ft.Text("Esegui l'Accesso")
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True)
    invio = ft.ElevatedButton("Invio", on_click=acceso)

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
    page.add(alignLabel, alignText, alignBottone)
    page.update()

ft.app(target=main)
