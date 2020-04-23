from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def insert_dados():
    db.fila.insert({
        "_id":11,
        "empresa":"4linuxx",
        "cursos": [
            {"nome":"Python Fundamentals",
            "carga horaria":40},
            {"nome":"Python for sysadmin",
            "carga horaria":40}
        ]})


def select_dados():
    for r in db.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['cursos']:
            print('================')
            print(f"Nome: {c['nome']} \nCarga Horaria:{c['carga horaria']}\n")

#insert_dados()

select_dados()

