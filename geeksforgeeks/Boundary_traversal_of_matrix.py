n = 4
m = 4
matrix = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15,16]]


class Solution:
    def boundaryTraversal(self, matrix, n, m):
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
ans = obj.boundaryTraversal(matrix, n, m)
for i in ans:
    print(i, end=' ')
print()

