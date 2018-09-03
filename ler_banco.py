# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:14:32 2018

@author: leonardo.correia
"""
import pymysql

#listas para armazenamento de variáveis
lista_data=[]
sumValLiq = [] 

print ("Connecting to the database...")
con = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='sgi_producao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print ("Connected!")
cursor = con.cursor()

#o cursor vai ser a única coisa que vai ser alterado para gerenciar informações
#de outras tabelas do SGI.
cursor.execute(""" 
    SELECT e.dataContrato,sum(e.valorLiquido) FROM sgi_producao.emprestimo e where e.estadoProposta='Contrato' group by e.dataContrato 
    HAVING SUM(e.valorLiquido) > 0;
""")

linhas = cursor.fetchall()


con.commit()
con.close()

print("\n\nDisconnected to the database!")








