# -*- coding: utf-8 -*-

"""
Primeiro programa de teste de bot telegram
API: python-telegram-bot

tutorial at. href<https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API>
"""

"""
As classes mais importantes da api são:
 * Updater
 * Dispatcher
 O updater continuamente busca novas atualizações do telegram 
 e as passa para o Dispatcher
"""
####################
# imports
####################
import telegram
import os
from telegram.ext import *
from handlers.commands_handler import *
from handlers.outros_handler import *

"""
Log
"""
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                level=logging.INFO)
logger = logging.getLogger(__name__)

####################
# global var
####################

pucmg_cc_bot = os.environ.get('BOT_TOKEN')
bot = telegram.Bot(token=pucmg_cc_bot)
# Updater
updater = Updater(token=pucmg_cc_bot, use_context=True)
# Dispatcher
dispatcher = updater.dispatcher

####################
# global func
####################
"""
fill_outros_handler() : outros_handler.py
    Adicona outras funções ao handler (manipulação de dados)
    exemplo:
    inline_caps_handler = InlineQueryHandler(inline_caps)
"""
def fill_outros_handler():
    # inline caps
    inline_caps_handler = InlineQueryHandler(inline_caps)
    dispatcher.add_handler(inline_caps_handler)
    # 
pass

"""
fill_command_handler(): commands_handler.py
    Adiciona os comandos ao handler (manipulação de dados)
    exemplo:
        comando_handler = CommandHandler('comando', funcao)
        # Adiciona 'comando' ao handler
"""
def fill_command_handler():
    # /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    """
        Grupo de estudos bot
    """
    # /group_list
    group_list_handler = CommandHandler('group_list', group_list)
    dispatcher.add_handler(group_list_handler)
    # /help
    help_handler = CommandHandler('help', ajuda)
    dispatcher.add_handler(help_handler)

    """
    Nao foram adicionadas.
    """
    # /add_group
    add_group_handler = CommandHandler('add_group', add_group)
    dispatcher.add_handler(add_group_handler)
    # /delete_group
    # /edit_group

    """
    # Em teste
    """
    update_handler = CommandHandler('update', update)
    dispatcher.add_handler(update_handler)
    new_group_list_handler = CommandHandler('new_group_list', new_group_list)
    dispatcher.add_handler(new_group_list_handler)

pass

####################
# main
####################
def main():
    # Verifica o funcionamento do bot retornando id e username 
    print(bot.get_me())
    # Adicionar comandos
    fill_command_handler()
    fill_outros_handler()
    # Inicializa o servidor 
    updater.start_polling()

    # Parar o servidor
    updater.idle()
    updater.stop()
pass

main()