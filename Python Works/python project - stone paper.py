import random
print("0-> rock \t 1-> paper \t 2-> pencil \t 3-> sissor")
num = int(input("enter the number (0-3): "))
if num == 0:
    print("you selected rock")
elif num == 1:
    print("you selected paper")
elif num == 2:
    print("you selected pencil")
elif num == 3:
    print("you selected sissor")
else:
    print("you entered invalid input...")
#random_num = random.randint(1,3)
#if 0 > 1:
    #print("you win")
