'''
Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through
that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is
minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).
'''
import heapq
class Solution:
    def minimumCostPath(self, grid):
        # Dimensions of the grid
        n = len(grid)

        # Directions for moving left, right, up, down
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Priority queue to store (cost, x, y)
        pq = [(grid[0][0], 0, 0)]

        # Cost matrix to track the minimum cost to reach each cell
        cost = [[float('inf')] * n for _ in range(n)]
        cost[0][0] = grid[0][0]

        while pq:
            curr_cost, x, y = heapq.heappop(pq)

            # If we have reached the bottom-right corner, return the cost
            if x == n - 1 and y == n - 1:
                return curr_cost

            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = curr_cost + grid[nx][ny]
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))


grid = [[9,4,9,9],[6,7,6,4],[8,3,3,7],[7,4,9,10]]
print(Solution().minimumCostPath(grid))