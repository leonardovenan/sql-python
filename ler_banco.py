# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:14:32 2018

@author: leonardo.correia
"""
import pymysql
import matplotlib.pyplot as plt

lista_data=[]
sumValLiq = []

con = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='sgi_producao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = con.cursor()

cursor.execute(""" 
    SELECT e.dataContrato,sum(e.valorLiquido) FROM sgi_producao.emprestimo e where e.estadoProposta='Contrato' group by e.dataContrato;
""")

linhas = cursor.fetchall()

for linha in linhas:
    dataCont = linha['dataContrato']
    sumValorLiq = linha['sum(e.valorLiquido)']
    
    #concatenar dados em duas lista
    lista_data.append(dataCont)
    sumValLiq.append(sumValorLiq)
    
    #impirmir
   # print ("Data: ", dataCont)
   # print ("Soma do Valor Liquido: ", sumValorLiq)
   
print (sumValLiq[-10:])
print ("\n\n")
print (lista_data[-10:])

x = lista_data[-10:]
y = sumValLiq[-10:]

plt.plot(x, y, label = 'Soma do Valor Líquido Diário', color = 'r')
plt.legend()
plt.grid(True)
plt.xticks(rotation=20)

plt.savefig('teste2.png', dpi=1024)

con.commit()
con.close()









