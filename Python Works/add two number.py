'''
Problem #3 
Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
 explanation (321 + 765 = 1086)
 '''
def addtwonumber(l1,l2):
    s1=""
    s2=""
    output_list=[]
    for i in l1:
        i =str(i)
        s1+=i
    for j in l2:
        j =str(j)
        s2+=j
    sum = int(s1)+int(s2)
    for i in range(len(str(sum))):
        rem = sum % 10
        sum = sum // 10
        output_list.append(rem)
    return output_list
        
list1 =[1,2,3]
list2 =[5,6,7]
# list1=[9,9,9,9,9,9,9]
# list2=[9,9,9,9]
list1.reverse()
list2.reverse()

result = addtwonumber(list1,list2)
print(result)

