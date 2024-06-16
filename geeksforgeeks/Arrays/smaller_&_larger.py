'''
Given a sorted array Arr of size N and a value X, find the number of array elements less than or equal to X
and elements more than or equal to X.
'''
class Solution:
    def getMoreAndLess(self,arr, n, x):
        more=0
        less=0
        for i in arr:
            if i>x:
                more+=1
            elif i<x:
                less+=1
            else:
                more += 1
                less += 1
        res=[]
        res.append(less)
        res.append(more)
        return res
arr=[1, 2, 8, 10, 11, 12, 19]
n=7
x=0
print(Solution().getMoreAndLess(arr,n,x))
