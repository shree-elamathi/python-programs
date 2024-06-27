'''
A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is
constant, i.e., all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to
complete the function isToeplitz which returns 1 if the matrix is Toeplitz otherwise, it returns 0.
'''
class Solution:
    def isToepliz(self,mat):
        if len(mat)==1 or len(mat[0])==1:
            return 1
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                if mat[i][j]!=mat[i-1][j-1]:
                    return 0
        return 1
mat = [[1,2,3], [4,5,6]]
print(Solution().isToepliz(mat))