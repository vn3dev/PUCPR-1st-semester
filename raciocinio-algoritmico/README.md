# Projeto de Doação de Sangue

### 📖 [Documentação de Rotas](docs/routes.md)

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