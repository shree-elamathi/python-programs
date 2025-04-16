'''
Given N, return the factorial of first N numbers
'''


class Solution:
    def NnumbersSum(self, N):
        def fact (i,N):
            if (i==N):
                return i
            return i * fact(i+1, N)
        if N == 0:
            return 1
        return fact(1,N)


N = 0
print(Solution().NnumbersSum(N))