'''
Given a grid[][] of size m * n, let us assume we are starting at (1, 1) and our goal is to reach (m, n). At any
instance, if we are on (x, y), we can either go to (x, y + 1) or (x + 1, y). The task is to find the number of
unique paths if some obstacles are added to the grid.
Note: An obstacle and space are marked as 1 and 0 respectively in the grid.
'''


def UniquePathHelper(i, j, r, c, grid, memo):
    # If out of bounds, return 0
    if i == r or j == c:
        return 0

    # If cell is an obstacle, return 0
    if grid[i][j] == 1:
        return 0

    # If reached the bottom-right cell, return 1
    if i == r - 1 and j == c - 1:
        return 1

    # If value is already computed, return it
    if (i, j) in memo:
        return memo[(i, j)]

    # Memoize the result of recursive calls
    memo[(i, j)] = UniquePathHelper(i + 1, j, r, c, grid, memo) + \
                   UniquePathHelper(i, j + 1, r, c, grid, memo)

    return memo[(i, j)]

def uniquePathsWithObstacles(grid):
    r, c = len(grid), len(grid[0])
    memo = {}
    return UniquePathHelper(0, 0, r, c, grid, memo)


grid = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]

print(uniquePathsWithObstacles(grid))