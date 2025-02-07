'''
Given a sentence s, the task is to check if it is a palindrome sentence or not. A palindrome sentence is a sequence
of characters, such as a word, phrase, or series of symbols, that reads the same backward as forward after converting
all uppercase letters to lowercase and removing all non-alphanumeric characters.
'''

class Solution:
    def sentencePalindrome(self, s):
        new_str = ""
        for letter in s:
            if letter.isalnum():
                new_str += letter
        new_str = new_str.lower()
        left, right = 0, len(new_str) - 1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True


s = "Too hot to hoot"
print(Solution().sentencePalindrome(s))