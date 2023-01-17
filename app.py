import telebot
from config import TOKEN, coin
from extensions1 import Converter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def instr(message: telebot.types.Message):
    bot.reply_to(message, 'Введите сообщение в виде:'
                          ' <валюта>'
                          ' <в какую перевести>'
                          '<количество первой валюты>')


@bot.message_handler(commands=['values'])
def values_(message: telebot.types.Message):
    text = ''
    for key in coin.keys():
        text += '\n' + key
        print(text)
    bot.reply_to(message, f'Доступные валюты:{text}')

@bot.message_handler(content_types=['text'])
def req(message: telebot.types.Message):
    try:
        mes = message.text.split()
        if len(mes) > 3:
            raise APIException('Слишком много параметров.')
        base, quote, amount = mes
        result = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, e)
    except Exception as e:
        bot.reply_to(message, e)
    else:
        text = f'''Цена {amount} {coin[base]} в {coin[quote]} - {result['result']}'''
        bot.reply_to(message, text)

bot.polling()
