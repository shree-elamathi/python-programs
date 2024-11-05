'''
Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.
'''


def rotate(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i].reverse()

    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(mat))
