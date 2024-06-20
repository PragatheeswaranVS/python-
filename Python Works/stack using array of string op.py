'''
Problem #5
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output =  15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output =  25
explanation (10 - ( 2 + 3)) * 5 = 25
'''
list1 = ["+","1", "2", "*", "5"]
#list1 = ["-","10", "+", "2", "3", "*", "5"]
arr =[]
count = 0
def add(arr):
    b = 0
    for i in range(3):
       a = arr.pop()
       if a != "+":
           b += a
    return b
def sub(arr):
    b = 0 
    for i in range(3):
        a = arr.pop()
        if a != "-":
            a -= b
    return b
def mul(arr):
    b = 1
    for i in range(3):
        a = arr.pop()
        if a != "*":
            b *= a
    return b
def div(arr):
     b=1
     for i in range(3):
         a = arr.pop()
         if a != "/":
             b /= a
     return b

for i in list1:
    try:
        i = int(i)
        arr.append(i)
        count += 1
        
    except:
        op = i
    if len(arr) < 3:
        continue
    else:
        if count >= 3:
                if op == "+":
                    res = add(arr)
                    arr.append(res)
                elif "-" in arr:
                    res = sub(arr)
                    arr.append(res)
                elif "*" in arr:
                    res = mul(arr)
                    arr.append(res)
                elif "/" in arr:
                    res = div(arr)
                    arr.append(res)
print(arr)
