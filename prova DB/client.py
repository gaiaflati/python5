import json
import jsonschema
import requests
import sys

base_url="http://127.0.0.1:8080"

def InserisciDatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci cognome cittadino: ")
    dataNascita = input("inserisci data nascita: ")
    codiceFiscale = input("inserisci codice fiscale: ")
    jRequest = {"nome": nome, "cognome":cognome, "data nascita": dataNascita, "codice fiscale": codiceFiscale}
    return jRequest

def RichiediDatiCittadino():
    codiceFiscale = input("inserisci codice fiscale: ")
    return {"codice fiscale": codiceFiscale}


def CreaInterfaccia():

    print("Operazioni disponibili: ")
    print("1. Inserisci cittadino (es.atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

CreaInterfaccia()

sOper = input("Seleziona operazione")
while (sOper != "5"):
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = InserisciDatiCittadino()
    
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1= response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova")
    
    if sOper == "2":
        api_url = base_url + "/richiedi_cittadino"
        jsonDataRequest = RichiediDatiCittadino()

        try:
            response=requests.post(api_url)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1= response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprovare")
            

    CreaInterfaccia()
    sOper= input("inserisci operazione: ")