# Documento de Rotas

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
            "id": UUID
        },
    ...
    ```

- `POST /doadores/adicionar`
    - Essa rota faz um POST para adicionar um novo doador na lista.

    Body da **request** ainda sem validação:
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
        "alergiasDoador": "string",       // opcional
        "medicamentosDoador": "string",   // opcional
        "aptoParaDoacao": true,
        "observacoes": "string",          // opcional
        "cadastrado": true,
    }
    ```
- `GET /sangue/listar`
    - Essa rota deve mostrar a quantidade de cada tipo de sangue no banco de dados.
    
    Body da **response** deve retornar uma lista com todos os 4 tipos e 4 fatoresRh:
    ```ts
    [
        {
            "tipo": "A+",
            "quantidade": "0"
        },
    ...
    ```

- `GET /bolsas/listar`
    - Essa rota mostra todas as bolsas de sangue em estoque.

    Body da **response** deve retornar uma lista com os atributos:
    ```ts
    [
        {
            "tipo_sangue": "O-",
            "quantidade_ml": 500,
            "data_coleta": "2026-03-22",
            "solucao_conservante": "AS-1",
            "id_doador": "456",
            "id": "82427272-f82e-47cd-88cb-b9cf9396dce0",
            "data_validade": "2026-05-03"
        }
    ]

- `GET /bolsas/adicionar`
    - Essa rota adiciona adiciona uma nova bolsa ao banco.

    Body do **request** ainda sem validação:
    ```ts
    [
        {
            "tipo_sangue": "string",
            "quantidade_ml": float,
            "data_coleta": "YYYY-MM-DD",
            "solucao_conservante": "string",
            "id_doador": "string"
        }
    ]

## Rotas ainda não implementadas:

- `DELETE /doadores/deletar`
    - Para excluir os dados dos doadores, em caso de exclusão de conta
- `PUT /doadores/update`
    - Para atualizar dados de registro dos doadores
- `GET /doadores/{id}`
    - Busca dados de um paciente especifico pelo id
- `PUT /sangue/atualizar/{id}`
    - Atualiza a quantidade em L do banco de sangue do front

Essas foram todas as rotas que arquitetei até o momento, acredito que novas rotas possam surgir conforme eu for me aprofundando no projeto.