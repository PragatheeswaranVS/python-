import sys
print("NOTE : PLEASE ENTER 8 CHARACTERS OR ABOVE...")
password = input("CREATE PASSWORD : ")
alpha_count = 0  
num_count = 0
spec_count = 0
if len(password) >= 8: 
    for i in password:
        if i.isalpha():
           alpha_count += 1
        elif i.isnumeric():
            num_count += 1
        else:
            spec_count +=1
else:
    print("your password password is short")
    sys.exit()
# To check if there is only alphabets or only numbers or only special characters...
if  password.isalpha() == True or password.isnumeric() == True or spec_count == 8: 
   print("your password is week")
   sys.exit()
# To check if there atleast 3 alphabets and 2 numbers and one special character... 
elif alpha_count >= 3 and num_count >= 2 and spec_count >= 1:
    if len(password) >= 16:  # To check if the length of the password is 16 then print very strong . else print strong...
        print("your password is very strong")
    else:
        print("your password is strong")
        sys.exit()
else:
      print("your password is good") 
