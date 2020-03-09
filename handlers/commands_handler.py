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
    & outros grupos da computação em formato Markdown
    comando :: /group_list
"""
def group_list(update, context):

    text_grupos_estudos = ("Lista de grupos de estudos:\n"
        "[Álgebra Linear](https://t.me/joinchat/CIoz-gwgPwKC8g8i5-CzZg)\n"
        "[Cálculo III](https://t.me/joinchat/IqDW5RFkiJ9MMVD11AJ_-Q)\n"
        "[Compiladores](https://t.me/joinchat/DbdJcFScE-QiB83OtVdmiQ)\n"
        "[Computação Distribuída](https://t.me/joinchat/DbdJcBAZKYbHscWnIw4JaA)\n"
        "[Computação Gráfica](https://t.me/joinchat/HJ7hGVPvD7y6vsOVgxAGDg)\n"
        "[Inteligência Artificial](https://t.me/joinchat/D0xe4lcFdfw1tl0N5LNd2g)\n"
        "[Modelagem e Avaliação de Desempenho](https://t.me/joinchat/HJ7hGRRpKczWZENW3fk1Bg)\n"
        "[Otimização de Sistemas](https://t.me/joinchat/D0xe4kr1znQKAllm2PA84A)\n"
        "[Redes de Computadores II](https://t.me/joinchat/PdOmS0RvlowETIEEfUu2QQ)\n"
        "[Release Engineering](https://t.me/joinchat/DbdJcBRZvaq3xXs1mFn9ig)\n"
        "[Redes de Computadores II](https://t.me/joinchat/PdOmS0RvlowETIEEfUu2QQ)\n"
        "[Lab. de Redes e SO](https://t.me/joinchat/PdOmSxcG5_JWA4tmi_ea1w)\n"
        "[Segurança e Auditoria de Sistemas](https://t.me/joinchat/DbdJcBN6Dl_cYqVWSNBqSA)\n"
        "[Tópicos I - Ciência dos Dados](https://t.me/joinchat/D0xe4hWM3WNUtIb1Wk7qJg)\n"
        "[Tópicos II - Machine Learning](https://t.me/joinchat/DbdJcBS0uSo6C-VQdpeD8w)\n"
        "[TCC 1](https://t.me/joinchat/D0xe4lPO_i3KJN4hIdlFZg)\n"
        "[TCC 2](https://t.me/joinchat/HQIiXUUFqPwTLlWoc-V2ug)\n"
    )

    text_grupos_geral = ("Lista de outros grupos: \n"
        "[Grupo de Estudos](https://t.me/joinchat/IEr6PEhoU9TdPmkaJli3GA)\n"
        "[Jogo do Lobinho](https://t.me/joinchat/IEr6PESXH6aDuWon4j3CoA) venha se matar com a gente !\n"
    )
  
    context.bot.send_message(chat_id = update.message.chat_id,
        text = text_grupos_estudos + text_grupos_geral,
        parse_mode = telegram.ParseMode.MARKDOWN,
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
            mensagem = '{} você quer adicionar o grupo <a href="{}"> {} </a>?.'.format(referencia_usuario, link_grupo, nome_grupo)
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
