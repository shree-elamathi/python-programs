'''You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a
subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without
changing the order of the remaining characters.'''
class Solution:
    def append_char(self,s,t):
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        count=0
        if j<len(t):
            for k in range(j,len(t)):
                s+=t[k]
                count+=1
            return count
        else:
            return count
t="abcde"
s="z"
print(Solution().append_char(s,t))