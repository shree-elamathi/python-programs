choc=10
stud=6
balance_choc=choc-stud
#print(balance_choc)
mat=[[0,1,0],[0,1,0],[0,1,0]]
'''
problem 1:
Given an unsorted array arr. Find the count of elements less than or equal to the given element x.
ex:
Input: x = 9, arr = [10, 1, 2, 8, 4, 5] 
Output: 5
Explanation: The 5 elements are 1, 2, 8, 4 and 5.
'''
class Solution:
    def minvalue(self,arr,x):
        arr.sort()
        count=0
        for i in arr:
            if i<=x:
                count+=1
            else:
                break
        return count

arr = [11,10, 1, 2, 8, 4, 5]
x = 9
#print(Solution().minvalue(arr,x))

'''
problem 2:
Given an array arr[]. The task is to rotate the array by d elements where d ≤ arr.size.
ex:
Input: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
Output: [-3, 4, 5, 6, 7, -1, -2]
Explanation: 
Rotate by 1: [-2, -3, 4, 5, 6, 7, -1]
Rotate by 2: [-3, 4, 5, 6, 7, -1, -2]
Note: Make changes in the same arr do not use temp arr
'''
'''
1,2,3,4,5,6,7,8
2,3,4,5,6,7,8,1
3,4,5,6,7,8,1,2
'''
class Solution:
    def rotatearr(self,arr,d):
        for i in range(d):
            x=arr.pop(0)
            arr.append(x)
        return arr
arr = [-1, -2, -3, 4, 5, 6, 7]
d=2
print(Solution().rotatearr(arr,d))