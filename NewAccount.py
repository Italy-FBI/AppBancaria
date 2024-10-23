import flet as ft
import json

filePathInfo = "InfoAccounts.json"
filePathCredenziali = "CredenzialiAccounts.json"

# Carica i dati info dal file
def caricaDatiInfo():
    with open(filePathInfo, 'r') as f:
        return json.load(f)
    
def salvaDatiInfo(dati):
    with open(filePathInfo, 'w') as f:
        json.dump(dati, f, indent=4)


def aggiungiUtenteInfo(nome, cognome, saldo):
    dati = caricaDatiInfo()
    ultimo_id = max(int(user['id']) for user in dati) if dati else -1
    nuovo_id = ultimo_id + 1

    nuovo_utente = {
        "id": nuovo_id,
        "nome": nome,
        "cognome": cognome,
        "saldo": saldo
    }
    dati.append(nuovo_utente)
    salvaDatiInfo(dati)

def caricaDatiCredenziali():
    with open(filePathCredenziali, 'r') as f:
        return json.load(f)

def salvaDatiCredenziali(dati):
    with open(filePathCredenziali, 'w') as f:
        json.dump(dati, f, indent=4)

def aggiungiUtenteCredenziali(username, password):
    dati = caricaDatiCredenziali()
    ultimo_id = max(int(user['id']) for user in dati) if dati else -1
    nuovo_id = ultimo_id + 1

    nuovo_utente = {
        "id": nuovo_id,
        "username": username,
        "password": password
    }
    dati.append(nuovo_utente)
    salvaDatiCredenziali(dati)  

def newAccount(page: ft.Page):

    def verificaCampiVuoti():
        print("Controllo i campi vuoti")
        registrazione = True
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
    
    def verificaDati(e):
        if not verificaCampiVuoti():
            return False
        else:
            creazioneAccount = True
            passwordCorta.visible = False
            print("Controllo lunghezza password...")
            if len(password.value) < 8:
                passwordCorta.visible = True
                creazioneAccount = False
                print("* ERROR  Password troppo corta")
                page.update()
            
            print("Controllo username...")
            with open(filePathCredenziali , "r") as f:
                data = json.load(f)
                for account in data:
                    if username.value == account["username"]:
                        usernameEsistente.visible = True
                        creazioneAccount = False
                        print("* ERROR  Username gia in uso")
            page.update()
            if creazioneAccount:
                aggiungiUtenteInfo(nome.value, cognome.value, 0.00)
                print("Dati Info Caricati...")
                aggiungiUtenteCredenziali(username.value, password.value)
                print("Dati Credenziali Caricati")
                
    #messaggi di errore
    nomeNonInserito = ft.Text("Nome non inserito", color="red", visible=False)
    cognomeNonInserito = ft.Text("*Cognome non inserito", color="red", visible=False)
    usernameNonInserito = ft.Text("*Username non inserito", color="red", visible=False)
    usernameEsistente = ft.Text("*Username già utilizzato", color="red", visible=False)
    passwordNonInserita = ft.Text("*Password non inserita", color="red", visible=False)
    passwordCorta = ft.Text("*Password più corta di 8 caratteri", color="red", visible=False)

    a = ft.Text("Non hai un account... Creane uno!!!")
    b = ft.Text("Inserisci i dati per la Registrazione")
    nome = ft.TextField(label="inserisci il tuo nome")
    cognome = ft.TextField(label="Inserisci il tuo cognome")
    username = ft.TextField(label="Inserisci un username")
    password = ft.TextField(label="Inserisci una password", password=True)

    registrati = ft.ElevatedButton("Registrati", on_click=verificaDati)  
    #elementi pagina
    controlli = ft.Column(controls=[
        a,b,
        nome,nomeNonInserito,
        cognome,cognomeNonInserito,
        username,usernameNonInserito,usernameEsistente,
        password,passwordNonInserita, passwordCorta,
        registrati
    ])

    page.add(controlli)

    # Impostazioni pagina
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "New Account"
    page.update()

# Da rimuovere
ft.app(target=newAccount)
