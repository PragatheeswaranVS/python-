'''
pattern printing program for H
'''
def pattern_E():
    num = int(input("enter the number: "))

    if num > 3 :
        for row in range(num):
            for col in range(num):
                if row == 0 or col == 0 or row == num-1 or row == (num//2): 
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
            print(" ")
    else:
        print("number should be above 3")

pattern_E()



