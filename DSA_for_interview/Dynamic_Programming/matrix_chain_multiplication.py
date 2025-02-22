'''
Given an array arr[] which represents dimensions of sequence of matrices where the ith matrix has the dimensions
(arr[i-1] x arr[i]) for i>=1., find the most efficient way to multiply these matrices together. The efficient way
is the one that involves the least number of multiplications.
'''

import sys


class Solution:
    def matrixMultiplication(self, arr):
        N = len(arr)
        dp = [[0] * N for _ in range(N)]
        for length in range(2, N):
            for i in range(1, N - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][N - 1]
