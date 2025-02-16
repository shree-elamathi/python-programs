'''
Given a string s and a dictionary of n words dictionary, find out if "s" can be segmented into a space-separated
sequence of dictionary words.
Return 1 if it is possible to break the s into a sequence of dictionary words, else return 0.

Note: From the dictionary dictionary each word can be taken any number of times and in any order.
'''


class Solution:
    def wordBreak(self, n, s, dictionary):
        word_set= set(dictionary)
        x = len(s)
        dp = [0] * (x+1)
        dp[0] = 1
        for i in range(1, x+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in word_set:
                    dp[i] = 1
                    break
        return dp[x]
#optimized version
'''
class Solution:
    def wordBreak(self, s, dictionary):
        word_set = set(dictionary)  # Convert dictionary to a set for fast lookup
        n = len(s)
        max_word_length = max(map(len, dictionary)) if dictionary else 0  # Max word length
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string is always breakable
        
        for i in range(1, n + 1):  
            for j in range(max(0, i - max_word_length), i):  # Only check recent max word length
                if dp[j] == 1 and s[j:i] in word_set:
                    dp[i] = 1
                    break  # Early termination when a valid split is found
        
        return dp[n]
'''

s="ilikesamsung"
n=6
dictionary={ "i", "like", "sam", "sung", "samsung", "mobile"}
print(Solution().wordBreak(n,s,dictionary))
