'''
pattern printing program for H
'''

num = int(input("enter the number: "))
def pattern_O():
    if num > 2 :
        for row in range(num):
            for col in range(num):
                if col == 0 or col == num-1 or row == num-1 or row == 0: 
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
            print(" ")
    else:
        print("number should be above 2")
pattern_O()


