from flask import Blueprint, json, jsonify, request
import uuid

doadores_bp = Blueprint('doadores', __name__)

# rota para listar todos as entidades do json
# fluxo:
# 1. lê o json doadores.json na permissão de readme, encoding para manter acentos
# 2. transforma o valor em uma dictionary do python com json.load
# 3. retorna uma resposta "jsonificada" do conteúdo da dictionary. Conteúddo jsonificado contém header content type e body com a dict
@doadores_bp.get("/doadores/listar")
def get_doadores():
    with open('doadores.json', 'r', encoding="utf-8") as listaDoador:
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

    # campos obrigatórios. todos exceto alergiasDoador, medicamentosDoador e observacoes
    campos_obrigatorios = [
        "nomeDoador",
        "cpfDoador",
        "telefoneDoador",
        "sexoDoador",
        "cidadeDoador",
        "EstadoDoador",
        "pesoDoador",
        "alturaDoador",
        "dataNascimentoDoador",
        "tipoSangue",
        "fatorRh",
        "dataUltimaDoacao",
        "quantidadeDoada",
        "localDoacao",
        "hemoglobinaDoador",
        "pressaoArterialDoador",
        "aptoParaDoacao",
        "cadastrado"
    ]

    # validação de campos obrigatórios
    faltando = [campo for campo in campos_obrigatorios if not novo_doador.get(campo)]
    if faltando:
        return jsonify({
            "erro": "Campos obrigatórios faltando",
            "campos": faltando
        }), 400

    # campos opcionais: definir como None se não presentes
    campos_opcionais = ["alergiasDoador", "medicamentosDoador", "observacoes"]
    for campo in campos_opcionais:
        if campo not in novo_doador:
            novo_doador[campo] = None

    with open('doadores.json', 'r', encoding="utf-8") as listaDoador:
        doadores = json.load(listaDoador)

    doadores.append(novo_doador)

    with open('doadores.json', 'w', encoding="utf-8") as listaDoador:
        json.dump(doadores, listaDoador, indent=4, ensure_ascii=False)

    return jsonify(novo_doador), 201
