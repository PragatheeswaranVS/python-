'''
Homework - Find sum of odd digits and sum of even digits in a number. 
For example, if the input is 58974, sum of odd digits is 5+9+7=21 and sum of even digits is 8+4=12
'''

num = int(input("enter the number: "))
sum_of_odd = 0
sum_of_even = 0
while num > 0:
    rem = num % 10
    num = num // 10
    if rem % 2 == 0:
        sum_of_even += rem
    else:
        sum_of_odd += rem
print(f"sum of odd digits: {sum_of_odd}")
print(f"sum of even digits: {sum_of_even}")