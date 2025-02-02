'''
Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by
changing rows to columns and columns to rows.
'''

class Solution:
    def transpose(self, mat, n):
        print(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i], mat[i][j]
        return mat

mat=[[1, 2],[4, 5] ]
n=2
print(Solution().transpose(mat,n))