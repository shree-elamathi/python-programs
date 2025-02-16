'''
Given an array arr[] of integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

A subsequence is strictly increasing if each element in the subsequence is strictly less than the next element.
'''

class Solution:
    def lis(self, arr):
        dp = [1 for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp [i] = max(dp[i] , dp[j] + 1)
                    print(dp)
        return max(dp)


arr = [5, 8, 3, 7, 9, 1]
print(Solution().lis(arr))