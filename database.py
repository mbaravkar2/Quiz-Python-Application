import mysql.connector
import re

db = mysql.connector.connect(host="localhost",user="root",password="root", auth_plugin='mysql_native_password',database='signup')

cursor = db.cursor()
file = open('questiondb.txt', 'r')
file_content = file.read()
print(file_content)
file.close()

#query = "INSERT INTO questiondb VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

#cursor.execute(query, (file_content,))

db.commit()
db.close()
