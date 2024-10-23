import flet as ft
from VerificaUtente import verificaUtente
import json
from Home import homepage
from log import *

filePathInfo = "C:\\Users\\Informatica\\Documents\\martini 4D\\AppBancaria-main\\AppBancaria-main\\InfoAccounts.json"
filePathCredenziali = "C:\\Users\\Informatica\\Documents\\martini 4D\\AppBancaria-main\\AppBancaria-main\\CredenzialiAccounts.json"

def caricaDatiInfo():
    with open(filePathInfo, 'r') as f:
        return json.load(f)

def salvaDatiInfo(dati):
    with open(filePathInfo, 'w') as f:
        json.dump(dati, f, indent=4)

def aggiungiUtenteInfo(nome, cognome, saldo):
        dati = caricaDatiInfo()  # Carica i dati esistenti
        # Calcola il nuovo ID come uno in più dell'ultimo ID esistente
        ultimo_id = max(user['id'] for user in dati) if dati else -1
        nuovo_id = ultimo_id + 1

        nuovo_utente = {
            "id": nuovo_id,
            "nome": nome,
            "cognome": cognome,
            "saldo": saldo
        }
        dati.append(nuovo_utente)  # Aggiungi il nuovo utente
        salvaDatiInfo(dati)

def caricaDatiCredenziali():
    with open(filePathInfo, 'r') as f:
        return json.load(f)

def salvaDatiCredenziali(dati):
    with open(filePathInfo, 'w') as f:
        json.dump(dati, f, indent=4)

def aggiungiUtenteCredenziali(nome, cognome, saldo):
        dati = caricaDatiInfo()  # Carica i dati esistenti
        # Calcola il nuovo ID come uno in più dell'ultimo ID esistente
        ultimo_id = max(user['id'] for user in dati) if dati else -1
        nuovo_id = ultimo_id + 1

        nuovo_utente = {
            "id": nuovo_id,
            "nome": nome,
            "cognome": cognome,
            "saldo": saldo
        }
        dati.append(nuovo_utente)  # Aggiungi il nuovo utente
        salvaDatiInfo(dati)

def newAccount(page: ft.Page):

    def verificaCampiVuoti(e):
        registrazione = True
        # Nascondi i messaggi di errore all'inizio
        nomeNonInserito.visible = False
        cognomeNonInserito.visible = False
        usernameNonInserito.visible = False
        passwordNonInserita.visible = False
        
        if nome.value == "":
            nomeNonInserito.visible = True
            registrazione = False
        if cognome.value == "":
            cognomeNonInserito.visible = True
            registrazione = False
        if username.value == "":
            usernameNonInserito.visible = True
            registrazione = False
        if password.value == "":
            passwordNonInserita.visible = True
            registrazione = False
        
        page.update()
        return registrazione
    
    def verificaDati():
        if verificaCampiVuoti == False: 
            return verificaCampiVuoti
        else:#finire di verificare le credenziali
            creazioneAccount = True
            passwordCorta.visible = False
            if len(password.value) < 8:
                passwordCorta.visible = True
                creazioneAccount = False
                page.update()

            with open(filePathInfo , "r") as f:
                data = json.load(f)
                for account in data:
                    if username.value == account["username"]:
                        usernameEsistente.visible = True
                        creazioneAccount = False
            page.update()
            if creazioneAccount:
                aggiungiUtenteInfo(nome.value, cognome.value, 00.00)
                caricaDatiInfo()
                #finire di caricare i dati nel file json delle credenziali
           



        
    nomeNonInserito = ft.Text("Nome non inserito", color="red", visible=False)
    cognomeNonInserito = ft.Text("*Cognome non inserito", color="red", visible=False)
    usernameNonInserito = ft.Text("*Username non inserito", color="red", visible=False)
    usernameEsistente = ft.Text("*Username già utilizzato", color="red", visible=False)
    passwordNonInserita = ft.Text("*Password non inserita", color="red", visible=False)
    passwordCorta = ft.TextField("*Password più corta di 8 caratteri", color="red", visible=False)

    a = ft.Text("Non hai un account... Creane uno!!!")
    b = ft.Text("Inserisci i dati per la Registrazione")
    nome = ft.TextField(label="inserisci il tuo nome")
    cognome = ft.TextField(label="Inserisci il tuo cognome")
    username = ft.TextField(label="Inserisci un username")
    password = ft.TextField(label="Inserisci una password", password=True)
    registrati = ft.ElevatedButton("Registrati", on_click=verificaDati)
    
    page.add(a,b,nome,nomeNonInserito,cognome,cognomeNonInserito,username,usernameNonInserito, password,passwordNonInserita,passwordCorta, registrati)

    #impostazioni pagina
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "New Account"
    page.update()
#da rimuovere
ft.app(target=newAccount)

