from flask import Blueprint, json, jsonify, request

sangue_bp = Blueprint('sangue', __name__)

# rota para listar a quantidade de sangue
# fluxo - o mesmo da rota anterior
@sangue_bp.get("/sangue/listar")
def get_sangue():
    with open('sangue.json', 'r') as listaSangue:
        resposta = json.load(listaSangue)

    return jsonify(resposta)

# rota para atualizar a quantidade de sangue
# fluxo:
# 1. obtém tipo e fatorRh da URL
# 2. o conteúdo do body da requisição é armazenado em uma dict python chamada payload
# 3. validação básica do payload para garantir que o campo quantidade está presente. Se n, retorna 400
# 4. validação de tipagem para garantir que quantidade é um número inteiro. Se n, retorna 400
# 5. lê sangue.json e armazena o conteúdo em uma dict chamada sangue
# 6. compara o tipo e fatorRh da URL com os do json para encontrar o registro correspondente. Se n, retorna 404
# 7. valida quantidade do registro encontrado para garantir que é um número inteiro. Se n, considera quantidade atual como 0
# 8. calcula o novo valor da quantidade somando a quantidade atual com a quantidade do payload. Se o novo valor for negativo, retorna 400
# 9. atualiza a quantidade do registro encontrado com o novo valor calculado
# 10. reescreve o json com a dict atualizada
# 11. retorna o registro atualizado com status code 200
@sangue_bp.put("/sangue/atualizar/<tipo>/<fatorRh>")
def update_sangue(tipo, fatorRh):

    payload = request.json

    # validação básica do payload para garantir que quantidade está no payload
    if not payload or 'quantidade' not in payload:
        return jsonify({"error": "Corpo deve ter quantidade"}), 400

    # validação de tipagem
    try:
        delta = int(payload['quantidade'])
    except (ValueError, TypeError):
        return jsonify({"error": "quantidade deve ser número inteiro"}), 400

    # normaliza tipo e fatorRh da URL
    tipo = str(tipo).upper()
    fatorRh = str(fatorRh).replace('+', '+').replace('-', '-')

    # abre o json e cria uma dict para manipular os dados
    with open('sangue.json', 'r', encoding='utf-8') as listaSangue:
        sangue = json.load(listaSangue)

    # compara o tipo e fatorRh da URL com os do json
    registro = next((item for item in sangue if item.get('tipo') == tipo and item.get('fatorRh') == fatorRh), None)
    if registro is None:
        return jsonify({"error": "Registro não encontrado para tipo/fatorRh fornecido"}), 404

    # valida quantidade para ser inteiro
    try:
        atual = int(registro.get('quantidade', 0))
    except (ValueError, TypeError):
        atual = 0

    # calcula o novo valor da quantidade somando a quantidade atual com a quantidade do payload
    novo_valor = atual + delta
    if novo_valor < 0:
        return jsonify({"error": "Quantidade final não pode ser negativa"}), 400

    # atualiza a quantidade do registro encontrado com o novo valor calculado
    registro['quantidade'] = str(novo_valor)

    # reescreve o json com a dict atualizada
    with open('sangue.json', 'w', encoding='utf-8') as listaSangue:
        json.dump(sangue, listaSangue, indent=4, ensure_ascii=False)

    # retorna o registro atualizado com status code 200
    return jsonify(registro), 200
