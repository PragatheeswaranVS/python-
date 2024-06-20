First_name=input("Enter your First_name: ")
First_name_length = len(First_name.strip())
if First_name_length < 3:
	print("Invalid name")
elif (First_name == First_name.lower()) or (First_name[0] == First_name.lower()):
    print("Invalid First_name not contains upper case.")

Last_name=input("Enter your Last_name: ")
Last_name_length = len(Last_name.strip())
if Last_name_length < 3:
	print("Invalid name")
elif (Last_name == Last_name.islower()) or (Last_name[0] == Last_name.islower()):
    print("Invalid Last_name.")


Age=int(input("Enter your Age: "))
if(Age<=0):
    print("invalid,Check the given Age.")

Phone_number=input("Enter your phone number: ")
Phone_number_length=len(Phone_number.strip())
if(Phone_number_length < 10) or (Phone_number_length > 10):
    print("Invalid, please enter the 10 digit number")

Email_id=input("Enter your Email_id: ")
if '@' not in Email_id or '.' not in Email_id:
    print("Invalid, Email_Id not contains @ and dot.")

print()
print("Firstname: ",First_name) 
print("Lastname: ",Last_name)    
print(f"Your Name is: {First_name} {Last_name}")     
print("Age: ",Age)
print("Phone number: ",Phone_number) 
print("Email id: ",Email_id)