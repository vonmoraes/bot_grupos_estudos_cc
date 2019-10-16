# -*- coding: utf-8 -*-
"""
https://core.telegram.org/bots/api#html-style
"""
####################
# imports
####################
import telegram
from telegram.ext import *
from handlers.commands_handler import *
from functools import wraps

####################
# global var
####################
CRIADOR = 00
lista_adm = []
####################
# wraps.
####################
"""
TODO: ADICIONAR LISTA_ADM NO BANCO DE DADOS
"""
def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        """
        chat privado:
            try: verifica lista de admistradores
            except: chat type 'private'
        """
        try:
            for membro_adm_grupo in update.message.chat.get_administrators():
                lista_adm.append(membro_adm_grupo.user.id)
                print('novo adm {}'.format(membro_adm_grupo.user.id))
            pass
        except telegram.error.BadRequest as identifier:
            if user_id not in lista_adm:
                print("Comando não autorizado para {}.".format(user_id))
                context.bot.send_message(chat_id = update.message.chat_id,
                    text="Este comando só pode ser executado em chat de grupo e por administradores!")
                return
            pass
            return func(update, context, *args, **kwargs)
        pass
        """
        chat de grupo
        """
        if user_id not in lista_adm:
            print("Comando não autorizado para {}.".format(user_id))
            context.bot.send_message(chat_id = update.message.chat_id,
                text="Somente administradores podem usar este comando."    
            )
            return
        pass
        return func(update, context, *args, **kwargs)
    return wrapped
pass

####################
# 
####################

"""
inline_caps():
    Define o comando /caps em linha
    ou seja, @nomebot utiliza o comando /caps
"""
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    pass
    results = []
    results.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'Caps',
            input_message_content = InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)
pass

"""
build_menu()
    Retorna um 'menu' com botões diretamente no chat

    buttons = list[
        InlineKeyboardButton("col1", callback_data = ...)
    ]

    verificar: https://python-telegram-bot.readthedocs.io/en/latest/telegram.inlinekeyboardbutton.html
    para saber qual argumento dos ...
    verificar: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#usage-2
    para saber como usar certinho o menu.
"""
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
pass