'''
Given a binary matrix mat of size n * m, find out the maximum length of a side of a square sub-matrix with all 1s.
'''
class Solution:
    def maxSquare(self,n,m,mat):
        if not mat or not mat[0]:
            return 0
        dp=[[0]*n for _ in range(m)]
        max_side=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    max_side=max(max_side,dp[i][j])
        return max_side

n = 6
m = 5
mat= [ [0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
print(Solution().maxSquare(n,m,mat))