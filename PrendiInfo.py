import json
from VerificaUtente import getIdUtente
with open("InfoAccounts.json", "r") as f:
    data = json.load(f)

id = 0

def prendiInfo():
    id = getIdUtente()
    print(id)
    print("----------------")
    for account in data:
        print("id: ",account["id"])
        print("nome: ", account["nome"])
        print("cognome: ",account["cognome"])
        print("saldo: ",account["saldo"])
        if id == account["id"]:
            print(f"Account Trovato con id: {id}")

def getNome():
   for account in data:
        if id == account["id"]:
            print(account["nome"])
   return account["nome"]

def getCognome():
   for account in data:
        if id == account["id"]:
            print(account["cognome"])
   return account["cognome"]

def getSaldo():
   for account in data:
        if id == account["id"]:
            print(account["saldo"])
   return account["saldo"]


print("prendo...")