'''
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with
creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
'''
class Solution:
    def construct2DArray(self,original,m,n):
        new_arr=[([0]*n) for _ in range(m)]
        if len(original)>m*n or len(original)<m*n:
            return []
        k=0
        for i in range(len(new_arr)):
            for j in range(len(new_arr[0])):
                new_arr[i][j]=original[k]
                k+=1
        return new_arr
original=[3]
m=1
n=2
print(Solution().construct2DArray(original,m,n))