from flask import Blueprint, json, jsonify, request
from schemas.doadores import DoadorSchema
import uuid

doadores_bp = Blueprint('doadores', __name__)

# rota para buscar um doador por id
@doadores_bp.get("/doadores/<id>")
def get_doador(id):
    with open('data/doadores.json', 'r', encoding="utf-8") as listaDoador:
        doadores = json.load(listaDoador)

        for doador in doadores:
            if doador.get('id') == id:
                return jsonify(doador)

    return jsonify({"erro": "Doador não encontrado"}), 404

# adiciona filtros para buscar doadores por sexo, tipo de sangue e aptidão para doação
@doadores_bp.get("/doadores")
def get_doadores2():
    with open('data/doadores.json', 'r', encoding='utf-8') as listaDoador:
        doadores = json.load(listaDoador)

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

# rota para listar todos as entidades do json
# fluxo:
# 1. lê o json doadores.json na permissão de readme, encoding para manter acentos
# 2. transforma o valor em uma dictionary do python com json.load
# 3. retorna uma resposta "jsonificada" do conteúdo da dictionary. Conteúddo jsonificado contém header content type e body com a dict
@doadores_bp.get("/doadores")
def get_doadores():
    with open('data/doadores.json', 'r', encoding="utf-8") as listaDoador:
        resposta = json.load(listaDoador)

    return jsonify(resposta)

# rota para adicionar um doador
# fluxo:
# 1. o conteúdo do body da requisição é armazenado em uma dict python chamada novo_doador
# 2. lê doadores.json e armazena o conteudo em uma dict chamada doadores
# 3. da append na dict doadores com o conteudo do body da request q agora e a dict
# 4. abre o arquivo em modo write "w" e reescreve a dict antiga doadores do "banco" com a nova dict doadores
# 5. retorna uma response com o conteudo adicionado e um status code 201 que significa criado
@doadores_bp.post("/doadores/adicionar")
def add_doador():

    novo_doador = request.json

    # gerar UUID automaticamente para o id
    novo_doador['id'] = str(uuid.uuid4())

    with open('data/doadores.json', 'r', encoding="utf-8") as listaDoador:
        doadores = json.load(listaDoador)

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

    with open('data/doadores.json', 'w', encoding="utf-8") as listaDoador:
        json.dump(doadores, listaDoador, indent=4, ensure_ascii=False)

    return jsonify(novo_doador), 201