'''
Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to reach the destination at
(n - 1, n - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in
which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents
that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel
through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other
cell. In case of no path, return an empty list. The driver will output "-1" automatically.
'''
class Solution:
    def findPaths(self,matrix):
        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and matrix[x][y] == 1
        def solve(x, y, path):
            # If destination is reached, add the path to the result
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return

            # Mark the current cell as visited
            visited[x][y] = True

            # Move Down
            if isSafe(x + 1, y) and not visited[x + 1][y]:
                solve(x + 1, y, path + 'D')

            # Move Left
            if isSafe(x, y - 1) and not visited[x][y - 1]:
                solve(x, y - 1, path + 'L')

            # Move Right
            if isSafe(x, y + 1) and not visited[x][y + 1]:
                solve(x, y + 1, path + 'R')

            # Move Up
            if isSafe(x - 1, y) and not visited[x - 1][y]:
                solve(x - 1, y, path + 'U')

            # Unmark the current cell (backtrack)
            visited[x][y] = False

        n = len(matrix)
        paths = []

        if matrix[0][0] == 0 or matrix[n - 1][n - 1] == 0:
            return paths

        visited = [[False for _ in range(n)] for _ in range(n)]
        solve(0, 0, "")
        return paths
mat= [[1, 0, 0, 0],[1, 1, 0, 1], [1, 1, 0, 0],[0, 1, 1, 1]]
print(Solution().findPaths(mat))