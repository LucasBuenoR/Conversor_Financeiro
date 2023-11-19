import requests
import time
import os
from user_interface import menu

def exibe_acoes(usuario_id, minha_chave):
    while True:

        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋        €   ₿   $        ┋\n"
                "┋• • • • A Ç Õ E S • • • •┋\n"
                "┋        $   ₿   €        ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        cod_empresa = input("\n🡆 (Obs.: Você pode inserir até três ticker - Ex.: AAPL, GOOG, AMZN)"
                            "\n🡆 Informe o ticker da empresa que deseja ver as ações:")

        tickers = cod_empresa.split(', ')

        for ticker in tickers:

            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={minha_chave}'
            r = requests.get(url)

            if r.status_code == 200:
                data = r.json()

                if 'Global Quote' in data:
                    global_quote = data['Global Quote']
        
                    symbol = global_quote.get('01. symbol', 'N/A')
                    latest_price = global_quote.get('05. price', 'N/A')
                    latest_time = global_quote.get('07. latest trading day', 'N/A')
                    open_price = global_quote.get('02. open', 'N/A')
                    high_price = global_quote.get('03. high', 'N/A')
                    low_price = global_quote.get('04. low', 'N/A')
                    volume = global_quote.get('06. volume', 'N/A')

                    print(f"\nInformações mais recentes sobre as ações - {symbol}")
                    print(f"Último preço: {latest_price}")
                    print(f"Última atualização: {latest_time}")
                    print(f"Preço de abertura: {open_price}")
                    print(f"Maior preço do dia: {high_price}")
                    print(f"Menor preço do dia: {low_price}")
                    print(f"Volume de negociação: {volume}")
                else:
                    print("\n【Erro: Não foi possível obter informações de ações. ✗✗】")
            else:
                print(f"\n【Erro na solicitação: Código de status {r.status_code} ✗✗】")

        escolha = input("\n🡆 Deseja fazer uma nova consulta ([S]im/[N]ão):").lower()
        if escolha == 's':
            time.sleep(2)
            os.system("cls")
            exibe_acoes(usuario_id, minha_chave)
        else:
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)

