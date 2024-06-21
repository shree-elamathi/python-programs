'''
Given an array arr of n non-negative numbers. The task is to find the first equilibrium point in an array.
The equilibrium point in an array is an index (or position) such that the sum of all elements before that index
is the same as the sum of elements after it.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.
'''
class Solution:
    def equilibriumPoint(self,arr, n):
        if len(arr)==1:
            return 1
        tot_sum=sum(arr)
        left_sum=0
        for i,num in enumerate(arr):
            tot_sum-=num
            if tot_sum==left_sum:
                return i+1
            else:
                left_sum+=num
        return "-1"


arr = [1,3,5,2,2]
n = len(arr)
print(Solution().equilibriumPoint(arr,n))