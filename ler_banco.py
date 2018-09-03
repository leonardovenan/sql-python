# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:14:32 2018

@author: leonardo.correia
"""
import pymysql

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


cursor.execute(""" 
    SELECT e.dataContrato,sum(e.valorLiquido) FROM sgi_producao.emprestimo e where e.estadoProposta='Contrato' group by e.dataContrato 
    HAVING SUM(e.valorLiquido) > 0;
""")

linhas = cursor.fetchall()


con.commit()
con.close()

print("\n\nDisconnected to the database!")








