num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))
num3=int(input("enter the third number :"))
print(num1)
print(num2)
print(num3)
if num1 > num2 and num1 > num3:
    max = num1
    print("the greater number is ",max)
elif num2 > num1 and num2 > num3:
    max = num2
    print("the graeter number is ",max)
else:
    max = num3
    print("the greater number is ",max)