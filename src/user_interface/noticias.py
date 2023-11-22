import requests
import json

api_key = 'H11QRWDOIE670Q2T'

def exibir_noticia(api_key):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=financial_markets&limit=10&apikey={api_key}'
    r = requests.get(url)

    try:
        data = json.loads(r.text)
    except json.JSONDecodeError:
        print('Erro ao decodificar a resposta JSON da API.')
        return

    # Verificar se a resposta contém um erro
    if 'Error Message' in data:
        print(f'Erro na API: {data["Error Message"]}')
        return

    # Tentar acessar a estrutura de dados esperada
    news_feed = data.get('feed', [])
    if not news_feed:
        print('Estrutura de dados inesperada na resposta da API.')
        return

    # Pegar a primeira notícia na lista (se houver)
    first_news = news_feed[0] if news_feed else {}

    # Processar os dados da primeira notícia
    print(f'Título: {first_news.get("title", "N/A")}')
    print(f'URL: {first_news.get("url", "N/A")}')
    print(f'Tempo de Publicação: {first_news.get("time_published", "N/A")}')
    print(f'Autor(es): {", ".join(first_news.get("authors", []))}')
    print(f'Resumo: {first_news.get("summary", "N/A")}')
    print(f'Fonte: {first_news.get("source", "N/A")}')
    print(f'Categoria dentro da fonte: {first_news.get("category_within_source", "N/A")}')
    print(f'Domínio da Fonte: {first_news.get("source_domain", "N/A")}')

    print('Tópicos:')
    for topic in first_news.get("topics", []):
        print(f' - {topic.get("topic", "N/A")}: {topic.get("relevance_score", "N/A")}')

    print(f'Sentimento Geral: {first_news.get("overall_sentiment_label", "N/A")}')

    print('Sentimento por Ticker:')
    for ticker_sentiment in first_news.get("ticker_sentiment", []):
        print(f' - Ticker: {ticker_sentiment.get("ticker", "N/A")}, Sentimento: {ticker_sentiment.get("ticker_sentiment_label", "N/A")}')

# Substitua 'H11QRWDOIE670Q2T' pela sua chave de API real
exibir_noticia('H11QRWDOIE670Q2T')