'''
Given a binary representation in the form of a string(s) of a number n, the task is to find a binary
representation of n+1.
'''
class Solution:
    def bin_rep(self,s):
        t="1"
        res=bin(int(s,2) + int(t,2))
        return res[2:]
s="01"
print(Solution().bin_rep(s))