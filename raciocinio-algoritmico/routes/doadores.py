from flask import Blueprint, jsonify, request
from schemas.doadores import DoadorSchema
from openwith import ler_json, salvar_json
import uuid

doadores_bp = Blueprint('doadores', __name__)

@doadores_bp.get("/doadores/<id>")
def get_doador(id):
    doadores = ler_json('doadores')

    for doador in doadores:
        if doador.get('id') == id:
            return jsonify(doador)

    return jsonify({"erro": "Doador não encontrado"}), 404

# adiciona filtros para buscar doadores por sexo, tipo de sangue e aptidão para doação
@doadores_bp.get("/doadores")
def get_doadores(id=None):
    doadores = ler_json('doadores')

    sexo        = request.args.get('sexoDoador')
    tipo_sangue = request.args.get('tipoSangue')
    apto        = request.args.get('aptoParaDoacao')

    resultado = []

    for doador in doadores:
        if sexo        and doador.get('sexoDoador') != sexo:
            continue
        if tipo_sangue and doador.get('tipoSangue') != tipo_sangue:
            continue
        if apto is not None:
            apto_bool = apto.lower() == 'true'
            if doador.get('aptoParaDoacao') != apto_bool:
                continue
        resultado.append(doador)

    return jsonify(resultado)

@doadores_bp.put("/doadores/atualizar/<id>")
def atualizar(id):
    doadores = ler_json('doadores')

    dados = request.get_json(force=True, silent=True)
    if not dados:
        return jsonify({"erro": "Body da requisição inválido ou ausente"}), 400

    dados, erros_400, erros_422 = DoadorSchema.validar_atualizacao(dados)
    if erros_400:
        return jsonify({
            "erro": "Campos não permitidos",
            "campos": erros_400
        }), 400
    if erros_422:
        return jsonify({
            "erro": "Tipo de dado inválido",
            "campos": erros_422
        }), 422

    for doador in doadores:
        if doador.get('id') == id:
            doador.update(dados)
            doador['aptoParaDoacao'] = DoadorSchema.calcular_apto(doador)
            salvar_json('doadores', doadores)
            return jsonify(doador), 200

    return jsonify({"erro": "Doador não encontrado"}), 404

@doadores_bp.delete("/doadores/deletar/<id>")
def deletar(id):
    doadores = ler_json('doadores')

    for i, doador in enumerate(doadores):
        if doador.get('id') == id:
            del doadores[i]
            salvar_json('doadores', doadores)
            return jsonify({"mensagem": "Doador deletado com sucesso"}), 200

    return jsonify({"erro": "Doador não encontrado"}), 404

@doadores_bp.post("/doadores/adicionar")
def add_doador():
    novo_doador = request.json
    novo_doador['id'] = str(uuid.uuid4())

    doadores = ler_json('doadores')

    # validação e normalização dos campos
    # se erros_400/erros_422 voltarem vazios, as condicionais são falsas, n ativam
    novo_doador, erros_400, erros_422 = DoadorSchema.validar(novo_doador, doadores)
    if erros_400:
        return jsonify({
            "erro": "Campos obrigatorios faltando",
            "campos": erros_400
        }), 400
    if erros_422:
        return jsonify({
            "erro": "Tipo de dado inválido",
            "campos": erros_422
        }), 422

    novo_doador['aptoParaDoacao'] = DoadorSchema.calcular_apto(novo_doador)
    doadores.append(novo_doador)
    salvar_json('doadores', doadores)

    return jsonify(novo_doador), 201
