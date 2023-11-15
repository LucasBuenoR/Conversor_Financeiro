import os
import sqlite3
from user_interface import menu_principal, login, menu, historico_conversao, historico_cotacao
from flask import Flask, send_file

app = Flask(__name__)

os.system("cls")

# conectando no banco
banco = sqlite3.connect('mybase.db')
# cursor = banco.cursor()

menu_principal.tela_bem_vindo()
# menu.meu_menu()

@app.route('/download/<int:usuario_id>')
def download_historico(usuario_id):
    nome_arquivo_json, nome_arquivo_zip = historico_conversao.exportar_historico_conversoes(usuario_id)
    print("teste")
    return send_file(nome_arquivo_zip, as_attachment=True)

    # Defina outras rotas 

if __name__ == "__main__":
    app.run(debug=True)

# Função para criar o banco de dados
def criar_db():
    banco = sqlite3.connect('mybase.db')
    banco.close()  # Abre e fecha a conexão para criar o arquivo de banco de dados vazio
# criar_db()

# Função para criar a tabela de usuários no banco de dados
def criar_tabela_usuarios():
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY,
                        nome_completo TEXT,
                        username TEXT UNIQUE,
                        senha TEXT,
                        email TEXT UNIQUE)''')
    banco.commit()
    banco.close()
# criar_tabela_usuarios()

def criar_tabela_historico_conversao():
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS historico_conversoes (
                        id INTEGER PRIMARY KEY,
                        usuario_id INTEGER,
                        moeda_origem TEXT,
                        moeda_destino TEXT,
                        valor_origem REAL,
                        valor_convertido REAL,
                        data_conversao TEXT,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                        )''')
    banco.commit()
    banco.close()

def criar_tabela_historico_cotacao():
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS historico_cotacoes (
                        id INTEGER PRIMARY KEY,
                        usuario_id INTEGER,
                        moeda_origem TEXT,
                        moeda_destino TEXT,
                        taxa_cambio REAL,
                        data_cotacao TEXT,
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                        )''')
    banco.commit()
    banco.close()
# criar_tabela_historico_cotacao()

# Função para realizar uma consulta de seleção (SELECT)
def fazer_select():
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Exemplo de SELECT
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()

    # Exibir os resultados
    for row in rows:
        print(row)

    banco.close()
# exibe_cotacao.registrar_cotacao(1, 'USD', 'BRL', 0.44, '2000-01-01')
# fazer_select()
