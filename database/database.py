# -*- coding: utf-8 -*-
"""
database:
    Banco de dados de t.me/pucmg_cc_bot
    tutorial: <href= http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html />
"""
import sqlite3
import io
import datetime
from Grupo import *


def criar_banco():
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    """
    cursor: é um interador que permite navegar e manipular os registros do bd.
    nota: cursor só aceita tuplas. 
    execute: lê e executa comandos SQL puro diretamente no bd.
    """
    cursor = conn.cursor()
    # schema tabela de grupos
    try:
        cursor.execute("""
        CREATE TABLE grupos (
        id_grupo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT NOT NULL,
        nome_grupo TEXT NOT NULL,
        link_grupo TEXT NOT NULL
        );
        """)
    except sqlite3.OperationalError:
        pass
    conn.close()
pass

def adicionar_grupo(novo_grupo):
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    cursor = conn.cursor()
    #
    cursor.execute("""
    INSERT INTO grupos (nome_grupo, link_grupo)
    VALUES (?,?);
    """, (novo_grupo.chat_id, novo_grupo.nome_grupo))
    # atualizar & fechar banco
    conn.commit()
    conn.close()
pass

def ler_grupos():
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    cursor = conn.cursor()
    #
    cursor.execute("""
    SELECT * FROM grupos;
    """)
    grupos = []
    for grupo in cursor.fetchall():
        grupos.append(grupo)
    pass
    # atualizar & fechar banco
    conn.commit()
    conn.close()
    return grupos
pass

def atualizar_grupo(nome_grupo, novo_link_grupo):
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    cursor = conn.cursor()
    #
    cursor.execute("""
    UPDATE grupos
    SET link_grupo = ?
    WHERE nome_grupo = ?
    """, (novo_link_grupo, nome_grupo))
    # atualizar & fechar banco
    conn.commit()
    conn.close()
pass

def excluir_grupo(nome_grupo):
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    cursor = conn.cursor()
    #
    cursor.execute("""
    DELETE FROM grupos
    WHERE nome_grupo = ?
    """, (nome_grupo,))
    # atualizar & fechar banco
    conn.commit()
    conn.close()
pass

def backup_db():
    # conectar ao banco
    conn = sqlite3.connect('pucmg_cc_bot.db')
    cursor = conn.cursor()
    data_atual = datetime.datetime.now()
    #
    with io.open('pucmg_cc_bot_dump.sql','w') as bckp_db:
        for linha in conn.iterdump():
            bckp_db.write('%s\n' % linha)
        pass
    pass
    print('backup realizado')
    # atualizar & fechar banco
    conn.commit()
    conn.close()
pass

"""
"""
def opcoes_db():
    print("""
    Escolha uma das operações do banco de grupos:
        1. Adicionar grupo.
        2. Ler grupos. 
        3. Editar link de um grupo.
        4. Excluir um grupo. 
        5. Realizar backup dos dados.
        0. Encerrar.
    """)
    op = input('Opção: ')
    op = int(op)
    #
    if op == 1:
        op_adicionar_grupo()
    elif op == 2:
        op_ler_grupos()
    elif op == 3:
        op_editar_grupo()
    elif op == 4:
        op_excluir_grupo()
    elif op == 5:
        backup_db()
    elif op == 0:
        print('Até mais')
        exit()
    pass
pass

def op_adicionar_grupo():
    nome_novo_grupo = input('Digite o nome do grupo a ser adicionado: ')
    link_novo_grupo = input('Digite o link do grupo a ser adicionado: ')
    novo_grupo = Grupo(nome_novo_grupo,link_novo_grupo)
    adicionar_grupo(novo_grupo)
pass

def op_ler_grupos():
    print(ler_grupos())
pass

def op_editar_grupo():
    nome_grupo = input('Digite o nome do grupo para alterar o seu link: ')
    link_novo_grupo = input('Digite o novo link do grupo: ')
    atualizar_grupo(nome_grupo,link_novo_grupo)
pass

def op_excluir_grupo():
    nome_grupo = input('Digite o nome do grupo a ser excluído: ')
    excluir_grupo(nome_grupo)
pass

"""
"""
def main():
    #
    criar_banco()
    # 
    while(True):
        opcoes_db()
    pass
    #
pass

main()