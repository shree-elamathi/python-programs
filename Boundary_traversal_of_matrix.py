n = 3
m = 4
matrix = [[12, 11, 10, 9],
         [8, 7, 6, 5],
         [4, 3, 2, 1]]


class Solution:
    def boundrytraversal(self, matrix, n, m):
        a = []
        if n and m >= 1:
            for j in range(m):
                var = matrix[0][j]
                a.append(var)
            for i in range(1, n):
                var1 = matrix[i][m - 1]
                a.append(var1)
            if n > 1:
                for j in range(m - 2, -1, -1):
                    var2 = matrix[n - 1][j]
                    a.append(var2)
            if m > 1:
                for i in range(n - 2, 0, -1):
                    var3 = matrix[i][0]
                    a.append(var3)
        return a


obj = Solution()
ans=obj.boundrytraversal(matrix,n,m)
for i in ans:
    print(i,end=' ')
print()

