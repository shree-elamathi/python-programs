'''
The task is to replace the existing color of the given pixel and all the adjacent same-colored pixels with the
given newColor.
'''


def dfs(image, x, y, oldColor, newColor):
    # Check boundary conditions and color match
    if (x < 0 or x >= len(image) or y < 0 or
            y >= len(image[0]) or image[x][y] != oldColor):
        return

    # Change the color
    image[x][y] = newColor

    # Visit all adjacent pixels
    dfs(image, x + 1, y, oldColor, newColor)
    dfs(image, x - 1, y, oldColor, newColor)
    dfs(image, x, y + 1, oldColor, newColor)
    dfs(image, x, y - 1, oldColor, newColor)


def floodFill(image, sr, sc, newColor):
    # If the starting pixel already has the new color
    if image[sr][sc] == newColor:
        return image

    # Call DFS with the starting pixel's original color
    dfs(image, sr, sc, image[sr][sc], newColor)

    return image