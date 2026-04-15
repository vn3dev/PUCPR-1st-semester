[< Voltar](../README.md)

# API Reference

## Rotas implementadas

| Rota | Método | Descrição |
|------|--------|-----------|
| /doadores | GET | Lista todos os doadores, com filtros opcionais por sexoDoador, tipoSangue e aptoParaDoacao |
| /doadores/&lt;id&gt; | GET | Busca um doador específico pelo ID |
| /doadores/adicionar | POST | Cadastra um novo doador |
| /bolsas | GET | Lista todas as bolsas, com filtros opcionais por tipo_sangue e valida |
| /bolsas/&lt;id&gt; | GET | Busca uma bolsa específica pelo ID |
| /bolsas/adicionar | POST | Registra uma nova bolsa de sangue |
| /sangue/listar | GET | Lista a quantidade de cada tipo de sangue em estoque |

---

## Campos esperados para POST /doadores/adicionar

| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| nomeDoador | string | Sim |
| cpfDoador | string | Sim |
| telefoneDoador | string | Sim |
| sexoDoador | string | Sim |
| cidadeDoador | string | Sim |
| EstadoDoador | string | Sim |
| pesoDoador | float | Sim |
| alturaDoador | float | Sim |
| dataNascimentoDoador | string (YYYY-MM-DD) | Sim |
| tipoSangue | string | Sim |
| fatorRh | string | Sim |
| dataUltimaDoacao | string (YYYY-MM-DD) | Sim |
| quantidadeDoada | int | Sim |
| localDoacao | string | Sim |
| hemoglobinaDoador | float | Sim |
| pressaoArterialDoador | string | Sim |
| aptoParaDoacao | boolean | Sim |
| cadastrado | boolean | Sim |
| alergiasDoador | string | Não |
| medicamentosDoador | string | Não |
| observacoes | string | Não |

---

## Campos esperados para POST /bolsas/adicionar

| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| tipo_sangue | string (ex: A+, O-) | Sim |
| quantidade_ml | float (deve ser positivo) | Sim |
| data_coleta | string (YYYY-MM-DD, não pode ser futura) | Sim |
| solucao_conservante | string (ACD, CPD, CPDA-1, AS-1, AS-3 ou AS-5) | Sim |
| id_doador | string | Sim |

> O campo `data_validade` é calculado automaticamente com base em `data_coleta` e `solucao_conservante`.

---

## Rotas ainda não implementadas

| Rota | Método | Descrição |
|------|--------|-----------|
| /doadores/deletar | DELETE | Exclui os dados de um doador |
| /doadores/update | PUT | Atualiza dados de registro de um doador |
| /sangue/atualizar/{id} | PUT | Atualiza a quantidade de um tipo de sangue no estoque |

---

## Status codes utilizados

| Código | Situação |
|--------|----------|
| 200 | Operação realizada com sucesso (quando não há criação de recurso) |
| 201 | Recurso criado com sucesso |
| 400 | Campos obrigatórios ausentes ou json mal formatado |
| 422 | Tipagem de dados incorreta |