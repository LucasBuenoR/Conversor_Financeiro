import requests
import json
import time
import os
from datetime import datetime
from dateutil import parser
from user_interface import menu

# api_key = 'H11QRWDOIE670Q2T'

def exibir_noticias(usuario_id, minha_chave):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=financial_markets&apikey={minha_chave}'
    r = requests.get(url)
    
    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
            "┋• • • NOTÍCIAS DO MERCADO FINANCEIRO • • •┋\n"
            "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
    try:
        data = json.loads(r.text)
    except json.JSONDecodeError:
        print('\n【Erro ao decodificar a resposta JSON da API.✗✗】')
        return

    if 'Error Message' in data:
        print(f'\n【Erro na API: {data["Error Message"]}✗✗】')
        return

    news_feed = data.get('feed', [])
    if not news_feed:
        print('\n【Estrutura de dados inesperada na resposta da API.✗✗】')
        return

    for idx, news in enumerate(news_feed, start=1):
        print(f"\nNotícia {idx}:\n")
        #formata e exibir informações
        time_published = news.get("time_published", "N/A")
        formatted_time_published = "N/A"
        if time_published != "N/A":
            formatted_time_published = parser.parse(time_published).strftime('%Y-%m-%d %H:%M:%S')
        print(f'Título: {news.get("title", "N/A")}')
        print(f'URL: {news.get("url", "N/A")}')
        print(f'Tempo de Publicação: {formatted_time_published}')
        print(f'Autor(es): {", ".join(news.get("authors", []))}')
        print(f'Resumo: {news.get("summary", "N/A")}')
        print(f'Fonte: {news.get("source", "N/A")}')
        print(f'Categoria dentro da fonte: {news.get("category_within_source", "N/A")}')
        print(f'Domínio da Fonte: {news.get("source_domain", "N/A")}')

        print('Tópicos:')
        for topic in news.get("topics", []):
            print(f' - {topic.get("topic", "N/A")}: {topic.get("relevance_score", "N/A")}')
        
        print(f'Sentimento Geral: {news.get("overall_sentiment_label", "N/A")}\n')

    escolha = input("\n🡆 Digite ([S]air) para sair:").lower()
    if escolha == 's':
        time.sleep(2)
        os.system("cls")
        menu.meu_menu(usuario_id)

