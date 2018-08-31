# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:28:54 2018

@author: leonardo.correia
"""

#Protótipo de gráfico

import matplotlib.pyplot as plt


x = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
y = [1,5,7,10,3,5,11,11,13,13,16,7,13,12,7]

x2 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
y2 = [3,5,6,7,8,4,6,8,10,16,10,15,16,17,11]
#criando um gráfico qualquer

plt.plot(x, y, label = 'Vendas', color = 'r')

#atribuindo um título ao gráfico

plt.title("Protótipo Gráfico")

plt.xlabel("Dia")
plt.ylabel("Produção")

#atribuindo legenda à curva

plt.plot(x2,y2, label = "Meta", color = 'b') 

plt.legend()
plt.grid(True)
plt.savefig('teste1.png', dpi=1024)
plt.show()

