#Given an integer s represented as a string, the task is to get the sum of all possible sub-strings of this string.
# As the answer will be large, return answer modulo 109+7.
# Note: The number may have leading zeros.
class Solution:
    def sumSubstrings(self,s):
        last=0
        n=len(s)
        mod=10**9+7
        ab=0
        for i in range(n):
            val=int(s[i])
            ab=((ab*10)+val*(i+1))%mod
            last=(last+ab)%mod
        return last
s="1234"
print(Solution().sumSubstrings(s))