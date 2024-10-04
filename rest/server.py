from flask import Flask, json, request
from myjson import JsonSerialize, JsonDeserialize

sFileAnagrafe = "./anagrafe.json"
api= Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print("RIcevuta chiamata"+ content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale =jRequest ["codice fiscale"]
        print("Ricevuto"+ sCodiceFiscale)

        dAnagrafe= JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale]= jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)

            jResponse = {"Error":"000", "Msg":"ok"}
            return json.dumps(jResponse),200
        else:
            jResponse= {"Error": "001", "Msg": "codice fiscale gia presente"}
            return json.dumps(jResponse),200

    else:
        return "Errore, formato non riconosciuto",401

    #controlla che il cittadino non sia gia presente in anagrafe
    #rispondi
api.run(host="127.0.0.1", port=8080)