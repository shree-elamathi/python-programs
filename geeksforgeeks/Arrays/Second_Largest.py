'''
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest
element doesn't exist then return -1.
'''
class Solution:
    def print2largest(self,arr, n):
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        arr = list(set(arr))
        arr.sort()
        if len(arr) >= 2:
            return arr[-2]
        else:
            return "-1"
arr=[10,5,10]
n=len(arr)
print(Solution().print2largest(arr,n))