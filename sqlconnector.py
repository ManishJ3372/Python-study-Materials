import mysql.connector
from mysql.connector import *

mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345678",database="manish")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute('select ename from emp')


result=mycursor.fetchall()

for i in result:
    print(i)
