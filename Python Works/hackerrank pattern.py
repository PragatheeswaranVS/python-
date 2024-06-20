num = int(input("enter the number: "))
number = 2*num-1
#for i in range(number):
for row in range(number):
    for col in range(number):
        if row == 0 or col == 0 or row == number-1 or col == number-1:
            print(num,end=" ") 
        elif row == 1 or col == 1 or row == number - 2 or col == number - 2:
            print(num-1,end=" ")
        elif row == 2 or col == 2 or row == number - 3 or col == number - 3:
            print(num-2,end=" ")
        elif row == 3 or col == 3 or row == number - 4 or col == number - 4:
            print(num-3,end=" ")
        else:
            print(num-4)
    print("")
   
    