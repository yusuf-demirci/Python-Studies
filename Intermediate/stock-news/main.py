import requests
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "025WXSB86FJYVT2G"
NEWS_API_KEY = "eb080aff8a71435ea12a0d861dd0ce6e"
ACCOUNT_SID = "ACa4af4229630de5bde56d8fdef36e3e7e"
AUTH_TOKEN = "ffea79a6ad462e531d7110f87decdc16"

parameters1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response1 = requests.get(url="https://www.alphavantage.co/query", params=parameters1)
response1.raise_for_status()

data = response1.json()["Time Series (Daily)"]

yesterday, previous_day = list(data.keys())[:2]
difference = float(data[yesterday]["4. close"]) - float(data[previous_day]["4. close"])
dif_percent = abs(difference) / float(data[yesterday]["4. close"]) * 100
 
if dif_percent > 3:
    current_date = datetime.now()

    parameters2 = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": "Tesla",
        "language": "en",
        "from": yesterday,
        "to": current_date,
        "sortBy": "popularity"
    }
    response2 = requests.get("https://newsapi.org/v2/everything", params=parameters2)
    response2.raise_for_status()

    news_data = response2.json()
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for new in news_data["articles"][:3]:
        message_title = new["title"]
        message_description = new["description"]
        
        if difference > 0:
            stock = f"{STOCK}: 🔺{round(dif_percent), 2}% "
        else:
            stock = f"{STOCK}: 🔻-{round(dif_percent), 2}% "

        message = client.messages.create(
            to="+905541510171", 
            from_="+12084860229",
            body=f"{stock}\n"
                 f"Headline: {message_title}\n"
                 f"Brief: {message_description}"
            )
        print(message.status) 


