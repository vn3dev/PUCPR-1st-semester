import re
from datetime import date, datetime

class DoadorSchema:
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
        "cadastrado"
    ]

    campos_string = ["nomeDoador", "cpfDoador", "telefoneDoador", "sexoDoador", "cidadeDoador", "EstadoDoador", "dataNascimentoDoador", "tipoSangue", "fatorRh", "dataUltimaDoacao", "localDoacao", "pressaoArterialDoador", "observacoes"]
    campos_numericos = ["pesoDoador", "alturaDoador", "quantidadeDoada", "hemoglobinaDoador"]
    campos_opcionais = ["alergiasDoador", "medicamentosDoador", "observacoes"]

    @classmethod
    def calcular_apto(cls, data: dict) -> bool:
        sexo = data.get("sexoDoador", "").upper()
        ultima_doacao = data.get("dataUltimaDoacao")

        intervalo = 60 if sexo == "H" else 90
        dias_desde_ultima = (date.today() - datetime.strptime(ultima_doacao, "%Y-%m-%d").date()).days

        return dias_desde_ultima >= intervalo

    @classmethod
    # passa a dict novo_doador e retorna tupla com dict para data, list para erros_400 e list para erros_422
    def validar(cls, data: dict, doadores: list = []) -> tuple[dict, list, list]:

        erros_400 = []
        erros_422 = []

        # validação para campos obrigatórios, se valor for vazio ele adiciona na list erros_400
        for campo in cls.campos_obrigatorios:
            valor = data.get(campo)
            if not valor:
                erros_400.append(campo)

        if any(d['cpfDoador'] == data.get('cpfDoador') for d in doadores):
            erros_422.append("cpfDoador já cadastrado")

        for campo in cls.campos_string:
            valor = data.get(campo)
            if valor is not None and not isinstance(valor, str):
                erros_422.append(f"{campo} deve ser uma string")

        nome = data.get("nomeDoador")
        if isinstance(nome, str) and nome and not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome):
            erros_422.append("nomeDoador não deve conter números ou caracteres especiais")

        sexo = data.get("sexoDoador")
        if isinstance(sexo, str) and sexo:
            if sexo.upper() not in ["H", "M"]:
                erros_422.append("sexoDoador deve ser 'H' para homem ou 'M' para mulher")

        for campo in cls.campos_numericos:
            valor = data.get(campo)
            if valor is not None and not isinstance(valor, (int, float)):
                erros_422.append(f"{campo} deve ser um número")

        # seta default os campos opcionais para None se n estiverem no payload
        for campo in cls.campos_opcionais:
            data.setdefault(campo, None)

        return data, erros_400, erros_422
