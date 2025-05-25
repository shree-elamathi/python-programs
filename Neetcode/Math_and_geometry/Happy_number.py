'''
A non-cyclical number is an integer defined by the following algorithm:

Given a positive integer, replace it with the sum of the squares of its digits.
Repeat the above step until the number equals 1, or it loops infinitely in a cycle which does not include 1.
If it stops at 1, then the number is a non-cyclical number.
Given a positive integer n, return true if it is a non-cyclical number, otherwise return false.
'''

class Solution:
    def isHappy(self, n):
        lst = []
        while n != 1:
            if n in lst:
                return False
            lst.append(n)
            summ = 0
            while n > 0:
                temp = n % 10
                summ += (temp*temp)
                n = int(n/10)
            n = summ
        return True


n = 145
print(Solution().isHappy(n))