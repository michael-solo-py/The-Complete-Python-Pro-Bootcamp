import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
API_KEY_STOCK = "ELHMOSLMECACNGW0"

UP_DOWN =None
def stock_price():
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&interval=60min&apikey={API_KEY_STOCK}")
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]
    yesterday = float(data_list[0]['4. close'])
    before_yesterday = float(data_list[1]['4. close'])
    difference = before_yesterday - yesterday
    diff_per = (difference / yesterday) * 100
    if difference > 0:
        UP_DOWN = "📈"
    else:
        UP_DOWN = "📉"
    return diff_per


stock_price()


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    response_news = requests.get(
        f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey=e7f09cf8cffd438ebc683096c4877dae")
    articles = response_news.json()["articles"][:3]
    three_articles = [f"{STOCK}: {UP_DOWN}\nHeadline: {article['title']}.\n Brief: {article['description']}" for article in articles]
    return three_articles

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_massage(massage_articles):
    account_sid = 'ACCOUNT_SID'
    auth_token = 'AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=massage_articles,
        from_='+13235290427',
        to='+380937173333'
    )

    print(message.sid)


if __name__ == "__main__":
    if stock_price() > 5:
        for massage in get_news():
            send_massage(massage)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
