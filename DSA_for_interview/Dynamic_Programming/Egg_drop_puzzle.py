'''
You are given n identical eggs and you have access to a k-floored building from 1 to k.

There exists a floor f where 0 <= f <= k such that any egg dropped from a floor higher than f will break, and any
egg dropped from or below floor f will not break.
There are few rules given below.

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the egg breaks on a certain floor, it will break on any floor above.
Return the minimum number of moves you need to determine the value of f with certainty.
'''


class Solution:
    def eggDrop(self, n, k):
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        moves = 0
        while dp[n][moves] < k:
            moves += 1
            for eggs in range(1, n + 1):
                dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1

        return moves