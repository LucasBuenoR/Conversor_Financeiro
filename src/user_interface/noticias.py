import requests

api_key = 'H11QRWDOIE670Q2T'
def exibir_noticia(api_key):
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics=financial_markets&limit=1&apikey={api_key}'
    r = requests.get(url)
    data = r.json()

    print("Resposta completa da API:")
    print(data)
    
    # Verificar se a resposta contém um erro
    if 'Error Message' in data:
        print(f'Erro na API: {data["Error Message"]}')
        return

    # Tentar acessar a estrutura de dados esperada
    news_data = data.get('Sentiments', []) or data.get('data', [])
    if not news_data:
        print('Estrutura de dados inesperada na resposta da API.')
        return

    # Processar os dados
    news_data = news_data[0]

    print(f'Título: {news_data.get("title", "N/A")}')
    print(f'URL: {news_data.get("url", "N/A")}')
    print(f'Tempo de Publicação: {news_data.get("time_published", "N/A")}')
    print(f'Autor(es): {", ".join(news_data.get("authors", []))}')
    print(f'Resumo: {news_data.get("summary", "N/A")}')
    print(f'Fonte: {news_data.get("source", "N/A")}')
    print(f'Categoria dentro da fonte: {news_data.get("category_within_source", "N/A")}')
    print(f'Domínio da Fonte: {news_data.get("source_domain", "N/A")}')
    
    print('Tópicos:')
    for topic in news_data.get("topics", []):
        print(f' - {topic.get("topic", "N/A")}: {topic.get("relevance_score", "N/A")}')

    print(f'Sentimento Geral: {news_data.get("overall_sentiment_label", "N/A")}')

    print('Sentimento por Ticker:')
    for ticker_sentiment in news_data.get("ticker_sentiment", []):
        print(f' - Ticker: {ticker_sentiment.get("ticker", "N/A")}, Sentimento: {ticker_sentiment.get("ticker_sentiment_label", "N/A")}')

# Substitua 'H11QRWDOIE670Q2T' pela sua chave de API real
exibir_noticia('H11QRWDOIE670Q2T')
