table = int(input("enter the table you want : "))
if table <= 0:
    print("INVALID NUMBER : NEGATIVE NUMBER AND ZERO NOT ACCEPTED !!!")
else:
    end = int(input("enter the end number : "))
    for i in range(1,end):
        result = table * i
        print(f"{table} * {i} = {result}")
