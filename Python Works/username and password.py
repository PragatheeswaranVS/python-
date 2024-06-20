import sys
user_name = input("enter the user name : ")
extention =(".com",".edu",".tech",".org")
if user_name.isnumeric() == True: # check if the user name has only numeric value or not... 
    print("user name should have combination alphabets and number.But don't have special character..")
    sys.exit()
# check if the "@" is present or not . if "@" present then check the no .of "@" occured.
if "@" not in user_name:
    print("user name should contain special charcter :'@' ") 
    sys.exit()
elif user_name.count("@") > 1: 
    print(f"user name contain only one '@'.Here {user_name.count("@")} times occured")
    sys.exit()
if user_name.endswith("@"):
    print("please enter the company name and extention")
    sys.exit()

# Here we checking the user name has extention : ('.com','.edu','.tech','.org')
if user_name.endswith(extention) == False:
    print("user name should ends with extention like : '.com','.edu','.tech','.org' ")
    sys.exit()
split_user_name = user_name.split("@")
first_name = split_user_name[0]
last_name = split_user_name[1]

# Here we check the last name starts with "."  
if last_name.startswith("."):
    print("After @ you should enter the company name")
    sys.exit()
split_last_name = last_name.split(".")
 
company_name = split_last_name[0]
if company_name not in user_name :
    print("user name should have company name")
    sys.exit()
# FOR PASSWORD....

first_character = first_name[0:1]
second_character = first_name[2:]
third_character = last_name[0:3]
fourth_character = input("enter the fourth character : ")
password = first_character + second_character + third_character +fourth_character
print("user name : ",user_name)
print("password : ",password)