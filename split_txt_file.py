import mysql.connector
import re


db = mysql.connector.connect(host="localhost",user="root",password="root", auth_plugin='mysql_native_password',database='signup')
##with  open('questiondb.txt') as fp:
##    contents = fp.read()
##    for entry in contents.split(';'): #Delimiter
##        print(entry)

cursor = db.cursor()

file = open("questiondb.txt","r")

#Repeat for each song in the text file
i=1
for line in file:
  
  #Let's split the line into an array called "fields" using the ";" as a separator:
  fields = line.split(";")
  
  #and let's extract the data:
  question = fields[0]
  opA = fields[1]
  opB = fields[2]
  opC = fields[3]
  opD = fields[4]
  CA = fields[5]
  Marks = fields[6]
  DL = fields[7]
 
  #Print the song
  print('Question No: ',i)
  print(question)
  print('Option A: ',opA)
  print('Option B: ',opB)
  print('Option C: ',opC)
  print('Option D: ',opD)
  print('Marks: ',Marks)
  query = "INSERT INTO questiondb(questions,opA,opB,opC,opD,correctop,marks,diff_level) VALUES(\""
  query+=question
  query+='\",\"'
  query+=opA
  query+='\",\"'
  query+=opB
  query+='\",\"'
  query+=opC
  query+='\",\"'
  query+=opD
  query+='\",\"'
  query+=CA
  query+='\",'
  query+=Marks
  query+=',\"'
  query+=DL
  query+='\")'
  print(query)
  cursor.execute(query)
  i=i+1
#It is good practice to close the file at the end to free up resources
print("Total Number of Record Inserted:: ",i)
file.close()
db.commit()
db.close()
