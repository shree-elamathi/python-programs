'''
Given an unsorted array arr[] of size n. Rotate the array to the left (counter-clockwise direction) by d steps,
where d is a positive integer.
'''
class Solution:
    def rotateArr(self,A,D,N):
        for i in range(D):
            A.append(A[0])
            A.pop(0)
        return A
A=[1,2,3,4,5]
N=5
D=2
print(Solution().rotateArr(A,D,N))
