'''day = "wed"
days =10
week = ["sun","mon","tue","wed","thu","fri","sat"]
c = 0
n = len(week) 
for i in range(days):
    if day == "sun":
        c +=1
    k = week.index(day)
    day = week[k%n+1]
print(c)
import sys
string = input("enter anything : ")
new_string = string.capitalize()
upper_character= new_string[0]
lower_character = new_string[1:].replace(" ","")
updated_lower_character = ""
numberic_case = ""
print(upper_character)
for ch in lower_character:
    if ch.isalpha() == True:
       updated_lower_character += ch 
    elif ch.isdigit() == True:
        numberic_case +=ch
print(updated_lower_character)       
print(numberic_case) 


from sqlquery import sql
# from tabulate import tabulate
query = "select name,regno from student_mark"
a = sql(query)
print(a)

'''
import mysql.connector
from tabulate import tabulate
connect = mysql.connector.connect(
    user = "root",
    password = "Pragathees@2004",
    host = "localhost",
    database = "projects"
)
cursor = connect.cursor()
def view():
    query = "select name,register_no,dob from student_mark"
    cursor.execute(query)
    show=cursor.fetchall()
    # for data in show:
    #     name = data[0]
    #     register_no = data[1]
    #     dob = data[2]

    print(tabulate(show,headers=["name","register_no","dob"]))
    
view()