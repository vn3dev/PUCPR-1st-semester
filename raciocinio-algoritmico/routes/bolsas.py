from flask import Blueprint, json, jsonify

bolsas_bp = Blueprint('bolsas', __name__)

# rota para listar as bolsas de sangue
@bolsas_bp.get("/bolsas/listar")
def get_bolsas():
    with open('data/bolsas.json', 'r', encoding='utf-8') as listaBolsas:
        resposta = json.load(listaBolsas)

    return jsonify(resposta)
