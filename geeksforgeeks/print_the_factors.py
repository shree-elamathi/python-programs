import math
class Solution:
    def countFactors (self, N):
        no_of_factors = 0
        i=1
        while i<=math.sqrt(N):
            if (N%i==0):
                if(N//i!=i):
                    no_of_factors += 2
                else:
                    no_of_factors += 1
            i+=1
        return no_of_factors
    def printFactors (self, N):
        no_of_factors = 0
        i=1
        while i<=math.sqrt(N):
            if (N%i==0):
                if(N//i!=i):
                    print(i , n//i , end = " ")
                else:
                    print(i, end = " ")
            i+=1

n = 36
print(Solution().countFactors(n))
Solution().printFactors(n)

# To print the factors

