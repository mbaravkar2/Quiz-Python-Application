import mysql.connector
import re

db = mysql.connector.connect(host="localhost",user="root",password="root", auth_plugin='mysql_native_password',database='signup')

cursor = db.cursor()
file = open('m.txt', 'r')
file_content = file.read()
file.close()

query = "INSERT INTO quiz VALUES (%s)"

cursor.execute(query, (file_content,))

db.commit()
db.close()
