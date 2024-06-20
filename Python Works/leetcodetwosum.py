'''def twosum():
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):  
            if i != j:
                sum = l1[i] + l1[j]
                if target == sum:
                   return [i,j]   
        
                
    
l1=[2,7,11,5,18]
target = int(input("target ="))
add = twosum()
print(add)'''
#l3 = [1,5,2,8,0,9]

"""l3 = [1,2,3,4]
l3=sorted(l3)
print(l3)
if len(l3) % 2 == 1:
    res = l3[len(l3) // 2] 
    print(float(res))
else:
    res = ( l3[len(l3) // 2 - 1] + l3[len(l3) // 2 ] ) / 2
    print(res)"""
    
    
class Solution:
    def findMedianSortedArrays(self, nums1, nums2,l3):
            for i in nums1:
                l3.append(i)
            for i in nums2:
                l3.append(i)
            l3 = l3.sort()
            if len(l3) % 2 == 1:
                return  float(l3[len(l3) // 2])
            else:
                return (l3[len(l3) // 2 - 1] + l3[len(l3)  // 2]) / 2
nums1 = []
nums2 = []
l3 = []


ret = Solution().findMedianSortedArrays(nums1,nums2,l3)
print(ret)