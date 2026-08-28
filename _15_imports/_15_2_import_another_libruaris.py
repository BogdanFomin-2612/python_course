# #! УСТАНОВКА СТОРОННИХ БИБЛИОТЕК

import requests

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': "BTCUSDT"})

# content = response.content
# print(content)
# print(type(content))

# price = response.json()
price_object = response.json()
price = float(price_object['price'])
print(price)
print(type(price))