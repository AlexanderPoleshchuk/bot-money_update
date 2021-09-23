import telebot
from telebot import types
from datetime import date

from emoji import emojize
from convert import convert_money

bot = telebot.TeleBot('2041081247:AAG7m_wP0bXA7vPhqm63_gRsko-Gc2I6H-A')
DATA = None

BEL = emojize(':Belarus:')
USA = emojize(':United_States:')
RUS = emojize(':Russia:')
EU = emojize(':European_Union:')
UAH = emojize(':Ukraine:')
dict_flags = {
    "BYN": ':Belarus:',
    "USD": ':United_States:',
    "RUB": ':Russia:',
    "EUR": ':European_Union:',
    "UAH": ':Ukraine:',
}


@bot.message_handler(commands=['start'])
def start_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/Валюта')

    bot.send_message(message.chat.id, "Добро пожаловать..\nЯ, Бот, который тебе поможет перевести валюту.",
                     reply_markup=user_markup)


@bot.message_handler(commands=['Валюта'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(f'{BEL} BYN', callback_data='get-BYN')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(f'{EU} EUR', callback_data='get-EUR'),
        telebot.types.InlineKeyboardButton(f'{USA} USD', callback_data='get-USD')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton(f'{RUS} RUB', callback_data='get-RUB'),
        telebot.types.InlineKeyboardButton(f'{UAH} UAH', callback_data='get-UAH')
    )
    bot.send_message(
        message.chat.id,
        'Выбери валюту:',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    global DATA
    DATA = query.data
    data = DATA.split("-")[1]
    if DATA.startswith('get-'):
        bot.send_message(chat_id=query.message.chat.id, text=f'Валюта: {emojize(dict_flags.get(data))} {data}\nНапишите сумму:')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        user_number = float(message.text)
        if user_number > 0:
            data = DATA.split('-')[1]
            bot.send_message(message.from_user.id, convert_money(user_number, data))
        else:
            bot.send_message(message.from_user.id, 'чепуху не пиши')


    except:
        bot.send_message(message.from_user.id, 'чепуху не пиши')


bot.polling()
