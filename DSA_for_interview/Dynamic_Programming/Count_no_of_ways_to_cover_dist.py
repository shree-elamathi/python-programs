'''
Given a distance ‘dist’, count total number of ways to cover the distance with 1, 2 and 3 steps.
'''


class Solution:
    def countWays(self, n):
        mat = [[0]*n]*(n//2)

n = 4
print(Solution().countWays(n))
