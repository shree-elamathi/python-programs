'''
Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n. Return the
missing element.
'''
class Solution:
    def missingNumber(self, n, arr):
        arr.sort()
        for i in range(1,n):
            if i!=arr[i-1]:
                return i
        return n
arr=[1,2,3,5]
n=5
print(Solution().missingNumber(n,arr))