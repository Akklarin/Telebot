import requests
import telebot
from telebot import types

bot = telebot.TeleBot('{__TOKEN__}')
appid = "{__MyAPPID__}}"
city_cod = {'Minsk': 625144, 'Kyiv': 703448, 'Warsaw': 756135, 'Krakow': 3094802, 'Vilnius': 593116, 'Tbilisi': 611717}


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "Minsk":
        bot.send_message(call.message.chat.id, "Погода в Минске: ")
    elif call.data == "Kyiv":
        bot.send_message(call.message.chat.id, "Погода в Киеве:")
    elif call.data == "Warsaw":
        bot.send_message(call.message.chat.id, "Погода в Варшаве")
    elif call.data == "Krakow":
        bot.send_message(call.message.chat.id, "Погода в Кракове:")
    elif call.data == "Vilnius":
        bot.send_message(call.message.chat.id, "Погода в Вильнюсе:")
    elif call.data == "Tbilisi":
        bot.send_message(call.message.chat.id, "Погода в Тбилиси:")
    city_id = city_cod[call.data]

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        inf = str(data['weather'][0]['description']) + ", температура " + str(data['main']['temp'])
    except Exception as e:
        print("Exception (weather):", e)
        pass

    bot.send_message(call.message.chat.id, inf)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text="Минск", callback_data="Minsk")
    b2 = types.InlineKeyboardButton(text="Киев", callback_data="Kyiv")
    b3 = types.InlineKeyboardButton(text="Варшава", callback_data="Warsaw")
    b4 = types.InlineKeyboardButton(text="Краков", callback_data="Krakow")
    b5 = types.InlineKeyboardButton(text="Вильнюс", callback_data="Vilnius")
    b6 = types.InlineKeyboardButton(text="Тбилиси", callback_data="Tbilisi")
    markup.add(b1, b2, b3, b4, b5, b6)
    bot.send_message(message.chat.id, "Выберите город:", reply_markup=markup)


bot.infinity_polling()
