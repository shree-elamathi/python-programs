'''
Given a grid of dimension nxm containing 0s and 1s. Find the unit area of the largest region of 1s.
Region of 1's is a group of 1's connected 8-directionally (horizontally, vertically, diagonally).
'''


class Solution:
    def findMaxArea(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_region = 0

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if visited[r][c] or grid[r][c] == 0:
                return 0

            visited[r][c] = True
            size = 1

            for dr,dc in directions:
                size += dfs(r + dr , c+dc)

            return size

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_region = max(max_region, dfs(i, j))

        return max_region


grid = [[1,1,1,0],[0,0,1,0],[0,0,0,1]]
print(Solution().findMaxArea(grid))
