from flask import Flask, render_template, request

api = Flask(__name__)

utenti = [['mario', 'password1', '1', '1'],
          ['gianni', 'password2', '1', '1'],
          ['A', '3', '2', '0']]


@api.route('/', methods=['GET'])
def home():
    return render_template('home.html')

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

    nome = request.args.get("fnome")
    print("nome inserito: ", nome)
    password = request.args.get("fcognome")
    sesso= request.args.get("sesso")  
    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append(sesso)
    utente.append("0")
    print(utente)
    if utente in utenti:
        index = utenti.index(utente)
        utenti[index][3]="1"
        return render_template('reg_ok.html')
    return render_template('reg_ko.html')


@api.route('/accedi', methods=['GET'])
def accedi():
    utente: list[str] = [request.args.get("fnome"), request.args.get("fcognome"), "1"]
    for i in utenti:
        u=i
        u.pop(2)
        if u==utente:
            if i[2]=="1":
                sesso = 'è un maschio'
                render_str = "<html><body>" + sesso +"</body></html>"
                return render_str
            else:
                sesso="è una femmina"
                render_str = "<html><body>" + sesso +"</body></html>"
                return render_str
    
    return render_template('reg_ko.html')
@api.route('/reg', methods=['GET'])  
def reg():
    return render_template('index.html')


@api.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@api.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

api.run(host="0.0.0.0",port=8085)
