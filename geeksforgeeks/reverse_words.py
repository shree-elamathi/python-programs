'''
Given a String str, reverse the string without reversing its individual words. Words are separated by dots.
Note: The last character has not been '.'.
'''


class Solution:
    def reverseWords(self, str):
        res = str.split(".")
        res = res[::-1]
        ans = ".".join(res)
        return ans


str = "i.like.this.program.very.much"
print(Solution().reverseWords(str))