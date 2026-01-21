import requests
import sqlite3

## 1) conectando com a API da câmara

def buscar_deputados():

    url = "https://dadosabertos.camara.leg.br/api/v2/deputados"

    params = {
        'siglaUf': 'PI', 
        'ordem': 'ASC', 
        'ordenarPor': 'nome'}

    headers = {'Accept': 'application/json'}

    try:
        response = requests.get(url, params=params, headers=headers)

        response.raise_for_status()

        return response.json()['dados']

    except Exception as e:

        print(f"Tente de novoo, erro ao acessar API: {e}")

        return []

## 2) API ---> BANCO
def salvar_no_banco(lista_deputados):
    conectar = sqlite3.connect('camara_dados.db')
    cursor = conectar.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS deputados (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            partido TEXT,
            uf TEXT
        )
    ''')

    cursor.execute('DELETE FROM deputados') 

    ## 3) Inserindo os dados da API
    for deputado in lista_deputados:
        cursor.execute('''
            INSERT INTO deputados (id, nome, partido, uf)
            VALUES (?, ?, ?, ?)
        ''', (deputado['id'], deputado['nome'], deputado['siglaPartido'], deputado['siglaUf']))

    conectar.commit()
    conectar.close()
    print("Dados salvos no SQLite!!")

## 4) EM EXECUÇÃO
if __name__ == "__main__":
    print("Rodando o request")
    dados = buscar_deputados()
    
    if dados:
        salvar_no_banco(dados)
        
        conectar = sqlite3.connect('camara_dados.db')

        cursor = conectar.cursor()

        cursor.execute('SELECT nome, partido, uf FROM deputados LIMIT 5')

        print("\nExibindo do 1º até o 5º deputado do banco:")

        for linha in cursor.fetchall():

            print(f"Deputado --> {linha[0]} | Partido --> {linha[1]} | UF --> {linha[2]}")

        conectar.close()
