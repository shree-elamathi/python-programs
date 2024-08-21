'''
There is a strange printer with the following two special properties:
The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original
existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
'''
class Solution:
    def strangePrinter(self,s):
        n = len(s)
        if n == 0:
            return 0

        # dp[i][j] will hold the minimum number of turns needed to print the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Fill the dp table
        for length in range(1, n + 1):  # length is the length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # maximum turns needed is the length of the substring
                if length == 1:
                    dp[i][j] = 1
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                    if s[i] == s[j]:
                        dp[i][j] -= 1

        return dp[0][n - 1]
s="a"
print(Solution().strangePrinter(s))