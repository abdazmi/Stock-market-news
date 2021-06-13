import requests
import os
from twilio.rest import Client


# account_sid = os.environ.get("SID")
# auth_token = os.environ.get("TOKEN")
# print(auth_token, account_sid)
# https://newsapi.org/
# https://www.twilio.com/
account_sid = "PUT YOURS HERE"
auth_token = "PUT YOURS HERE"
client = Client(account_sid, auth_token)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters ={
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": "461YB45R3EKKAOZ3",

    # "interval" : "5min",
    # "outputsize" :"full"
}

response =requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data1 = [value for (key, value) in data.items()]

first_day_close=data1[0]["4. close"]
second_day_close=data1[1]["4. close"]

print(first_day_close,second_day_close)

if abs(float(first_day_close) - float(second_day_close)) >= 5:
    send_msg="PUT YOUR MSG HERE"

    if float(first_day_close) > float(second_day_close):
    # stock is increaceing
        persentage = (float(second_day_close)*100)/float(first_day_close) - 100
        send_msg += f"There are increasing in Tesla Stock ⬆ {persentage}%"
    else:
        persentage = (float(first_day_close) * 100) / float(second_day_close) - 100
        send_msg += f"There are decreasing in Tesla Stock  -{persentage}%"
    news_par = {
        "country": "us",
        "apiKey": "PUT YOURS HERE",
        "category": "business",
        "q": "Tesla"
    }
    news = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_par)
    news.raise_for_status()
    data = news.json()["articles"]

    for art in range(3):
        send_msg += f"Title:\n{ data[art]['title'] }\n\n Description:\n { data[art]['description'] }"

    message = client.messages \
        .create(
        body=send_msg,
        from_='API NUMBER',
        to='YOUR NUMBER'
    )

    print(message.status)
    print(message.sid)


else:
    print("get the fuck out of here")



