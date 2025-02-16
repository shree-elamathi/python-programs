'''
You are given weights and values of items, and put these items in a knapsack of capacity W to get the maximum total
value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val and wt which represent values and weights associated with items
respectively. Also given an integer W which represents knapsack capacity, find out the maximum sum values subset of
val[] such that the sum of the weights of the corresponding subset is smaller than or equal to W. You cannot break an
item, either pick the complete item or don't pick it (0-1 property).
'''
class Solution:
    def knapSack(self, W, wt, val):
        n = len(val)  # Infer the number of items from the length of val or wt

        # Create a 2D array to store the maximum value that can be obtained with the given capacity
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Build the dp array from the bottom up
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]
W = 4
val = [1,2,3]
wt = [4,5,1]
print(Solution().knapSack(W,wt,val))