'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
'''
class Solution:
    def countConsistentStrings(self, allowed, words):
        c=0
        for word in words:
            if self.check_word(allowed,word):
                c+=1
        return c
    def check_word(self,allowed,word):
        for i in word:
            if i not in allowed:
                return False
        return True


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(Solution().countConsistentStrings(allowed,words))