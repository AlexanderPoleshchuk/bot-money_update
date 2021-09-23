from currency import get_currency_dict
from datetime import date
from emoji import emojize

BEL = emojize(':Belarus:')
USA = emojize(':United_States:')
RUS = emojize(':Russia:')
EU = emojize(':European_Union:')
UA = emojize(':Ukraine:')

fresh_rates = get_currency_dict()

USD = fresh_rates.get('USD')
RUB = fresh_rates.get('RUB')
EUR = fresh_rates.get('EUR')
UAH = fresh_rates.get('UAH')


def convert_money(number, rate):
    if rate == 'USD':
        return f"{transfer_usd(number)}\n\nДата: {date.today()}"
    elif rate == 'RUB':
        return f"{transfer_rub(number)}\n\nДата: {date.today()}"
    elif rate == 'EUR':
        return f"{transfer_eur(number)}\n\nДата: {date.today()}"
    elif rate == 'UAH':
        return f"{transfer_uah(number)}\n\nДата: {date.today()}"
    elif rate == 'BYN':
        return f"{transfer_byn(number)}\n\nДата: {date.today()}"


def dec(number):
    return round(number, 2)


def transfer_usd(money):
    MONEY = float(money)
    return f'{BEL} {dec(MONEY * USD)}\n{USA} {dec(MONEY)}\n{EU} {dec(USD / EUR * MONEY)}\n{RUS} {dec(MONEY * USD / RUB * 100)}\n{UA} {dec(MONEY * USD / UAH * 100)}'


def transfer_eur(money):
    MONEY = float(money)
    return f'{BEL} {dec(MONEY * EUR)}\n{USA} {dec(EUR / USD * MONEY)}\n{EU} {dec(MONEY)}\n{RUS} {dec(MONEY * EUR / RUB * 100)}\n{UA} {dec(MONEY * EUR / UAH * 100)}'


def transfer_rub(money):
    MONEY = float(money)
    return f'{BEL} {dec(MONEY / 100 * RUB)}\n{USA} {dec(MONEY / 100 * RUB / USD)}\n{EU} {dec(MONEY / 100 * RUB / EUR)}\n{RUS} {dec(MONEY)}\n{UA} {dec(((MONEY*RUB)/100)/(UAH/100))}'


def transfer_uah(money):
    MONEY = float(money)
    return f'{BEL} {dec(MONEY / 100 * UAH)}\n{USA} {dec(MONEY / 100 * UAH / USD)}\n{EU} {dec(MONEY / 100 * UAH / EUR)}\n{RUS} {dec(((MONEY*UAH)/100)/(RUB/100))}\n{UA} {dec(MONEY)}'


def transfer_byn(money):
    MONEY = float(money)
    return f'{BEL} {dec(MONEY)}\n{USA} {dec(MONEY / USD)}\n{EU} {dec(MONEY / EUR)}\n{RUS} {dec(MONEY / RUB * 100)}\n{UA} {dec(MONEY / UAH * 100)}'
