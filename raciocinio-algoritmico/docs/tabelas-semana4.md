[< Voltar](../README.md)

## /doadores/adicionar

| Rota | Método | Campo | Tipo esperado | Obrigatório |
|------|--------|-------|---------------|-------------|
| /doadores/adicionar | POST | nomeDoador | string | Sim |
| /doadores/adicionar | POST | cpfDoador | string | Sim |
| /doadores/adicionar | POST | telefoneDoador | string | Sim |
| /doadores/adicionar | POST | sexoDoador | string | Sim |
| /doadores/adicionar | POST | cidadeDoador | string | Sim |
| /doadores/adicionar | POST | EstadoDoador | string | Sim |
| /doadores/adicionar | POST | pesoDoador | número | Sim |
| /doadores/adicionar | POST | alturaDoador | número | Sim |
| /doadores/adicionar | POST | dataNascimentoDoador | string | Sim |
| /doadores/adicionar | POST | tipoSangue | string | Sim |
| /doadores/adicionar | POST | fatorRh | string | Sim |
| /doadores/adicionar | POST | dataUltimaDoacao | string | Sim |
| /doadores/adicionar | POST | quantidadeDoada | número | Sim |
| /doadores/adicionar | POST | localDoacao | string | Sim |
| /doadores/adicionar | POST | hemoglobinaDoador | número | Sim |
| /doadores/adicionar | POST | pressaoArterialDoador | string | Sim |
| /doadores/adicionar | POST | cadastrado | booleano | Sim |
| /doadores/adicionar | POST | alergiasDoador | string | Não |
| /doadores/adicionar | POST | medicamentosDoador | string | Não |
| /doadores/adicionar | POST | observacoes | string | Não |

## /bolsas/adicionar

| Rota | Método | Campo | Tipo esperado | Obrigatório |
|------|--------|-------|---------------|-------------|
| /bolsas/adicionar | POST | tipo_sangue | string | Sim |
| /bolsas/adicionar | POST | quantidade_ml | número | Sim |
| /bolsas/adicionar | POST | data_coleta | string | Sim |
| /bolsas/adicionar | POST | solucao_conservante | string | Sim |
| /bolsas/adicionar | POST | id_doador | string | Sim |

---

## Validações — /doadores/adicionar

| Campo | Situação | Mensagem retornada | Status code |
|-------|----------|--------------------|-------------|
| qualquer campo obrigatório | ausente ou vazio | `"Campos obrigatorios faltando"` + lista dos campos | 400 |
| cpfDoador | CPF já cadastrado | `"cpfDoador já cadastrado"` | 422 |
| nomeDoador | tipo inválido (não é string) | `"nomeDoador deve ser uma string"` | 422 |
| nomeDoador | contém números ou caracteres especiais | `"nomeDoador não deve conter números ou caracteres especiais"` | 422 |
| sexoDoador | valor diferente de `"H"` ou `"M"` | `"sexoDoador deve ser 'H' para homem ou 'M' para mulher"` | 422 |
| cpfDoador / telefoneDoador / etc. | tipo inválido (não é string) | `"{campo} deve ser uma string"` | 422 |
| pesoDoador / alturaDoador / etc. | tipo inválido (não é número) | `"{campo} deve ser um número"` | 422 |

## Validações — /bolsas/adicionar

| Campo | Situação | Mensagem retornada | Status code |
|-------|----------|--------------------|-------------|
| qualquer campo obrigatório | ausente ou vazio | `"Campos obrigatórios faltando"` + lista dos campos | 400 |
| tipo_sangue | valor fora de A+, A-, B+, B-, AB+, AB-, O+, O- | `"tipo_sangue invalido. Valores aceitos: A+, A-, B+, B-, AB+, AB-, O+, O-"` | 422 |
| tipo_sangue / data_coleta / etc. | tipo inválido (não é string) | `"{campo} deve ser uma string"` | 422 |
| quantidade_ml | tipo inválido (não é número) | `"quantidade_ml deve ser um número"` | 422 |
| quantidade_ml | valor zero ou negativo | `"quantidade_ml deve ser um número positivo"` | 422 |
| solucao_conservante | valor fora de ACD, CPD, CPDA-1, AS-1, AS-3, AS-5 | `"Solução conservante '{valor}' não reconhecida. Valores aceitos: ACD, CPD, CPDA-1, AS-1, AS-3, AS-5"` | 422 |
| data_coleta | formato diferente de `YYYY-MM-DD` | `"data_coleta inválida. Use o formato YYYY-MM-DD"` | 422 |
| data_coleta | data futura | `"data_coleta não pode ser uma data futura"` | 422 |

---

## Status codes utilizados

| Código | Situação |
|--------|----------|
| 201 | Recurso criado com sucesso |
| 400 | Campo obrigatório ausente ou valor inválido |
| 422 | Campo presente, mas com tipo de dado inválido |