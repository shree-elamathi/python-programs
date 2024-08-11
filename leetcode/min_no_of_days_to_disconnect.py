'''
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal
4-directionally (horizontal or vertical) connected group of 1's.
The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
In one day, we are allowed to change any single land cell (1) into a water cell (0).
Return the minimum number of days to disconnect the grid.
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            grid[i][j] = 0  # Mark this cell as visited (convert to water)
            dfs(i + 1, j)  # Explore down
            dfs(i - 1, j)  # Explore up
            dfs(i, j + 1)  # Explore right
            dfs(i, j - 1)  # Explore left

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count

    def minDays(self, grid: List[List[int]]) -> int:
        # Check if the grid is already disconnected
        if self.numIslands([row[:] for row in grid]) != 1:
            return 0

        # Try disconnecting by removing each land cell one by one
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0  # Temporarily make this cell water
                    if self.numIslands([row[:] for row in grid]) != 1:
                        return 1
                    grid[i][j] = 1  # Revert the change

        # If no single removal leads to disconnection, return 2
        return 2
grid=[[0,1,1,0],[0,1,1,0],[0,0,0,0]]
print(Solution().minDays(grid))