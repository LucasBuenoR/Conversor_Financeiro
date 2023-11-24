import requests
import os
import time
from datetime import datetime
import sqlite3
from user_interface import menu

def iniciar_cotacao(usuario_id):
    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋        €       ₿       $        ┋\n"
            "┋  • • • FORMAS DE COTAÇÃO • • •  ┋\n"
            "┋        $       ₿       €        ┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n"
            "[1] - Consultar principais cotações de moedas\n"
            "[2] - Informar moedas específicas\n" 
            "[0] - Voltar para o menu\n")
    op = int(input("🡆 Escolha uma opção:"))

    if op == 1:
        time.sleep(2)
        os.system("cls")
        dados_moedas = obter_cotacoes_1(usuario_id)
        exibir_todas_cotacoes_moedas_1(dados_moedas, usuario_id)
    elif op == 2:
        time.sleep(2)
        os.system("cls")
        dados_moedas = obter_cotacoes_2(usuario_id)
        exibir_todas_cotacoes_moedas_2(dados_moedas, usuario_id)
    elif op == 0:
        time.sleep(2)
        os.system("cls")
        menu.meu_menu(usuario_id)



def obter_cotacoes_1(usuario_id):
    principais_moedas = 'USD-BRL,CAD-BRL,EUR-BRL,GBP-BRL,ARS-BRL,BTC-BRL,LTC-BRL,JPY-BRL,CHF-BRL,AUD-BRL,CNY-BRL,ILS-BRL,ETH-BRL,XRP-BRL'
    url = f'https://economia.awesomeapi.com.br/last/{principais_moedas}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("\nFalha ao obter as cotações. Código de status: ", response.status_code)
            return None
    except requests.RequestException as e:
        print("\nErro de solicitação:\n", e)
        return None

def exibir_todas_cotacoes_moedas_1(data, usuario_id):
    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋        €       ₿       $        ┋\n"
            "┋  • • •      COTAÇÃO      • • •  ┋\n"
            "┋               DAS               ┋\n"
            "┋            PRINCIPAIS           ┋\n"
            "┋  • • •       MOEDAS      • • •  ┋\n"
            "┋        $       ₿       €        ┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n")
    if data:
        for key, value in data.items():
            moeda = key[:3]
            cotacao = value['bid']
            print(f"1 {moeda} igual a {cotacao} Real Brasileiro")
        print(" ")
    else:
        print("\n【Não foi possível exibir as cotações.✗✗】\n")
    escolha = input("🡆 Voltar para o menu formas de cotação ([S]im/[N]ão):").lower()
    if escolha == 's':
        time.sleep(2)
        os.system("cls")
        iniciar_cotacao(usuario_id)
        dados_moedas = obter_cotacoes_1(usuario_id)
        exibir_todas_cotacoes_moedas_1(dados_moedas, usuario_id)
    else:
        time.sleep(2)
        os.system("cls")
        exibir_todas_cotacoes_moedas_1(data, usuario_id)

def obter_cotacoes_2(usuario_id):

    moedas = input("\n🡆 Informe os códigos das moedas no formato ('USD-BRL,BRL-USD,...'):")
    moedas_lista = moedas.split(',')
    url = f'https://economia.awesomeapi.com.br/last/{",".join(moedas_lista)}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("\nFalha ao obter as cotações. Código de status: ", response.status_code)
            return None
    except requests.RequestException as e:
        print("\nErro de solicitação:\n", e)
        return None

def exibir_todas_cotacoes_moedas_2(data, usuario_id):
    print("\n• • • • • C O T A Ç Ã O • • • • •\n")

    if data:
        for key, value in data.items():
            moeda_origem, moeda_destino, cotacao = None, None, None

            if '-' in key:
                moeda_origem, moeda_destino = key.split('-')
            else:
                moeda_origem = key[:3]
                moeda_destino = key[3:]

            cotacao = value.get('bid', None)

            if moeda_origem is not None and moeda_destino is not None and cotacao is not None:
                print(f"1 {moeda_origem} igual a {cotacao} {moeda_destino}")
                registrar_cotacao(usuario_id, moeda_origem, moeda_destino, cotacao, datetime.now().date())
            else:
                print("\nFormato de chave inválido:", key)

        print(" ")
    else:
        print("\n【Não foi possível exibir as cotações.✗✗】\n")
    escolha = input("🡆 Voltar para o menu formas de cotação ([S]im/[N]ão):").lower()
    if escolha == 's':
        time.sleep(2)
        os.system("cls")
        iniciar_cotacao(usuario_id)
        dados_moedas = obter_cotacoes_2(usuario_id)
        exibir_todas_cotacoes_moedas_2(dados_moedas, usuario_id)
    else:
        time.sleep(2)
        os.system("cls")
        dados_moedas = obter_cotacoes_2(usuario_id)
        exibir_todas_cotacoes_moedas_2(dados_moedas, usuario_id)

def registrar_cotacao(usuario_id, moeda_origem, moeda_destino, taxa_cambio, data_cotacao):
        data_cotacao = datetime.now().date()
        try:
        
            banco = sqlite3.connect('mybase.db')
            cursor = banco.cursor()

            # Query para inserir os dados no banco
            query = '''INSERT INTO historico_cotacoes (usuario_id, moeda_origem, moeda_destino, taxa_cambio, data_cotacao)
                        VALUES (?, ?, ?, ?, ?)'''

            # Dados a serem inseridos no banco
            dados = (usuario_id, moeda_origem, moeda_destino, taxa_cambio, data_cotacao)

            # Executar a query
            cursor.execute(query, dados)

            # Commit
            banco.commit()
            # print("Conversão registrada com sucesso no histórico!")

            # Fechar a conexão
            banco.close()
        except sqlite3.Error as e:
            print("\nErro ao inserir dados no banco:", e)


