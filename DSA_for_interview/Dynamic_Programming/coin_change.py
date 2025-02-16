'''
Given an integer array coins[ ] representing different denominations of currency and an integer sum, find the number
 of ways you can make sum by using different combinations from coins[ ].
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you
want.
Answers are guaranteed to fit into a 32-bit integer.
'''

class Solution:
    def count(self, coins, Sum):
        dp = [[0 for i in range(Sum + 1)]for _ in range(len(coins))]
        for i in range(len(coins)):
            dp [i][0] = 1
        for j in range(1,Sum + 1):
            if (j >= coins[0]) and (j % coins[0] == 0):
                dp[0][j] = 1
        for i in range(1,len(coins)):
            for j in range(Sum + 1):
                if j < coins[i]:
                    dp [i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i]]
        return dp[len(coins)-1][Sum]
coins = [2,3,5,10]
sum = 15
print(Solution().count(coins,sum))
