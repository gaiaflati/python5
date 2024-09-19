from flask import Flask, render_template, request

api = Flask(__name__)

utenti = [['mario', 'password1', 'M', '0'],
          ['gianni', 'password2', 'M', '0'],
          ['AnitaGaribaldi', 'pass3', 'F', '0']]


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regOk():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regKo():
    return render_template('reg_ko.html')

@api.route('/registrati', methods=['GET'])
def registra():
    #prendi i dati che ti ha inviato il server

    #verifica la correttezza

    nome = request.args.get("name")
    print("nome inserito: ", nome)
    password = request.args.get("cognome")

    if request.args.get("sesso")=="1":
        sesso="M"
    else:
        sesso="F"
    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    utente.append("0")
    if utente in utenti:
        index = utenti.index(utente)
        utenti[index][3]="1"
        return render_template('reg_ok.html')
    return render_template('reg_ko.html')

@api.route('/accedi', methods=['GET'])
def accedi():
    #prendi i dati che ti ha inviato il server

    #verifica la correttezza

    nome = request.args.get("name")
    print("nome inserito: ", nome)
    password = request.args.get("cognome")

    if request.args.get("sesso")=="1":
        sesso="M"
    else:
        sesso="F"
    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    #utente == u[:2]
    for i in utenti:
        utente== i[:2]
    if utente in utenti:
        index = utenti.index(utente)
        if utenti[index][3]=="1":
            sesso = 'è un maschio'
            render_str = "<html><body>" + sesso +"</body></html>"
        else:
            sesso="è una femmina"
            render_str = "<html><body>" + sesso +"</body></html>"
        return render_str
    else:
        render_str = "<html><body>" + "Utente non registrato" +"</body></html>"
        return render_str
    


@api.route('/login', methods=['GET'])
def login():
    return render_template('login.html')




api.run(host="0.0.0.0",port=8085)
