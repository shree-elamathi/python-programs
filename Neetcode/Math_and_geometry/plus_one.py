'''
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from
most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.
'''


class Solution:
    def plusOne(self, digits):
        val = 0
        ans = []

        #remove the digits and make the sum of valid type
        for i in digits:
            val = val * 10
            val += i


        #Now add 1 to it
        val += 1

        #Now insert the values into the answer list
        while val > 0:
            temp = val % 10
            ans.insert(0, temp)
            val = int(val / 10)

        return ans


digits = [1,2,3,4]
print(Solution().plusOne(digits))