import mysql.connector as conn
''' pip install mysql-connector-python'''
''' creating connection with sql  '''
mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Ganpati@2022")
print(mydb)
'''connection established with sql '''
cursor=mydb.cursor()
cursor.execute("show databases") #same as show databses in sql
print(cursor.fetchall())#pulling all the tables in sql


