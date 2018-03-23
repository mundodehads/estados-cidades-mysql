*ESTADOS-CIDADES-MYSQL*
===================

Neste repositório você encontra todos 27 estados e 5570 cidades retirados da base de dados do IBGE.
Os dados estão em utf8 para consumir em mysql, a tabela cidades possui uma FK para identificar qual seu estado.

Dados retirados do repositório: [chandez/Estados-Cidades-IBGE](https://github.com/chandez/Estados-Cidades-IBGE) e modificados por mim.


---
## Arquivos json para inserir dados através de fixtures

### cidades.json
array de {"id": id, "nome": nome, "estados_id": estados_id}

### estados.json
array de {"id": id, "nome": nome, "sigla": sigla}


Como os arquivos foram gerados se encontra em jsondata/comandos.txt


[License description](LICENSE.md).
