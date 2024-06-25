'''
You are given an integer k and matrix mat. Return a matrix where it is rotated Left k times.
'''
class Solution:
    def rotatematrix(self, k, mat):
        for each in mat:
            for i in range((k%len(mat[0]))):
                each.append(each[0])
                each.pop(0)
        return mat

mat=[[1,2,3],[4,5,6],[7,8,9]]
k=1
print(Solution().rotatematrix(k,mat))