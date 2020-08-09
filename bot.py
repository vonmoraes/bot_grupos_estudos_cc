# -*- coding: utf-8 -*-
from os import environ, path
from dotenv import load_dotenv
import telebot
from telebot import types
import redis

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
# config
BOT_TOKEN = environ.get('BOT_TOKEN')
REDIS_HOST = environ.get('REDIS_HOST')
REDIS_PORT = environ.get('REDIS_PORT')
REDIS_PASSWORD = environ.get('REDIS_PASSWORD')

# bot config
bot = telebot.TeleBot(BOT_TOKEN)

# redis config
redis = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    charset='utf-8',
    decode_responses=True
)


bot.state = None

# message_sent_id = 0 
# handlers
@bot.message_handler(commands=['start'])
def start_command_handler(message):
    bot.send_message(message.chat.id, "bot")
    log = message.date, message.message_id, message.from_user.id, message.text
    print(log)

    teste = redis.hgetall('1')

    for key in teste:
        print(key, teste[key])

    bot.state = None
pass

@bot.message_handler(commands=['grouplist','listagrupo','lista'])
def group_list_command_handler(message):
    keyboard = types.InlineKeyboardMarkup()

    text = ("Segue a lista dos principais grupos:\n"
    )

    btn_grupo_estudos = types.InlineKeyboardButton(
        text="Grupo A"
        ,url="https://t.me/testeBotLuanaELucas"
    )

    btn_discord = types.InlineKeyboardButton(
        text="Grupo B"
        ,url="https://t.me/joinchat/HQIiXRVZNYRQtcqE327jdw"
    )

    btn_lobinho = types.InlineKeyboardButton(
        text="Lobinho"
        ,url="https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA"
    )

    btn_todos_grupos = types.InlineKeyboardButton(
        text="Todos os grupos"
        ,callback_data='TodosOsGrupos'
    )

    btn_selecionar_periodo = types.InlineKeyboardButton(
        text="Selecionar Período"
        ,callback_data='SelecionaPeriodo'
    )


    btn_ajuda = types.InlineKeyboardButton(
        text="Ajuda", callback_data = 1
    )

    btn_cancel = types.InlineKeyboardButton(
        text="Cancelar", callback_data = 2
    )

    # keyboard.add(btn_todos_grupos)
    # keyboard.add(btn_selecionar_periodo)
    keyboard.add(btn_grupo_estudos)
    keyboard.add(btn_discord)
    # keyboard.add(btn_lobinho)
    # keyboard.add(btn_ajuda, btn_cancel)

    # print("message id:",message.message_id)

    reply_message = bot.send_message(
            message.chat.id
            ,text
            ,reply_markup=keyboard
    )

    print("message.chat.id", message.chat.id)

    bot.last_message_sent = reply_message.chat.id, reply_message.message_id
    print(*bot.last_message_sent)
pass


@bot.callback_query_handler(func=lambda call: call.data == "SelecionaPeriodo")
def callback_selec_period(call):
    keyboard = types.InlineKeyboardMarkup()
    btn_period = types.InlineKeyboardButton(
        text="1º"
        ,callback_data = "1"
    )
    keyboard.add(
        btn_period, btn_period, btn_period, btn_period
        ,btn_period, btn_period, btn_period, btn_period
        ,btn_period, btn_period
    )

    chat_id, b = bot.last_message_sent
    print(bot.delete_message(*bot.last_message_sent))
    reply_message = bot.send_message(chat_id
        ,"Selecione o período desejado"
        ,reply_markup=keyboard
    )
    bot.last_message_sent = reply_message.chat.id, reply_message.message_id
pass

@bot.callback_query_handler(func=lambda call: call.data == "1")
def callback_selec_period(call):
    print(bot.delete_message(*bot.last_message_sent))
    reply_message = bot.send_message(
        call.from_user.id
        ,"FUNCIONOU :D"
    )
    bot.last_message_sent = reply_message.chat.id, reply_message.message_id
    print(*bot.last_message_sent)
pass

print("bot listening:")
bot.polling()
