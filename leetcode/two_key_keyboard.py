'''
You said:
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad
for each step:
Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
'''
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i  # Maximum number of operations could be i (all paste operations after a single copy)
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]
n = 3
print(Solution().minSteps(n))