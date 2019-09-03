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
        '<a href="https://t.me/joinchat/CIoz-hRPWS_bAOXEptVP5Q"> Computação Gráfica (CG) </a>\n'
	'<a href="https://t.me/joinchat/DbdJcA_gOi5p4oYYkOCbvw"> Redes de Computadores II (REDES-II) </a>\n'
	'<a href="https://t.me/joinchat/CIoz-lfkQXIwBPcwoee3-g"> Processamento de Imagens Digitais (PID) </a>\n'
	'<a href="https://t.me/joinchat/CIoz-hZQxMd1JzjfZjRRLg"> Tópicos I/III </a>\n'
	'<a href="https://t.me/joinchat/HQIiXRITL-Pg2UZaYMMQ3A"> Tópicos II/IV </a>\n'
	'<a href="https://t.me/joinchat/HQIiXRFuRCYdoIetfodKSw"> Tópicos Virtual </a>\n'
	'<a href="https://t.me/joinchat/HQIiXUUFqPzt2wOysBd_Sg"> TCC 1 </a>\n'
	'<a href="https://t.me/joinchat/DbdJcFScE-QiB83OtVdmiQ"> Compiladores </a>\n'
	'<a href="https://t.me/joinchat/DbdJcFcFdfyNw7vVu0OhPw"> Inteligência Artificial (IA) </a>\n'
	'<a href="https://t.me/joinchat/DbdJcEr1znS4BDvc7K1WVA"> Otimização de Sistemas (OS) </a>\n'
	'<a href="https://t.me/joinchat/DbdJcBe5D184bGlDR-nyGw"> Lab. de Redes e S.O </a>\n'
                          )
    text_grupos_geral = ("Lista de outros grupos: \n"
        '<a href="https://t.me/joinchat/HQIiXUhoU9S_3U9L-K6T_Q"> Grupo de estudos </a>\n'
        '<a href="https://t.me/joinchat/HQIiXUSXH6Ysldd07yCzRA"> Jogo do Lobinho </a> Venha se matar com a gente !\n'
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
def help(update, context):
    text_help = 'Informações sobre o bot em [github](https://github.com/vonmoraes/bot_grupos_estudos_cc).'

    context.bot.send_message(chat_id = update.message.chat_id,
    text = text_help,
    parse_mode = telegram.ParseMode.MARLDOWN,
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
