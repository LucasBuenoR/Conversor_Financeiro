import requests
import os
import time
# from user_interface import menu
minha_chave = 'H11QRWDOIE670Q2T'
def buscar_ticker(minha_chave):
    nome_empresa = input("\nInforme o nome da empresa: ")

    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={nome_empresa}&apikey={minha_chave}'
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        print(data)
    else:
        print("\nAgora não")

buscar_ticker('H11QRWDOIE670Q2T')