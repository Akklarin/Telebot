import telebot
from bot_DB2 import *

bot = telebot.TeleBot('{__MyTOKEN__}')

name = ''
age = 0
workplase = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Введите ФИО:")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'Введите возраст:')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    age = message.text
    bot.send_message(message.chat.id, 'Введите место работы:')
    bot.register_next_step_handler(message, get_wp)


def get_wp(message):
    global workplase
    workplase = message.text
    bot.send_message(message.chat.id, 'Ввод завершен')
    info_write(name, age, workplase)


@bot.message_handler(commands=['rez'])
def rez_message(message):
    t = session.query(Employees.name, Employees.age, Employees.place_of_work).all()
    a = ''
    for i in t:
        a += str(i)
        a += '\n'
    bot.send_message(message.chat.id, a)


bot.infinity_polling()
