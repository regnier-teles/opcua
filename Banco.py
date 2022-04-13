from asyncio.windows_events import NULL
from calendar import c
from logging import exception
import sqlite3
from sqlite3 import Date, Error
from xmlrpc.client import DateTime
import Servidor
 

########## CRIANDO UMA CONEXÃO ENTRE O BANCO DE DADOS E O PYTHON ##########

caminho = ".\\db_opcua\\OpcDB.db"
con = None
try:
    con = sqlite3.connect(caminho)
    print('Conectou!')
    
except Error as ex:
    print(ex)
        




########## Banco de dados recebe vARiavel do Sistema 
       ########## Y é uma vARiavel auxiliar para comparação com os valores do sistema 

   ########## y recebendo vARiavel do servidor  
try:
    y1 = Servidor.estado01.get_value()
    y2 = Servidor.estado02.get_value()
    y3 = Servidor.estado03.get_value()
    y4 = Servidor.estado04.get_value()
    y5 = Servidor.estado05.get_value()

    print(con)
    try:
        con.execute ('''CREATE TABLE stockss (NVAR01 INTEGER, NVAR02 INTEGER, NVAR03 INTEGER, NVAR04 INTEGER, NVAR05 INTEGER, DDATA TEXT, DTH TEXT)''')
        
            
    except:
        print(DateTime())
    try:
        con.execute('INSERT INTO stockss VALUES (?, ?, ?, ?, ?, ?, ?)', (y1, y2, y3, y4, y5, 'Date', '2'))
        con.commit()
        print('Dado Inserido com Sucesso!')
    except:
         print('falha ao adicionar dado!!', Error)
except:
    print(Error)

Servidor.servidor.stop()