n = 3
m = 4
matrix = [[12, 11, 10, 9],
         [8, 7, 6, 5],
         [4, 3, 2, 1]]


class Solution:
    def boundrytraversal(self, matrix, n, m):
        a=[]
        if n and m>=1:
            i=0
            for j in range(m):
                var=matrix[i][j]
                a.append(var)
            obj.rightside(matrix,i+1,j,n,m,a)
        return a
    def rightside(self,matrix,i,j,n,m,a):
        for k in range(i,n):
            var1=matrix[k][j]
            a.append(var1)
        obj.bottomside(matrix,i,j-1,n,m,a)
        return a
    def bottomside(self,matrix,i,j,n,m,a):
        for k in range(j,-1,-1):
            var2=matrix[n-1][k]
            a.append(var2)
        obj.leftside(matrix,i-1,j,n,m,a)
        return a
    def leftside(self,matrix,i,j,n,m,a):
        for k in range(j,-1,-1):
            if k>0:
                var3=matrix[k][i]
                a.append(var3)
        return a


obj = Solution()
ans=obj.boundrytraversal(matrix,n,m)
for i in ans:
    print(ans,end=' ')
print()

