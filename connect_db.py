import pymysql

print ("connecting to the database...")
con = pymysql.connect(host='localhost',
                             user='root',
                             password='1234567',
                             db='sgi_producao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print ("Connected")
con.commit()
con.close()
