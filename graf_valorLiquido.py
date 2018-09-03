# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:14:32 2018

@author: leonardo.correia
"""
import pymysql
import matplotlib.pyplot as plt
import numpy as np

lista_data=[]
sumValLiq = []
width = 0.2


print ("Connecting to the database...")
con = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='sgi_producao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print ("Connected!")
cursor = con.cursor()

#primeiro cursor 
cursor.execute(""" 
    SELECT e.dataContrato,sum(e.valorLiquido) FROM sgi_producao.emprestimo e where e.estadoProposta='Contrato' group by e.dataContrato 
    HAVING SUM(e.valorLiquido) > 0;
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
   
#print (sumValLiq[-10:])
#print ("\n\n")
#print (lista_data[-10:])

x = lista_data[-12:]
y = sumValLiq[-12:]

m_mensal = 1534707.22

z = [m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal,m_mensal]
plt.bar(x, y, label = 'Valor Líquido', color = 'red')
plt.ylabel("R$")
plt.xlabel("Data")
plt.plot(x, z, label = 'Meta diária', color = 'blue')
plt.legend(loc = 2, prop={'size':7})
plt.title("Soma do Valor Líquido Diário")


plt.xticks(rotation=20)

plt.savefig('teste2.png', dpi=1000)

con.commit()
con.close()

print("\n\nDisconnected to the database!")


