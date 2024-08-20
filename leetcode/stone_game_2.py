'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each
pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then,
we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
'''
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        suffix_sum = [0] * (n + 1)

        # Compute the suffix sums
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Bottom-up DP approach
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                # Try all possible X values Alice can take
                for X in range(1, 2 * M + 1):
                    if i + X > n:
                        break
                    dp[i][M] = max(dp[i][M], suffix_sum[i] - dp[i + X][max(M, X)])

        return dp[0][1]
piles = [2,7,9,4,4]
print(Solution().stoneGameII(piles))