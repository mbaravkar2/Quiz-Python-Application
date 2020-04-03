import mysql.connector



mydb = mysql.connector.connect(host="localhost",
                               user="root",password="root",
                              auth_plugin='mysql_native_password',database='signup')

print("Database Connected")

cur = mydb.cursor()
query = 'select * from questiondb'
cur.execute(query)
data = cur.fetchall()
mydb.commit()
mydb.close()
#print(list(data))
que = []
opa = []
opb = []
opc = []
opd = []
for set in data:
    q_no = set[0]
    
    question = set[1]
    que += list(question.split(","))
    
    optionA = set[2]
    opa += list(optionA.split(","))
    
    optionB = set[3]
    opb += list(optionB.split(","))
    
    optionC = set[3]
    opc += list(optionC.split(","))
    
    optionD = set[5]
    opd += list(optionD.split(","))
    
    correct_ANS = set[6]
    marks = set[7]
    diff_level = set[8]
    print("Question No : ",q_no)
    print("Question: ",question)
    print("OPTa: ",optionA)
    print("OPTb: ",optionB)
    print("OPTc: ",optionC)
    print("OPTd: ",optionD)
    print("correct ans: ",correct_ANS)
    print("marks: ",marks)
    print("difficulties: ",diff_level)






