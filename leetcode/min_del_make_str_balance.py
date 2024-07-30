'''
You are given a string s consisting only of characters 'a' and 'b'.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j)
such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.
'''
class Solution:
    def minDeletionsToBalance(self,str) :
        n = len(s)
        countB = [0] * (n + 1)
        countA = [0] * (n + 1)
        for i in range(1, n + 1):
            countB[i] = countB[i - 1] + (1 if s[i - 1] == 'b' else 0)
        for i in range(n - 1, -1, -1):
            countA[i] = countA[i + 1] + (1 if s[i] == 'a' else 0)
        min_deletions = float('inf')
        for i in range(n + 1):
            min_deletions = min(min_deletions, countB[i] + countA[i])

        return min_deletions
s="bbaaaabb"
print(Solution().minDeletionsToBalance(s))