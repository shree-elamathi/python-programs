'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '.
These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.
'''
class Solution:
    def regionsBySlashes(self,grid):
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                char = grid[i][j]

                if char in ['/', ' ']:
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)

                if char in ['\\', ' ']:
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)

                if i + 1 < n:
                    union(root + 2, root + 4 * n + 0)

                if j + 1 < n:
                    union(root + 1, root + 4 + 3)

        return sum(find(x) == x for x in range(4 * n * n))
grid= [" /","/ "]
print(Solution().regionsBySlashes(grid))