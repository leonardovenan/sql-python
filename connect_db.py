import pymysql

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

con.commit()
con.close()
