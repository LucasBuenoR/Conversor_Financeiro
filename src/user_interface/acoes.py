import requests

def inicia_acoes(usuario_id):
    print("")

minha_chave = 'H11QRWDOIE670Q2T'

def exibe_acoes(minha_chave):
    cod_empresa = input("\nInforme o código da empresa que deseja ver a cotação: ")

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={cod_empresa}&apikey={minha_chave}'
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

            print(f"\n\nInformações mais recentes sobre as ações - {symbol}")
            print(f"Último preço: {latest_price}")
            print(f"Última atualização: {latest_time}")
            print(f"Preço de abertura: {open_price}")
            print(f"Maior preço do dia: {high_price}")
            print(f"Menor preço do dia: {low_price}")
            print(f"Volume de negociação: {volume}")
        else:
            print("Erro: Não foi possível obter informações de ações.")
    else:
        print(f"Erro na solicitação: Código de status {r.status_code}")

exibe_acoes('H11QRWDOIE670Q2T')


def exibe_indicadores(minha_chave):
    print("em desenvolvimento")
