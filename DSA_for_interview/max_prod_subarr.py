'''
Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum
product that we can get in a subarray of arr[].
Note: It is guaranteed that the output fits in a 32-bit integer
'''

class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        max_prod = float('-inf')
        lefttoright = 1
        righttoleft = 1
        for i in range(n):
            if lefttoright == 0:
                lefttoright = 1
            if righttoleft == 0:
                righttoleft = 1
            lefttoright *= arr[i]
            righttoleft *= arr[n - 1 - i]
            max_prod = max(righttoleft, lefttoright, max_prod)
        return max_prod

arr = [-2, 6, -3, -10, 0, 2]
print(Solution().maxProduct(arr))