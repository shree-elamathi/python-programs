'''
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest
element doesn't exist then return -1.
'''
class Solution:
    def print2largest(self,arr, n):
        arr.sort()
        mx=max(arr)
        for i in range(n-1,-1,-1):
            if arr[i]<mx:
                return arr[i]
arr=[10,5,10]
n=len(arr)
print(Solution().print2largest(arr,n))