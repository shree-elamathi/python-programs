'''
Given an integer n denoting the Length of a line segment. You need to cut the line segment in such a way that the
cut length of a line segment each time is either x , y or z. Here x, y, and z are integers.
After performing all the cut operations, your total number of cut segments must be maximum. Return the maximum number
of cut segments possible.
Note: if no segment can be cut then return 0.
'''


class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        return max(dp[n], 0)
n = 4
x = 2
y = 1
z = 1
print(Solution().maximizeTheCuts(n,x,y,z))