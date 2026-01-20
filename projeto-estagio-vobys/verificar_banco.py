import sqlite3

conexao = sqlite3.connect('camara_dados.db')
cursor = conexao.cursor()

# O comando PRAGMA table_info = detalhes de cada coluna

cursor.execute("PRAGMA table_info(deputados)")
colunas = cursor.fetchall()

print("Colunas da tabela 'deputados':")
for coluna in colunas:
    # coluna[1] é o nome da coluna, coluna[2] é o tipo (TEXT, INTEGER, etc)
    print(f"Nome da coluna: {coluna[1]} | Tipo dela: {coluna[2]}")

conexao.close()
