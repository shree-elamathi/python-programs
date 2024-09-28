'''
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the
following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be
|hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek
reaches the last stone.
'''


class Solution:
    def minCost(self, arr, k):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, min(k, i) + 1):
                dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))

        return dp[-1]


arr = [10, 30, 40, 50, 20]
k = 3
sol = Solution()
print(sol.minCost(arr, k))  # Output will be the minimum cost to reach the last stone
