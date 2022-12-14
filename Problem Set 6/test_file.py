# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import json

try:

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if r.status_code == 200:

        try:
            user_input = int(input('Ile BTC chcesz kupić? '))
            with open('bitcoin.json', 'wb') as fw:
                for data in r.iter_lines(chunk_size=128):
                    fw.write(data)

            with open('bitcoin.json', 'r') as f:
                json_object = json.loads(f.read())

            bitcoin_rate = json_object["bpi"]["USD"]["rate_float"]
            total_price = bitcoin_rate * user_input
            print(f"%{total_price:,.4f}")

        except ValueError:
            print('Wprowadź poprawną wartość')


except requests.RequestException:
    print('Błąd przy zapytaniu do API')