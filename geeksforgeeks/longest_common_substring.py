'''
You are given two strings str1 and str2. Your task is to find the length of the longest common substring among
the given strings.
'''
class Solution:
    def longestCommonSubstr(self, str1, str2):
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len
s1 = "ABCDGH"
s2 = "ACDGHR"
print(Solution().longestCommonSubstr(s1,s2))