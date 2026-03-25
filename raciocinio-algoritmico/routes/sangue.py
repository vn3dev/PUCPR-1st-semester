from flask import Blueprint, json, jsonify, request
from schemas.sangue import SangueUpdateSchema

sangue_bp = Blueprint('sangue', __name__)

# rota para listar a quantidade de sangue
# fluxo - o mesmo da rota anterior
@sangue_bp.get("/sangue/listar")
def get_sangue():
    with open('data/sangue.json', 'r', encoding='utf-8') as listaSangue:
        resposta = json.load(listaSangue)

    return jsonify(resposta)
