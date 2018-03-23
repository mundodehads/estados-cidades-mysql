import json

import pymysql

# por Alex D. Aleluia

banco_nome = 'dbtemp'

def get_db_conn():
    conn = pymysql.connect(
        host='localhost', user='root', password='',
        db=banco_nome
    )
    return conn

def get_many(conn, query):
    conn.execute(query)
    return conn.fetchall()

def save_string(content, path_file):
    with open(path_file, 'w') as hfile:
        hfile.write(content)

def main():
    query_estados = "SELECT * FROM estados"
    query_cidades = "SELECT * FROM cidades"
    estados = []
    cidades = []
    conn = get_db_conn()
    try:
        with conn.cursor() as cursor:
            # estados
            rp = get_many(cursor, query_estados)
            for e in rp:
                id_, nome, sigla = e
                elemento = {"id": id_, "nome": nome, "sigla": sigla}
                estados.append(elemento)
            
            json_estados = json.dumps(estados)
            save_string(json_estados, '../estados.json')
            
            # cidades
            rp = get_many(cursor, query_cidades)
            for e in rp:
                id_, nome, estados_id = e
                elemento = {"id": id_, "nome": nome, "estados_id": estados_id}
                cidades.append(elemento)
            
            json_cidades = json.dumps(cidades)
            save_string(json_cidades, '../cidades.json')

    finally:
        conn.close()

if __name__ == '__main__':
    main()

