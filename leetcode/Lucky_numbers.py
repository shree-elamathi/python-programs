'''
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
'''
import numpy as np
class Solution:
    def luckyNumbers(self,mat):
        mat1=np.array(mat)
        ans=[]
        for i in mat:
            x=i.index(min(i))
            y=max(mat1[:,x])
            if i[x]==y:
                ans.append(y)
        return ans

mat=[[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(Solution().luckyNumbers(mat))
