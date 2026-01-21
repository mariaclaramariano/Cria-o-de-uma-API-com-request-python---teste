from flask import Flask, render_template_string
import requests
import sqlite3

app = Flask(__name__)

# ---BUSCAR E SALVAR
def atualizar_banco():
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome" 
    
    try:
        response = requests.get(url)
        dados = response.json()['dados']
        
        conexao = sqlite3.connect('camara_dados.db')
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS deputados (id INTEGER, nome TEXT, partido TEXT, uf TEXT)')
        
        cursor.execute('DELETE FROM deputados')
        
        for d in dados:
            cursor.execute('INSERT INTO deputados VALUES (?, ?, ?, ?)', 
                           (d['id'], d['nome'], d['siglaPartido'], d['siglaUf']))
        
        conexao.commit()
        conexao.close()
    except Exception as e:
        print(f"Erro ao atualizar: {e}")

# --- ROTA DO SITE
@app.route('/')
def index():
    atualizar_banco()
    
    conexao = sqlite3.connect('camara_dados.db')
    cursor = conexao.cursor()
    cursor.execute('''
                    SELECT nome, partido, uf FROM deputados WHERE 
                    UPPER (UF) = "RJ" 
                    AND nome LIKE "P%" 
                    ORDER BY partido ASC
                    ''')
    lista = cursor.fetchall()
    conexao.close()

    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portal da Câmara - Deputados</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background-color: #f8f9fa; }
            .header-section { 
                background: linear-gradient(135deg, #004a8e 0%, #007bff 100%); 
                color: white; 
                padding: 40px 0; 
                margin-bottom: 30px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .card { border: none; box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075); }
        </style>
    </head>
    <body>

    <div class="header-section text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">Deputados Federais</h1>
            <p class="lead">Câmera Legislativa</p>
            <p class="lead">Última Atualização: 15/01/2026</p>
        </div>
    </div>

    <div class="container">
        <div class="card p-4">
            <div class="table-responsive">
                <table class="table table-hover align-middle">
                    <thead class="table-dark">
                        <tr>
                            <th>Parlamentar</th>
                            <th class="text-center">Partido</th>
                            <th class="text-center">UF</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for dep in lista %}
                        <tr>
                            <td class="fw-bold text-primary">{{ dep[0] }}</td>
                            <td class="text-center"><span class="badge bg-secondary">{{ dep[1] }}</span></td>
                            <td class="text-center fw-bold">{{ dep[2] }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
        <footer class="text-center mt-5 mb-4 text-muted">
            <small>Desenvolvido com Flask & SQLite</small>
            <small> -- maria clara mariano</small>
        </footer>
    </div>

    </body>
    </html>
    '''
    return render_template_string(html, lista=lista)

if __name__ == '__main__':
    app.run(debug=True)


