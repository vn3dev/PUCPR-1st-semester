from datetime import datetime, timedelta

TIPOS_SANGUE_VALIDOS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# para bolsas de sangue, a validade varia de acordo com o conservante utilizado
VALIDADE_POR_SOLUCAO = {
    "ACD": 21,
    "CPD": 21,
    "CPDA-1": 35,
    "AS-1": 42,
    "AS-3": 42,
    "AS-5": 42,
}


class BolsasSchema:
    campos_obrigatorios = [
        "tipo_sangue",
        "quantidade_ml",
        "data_coleta",
        "solucao_conservante",
        "id_doador"
    ]

    campos_string = ["tipo_sangue", "data_coleta", "solucao_conservante"]
    campos_numericos = ["quantidade_ml"]

    # esse metodo valida os campos obrigatórios, verifica se o tipo de sangue é válido e se a quantidade é positivo
    @classmethod
    def validar(cls, bolsa):
        erros_400 = []
        erros_422 = []

        # compara cada um dos campos que veio no payload com a classe, se estiver faltando ele adiciona na list erros_400
        for campo in cls.campos_obrigatorios:
            if campo not in bolsa or bolsa[campo] == "" or bolsa[campo] is None:
                erros_400.append(campo)

        # valida se o tipo de sangue esta na lista
        if bolsa.get("tipo_sangue") not in TIPOS_SANGUE_VALIDOS:
            erros_422.append("tipo_sangue invalido. Valores aceitos: A+, A-, B+, B-, AB+, AB-, O+, O-")

        # loops p comparar se é string ou num
        for campo in cls.campos_string:
            valor = bolsa.get(campo)
            if valor is not None and not isinstance(valor, str):
                erros_422.append(f"{campo} deve ser uma string")

        for campo in cls.campos_numericos:
            valor = bolsa.get(campo)
            if valor is not None and not isinstance(valor, (int, float)):
                erros_422.append(f"{campo} deve ser um número")

        # valida se a quantidade de ml é um número e se não é negativa ou zero
        quantidade = bolsa.get("quantidade_ml")
        if isinstance(quantidade, (int, float)) and quantidade <= 0 and not None:
            erros_422.append("quantidade_ml deve ser um número positivo")

        return bolsa, erros_400, erros_422

    # esse metodo calcula a data de validade da bolsa com base na data de coleta e no tipo de solução conservante utilizada
    @classmethod
    def calcular_validade(cls, bolsa):
        solucao = bolsa["solucao_conservante"]

        # valida se a solucao esta na lista de solucoes reconhecidas, se não estiver ele retorna um erro
        if solucao not in VALIDADE_POR_SOLUCAO:
            erro = "Solução conservante '" + solucao + "' não reconhecida. Valores aceitos: ACD, CPD, CPDA-1, AS-1, AS-3, AS-5"
            return bolsa, erro

        # coloca o numero de dias da validade da bolsa de acordo com o conservante
        dias_de_validade = VALIDADE_POR_SOLUCAO[solucao]

        # valida se a data esta na forma correta
        try:
            data_coleta = datetime.strptime(bolsa["data_coleta"], "%Y-%m-%d")
        except ValueError:
            return bolsa, "data_coleta inválida. Use o formato YYYY-MM-DD"

        # valida se a data de coleta não é uma data futura
        hoje = datetime.now()
        if data_coleta > hoje:
            return bolsa, "data_coleta não pode ser uma data futura"

        data_validade = data_coleta + timedelta(days=dias_de_validade)
        bolsa["data_validade"] = data_validade.strftime("%Y-%m-%d")

        return bolsa, None
