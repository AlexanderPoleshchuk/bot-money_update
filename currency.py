import requests
import json

URL = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
MY_CURRENCIES = ["USD", "RUB", "EUR", "UAH",]


def get_currency_dict():
    data = json.loads(requests.get(url=URL).text)
    update_data={}
    for currency in data:
        if currency.get("Cur_Abbreviation") in MY_CURRENCIES:
            update_data[currency.get('Cur_Abbreviation')] = currency.get('Cur_OfficialRate')

    return update_data
print(get_currency_dict())




