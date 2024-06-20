'''
Homework - Write a program to continuously get firstname and last name of various students from the user. 
Stop when the user's first name or last name starts with "Z".
'''
is_name = True
count =  0
while (is_name == True):
   count += 1
   
# code for first name...
   first_name = input(f"enter first name of person {count}: ")
   first_name_length = len(first_name)
   if first_name.startswith("z") or first_name.startswith("Z"):
       is_name = False
       print("Don't startwith 'z' in the first name")
       break
   elif first_name_length < 3:
       print("first name is too short")
   elif first_name.isalpha() == False:
       print("first name should have alphabetic characters")
       
# code for last name... 
   last_name = input(f"enter last name of person {count}: ")
   last_name_length = len(last_name)
   if last_name.startswith("z") or last_name.startswith("Z"):
       is_name = False
       print("Don't startwith 'z' in the last name")
       break
   elif last_name_length < 3:
       print("last name is too short")
   elif last_name.isalpha() == False:
       print("last name should have alphabetic characters")
       
    # printing the name... 
   if (first_name.isalpha() and last_name.isalpha()) and (first_name_length > 3 and last_name_length > 3):
     name = first_name + " " + last_name
     print(f"person {count} name: {name}") 

      