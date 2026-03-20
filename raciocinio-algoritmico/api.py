from flask import Flask, json, jsonify, request

app = Flask(__name__)

# mantem a ordem dos atributos na hora de exibir o json pq sou fresco
app.json.sort_keys = False

# rota para listar todos as entidades do json
# fluxo:
# 1. lê o json doadores.json na permissão de readme, encoding para manter acentos
# 2. transforma o valor em uma dictionary do python com json.load
# 3. retorna uma resposta "jsonificada" do conteúdo da dictionary. Conteúddo jsonificado contém header content type e body com a dict
@app.get("/doadores/listar")
def get_doadores():
    with open('doadores.json', 'r', encoding="utf-8") as listaDoador:
        resposta = json.load(listaDoador)
    
    return jsonify(resposta)

# rota para listar a quantidade de sangue
# fluxo - o mesmo da rota anterior
@app.get("/sangue/listar")
def get_sangue():
    with open('sangue.json', 'r') as listaSangue:
        resposta = json.load(listaSangue)

    return jsonify(resposta)

# rota para adicionar um doador
# fluxo:
# 1. o conteúdo do body da requisição é armazenado em uma dict python chamada novo_doador
# 2. lê doadores.json e armazena o conteudo em uma dict chamada doadores
# 3. da append na dict doadores com o conteudo do body da request q agora e a dict
# 4. abre o arquivo em modo write "w" e reescreve a dict antiga doadores do "banco" com a nova dict doadores
# 5. retorna uma response com o conteudo adicionado e um status code 201 que significa criado
@app.post("/doadores/adicionar")
def add_doador():

    novo_doador = request.json

    with open('doadores.json', 'r', encoding="utf-8") as listaDoador:
        doadores = json.load(listaDoador)

    doadores.append(novo_doador)

    with open('doadores.json', 'w', encoding="utf-8") as listaDoador:
        json.dump(doadores, listaDoador, indent=4, ensure_ascii=False)

    return jsonify(novo_doador), 201

# rota para atualizar a quantidade de sangue
# fluxo:
# 1. o conteúdo do body da requisição é armazenado em uma dict python chamada payload
# 2. validação básica do payload para garantir que os campos tipo, fatorRh e quantidade estão presentes. Se n, retorna 400
# 3. validação de tipagem para garantir que quantidade é um número inteiro. Se n, retorna 400
# 4. validação dos campos tipo e fatorRh para garantir que tipo é uma string e fatorRh é uma string com + ou -. Se n, retorna 400
# 5. lê sangue.json e armazena o conteúdo em uma dict chamada sangue
# 6. compara o tipo e fatorRh do payload com os do json para encontrar o registro correspondente. Se n, retorna 404
# 7. valida quantidade do registro encontrado para garantir que é um número inteiro. Se n, considera quantidade atual como 0
# 8. calcula o novo valor da quantidade somando a quantidade atual com a quantidade do payload. Se o novo valor for negativo, retorna 400
# 9. atualiza a quantidade do registro encontrado com o novo valor calculado
# 10. reescreve o json com a dict atualizada
# 11. retorna o registro atualizado com status code 200
@app.put("/sangue/atualizar")
def update_sangue():

    payload = request.json

    # validação básica do payload para garantir todos os campos no payload
    if not payload or 'tipo' not in payload or 'fatorRh' not in payload or 'quantidade' not in payload:
        return jsonify({"error": "Corpo deve ter tipo, fatorRh e quantidade"}), 400

    # validação de tipagem
    try:
        delta = int(payload['quantidade'])
    except (ValueError, TypeError):
        return jsonify({"error": "quantidade deve ser número inteiro"}), 400

    # validação dos campos de tipo e fatorRh
    tipo = str(payload['tipo']).upper()
    fatorRh = str(payload['fatorRh']).replace('+', '+').replace('-', '-')

    # abre o json e cria uma dict para manipular os dados
    with open('sangue.json', 'r', encoding='utf-8') as listaSangue:
        sangue = json.load(listaSangue)

    # compara o tipo e fatorRh do payload com os do json
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

app.run(debug = True)