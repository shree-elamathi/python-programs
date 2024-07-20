'''
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in
the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not
know the elements of the matrix, but you do know the sums of each row and column.
Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum
requirements.
Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix
that fulfills the requirements exists.
'''
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                min_value = min(rowSum[i], colSum[j])
                matrix[i][j] = min_value
                rowSum[i] -= min_value
                colSum[j] -= min_value
        return matrix

rowSum = [3,8]
colSum = [4,7]
print(Solution().restoreMatrix(rowSum,colSum))