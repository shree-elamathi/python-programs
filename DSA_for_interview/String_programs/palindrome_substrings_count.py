'''
Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string
must be greater than or equal to 2.
'''

class Solution:
    def isPalaindrome(self, word):
        new_word = word[::-1]
        if new_word == word:
            return True
        return False
    def CountPs(self, s):
        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    word = s[i:j + 1]
                    if self.isPalaindrome(word):
                        count += 1
        return count

s = "abaab"
print(Solution().CountPs(s))