'''
Given a string, remove the vowels from the string.
'''
class Solution:
    def removeVowels(self,S):
        vow=["a","e","i","o","u"]
        new_s=""
        for i in S:
            if i not in vow:
                new_s+=i
        return new_s
S="what is your name ?"
print(Solution().removeVowels(S))