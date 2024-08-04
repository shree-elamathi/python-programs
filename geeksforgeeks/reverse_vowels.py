'''
Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the
resulting string.
'''
class Solution:
    def modify(self, s):
        vow=["a","e","i","o","u"]
        pre=[]
        for i in s:
            if i in vow:
                pre.append(i)
        pre.reverse()
        s1=""
        for i in s:
            if i in vow:
                s1+=pre.pop(0)
            else:
              s1+=i
        return s1
s="practice"
print(Solution().modify(s))
