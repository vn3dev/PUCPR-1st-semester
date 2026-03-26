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

    # esse metodo valida os campos obrigatórios, verifica se o tipo de sangue é válido e se a quantidade é positivo
    @classmethod
    def validar(cls, bolsa):
        campos_faltando = []

        # compara cada um dos campos que veio no payload com a classe, se estiver faltando ele adiciona na list campos_faltando
        for campo in cls.campos_obrigatorios:
            if campo not in bolsa or bolsa[campo] == "" or bolsa[campo] is None:
                campos_faltando.append(campo)

        # valida se o tipo de sangue esta na lista
        if bolsa["tipo_sangue"] not in TIPOS_SANGUE_VALIDOS:
            campos_faltando.append("tipo_sangue invalido. Valores aceitos: A+, A-, B+, B-, AB+, AB-, O+, O-")
            return bolsa, campos_faltando

        # valida se a quantidade de ml não é negativa ou zero
        if bolsa["quantidade_ml"] <= 0:
            campos_faltando.append("quantidade_ml deve ser um número positivo")
            return bolsa, campos_faltando

        return bolsa, campos_faltando

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
