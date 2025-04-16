'''
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.
'''


class Solution:
    def NnumbersSum(self, N):
        def sum1 (i,N):
            if (i==N):
                return i
            return i + sum1(i+1, N)

        return sum1(1,N)





N = 4
print(Solution().NnumbersSum(N))