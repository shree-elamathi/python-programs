arr1=[1,3,2]
arr2=[3,4,2,1]
x=4
pairs=[]
for i in arr1:
    for j in arr2:
        if i+j==x:
            pairs.append(i)
            pairs.append(j)
print (int(len(pairs)/2))
