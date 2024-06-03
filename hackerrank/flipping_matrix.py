'''
Given an 2n×2n matrix, your goal is to maximize the sum of the n×n submatrix in the top-left corner.
You are allowed to flip rows and columns to achieve this.
'''
class Solution:
    def max_sum(self,matrix):
        n=len(matrix)//2
        sum=0
        for i in range(n):
            for j in range(n):
                sum+=max(matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j],matrix[2*n-1-i][2*n-1-j])
        return sum
matrix=[[112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]]
print(Solution().max_sum(matrix))
