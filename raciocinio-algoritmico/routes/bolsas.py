from flask import Blueprint, jsonify, request
from schemas.bolsas import BolsasSchema
from openwith import ler_json, salvar_json
from datetime import date
import uuid

bolsas_bp = Blueprint('bolsas', __name__)

@bolsas_bp.get("/bolsas/<id>")
def get_bolsa(id):
    bolsas = ler_json('bolsas')

    for bolsa in bolsas:
        if bolsa.get('id') == id:
            return jsonify(bolsa)

    return jsonify({"erro": "Bolsa não encontrada"}), 404

# adiciona filtros para buscar bolsas por tipo de sangue e validade
@bolsas_bp.get("/bolsas")
def get_bolsas():
    bolsas = ler_json('bolsas')

    tipo  = request.args.get('tipo_sangue', '').replace(' ', '+') or None
    valida = request.args.get('valida')

    resultado = []

    for bolsa in bolsas:
        if tipo and bolsa.get('tipo_sangue') != tipo:
            continue
        if valida is not None:
            data_validade = date.fromisoformat(bolsa.get('data_validade'))
            eh_valida = data_validade >= date.today()
            if (valida.lower() == 'true') != eh_valida:
                continue
        resultado.append(bolsa)

    return jsonify(resultado)

@bolsas_bp.put("/bolsas/atualizar/<id>")
def atualizar(id):
    bolsas = ler_json('bolsas')

    dados = request.get_json(force=True, silent=True)
    if not dados:
        return jsonify({"erro": "Body da requisição inválido ou ausente"}), 400

    dados, erros_400, erros_422 = BolsasSchema.validar_atualizacao(dados)
    if erros_400:
        return jsonify({
            "erro": "Campos não permitidos",
            "campos": erros_400
        }), 400
    if erros_422:
        return jsonify({
            "erro": "Erros de validação",
            "campos": erros_422
        }), 422

    for bolsa in bolsas:
        if bolsa.get('id') == id:
            bolsa.update(dados)
            if "data_coleta" in dados or "solucao_conservante" in dados:
                bolsa, erro = BolsasSchema.calcular_validade(bolsa)
                if erro:
                    return jsonify({"erro": erro}), 422
            salvar_json('bolsas', bolsas)
            return jsonify(bolsa), 200

    return jsonify({"erro": "Bolsa não encontrada"}), 404

@bolsas_bp.delete("/bolsas/deletar/<id>")
def deletar(id):
    bolsas = ler_json('bolsas')

    for i, bolsa in enumerate(bolsas):
        if bolsa.get('id') == id:
            del bolsas[i]
            salvar_json('bolsas', bolsas)
            return jsonify({"mensagem": "Bolsa deletada com sucesso"}), 200

    return jsonify({"erro": "Bolsa não encontrada"}), 404

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

    bolsas = ler_json('bolsas')
    bolsas.append(nova_bolsa)
    salvar_json('bolsas', bolsas)

    return jsonify(nova_bolsa), 201
