'''
Given two strings str1 and str2. Return the minimum number of operations required to convert str1 to str2.
The possible operations are permitted:
Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
'''
class Solution:
    def editDistance(self, str1, str3):
        m,n=len(str1),len(str3)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str3[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[m][n]

str1="geek"
str2="gesek"
print(Solution().editDistance(str1,str2))