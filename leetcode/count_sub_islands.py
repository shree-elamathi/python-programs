'''
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing
land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid
are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up
this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
'''


class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            is_sub_island = grid1[i][j] == 1
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i, j + 1)
            is_sub_island &= dfs(i, j - 1)
            return is_sub_island

        m, n = len(grid2), len(grid2[0])
        sub_islands_count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands_count += 1

        return sub_islands_count

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(Solution().countSubIslands(grid1,grid2))