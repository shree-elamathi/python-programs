'''
A matrix is constructed of size n*n and given an integer ‘q’. The value at every cell of the matrix is given
as, M(i,j) = i+j, where ‘M(i,j)' is the value of a cell, ‘i’ is the row number, and ‘j’ is the column number.
Return the number of cells having value ‘q’.
Note: Assume, the array is in 1-based indexing.
'''
class Solution:
    def sumMatrix(self, n, q):
        x=n-q
        if x>=0:

        return x
n=5
q=4
print(Solution().sumMatrix(n,q))