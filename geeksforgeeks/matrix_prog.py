##matrix programs
##matrix addition
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j]=X[i][j]+Y[i][j]

print(result)

##matrix multiplication
X = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]
Y = [[1, 1, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
result=[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]

print(result)
    
