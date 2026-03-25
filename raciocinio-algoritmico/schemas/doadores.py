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
    # passa a dict novo_doador e retorna tupla com dict para data e list para faltando
    def validar(cls, data: dict) -> tuple[dict, list]:

        faltando = []

        # validação para campos obrigatórios, se valor for vazio ele adiciona na list faltando
        for campo in cls.campos_obrigatorios:
            valor = data.get(campo)
            if not valor:
                faltando.append(campo)

        # seta default os campos opcionais para None se n estiverem no payload
        for campo in cls.campos_opcionais:
            data.setdefault(campo, None)

        return data, faltando
