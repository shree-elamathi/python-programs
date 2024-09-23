'''
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more
non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in
s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.
'''
class Solution:
    def minExtraChar(self, s: str, dictionary: list) -> int:
        n = len(s)
        word_set = set(dictionary)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]


solution = Solution()
s = "leetcodelovesleetcode"
dictionary = ["leet", "code", "loves"]
print(solution.minExtraChar(s, dictionary))
