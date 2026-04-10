from flask import Blueprint, json, jsonify, request
from schemas.bolsas import BolsasSchema
import uuid

bolsas_bp = Blueprint('bolsas', __name__)

@bolsas_bp.get("/bolsas")
def get_bolsas2():
    with open('data/bolsas.json', 'r', encoding='utf-8') as listaBolsas:
        bolsas = json.load(listaBolsas)

        tipo = request.args.get('tipo_sangue', '').replace(' ', '+') or None

        resultado = []

        for bolsa in bolsas:
            if tipo and bolsa.get('tipo_sangue') != tipo:
                continue
            resultado.append(bolsa)
    return jsonify(resultado)

# rota para listar as bolsas de sangue
@bolsas_bp.get("/bolsas/listar")
def get_bolsas():
    with open('data/bolsas.json', 'r', encoding='utf-8') as listaBolsas:
        resposta = json.load(listaBolsas)

    return jsonify(resposta)

# rota para adicionar uma bolsa de sangue
@bolsas_bp.post("/bolsas/adicionar")
def add_bolsa():

    nova_bolsa = request.json

    nova_bolsa['id'] = str(uuid.uuid4())

    # chama validar do bolsasschema e passa o nova_bolsa
    # se erros_400 retornar lista vazia, a cond nao ativa, é falsa
    nova_bolsa, erros_400, erros_422 = BolsasSchema.validar(nova_bolsa)
    if erros_400:
        return jsonify({
            "erro": "Campos obrigatórios faltando",
            "campos": erros_400
        }), 400
    if erros_422:
        return jsonify({
            "erro": "Erros de validação",
            "campos": erros_422
        }), 422


    # chama function para calcular validade da bolsa, se tiver erro ele retorna a resposta com o erro
    nova_bolsa, erro = BolsasSchema.calcular_validade(nova_bolsa)
    if erro:
        return jsonify({"erro": erro}), 422

    with open('data/bolsas.json', 'r', encoding='utf-8') as listaBolsas:
        bolsas = json.load(listaBolsas)

    bolsas.append(nova_bolsa)

    with open('data/bolsas.json', 'w', encoding='utf-8') as listaBolsas:
        json.dump(bolsas, listaBolsas, indent=4, ensure_ascii=False)

    return jsonify(nova_bolsa), 201
