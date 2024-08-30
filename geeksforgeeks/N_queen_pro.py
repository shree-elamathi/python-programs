'''
The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each
other. Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board
configurations of the n-queens placement, where the solutions are a permutation of [1,2,3..n] in increasing order,
here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg
below figure represents a chessboard [3 1 4 2].
'''


class Solution:
    def nQueen(self, n):
        def solveNQueens(row, columns, diagonals1, diagonals2, board, solutions):
            if row == n:
                solutions.append(board[:])
                return
            for col in range(n):
                if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                board.append(col + 1)

                solveNQueens(row + 1, columns, diagonals1, diagonals2, board, solutions)

                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
                board.pop()

        solutions = []
        solveNQueens(0, set(), set(), set(), [], solutions)
        return solutions

n=4
print(Solution().nQueen(n))
