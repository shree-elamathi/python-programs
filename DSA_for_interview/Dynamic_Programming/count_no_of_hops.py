'''
A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top of nth step.
'''


class Solution:
    # Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return self.countWays(n-1) + self.countWays(n-2) + self.countWays(n-3)



n = 4
print(Solution().countWays(n))
