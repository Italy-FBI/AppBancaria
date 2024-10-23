import json
with open("CredenzialiAccounts.json", "r") as f:#"C:\\Users\\Informatica\\Documents\\martini 4D\\APPBANCARIA-MAIN\\CredenzialiAccounts.json"
      data = json.load(f)

def verificaUtente(usernameIns, passwordIns):
   print(usernameIns, " : ",passwordIns)
   for account in data:
      print(account["username"])
      print(account["password"])
      if account["username"] == usernameIns and account["password"] == passwordIns:
         print(account["id"])
         idUtente = account["id"]
         return True
   return False
   

   
def getIdUtente(usernameIns, passwordIns):
   for account in data:
         print(account["username"])
         print(account["password"])
   if account["username"] == usernameIns and account["password"] == passwordIns:
            print(account["id"])
            idUtente = account["id"]
   return idUtente
      

 
# def verificaUtente(usernameIns, passwordIns):
