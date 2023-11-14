import requests
import os
import time
from datetime import datetime
import sqlite3
from user_interface import menu, login

def obter_cotacao(moeda_origem, moeda_destino, quantidade, usuario_id):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        valor_cotacao = float(data[f'{moeda_origem}{moeda_destino}']['high'])
        resultado = quantidade * valor_cotacao
        print(f"\n==> {quantidade} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino} <==\n")
        valor_origem = quantidade
        valor_convertido = resultado
        registrar_conversao(usuario_id, moeda_origem, moeda_destino, valor_origem, valor_convertido)
    else:
        print("\nOcorreu um erro ao obter a cotação.\n\n")

def faz_conversao(usuario_id):
    print("+==================================================+\n"
          "|---------------CONVERSÃO DE MOEDA$----------------|\n"
          "|-----------------CÓD.DAS MOEDA$$------------------|\n"
          "|==================================================|\n"
          "|                                                  |\n"
          "|             Dolar (USD)                          |\n"
          "|             Euro (EUR)                           |\n"
          "|             Real (BRL)                           |\n"
          "|             Iene Japonês (JPY)                   |\n"
          "|             Libra Esterlina (GBP)                |\n"
          "|             Dólar Australiano (AUD)              |\n"
          "|             Dólar Canadense (CAD)                |\n"
          "|             Franco Suíço (CHF)                   |\n"
          "|             Dólar Neozelandês (NZD)              |\n"
          "|             Coroa Sueca (SEK)                    |\n"
          "|             Coroa Norueguesa (NOK)               |\n"
          "|                                                  |\n"
          "|     (Obs.: Alguns exemplos de CÓD. DE MOEDAS)    |\n"
          "+==================================================+\n")
    moeda_origem = input("==> Informe a moeda de origem: ")
    moeda_destino = input("==> Informe a moeda de destino: ")
    quantidade = float(input("==> Informe o valor para conversão: "))
    obter_cotacao(moeda_origem, moeda_destino, quantidade, usuario_id)
    escolha = input("Deseja fazer outra convesão ([S]im/[N]ão):").lower()
    if escolha == 's':
        time.sleep(2)
        os.system("cls")
        faz_conversao(usuario_id)
    else:
        time.sleep(2)
        os.system("cls")
        menu.meu_menu(usuario_id)

def registrar_conversao(usuario_id, moeda_origem, moeda_destino, valor_origem, valor_convertido):
    data_conversao = datetime.now().date()
    try:
        # Estabelecer a conexão com o banco de dados
        banco = sqlite3.connect('mybase.db')
        cursor = banco.cursor()

        # Query para inserir os dados no banco
        query = '''INSERT INTO historico_conversoes (usuario_id, moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao)
                    VALUES (?, ?, ?, ?, ?, ?)'''

        # Dados a serem inseridos no banco
        dados = (usuario_id, moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao)

        # Executar a query
        cursor.execute(query, dados)

        # Commit para salvar as mudanças
        banco.commit()
        # print("Conversão registrada com sucesso no histórico!")

        # Fechar a conexão com o banco de dados
        banco.close()
    except sqlite3.Error as e:
        print("Erro ao inserir dados no banco:", e)


