'''
Given a 2D grid of n*m of characters and a word, find all occurrences of given word in grid. A word can be matched
in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction
(not in zig-zag form). The 8 directions are, horizontally left, horizontally right, vertically up, vertically down,
and 4 diagonal directions.

Note: The returning list should be lexicographically smallest. If the word can be found in multiple directions
starting from the same coordinates, the list should contain the coordinates only once.
'''


class Solution:
    def searchWord(self, grid, word):
        def checkLeft(grid, i, j, word):
            k = 0
            while j >= 0 and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                j -= 1
                k += 1
            if k == len(word) :
                return True
            return False

        def checkRight(grid, i, j, word):
            k = 0
            while (j < len(grid[i])) and (k < len(word)):
                if grid[i][j] != word[k]:
                    return False
                j += 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkUp(grid, i, j, word):
            k = 0
            while i >= 0  and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                i -= 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkDown(grid, i, j, word):
            k = 0
            while i < len(grid)  and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                i += 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkUpLeft(grid, i, j, word):
            k = 0
            while (i>=0 and j>=0) and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                j -= 1
                i -= 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkUpRight(grid, i, j, word):
            k = 0
            while (i >=0 and j < len(grid[0])) and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                j += 1
                i -= 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkDownLeft(grid, i, j, word):
            k = 0
            while (i < len(grid) and j >= 0) and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                j -= 1
                i += 1
                k += 1
            if k == len(word):
                return True
            return False

        def checkDownRight(grid, i, j, word):
            k = 0
            while (i <len(grid) and j < len(grid[0])) and k < len(word):
                if grid[i][j] != word[k]:
                    return False
                j += 1
                i += 1
                k += 1
            if k == len(word):
                return True
            return False

        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == word[0]:
                    if checkLeft(grid, i, j, word):
                        res.append([i, j])
                    elif checkRight(grid, i, j, word):
                        res.append([i, j])
                    elif checkUp(grid, i, j, word):
                        res.append([i, j])
                    elif checkDown(grid, i, j, word):
                        res.append([i, j])
                    elif checkUpLeft(grid, i, j, word):
                        res.append([i, j])
                    elif checkUpRight(grid, i, j, word):
                        res.append([i, j])
                    elif checkDownLeft(grid, i, j, word):
                        res.append([i, j])
                    elif checkDownRight(grid, i, j, word):
                        res.append([i, j])
        return res


grid = [['a','b','a','b'],['a','b','e','b'],['e','b','e','b']]
word = "abe"
print(Solution().searchWord(grid,word))

