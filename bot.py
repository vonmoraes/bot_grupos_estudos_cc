# -*- coding: utf-8 -*-
from os import environ, path
from dotenv import load_dotenv
import telebot
from telebot import types

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

BOT_TOKEN = environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)
bot.state = None

MAIN = 0
CANCEL = 1
BACK = 2


@bot.message_handler(commands=['start'])
def start_command_handler(message):
    bot.send_message(message.chat.id, "bot")
    log = message.date, message.message_id, message.from_user.id, message.text
    print(log)
    bot.state = None
pass

@bot.message_handler(commands=['grouplist','listagrupo','lista'])
def group_list_command_handler(message):
    text = ("listinha dos grupos de teste:\n"
    )
    keyboard = types.InlineKeyboardMarkup()

    btn_grupo_estudos = types.InlineKeyboardButton(
        text="Grupo de Estudos"
        ,url="https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA"
    )

    btn_grupo_2 = types.InlineKeyboardButton(
        text="Grupo de Estudos"
        ,url="https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA"
    )

    keyboard.add(btn_grupo_estudos, btn_grupo_2, btn_grupo_2, btn_grupo_2)
    # keyboard.add(btn_grupo_2)


    bot.send_message(message.chat.id
        ,text
        ,reply_markup=keyboard)
pass




print("bot listening:")
bot.polling()
