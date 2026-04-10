# Projeto de Doação de Sangue

### 📖 [Documentação de Rotas](docs/routes.md)

###  [Documentação de Rotas - Formato Tabela](docs/routes2.md)

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

Foi realizada uma revisão das rotas já existentes e dos dados que entram no sistema. Foi implementada uma verificação de presença e tipagem usando `isinstance()`. 

E também, validações específicas para os campos:
1. sexoDoador: agora só aceita "h", "H", "m" ou "M".

2. quantidade_ml: só deve aceitar numeros positivos.
    
3. nomeDoador: foi adicionado regex para aceitar somente letras.

[schemas/doadores.py linha 47-72](schemas/doadores.py#L47-L73)

[schemas/bolsas.py linhas 41-45](schemas/bolsas.py#L35-L58)

Para cada erro, o sistema retorna uma mensagem personalizada e um status code adequado.

Além disso, foram adicionadas funções para tarefas especificas:
1. Calcular se o doador esta apto com base no sexo e na data da ultima doação. [schemas/doadores.py linha 29-37](schemas/doadores.py#L29-L38)
2. Calcular a data da validade da bolsa com base no tipo de conservante. [schemas/bolsas.py linhas 62-86](schemas/bolsas.py#L63-L88)

Foram criadas tabelas de validações, como solicitado na atividade da semana 4.

###  [Tabela de Validações - Semana 4](docs/tabelas-semana4.md)

###  [Prints do Postman - Semana 4](docs/prints-semana4.md)
