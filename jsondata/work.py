import json

import pymysql

# por Alex D. Aleluia

banco_nome = 'dbtemp'

def get_db_conn():
    conn = pymysql.connect(
        host='localhost', user='root', password='pl90alex',
        db=banco_nome
    )
    return conn

def main():
    query_estados = "SELECT * FROM estados"
    query_cidades = "SELECT * FROM cidades"
    estados = []
    cidades = []
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            # estados
            cursor.execute(query_estados)
            rp = cursor.fetchall()
            for e in rp:
                id_, nome, sigla = e
                elemento = {"id": id_, "nome": nome, "sigla": sigla}
                estados.append(elemento)
            
            json_estados = json.dumps(estados)
            with open('../estados.json', 'w') as hestados:
                hestados.write(json_estados)
            
            # cidades
            cursor.execute(query_cidades)
            rp = cursor.fetchall()
            for e in rp:
                id_, nome, estados_id = e
                elemento = {"id": id_, "nome": nome, "estados_id": estados_id}
                cidades.append(elemento)
            
            json_cidades = json.dumps(cidades)
            with open('../cidades.json', 'w') as hecidades:
                hecidades.write(json_cidades)

    finally:
        conn.close()

if __name__ == '__main__':
    main()


