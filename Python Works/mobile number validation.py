import sys
mobile_number = input("enter your mobile number: ")
if len(mobile_number) != 10:
   print("invalid mobile number")
   sys.exit()
elif mobile_number[0] == "0":
    print("mobile number does not starts with 0")
    sys.exit()
elif mobile_number.isnumeric() == False:
    print("Alphabet not allowed in mobile number")
    sys.exit()
else:
    print(mobile_number)