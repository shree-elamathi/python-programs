'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both
diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
'''
import numpy as np
class Solution:
    def numMagicSquaresInside(self, grid):
        #check if the grid consists only rows and if length of rows is less than 3
        if len(grid)<3 or len(grid[0])<3:
            return 0
        mat=np.array(grid)
        count=0
        def checkMagicSquare(mat):
            row_sum=sum(mat[0]) #sum of the row ele and for checking all conditions

            #check all elements are unique
            arr=[]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] not in arr:
                        arr.append(mat[i][j])
            if len(arr)<9 or max(arr)>9 or min(arr)<1:
                return False

            #For checking the rows
            for i in range(1,len(mat)):
                if sum(mat[i])!=row_sum:
                    return False

            #for checking columns
            j=0
            for _ in range(3):
                c_sum=0
                for i in range(3):
                    c_sum+=mat[i][j]
                j+=1
                if c_sum!=row_sum:
                    return False

            #right diagonal
            di_sum=0
            for i in range(3):
                di_sum+=mat[i][i]
            if di_sum!=row_sum:
                return False

            #left diagonal
            diag_sum=mat[0][2] + mat[1][1] + mat[2][0]
            if diag_sum!=row_sum:
                return False
            return True

        for i in range(len(grid)-2): #for rows
            for j in range(len(grid[0])-2):#for columns
                sl_mat=mat[i:i+3,j:j+3]
                if checkMagicSquare(sl_mat):
                    count+=1

        return count

grid=[[7,0,5],[2,4,6],[3,8,1]]
print(Solution().numMagicSquaresInside(grid))
