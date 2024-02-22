n=int(input("Enter the limit: "))
for i in range(0,n+1):
    for k in range(i+1,0,-1):
        print("",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
