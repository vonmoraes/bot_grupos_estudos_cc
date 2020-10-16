# -*- coding: utf-8 -*-

"""
Primeiro programa de teste de bot telegram
API: python-telegram-bot

tutorial at. href<https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API>
"""


####################
# imports
####################

import telebot
from telebot import types
import os

#Log
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Sou um bot, por favor converse comigo! ;)')
pass    

@bot.message_handler(commands=['grupos'])
def grupos(message):
    text_grupos_estudos = ("Lista de grupos de estudos:\n"
        # "[Álgebra Linear](https://t.me/joinchat/CIoz-gwgPwKC8g8i5-CzZg)\n"
        "[Aplicações Híbridas](https://t.me/joinchat/CIoz-hpuIUK3c4HC_7YZHA)\n"
        "[Cálculo III](https://t.me/joinchat/IqDW5RFkiJ9MMVD11AJ_-Q)\n"
        "[Compiladores](https://t.me/joinchat/DbdJcFScE-QiB83OtVdmiQ)\n"
        "[Filosofia 2](https://t.me/joinchat/DbdJcBv2oxoZONV-yGRLGA)\n"
        "[Computação Distribuída](https://t.me/joinchat/DMDdalJhAFbGEu7d6SJeLA)\n"
        #"[Computação Gráfica](https://t.me/joinchat/HJ7hGVPvD7y6vsOVgxAGDg)\n"
        "[Inteligência Artificial](https://t.me/joinchat/D0xe4lcFdfw1tl0N5LNd2g)\n"
        "[Modelagem e Avaliação de Desempenho](https://t.me/joinchat/DbdJcBvsBi8W8axMo4zZxQ)\n"
        "[Otimização de Sistemas](https://t.me/joinchat/D0xe4kr1znQKAllm2PA84A)\n"
        #"[Release Engineering](https://t.me/joinchat/DbdJcBRZvaq3xXs1mFn9ig)\n"
        "[Redes de Computadores II](https://t.me/joinchat/PdOmS0RvlowETIEEfUu2QQ)\n"
        "[Lab. de Redes e SO](https://t.me/joinchat/PdOmSxcG5_JWA4tmi_ea1w)\n"
        "[Segurança e Auditoria de Sistemas](https://t.me/joinchat/HQIiXVeXLuTKm30snm_aXw)\n"
        "[Tópicos I/III](https://t.me/joinchat/DbdJcBO1QMm3gG38IQcHpg)\n"
        "[Processamento de Imagens Digitais](https://t.me/joinchat/DMDdalfkQXKcqnetLH1ZpQ)\n"
        "[Estatística](https://t.me/joinchat/DbdJcBuOcvRr-rep6eX9Zg)\n"
        "[TCC](https://t.me/joinchat/HQIiXUUFqPwTLlWoc-V2ug)\n"
    )

    text_grupos_geral = ("Lista de outros grupos: \n"
        "[Discord](https://discord.gg/6qS6vZT)\n"
        "[Grupo de Estudos](https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA)\n"
        "[Jogo do Lobinho](https://t.me/joinchat/IEr6PESXH6aDuWon4j3CoA) venha se matar com a gente !\n"
    )

    bot.send_message(message.chat.id, (text_grupos_estudos + text_grupos_geral), parse_mode="markdown")
pass    

@bot.message_handler(commands=['ajuda'])    
def ajuda(message):
    text_help = 'Informações sobre o bot em [github](https://github.com/vonmoraes/bot_grupos_estudos_cc).'
    bot.send_message(message.chat.id, text_help, parse_mode="markdown")
pass

bot.polling()
