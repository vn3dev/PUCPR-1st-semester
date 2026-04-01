import re

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
        "aptoParaDoacao",
        "cadastrado"
    ]

    campos_opcionais = ["alergiasDoador", "medicamentosDoador", "observacoes"]

    @classmethod
    # passa a dict novo_doador e retorna tupla com dict para data, list para faltando e list para erros_tipo
    def validar(cls, data: dict) -> tuple[dict, list, list]:

        faltando = []
        erros_tipo = []

        # validação para campos obrigatórios, se valor for vazio ele adiciona na list faltando
        for campo in cls.campos_obrigatorios:
            valor = data.get(campo)
            if not valor:
                faltando.append(campo)

        nome = data.get("nomeDoador", "")
        if nome and not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome):
            erros_tipo.append("nomeDoador não deve conter números ou caracteres especiais")

        if not isinstance(data.get("quantidadeDoada"), (int, float)):
            erros_tipo.append("quantidadeDoada deve ser um número")

        if not isinstance(data.get("pesoDoador"), (int, float)):
            erros_tipo.append("pesoDoador deve ser um número")

        if not isinstance(data.get("alturaDoador"), (int, float)):
            erros_tipo.append("alturaDoador deve ser um número")

        if not isinstance(data.get("hemoglobinaDoador"), (int, float)):
            erros_tipo.append("hemoglobinaDoador deve ser um número")

        # seta default os campos opcionais para None se n estiverem no payload
        for campo in cls.campos_opcionais:
            data.setdefault(campo, None)

        return data, faltando, erros_tipo
