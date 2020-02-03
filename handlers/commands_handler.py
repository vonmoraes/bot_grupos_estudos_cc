# -*- coding: utf-8 -*-
"""
https://core.telegram.org/bots/api#html-style
"""
####################
# imports
####################
import telegram
from telegram.ext import *
from handlers.outros_handler import *

####################
# comandos
####################

"""
start():
    Envia uma mensagem ao receber comando /start
    comando :: /start
"""
def start(update, context):
    context.bot.send_message(chat_id = update.message.chat_id,
        text = 'Sou um bot, por favor converse comigo! ;)')
pass

"""
    Grupo de estudos bot
"""

"""
group_list():
    Retorna uma mensagem contendo a lista de grupos das máterias
    & outros grupos da computação em formato HTML
    comando :: /group_list
"""
def group_list(update, context):

    text_grupos_estudos = ("Lista de grupos de estudos:\n"
        '<a href="https://t.me/joinchat/CIoz-gwgPwKC8g8i5-CzZg"> Álgebra Linear (AL) </a>\n'
	    '<a href="https://t.me/joinchat/IqDW5RFkiJ9MMVD11AJ_-Q"> Cálculo III </a>\n'
	    '<a href="https://t.me/joinchat/DbdJcFScE-QiB83OtVdmiQ"> Compiladores </a>\n'
	    '<a href="https://t.me/joinchat/DbdJcBRZvaq3xXs1mFn9ig"> Release Engineering  </a>\n'
	    '<a href="https://t.me/joinchat/DbdJcBN6Dl_cYqVWSNBqSA"> Segurança e Auditoria de Sistemas </a>\n'
	    '<a href="https://t.me/joinchat/DbdJcBAZKYbHscWnIw4JaA"> Computaçao Distribuída </a>\n'
	    '<a href="https://t.me/joinchat/D0xe4lPO_i3KJN4hIdlFZg"> TCC 1 </a>\n'
	    '<a href="https://t.me/joinchat/HQIiXUUFqPwTLlWoc-V2ug"> TCC 2 </a>\n'
    )
    text_grupos_geral = ("Lista de outros grupos: \n"
        '<a href="https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA"> Grupo de estudos </a>\n'
        '<a href="https://t.me/joinchat/IEr6PESXH6aDuWon4j3CoA"> Jogo do Lobinho </a> Venha se matar com a gente !\n'
        )
        
    context.bot.send_message(chat_id = update.message.chat_id,
        text = text_grupos_estudos + text_grupos_geral,
        parse_mode = telegram.ParseMode.HTML,
        disable_web_page_preview=True)
pass

"""
help():
    Retorna uma mensagem contendo informações sobre o bot.
    comando :: /help
"""
def ajuda(update, context):
    text_help = 'Informações sobre o bot em [github](https://github.com/vonmoraes/bot_grupos_estudos_cc).'

    context.bot.send_message(chat_id = update.message.chat_id,
    text = text_help,
    parse_mode = telegram.ParseMode.MARKDOWN,
    disable_web_page_preview = True)
pass


"""
TENTATIVAS que não foram pra frente.
"""
@restricted
def add_group(update, context):
    # verificar_usuario()
    # Nota: referencia do usuario = nome + link do chat do usuario
    #       chat_usuario = id privado do usuario
    referencia_usuario = update.message.from_user.mention_html()
    chat_usuario = update.message.from_user.id
    
    mensagem_instrucao = """Mande novamente o comando <code>/add_group</code> da seguinte forma:
        <code>/add_group nome_grupo link_grupo</code>"""

    """
    if: grupo ou supergrupo
    else: privado
    """
    if (update.message.chat.type == 'group' 
    or update.message.chat.type == 'supergroup'):
        mensagem = "Olá, {} te mandei uma mensagem no privado com instruções ;)".format(referencia_usuario)
        # Mandar mensagem de instrução no privado
        context.bot.send_message(chat_id = chat_usuario,
            text = mensagem_instrucao,
            parse_mode = telegram.ParseMode.HTML)
    elif (update.message.chat.type == 'private'):
        try:
            comando, nome_grupo, link_grupo = update.message.text.split()
            mensagem = '{} você quer adicionar o grupo <a href="{}"> {} </a>?.'.format(referencia_usuario,link_grupo,nome_grupo)
        except ValueError as identifier:
            mensagem = mensagem_instrucao
        pass
    pass
    context.bot.send_message(chat_id = update.message.chat_id,
        text = mensagem,
        parse_mode = telegram.ParseMode.HTML,
        disable_web_page_preview = True
    )
pass
