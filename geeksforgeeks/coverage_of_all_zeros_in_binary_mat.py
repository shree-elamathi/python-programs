'''
Given a binary matrix contains 0s and 1s only, we need to find the sum of coverage of all zeros of the
matrix where coverage for a particular 0 is defined as a total number of ones around a zero in left, right,
up and bottom directions.
'''
class Solution:
    def findCoverage(self, matrix):
        count=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    count+=checksurround(matrix,i,j)
        return count
def checksurround(matrix,i,j):
    c_sum=0
    if i-1>=0:
        if matrix[i-1][j]==1:
            c_sum+=1
    if i+1<len(matrix):
        if matrix[i+1][j]==1:
            c_sum+=1
    if j-1>=0:
        if matrix[i][j-1]==1:
            c_sum+=1
    if j+1<len(matrix[0]):
        if matrix[i][j+1]==1:
            c_sum+=1
    return c_sum
matrix=[[0, 1]]
print(Solution().findCoverage(matrix))