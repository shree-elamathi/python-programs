X= [[1,2],[3,4],[5,6]]
Y=[[0,0],[0,0],[0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        X[i][j]=Y[i][j]

print(Y)
