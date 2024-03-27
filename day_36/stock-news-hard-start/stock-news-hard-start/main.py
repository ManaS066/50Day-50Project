import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
Trigger = 0
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_key = "VTTZCCZCL4J2TVEY"
news_key ="ae052356898a416caeca11ccbab33b59"
account_sid = 'ACe515033498b7964d8305b308d0446824'
auth_token = '1092becb238daecbee944cdd61d14162'
client = Client(account_sid, auth_token)
stock_para = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":"A2UJYSH30OZH6WWU"
}
response_s= requests.get(STOCK_ENDPOINT,params=stock_para)
print(response_s.status_code)
d = response_s.json()

data = d["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
y_data = float(data_list[0]["4. close"])
dy_data = float(data_list[1]["4. close"])
dif = round((float(((y_data - dy_data) * 100) / y_data)),2)
if dif>3.00 :
    news_para = {
        "apiKey":news_key,
        "qInTitle":COMPANY_NAME,
    }
    response_n = requests.get(NEWS_ENDPOINT,news_para)
    news_data = response_n.json()
    articles = news_data["articles"]
    top_article = articles[0:3]
    print(top_article)
    formated_article = [f"Headline:{article['title']},\n  Breif : {article['description']} ,\n Url :{article['url']}" for article in top_article]

    #sending message
    for article in formated_article:
        message = client.messages.create(
            from_='+15043157922',
            body=f" {COMPANY_NAME}: ↗️{dif}% \n {article}" ,
            to='+918984398009'
        )
        print(message.status)
elif dif <-3.00:
    news_para = {
        "apiKey": news_key,
        "qInTitle": COMPANY_NAME,
    }
    response_n = requests.get(NEWS_ENDPOINT, news_para)
    news_data = response_n.json()
    articles = news_data["articles"]
    top_article = articles[0:3]
    print(top_article)
    formated_article = [f"Headline:{article['title']},\n  Breif : {article['description']} ,\n Url :{article['url']}" for article in top_article]
    # sending message
    for article in formated_article:
        message = client.messages.create(
            from_='+15043157922',
            body=f" {COMPANY_NAME}: ↘️🔻{dif}% \n {article}",
            to='+918984398009'
        )
        print(message.status)

