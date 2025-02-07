'''
Given a string s, your task is to find the longest palindromic substring within s.
A substring is a contiguous sequence of characters within a string, defined as s[i...j] where 0 ≤ i ≤ j < len(s).
A palindrome is a string that reads the same forward and backward. More formally, s is a palindrome if
reverse(s) == s.
Note: If there are multiple palindromic substrings with the same length, return the first occurrence of the longest
palindromic substring from left to right.
'''

class Solution:
    def isPalaindrome(self, word):
        new_word = word[::-1]
        if new_word == word:
            return True
        return False
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        res = []
        ind = 0
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    word = s[i:j+1]
                    if self.isPalaindrome(word):
                        res.append(word)
                        if len(word) > max_len:
                            max_len = len(word)
                            ind = res.index(word)
        return res[ind]


s= "aaaabbaa"
print(Solution().longestPalindrome(s))
