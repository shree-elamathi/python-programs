'''
A matrix is constructed of size n*n and given an integer ‘q’. The value at every cell of the matrix is given
as, M(i,j) = i+j, where ‘M(i,j)' is the value of a cell, ‘i’ is the row number, and ‘j’ is the column number.
Return the number of cells having value ‘q’.
Note: Assume, the array is in 1-based indexing.
'''
class Solution:
    def sumMatrix(self, n, q):
        count=0
        x=q-n
        if x>0:
            for i in range(x,n+1):
                count+=1
            return count
        else:
            n-=1
            while n>0:
                if n!=q:
                    count+=1
                n-=1
        return count
n=6
q=9
print(Solution().sumMatrix(n,q))