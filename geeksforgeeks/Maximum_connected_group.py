'''
You are given a square binary grid. A grid is considered binary if every value in the grid is either 1 or 0. You
can change at most one cell in the grid from 0 to 1. You need to find the largest group of connected  1's. Two
cells are said to be connected if both are adjacent(top, bottom, left, right) to each other and both have the same
value.
'''
class Solution:
    def MaxConnection(self,grid):
        def dfs(grid,i,j,island_no):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = island_no
            size = 1
            size += dfs(grid, i - 1, j, island_no)
            size += dfs(grid, i + 1, j, island_no)
            size += dfs(grid, i, j - 1, island_no)
            size += dfs(grid, i, j + 1, island_no)
            return size
        island_no=2 #since 0 and 1 are already present in the matrix
        island_sizes={}
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = dfs(grid, i, j, island_no)
                    island_sizes[island_no] = size
                    ans = max(ans, size)
                    island_no += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    seen_islands = set()
                    maxSize = 1  # the size of the island if we convert this 0 to 1
                    if i > 0:
                        seen_islands.add(grid[i - 1][j])
                    if i < len(grid) - 1:
                        seen_islands.add(grid[i + 1][j])
                    if j > 0:
                        seen_islands.add(grid[i][j - 1])
                    if j < len(grid[0]) - 1:
                        seen_islands.add(grid[i][j + 1])
                    for island in seen_islands:
                        if island > 1:  # only consider valid islands
                            maxSize += island_sizes[island]
                    ans = max(ans, maxSize)
        return ans

grid=[ [1, 1],  [0, 1]]
print(Solution().MaxConnection(grid))