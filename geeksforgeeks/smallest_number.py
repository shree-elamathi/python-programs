'''
Given two integers s and d. The task is to find the smallest number such that the sum of its digits is s and the
number of digits in the number are d. Return a string that is the smallest possible number. If it is not possible
then return -1.
'''
class Solution:
    def smallestNumber(self, s, d):
        if s == 0:
            if d == 1:
                return "0"
            else:
                return "-1"
        if s > 9 * d:
            return "-1"
        digits = [0] * d
        for i in range(d - 1, -1, -1):
            if s > 9:
                digits[i] = 9
                s -= 9
            else:
                digits[i] = s
                s = 0
        if digits[0] == 0:
            digits[0] = 1
            for i in range(1, d):
                if digits[i] > 0:
                    digits[i] -= 1
                    break
        return ''.join(map(str, digits))

s=9
d=2
print(Solution().smallestNumber(s,d))