'''
############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
'''
count = 0
money_received = 0
for i in range(5):
    money = int(input("please give me some money to buy ticket for movie : "))
    count += 1
    money_received += money
    if money > 10:
        
        print(f"I got {money_received} . Thank you so much\n")
        if money_received == 1000:
            print("I got enough money to buy ticket")
            break
        elif money > 1000:
            print("I am very glad that you gave extra money to me")
            break
    else:
        print(f"{money_received} rupee is not enough to buy ticket")  
        break
if money_received >= 1000:
     print(f"I asked money from my parents for {count} time to get the ticket")
else:
    print(f"{money_received} is not enough to buy ticket and i asked {count} time to get this money")
    
