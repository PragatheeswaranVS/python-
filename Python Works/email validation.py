import sys
email = input("enter your email address: ")
if len(email) < 10:
    print("email is too short")
    sys.exit()
if "@" not in email or "." not in email:
     print("email must contains '@' and '.'") 
     sys.exit() 
if email.count("@") > 1:
    print(f"email contains only one '@' . Here '@'  symbol {email.count("@")} times occured")
    sys.exit()
split_string = email.split("@")
user_name= split_string[0]
last_portion = split_string[1]
if user_name.isalnum() == False:
    print("User name does not allow special characters")
    sys.exit()
split_last_portion = last_portion.split(".")
domain = split_last_portion[0]
extention = split_last_portion[1]
if len(domain) < 3:
    print("domain name atleast contains 3 characters")
    sys.exit()
print(email)




