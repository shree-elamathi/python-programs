'''
Given a string, find the minimum number of characters to be inserted to convert it to a palindrome.
'''
class Solution:
    def countMin(self, str):
        def LCM(self, S1, S2, n):
            # Initialize a 2D dp array with zeros
            dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

            # Fill the dp array based on LCS logic
            for i in range(n + 1):
                for j in range(n + 1):
                    # Base case: If either string is empty, LCS length is 0
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    # If characters match, take diagonal value and add 1
                    elif S1[i - 1] == S2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    # If characters don't match, take the maximum of left and top values
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

            # Return the length of LCS for S1 and S2
            return dp[n][n]

        def countMin(self, s):
            # Get the length of the input string
            n = len(s)
            # Get the reverse of the input string
            R_str = s[::-1]

            # Get the length of the Longest Common Subsequence between the string and its reverse
            lcm = self.LCM(s, R_str, n)

            # The minimum number of insertions to make the string a palindrome
            # is the length of the string minus the length of the LCS
            return n - lcm

str="dmtjtvqyiedezraoqkfu"
print(Solution().countMin(str))