'''
Given an integer array arr[]. You need to find the maximum sum of a subarray.
'''

class Solution:
    def maxSubArraySum(self,arr):
        res= arr[0]
        cur = arr[0]
        for i in range(1,len(arr)):
            cur = max(cur+arr[i], arr[i])
            res = max(res, cur)
        return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(Solution().maxSubArraySum(arr))