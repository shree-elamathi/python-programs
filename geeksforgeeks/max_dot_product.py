#Given two arrays a and b of positive integers of size n and m where n >= m, the task is to
# maximize the dot product by inserting zeros in the second array but you cannot disturb the order
# of elements.
#Dot product of array a and b of size n is a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1].
class Solution:
    def maxpro(self,n,m,a,b):
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(min(m,i+1)):
                dp[i+1][j+1]=max(dp[i][j+1],dp[i][j]+a[i]*b[j])
        return dp[-1][-1]

n=8
m=6
a=[6, 3, 6, 3, 8, 6, 3, 9]
b=[6, 3, 9, 8, 4, 2]
print(Solution().maxpro(n,m,a,b))