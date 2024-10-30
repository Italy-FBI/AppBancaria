import flet as ft
from VerificaUtente import verificaUtente

from log import *

def paginaUtente(page: ft.Page):
    page.clean()
    page.add(ft.Text("ciaooo"))
    page.title="Pagina Utente"
    page.update()
