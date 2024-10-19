'''
A string str is given to represent a positive number. The task is to round str to the nearest multiple of 10.
If you have two multiples equally apart from str, choose the smallest element among them.
'''

import sys
class Solution:
    def roundToNearest(self, s):
        sys.set_int_max_str_digits(70000)
        x = int(s)
        temp = x // 10
        rem = x % 10
        lead_zero = len(s) - len(str(x))

        if rem > 5:
            result = (temp * 10) + 10
        else:
            result = temp * 10

        ans = '0' * lead_zero + str(result)
        return ans


num="22"
print(Solution().roundToNearest(num))