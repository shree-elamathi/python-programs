'''
Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so, as
to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of
str1 and inserted to some another point.
'''
class Solution:
    def minInsertandDelete(self,str1,str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_length = dp[m][n]
        deletions = m - lcs_length
        insertions = n - lcs_length

        return deletions + insertions
s1="pea"
s2="heap"
print(Solution().minInsertandDelete(s1,s2))