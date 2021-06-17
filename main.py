import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "YOUR API KEY"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK, #TSLA
    "apikey" : ALPHA_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query?", params=parameters)
stock_data = response.json()
stock_daily = stock_data['Time Series (Daily)']

stock_data_list = [value for (key, value) in stock_daily.items()]
date = [x for x in stock_daily]

#price
yesterday_closing_price         = float(stock_data_list[0]['4. close'].replace(".", ""))
day_bf_yesterday_closing_price  = float(stock_data_list[1]['4. close'].replace(".", ""))

#difference price
diff_percent = ((yesterday_closing_price - day_bf_yesterday_closing_price) / yesterday_closing_price) * 100

print(f"closing_price_now :{yesterday_closing_price} | closing_price_ystrdy :{day_bf_yesterday_closing_price} |diff :{diff_percent}")
print("\n")






