'''
Given a rod of length n(size of price) inches and an array of prices, price. price[i] denotes the value of a piece
of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
'''


class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], price[j] + dp[i - (j + 1)])

        return dp[n]

price = [1, 5, 8, 9, 10, 17, 17, 20]
print(Solution().cutRod(price))