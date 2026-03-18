# Documento de Rotas

[17/03/2026] - Vinicius

## Rotas implementadas:
- `GET /pacientes/listar`
- `POST /pacientes/adicionar`
- `GET /sangue/listar`

## Rotas ainda não implementadas:

- `PUT /sangue/update`
    - A ideia é que o JSON de sangue não receba novos sangues, todos os 8 tipos de sangue ja foram listados. Minha intenção é alterar apenas o atributo quantidade para fazer o controle de estoque
- `DELETE /pacientes/deletar`
    - Para excluir os dados dos doadores, em caso de exclusão de conta
- `PUT /pacientes/update`
    - Para atualizar dados de registro dos doadores

Essas foram todas as rotas que arquitetei até o momento, acredito que novas rotas possam surgir conforme eu for me aprofundando no projeto.