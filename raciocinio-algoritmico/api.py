from flask import Flask, json, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False

@app.get("/pacientes/listar")
def get_paciente():
    with open('pacientes.json', 'r', encoding="utf-8") as listaDoador:
        resposta = json.load(listaDoador)
    
    return jsonify(resposta)

@app.get("/sangue/listar")
def get_sangue():
    with open('sangue.json', 'r') as listaSangue:
        resposta = json.load(listaSangue)

    return jsonify(resposta)

@app.post("/pacientes/adicionar")
def add_doador():

    novo_doador = request.json

    with open('pacientes.json', 'r', encoding="utf-8") as listaDoador:
        doadores = json.load(listaDoador)

    doadores.append(novo_doador)

    with open('pacientes.json', 'w', encoding="utf-8") as listaDoador:
        json.dump(doadores, listaDoador, indent=4, ensure_ascii=False)

    return jsonify(novo_doador), 201    
    
app.run(debug = True)