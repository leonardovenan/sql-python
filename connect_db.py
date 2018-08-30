import pymysql

lista_data=[]
sumValLiq = []

con = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='sgi_producao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


con.commit()
con.close()
