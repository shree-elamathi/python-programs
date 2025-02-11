'''
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by
some people.  A square matrix mat is used to represent people at the party such that if an element of row i and
column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the
party, if the celebrity does not exist, return -1.
'''
class Solution:
    def celebrity(self, mat):
        if len(mat)==1:
            return 0
        rough=[]
        for person in mat:
            for ind in range(len(person)):
                if person[ind]==1:
                    rough.append(ind)
        for i in rough:
            if rough.count(i)==len(mat)-1:
                # to check if there is no one in that row
                if 1 not in mat[i]:
                    return i
        return "-1"
mat=   [[0, 0, 0, 1, 0],[1, 0, 0, 0, 0],[1, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0]]
print(Solution().celebrity(mat))
