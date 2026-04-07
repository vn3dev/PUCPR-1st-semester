# Projeto de Doação de Sangue

### 📖 [Documentação de Rotas](docs/routes.md)
### 📖 [Documentação de Rotas - Formato Tabela](docs/routes2.md)

## Changelogs:

### [Semana 2]

Início do projeto, foi criado estrutura json de [doadores](data/doadores.json) e [sangue](data/sangue.json). Além de, algumas rotas iniciais:

- `GET /doadores/listar`
- `POST /doadores/adicionar`
- `GET /sangue/listar`

### [Semana 3]

Foram criados os diretórios [/data](data), [/routes](routes) e [/schemas](schemas) para melhor organização do projeto e separação de funções e métodos.


Foi adicionada validação para campos faltantes em [doadores](routes/doadores.py). Também foram criadas duas rotas novas:

- `GET /bolsas/listar`
- `POST /bolsas/adicionar`

A nova rota POST tem uma validação de campo faltante e atributos com valores inválidos. Ainda é necessário validação de tipagem em todas as rotas POST. Para as validações existentes, o status code correto já foi implementado.

### [Semana 4]

Nenhuma rota nova foi criada. 

Foi realizada uma revisão das rotas já existentes e dos dados que entram no sistema. Para dados obrigatórios, foi implementada uma verificação de presença e tipagem usando `isinstance()`. E também, uma validação para CPF's já existentes.

[schemas/doadores.py linha 40-57](schemas/doadores.py#L40-L55)

[schemas/bolsas.py linhas 41-45](schemas/bolsas.py#L41-L45)

Para cada erro, o sistema retorna uma mensagem personalizada e um status code adequado.