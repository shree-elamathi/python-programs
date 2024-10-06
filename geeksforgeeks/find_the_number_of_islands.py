'''
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's
(Water) and '1's(Land). Find the number of islands.
Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands
horizontally or vertically or diagonally i.e., in all 8 directions.
'''
from collections import deque
class Solution:
    def numIslands(self, grid):
        def main(r,c,grid,visited):
            q=deque([(r,c)])
            visited[r][c]=1
            m=len(grid)
            n=len(grid[0])
            while q:
                r,c=q.popleft()
                if r>0 and visited[r-1][c]==0 and grid[r-1][c]==1:
                    q.append((r-1,c))
                    visited[r-1][c]=1
                if r+1<m and visited[r+1][c]==0 and grid[r+1][c]==1:
                    q.append((r+1,c))
                    visited[r+1][c]=1
                if c>0 and visited[r][c-1]==0 and grid[r][c-1]==1:
                    q.append((r,c-1))
                    visited[r][c-1]=1
                if c+1<n and visited[r][c+1]==0 and grid[r][c+1]==1:
                    q.append((r,c+1))
                    visited[r][c+1]=1
                if r>0 and c>0 and visited[r-1][c-1]==0 and grid[r-1][c-1]==1:
                    q.append((r-1,c-1))
                    visited[r-1][c-1]=1
                if r>0 and c+1<n and visited[r-1][c+1]==0 and grid[r-1][c+1]==1:
                    q.append((r-1,c+1))
                    visited[r-1][c+1]=1
                if r+1<m and c>0 and visited[r+1][c-1]==0 and grid[r+1][c-1]==1:
                    q.append((r+1,c-1))
                    visited[r+1][c-1]=1
                if r+1<m and c+1<n and visited[r+1][c+1]==0 and grid[r+1][c+1]==1:
                    q.append((r+1,c+1))
                    visited[r+1][c+1]=1
        m=len(grid)
        n=len(grid[0])
        visited=[[0 for j in range(n)] for i in range(m)]
        num=0
        for r in range(m):
            for c in range(n):
                if visited[r][c]==0 and grid[r][c]==1:
                    main(r,c,grid,visited)
                    num+=1
        return num


grid = [[0,1],[1,0],[1,1],[1,0]]
print(Solution().numIslands(grid))