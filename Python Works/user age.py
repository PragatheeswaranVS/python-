import sys
member = int(input("How many member in your family : "))
minor_member = 0
major_member = 0
senior_member = 0
if member <= 0:
    print("ATLEAST ONE MEMBER IN A FAMILY...")
    sys.exit()
for i in range(member):
    age = int(input(f"enter the member {i+1} age : "))
    if age > 0:
        if age >= 110:
            break
        elif age >= 60:
            senior_member += 1  
        elif age >= 18:
            major_member += 1
        else:
            minor_member += 1  
    
    else:
        print("YOU ENTERED INVALID AGE !!!")
        sys.exit()
print("major member in the family is :",major_member + senior_member)   # Here senior citizen are also consider as major member
print("minor member in the family is :",minor_member)    
print("senior member in the family is :",senior_member)       
