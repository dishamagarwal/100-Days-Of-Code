import requests
import os
from datetime import datetime, timedelta

# class Main():
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_news(difference, yesterday):
    news_url = 'https://newsapi.org/v2/top-headlines'
    news_param = {
        'apiKey': os.environ.get('NEWS_APIKEY'),
        'country': 'us',
        'q': COMPANY_NAME,
        'pageSize': 3
    }
    news_response = requests.get(url=news_url, params=news_param)
    news_response.raise_for_status()
    news = news_response.json()
    
    message = STOCK + ": "
    if difference > 0:
        message += '🔺'
    else:
        message += '🔻'
    message +=  + str(round(abs(difference) * float(yesterday * 0.01))) * '%\n'
    
    if news['totalResults'] > 3:
        for x in range(3):
            message += news['articles'][x]['title'] + '\n' + news['articles'][x]['description'] + '\n'
    elif news['totalResults'] > 0:
        for x in news['articles']:
            message += x['title'] + '\n' + x['description'] + '\n'
            return message
    
def send_text(message):
    # send message as text using twillo
    ...

def stock_difference():
    yesterday = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
    day_before = (datetime.today() - timedelta(2)).strftime('%Y-%m-%d')
    url = 'https://www.alphavantage.co/query'
    param = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'outputsize': 'compact',
        'apikey': os.environ.get('ALPHAVANTAGE_APIKEY')
    }
    response = requests.get(url=url, params=param)
    response.raise_for_status()
    print(response.json())
    data = response.json()['Time Series (Daily)']
    difference = float(data[yesterday]['4. close']) - float((data[day_before]['4. close']))
    if abs(difference) >= 0.05 * float(data[yesterday]['4. close']):
        message = get_news(difference, data[yesterday]['4. close'])
        send_text(message)

stock_difference()