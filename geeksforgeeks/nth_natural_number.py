'''
Given a positive integer n. You have to find nth natural number after removing all the numbers containing the digit 9.
'''
class Solution:
    def findNth(self,n):
        result = 0
        power = 1

        while n > 0:
            result += (n % 9) * power
            n //= 9
            power *= 10

        return result
n=20
print(Solution().findNth(n))