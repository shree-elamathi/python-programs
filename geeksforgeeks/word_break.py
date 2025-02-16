#Given a string s and a dictionary of n words dictionary, find out if a s can be segmented into
# a space-separated sequence of dictionary words. Return 1 if it is possible to break the s into a
# sequence of dictionary words, else return 0.
# Note: From the dictionary dictionary each word can be taken any number of times and in any order.
class solution:
    def wordbreak(self,s,n,dictionary):
        word_set = set(dictionary)
        x = len(s)
        dp = [0] * (x + 1)
        dp[0] = 1
        for i in range(1, x + 1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in word_set:
                    dp[i] = 1
                    break
        return dp[x]





s="ilikesamsung"
n=6
dictionary={ "i", "like", "sam", "sung", "samsung", "mobile"}

print(solution().wordbreak(s,n,dictionary))