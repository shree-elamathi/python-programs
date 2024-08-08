'''
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first
row and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's
boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach
all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.
'''
class Solution:
    def spiralOrder(self,rows, cols, rStart, cStart):
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        result = []
        visited = set()

        r, c = rStart, cStart
        dir_idx = 0
        step_limit = 1

        # We need to visit all cells, so we'll loop until we have them all.
        while len(result) < rows * cols:
            for _ in range(2):  # We need to increase the step limit every two direction changes.
                for _ in range(step_limit):
                    # If we're within the bounds, add the position to the result.
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append((r, c))

                    # Move to the next cell in the current direction.
                    r += directions[dir_idx][0]
                    c += directions[dir_idx][1]

                # Change direction clockwise.
                dir_idx = (dir_idx + 1) % 4

            # Increase the step limit every two directions (right & down, then left & up).
            step_limit += 1

        return result
rows = 1
cols = 4
rStart = 0
cStart = 0
print(Solution().spiralOrder(rows, cols, rStart, cStart))