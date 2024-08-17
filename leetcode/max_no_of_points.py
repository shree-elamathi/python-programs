'''
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of
points you can get from the matrix.To gain points, you must pick one cell in each row. Picking the cell at coordinates
(r, c) will add points[r][c] to your score. However, you will lose points if you pick a cell too far from the cell
that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at
coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.
abs(x) is defined as:
x for x >= 0.
-x for x < 0.
'''
import numpy as np
class Solution:
    def maxPoints(self,points):
        m, n = len(points), len(points[0])

        dp = points[0]

        for r in range(1, m):
            left_to_right = [0] * n
            right_to_left = [0] * n

            # Left-to-right pass
            left_to_right[0] = dp[0]
            for c in range(1, n):
                left_to_right[c] = max(left_to_right[c - 1] - 1, dp[c])

            # Right-to-left pass
            right_to_left[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right_to_left[c] = max(right_to_left[c + 1] - 1, dp[c])

            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left_to_right[c], right_to_left[c])

        return max(dp)
points =[[1],[2],[3]]
print(Solution().maxPoints(points))