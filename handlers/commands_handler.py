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
from database import database, Grupo
####################
# comandos
####################


TEMPLATE_GROUP_LIST = """
Lista de grupos de estudos:
{}
Lista de outros grupos:
{}
"""


"""
start():
    Envia uma mensagem ao receber comando /start
    comando :: /start
"""
def start(update, context):
    update.message.chat_id
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
	'<a href="https://t.me/joinchat/IEr6PE6mw8p-k9C1wzUdvQ"> Redes de Computadores II (REDES-II) </a>\n'
	'<a href="https://t.me/joinchat/CIoz-lfkQXIwBPcwoee3-g"> Processamento de Imagens Digitais (PID) </a>\n'
	'<a href="https://t.me/joinchat/CIoz-hZQxMd1JzjfZjRRLg"> Tópicos I/III </a>\n'
	'<a href="https://t.me/joinchat/HQIiXRITL-Pg2UZaYMMQ3A"> Tópicos II/IV </a>\n'
	'<a href="https://t.me/joinchat/HQIiXRFuRCYdoIetfodKSw"> Tópicos Virtual </a>\n'
	'<a href="https://t.me/joinchat/IEr6PEUFqPwQB3b3SeoLzQ"> TCC 1 </a>\n'
	'<a href="https://t.me/joinchat/IEr6PFScE-ROAHwJK0FcsA"> Compiladores </a>\n'
	'<a href="https://t.me/joinchat/IEr6PFcFdfzlT_sw0s8nEw"> Inteligência Artificial (IA) </a>\n'
	'<a href="https://t.me/joinchat/IEr6PEr1znSyU7dokXigGw"> Otimização de Sistemas (OS) </a>\n'
	'<a href="https://t.me/joinchat/IEr6PFQ43feuPMbd_Mzkhg"> Lab. de Redes e S.O </a>\n'
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

def new_group_list(update, context):
    formato_link = '<a href="{}"> {} </a>'
    grupos = database.ler_grupos()
    for g in grupos:
        g['link'] = context.bot.export_chat_invite_link(chat_id=chatid)
    estudos = [formato_link.format(g['link'], g['nome']) for g in grupos if g['tipo'].lower() == 'm']
    trollagem = [formato_link.format(g['link'], g['nome']) for g in grupos if g['tipo'].lower() == 't']

    mensagem = TEMPLATE_GROUP_LIST.format('\n'.join(estudos), '\n'.join(trollagem))

    context.bot.send_message(chat_id = update.message.chat_id,
                             text = mensagem,
                             parse_mode = telegram.ParseMode.HTML,
                             disable_web_page_preview=True)



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
    if (update.message.chat.type == 'group' or update.message.chat.type == 'supergroup'):
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


def update(update, context):
    _, nome, tipo = update.message.text.split()
    chatid = update.message.chat_id

    tipo.lower()

    grupo = grupo.Grupo(nome, chatid, tipo)
    database.adicionar_grupo(grupo)
    try:
        link = context.bot.export_chat_invite_link(chat_id=chatid) 
        mensagem = 'Grupo <a href="{}"> {} </a> adicionado com sucesso.'.format(link, nome)
        context.bot.send_message(chat_id=chatid, 
                             text=mensagem,
                             parse_mode=telegram.ParseMode.HTML,
                             disable_web_page_preview=True)
    except Exception as exp:
        context.bot.send_message(chat_id=chatid, 
                             text="Um erro ocorreu, tente novamente mais tarde.",
                             parse_mode=telegram.ParseMode.HTML,
                             disable_web_page_preview=True)
        print(exp)
pass
