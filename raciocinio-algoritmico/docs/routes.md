# Documento de Rotas

[17/03/2026] - Vinicius

## Rotas implementadas:
- `GET /doadores/listar`
    - Essa rota lista todos os doadores cadastrados no "banco de dados"
    Body da **response**:
    ```ts
    [
        {
            "nomeDoador": "Lord Kainan, senhor das sombras",
            "cpfDoador": "123.456.789-00",
            "telefoneDoador": "(11) 98765-4321",
            "sexoDoador": "Masculino",
            "cidadeDoador": "São Paulo",
            "EstadoDoador": "SP",
            "pesoDoador": 85.5,
            "alturaDoador": 1.8,
            "dataNascimentoDoador": "2000-01-15",
            "tipoSangue": "O",
            "fatorRh": "+",
            "dataUltimaDoacao": "2024-06-01",
            "quantidadeDoada": 500,
            "localDoacao": "UCT Toledo",
            "hemoglobinaDoador": 15.2,
            "pressaoArterialDoador": "120/80",
            "alergiasDoador": "Nenhuma",
            "medicamentosDoador": "Nenhum",
            "aptoParaDoacao": true,
            "observacoes": "Doador frequente",
            "cadastrado": true,
            "id": 1
        },
    ...
    ```

- `POST /doadores/adicionar`
    - Essa rota faz um POST para adicionar um novo doador na lista.

    Body da **request**, ainda sem validação:
    ```ts
    {
        "nomeDoador": "string",
        "cpfDoador": "string",
        "telefoneDoador": "string",
        "sexoDoador": "string",
        "cidadeDoador": "string",
        "EstadoDoador": "string",
        "pesoDoador": 0.0,
        "alturaDoador": 0.0,
        "dataNascimentoDoador": "YYYY-MM-DD",
        "tipoSangue": "string",
        "fatorRh": "string",
        "dataUltimaDoacao": "YYYY-MM-DD",
        "quantidadeDoada": 0,
        "localDoacao": "string",
        "hemoglobinaDoador": 0.0,
        "pressaoArterialDoador": "string",
        "alergiasDoador": "string",
        "medicamentosDoador": "string",
        "aptoParaDoacao": true,
        "observacoes": "string",
        "cadastrado": true,
        "id": 0
    }
    ```
- `GET /sangue/listar`
    - Essa rota deve mostrar a quantidade de cada tipo de sangue no banco de dados.
    
    Body da **response**, deve retornar uma lista com todos os 4 tipos e 4 fatoresRh:
    ```ts
    [
        {
            "tipo": "A",
            "fatorRh": "-",
            "quantidade": "0"
        },
    ...
    ```

- `PUT /sangue/atualizar/{tipo}/{fatorRh}`
    - Essa rota atualiza a quantidade de sangue disponível na tela do app. Pretendo usar essa rota apenas para atualizar o gráfico de estoque do mobile
    
    Body da **request** deve ser:
    ```ts
    {
        "quantidade": "inteiro"
    }
    ```

## Rotas ainda não implementadas:

- `DELETE /doadores/deletar`
    - Para excluir os dados dos doadores, em caso de exclusão de conta
- `PUT /doadores/update`
    - Para atualizar dados de registro dos doadores
- `GET /doadores/id`
    - Busca dados de um paciente especifico pelo id

Essas foram todas as rotas que arquitetei até o momento, acredito que novas rotas possam surgir conforme eu for me aprofundando no projeto.