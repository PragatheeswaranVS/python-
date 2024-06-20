'''
no_of_student_dp_1 = input("enter the number of student learning python in department 1:")
#no_of_student_dp_2 = input("enter the number of student learning python in department 2:")
#no_of_student_dp_3 = input("enter the number of student learning python in department 3:")
python_mark_dp_1 = input("enter the python mark of students in department 1 and seperate by comma:")
#python_mark_dp_2 = input("enter the python mark of students in department 2 and seperate by comma:")
#python_mark_dp_3 = input("enter the python mark of students in department 3 and seperate by comma:")
mark_split_dp_1 = python_mark_dp_1.split(",")
#mark_split_dp_2 = python_mark_dp_2.split(",")
#mark_split_dp_3 = python_mark_dp_3.split(",")
mark_in_dp_1={}
mark_in_dp_2={}
mark_in_dp_3={}

roll_no =1
for value in mark_split_dp_1:
    value = int(value)
    mark_in_dp_1[roll_no]=value
    roll_no += 1

for value in mark_split_dp_2:
    value = int(value)
    mark_in_dp_2[roll_no]=value
    roll_no += 1

for value in mark_split_dp_3:
    value = int(value)
    mark_in_dp_3[roll_no]=value
    roll_no += 1

for i in range(no_of_student_dp_1):
    for value in mark_in_dp_1.values():
        max = mark_in_dp_1[1]
        if max > value:
            continue
        else:
            max = value
print(f"the top three marks are: {max}")       
'''
def ip():
    file = open("ip address.txt","w")
    for i in range(5):
        ip=input(f"ip {i+1}:")
        print(ip)
        file.write(ip+"\n")
    file.close()
ip()
