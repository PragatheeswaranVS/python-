first_number = int(input("enter the first number : "))
second_number = int(input("enter the second number : "))
end_number = int(input("how many time you need to loop : "))
temp = 0
for i in range(0,end_number):
    temp = first_number  + second_number
    first_number = second_number
    second_number = temp
    print(temp)
    