import requests
import os
import time
from user_interface import menu

def buscar_ticker(usuario_id, minha_chave):
    while True:
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋            €   ₿   $           ┋\n"
                "┋• • • • PESQUISAR TICKER • • • •┋\n"
                "┋            $   ₿   €           ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        empresas = input("\n(Obs.: Você pode inserir até três empresas - Ex.: Apple, Microsoft, Amazon)"
                             "\n🡆 Informe o nome da empresa:")
        empresas = [empresa.strip() for empresa in empresas.split(',')]

        for nome_empresa in empresas:
            url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={nome_empresa}&apikey={minha_chave}'
            resposta = requests.get(url)

            if resposta.status_code == 200:
                dados = resposta.json()
                matches = dados.get('bestMatches', [])

                if matches:
                    print(f"\nResultados encontrados para {nome_empresa}:\n")
                    for match in matches:
                        ticker = match.get('1. symbol', 'N/A')
                        nome = match.get('2. name', 'N/A')
                        tipo = match.get('3. type', 'N/A')
                        regiao = match.get('4. region', 'N/A')
                        moeda = match.get('8. currency', 'N/A')

                        print(f"Ticker: {ticker}, Nome: {nome}, Tipo: {tipo}, Região: {regiao}, Moeda: {moeda}")
                else:
                    print("\n【Nenhuma correspondência encontrada para a empresa informada.✗✗】")
            else:
                print("\n【Erro ao acessar a API. Por favor, tente novamente mais tarde.✗✗】")

        escolha = input("\n🡆 Deseja fazer uma nova pesquisa ([S]im/[N]ão):").lower()
        if(escolha == 's'):
            time.sleep(2)
            os.system("cls")
            buscar_ticker(usuario_id, minha_chave)
        else:
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)

