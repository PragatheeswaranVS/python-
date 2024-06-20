'''
Home work: Write a program to get first name, last name, age, phone number and email id from the user. Validate all the inputs and print the user information in a readable manner.
User's name must be printed in capital letters (or first letter should be capital). Phone number must contain 10 digits and no alphabets. Email id must contain a dot and @. Age must be a valid number.
'''

first_name = input("enter your First name : ")
first_name_length = len(first_name.strip())
if first_name_length < 3 :
    print("incorrect First name ")
elif (first_name == first_name.lower() or first_name[0] == first_name.lower()):
    print("please enter your First name in capital letter")

last_name = input("enter your Last name : ")
last_name_length = len(last_name.strip())
if last_name_length < 3:
    print("incorrect Last name")
elif (last_name == last_name.lower() or last_name[0] == last_name.lower()):
    print("please enter your Last name in capital letter")
age = int(input("enter your age : "))
if age <= 0:
    print("please enter your age correctly")
phone_number = input("enter your mobile number: ")
phnone_number_length = len(phone_number.strip())
if  phnone_number_length < 10 or phnone_number_length > 10:
    print("please enter 10 digit ")
email = input("enter your email address : ")
if "@" not in email or "." not in email:
    print("you entered invalid email address")
print(f"Name : {first_name} {last_name}")
print("Age :",age)
print("Mobile Number :",phone_number)
print(f"Email :{email}")