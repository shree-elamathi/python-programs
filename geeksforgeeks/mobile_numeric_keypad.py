'''
There is a standard numeric keypad on a mobile phone. You can only press the current button or buttons that
are directly up, left, right, or down from it (for ex if you press 5, then pressing 2, 4, 6 & 8 are allowed).
Diagonal movements and pressing the bottom row corner buttons (* and #) are prohibited.
Given a number n, find the number of possible unique sequences of length n that you can create by pressing
buttons. You can start from any digit.
'''
class Solution:
    def getcount(self,n):
        neighbors = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        dp = [[0] * 10 for _ in range(n + 1)]
        for j in range(10):
            dp[1][j] = 1
        for i in range(2, n + 1):
            for j in range(10):
                dp[i][j] = sum(dp[i - 1][neighbor] for neighbor in neighbors[j])
        return sum(dp[n][j] for j in range(10))
n=1
print(Solution().getcount(n))
