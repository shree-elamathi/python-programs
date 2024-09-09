'''
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise),
starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.
'''
class Solution:
    def spiralMatrix(self,m,n,head):
        mat = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_ind = 0
        row, col = 0, 0
        current = head
        for _ in range(m * n):
            if current:
                mat[row][col] = current.val
                current = current.next
            next_row = row + directions[dir_ind][0]
            next_col = col + directions[dir_ind][1]
            if not (0 <= next_row < m and 0 <= next_col < n and mat[next_row][next_col] == -1):
                dir_ind = (dir_ind + 1) % 4
                next_row = row + directions[dir_ind][0]
                next_col = col + directions[dir_ind][1]
            row, col = next_row, next_col

        return mat

m = 3
n = 5
head = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]