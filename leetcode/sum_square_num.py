'''
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
'''
class Solution:
    def judgeSquareSum(self,c):
        for i in range(c+1):
            for j in range(i,c+1):
                a=i*i
                b=j*j
                if a+b==c:
                    return True
        return False
c=3
print(Solution().judgeSquareSum(c))