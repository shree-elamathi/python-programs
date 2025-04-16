'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all
non-alphanumeric characters.
'''


class Solution:
    def isPalindrome(self, s):
        new_s = ""
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
        return new_s[::-1] == new_s



s = "0P"
print(Solution().isPalindrome(s))