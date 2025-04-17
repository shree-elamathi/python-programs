'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit
would be 0.
'''


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        pro = 0
        for i in range(n):
            for j in range(i+1, n):
                pro = max(pro, prices[j] - prices[i])
        return pro


prices = [10,8,7,5,2]
print(Solution().maxProfit(prices))