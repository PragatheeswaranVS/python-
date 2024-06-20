'''
Problem #4
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output =  15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''
list1=["10","2","3","+","-","5","*"]
#list1=["1","2","+","5","*"]
arr =[]
def add(arr):
    b=0
    for i in range(2):
         b+=arr.pop(len(arr)-1)
    return b
def sub(arr):
    b = 0
    for i in range(2):
        b = arr.pop(len(arr)-1) - b
    return b
def mul(arr):
    b = 1
    for i in range(2):
        b= arr.pop(len(arr)-1) * b
    return b
def div(arr):
     b=1
     for i in range(2):
         b= arr.pop(len(arr)-1) / b
     return b

for i in list1:
    try:
       i = int(i)
       arr.append(i)
    except:
        i = i
    if i == "+":
       res = add(arr)
       arr.append(res)
    elif i == "-":
        res = sub(arr)
        arr.append(res)
    elif i == "*":
        res = mul(arr)
        arr.append(res)
    elif i == "/":
        res = div(arr)
        arr.append(res)
print(arr)