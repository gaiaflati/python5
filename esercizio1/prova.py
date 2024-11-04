from flask import Flask, jsonify, request

import sys
import dbclient as db

api = Flask(__name__)

#Devo connettermi al database
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	sys.exit()

pos= input("cosa vuoi fare? \
		    1. per scrivere \
		    2. per leggere ")


    

if pos == "1":
	codice_fiscale = input('inserisci codice fiscale: ')
	nome = input('inserisci nome: ')
	cognome = input('inserisci cognome: ')
	dataNascita = input('inserisci data di nascita: ')
	sQuery = "insert into cittadini(codice_fiscale,nome,cognome,data_nascita) values ("
	sQuery += "'" + codice_fiscale + "','" + nome + "','" + cognome + "','" + dataNascita + "');"
	ret = db.write_in_db(cur,sQuery)    
	

elif pos== "2":
	codice_fiscale = input('inserisci il cf di chi vuoi vedere i dati')
	sQuery= f"select * from cittadini where codice_fiscale= {codice_fiscale}"
	ret=db.read_in_db(cur, sQuery)
	if (ret == 0):

		print("Query eseguita correttamente")
	