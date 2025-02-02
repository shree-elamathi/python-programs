'''
Given a boolean matrix mat where each cell contains either 0 or 1, the task is to modify it such that if a matrix cell
matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.
'''


class Solution:
    def booleanMatrix(self, mat):
        rows = [0]*len(mat)
        cols = [0]*len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rows[i] == 1 or cols[j] == 1:
                    mat[i][j] = 1
        return mat


mat = [[1, 0, 0, 1],[0, 0, 1, 0], [0, 0, 0, 0]]
print(Solution().booleanMatrix(mat))