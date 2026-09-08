import requests

#! ЧТО ДЕЛАТЬ ПРИ CONNECTION ERROR

try:
    response = requests.get(
        'https://api.binance.com/api/v3/ticker/price',
        params={'symbol': 'BTCUSDT'}
    )
    bitcoin_price = response.json()["price"]
    bitcoin_price = float(bitcoin_price)
    print(bitcoin_price)

except requests.exceptions.ConnectionError as error:
    print(f"Something went wrong: {error}")
    # print("There is no connection to the Internet")