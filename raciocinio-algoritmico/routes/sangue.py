from flask import Blueprint, jsonify
from openwith import ler_json

sangue_bp = Blueprint('sangue', __name__)

@sangue_bp.get("/sangue/listar")
def get_sangue():
    return jsonify(ler_json('sangue'))
