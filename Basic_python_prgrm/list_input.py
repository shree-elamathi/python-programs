v1=[]
v2=[]
n=int(input("Enter the number of elements in V1: "))
for i in range(0,n):
    ele=int(input("Enter the elements of V1: "))
    v1.append(ele)
m=int(input("\nEnter the number of elements in V2: "))
for i in range(0,m):
    elem=int(input("Enter the elements of V2: "))
    v2.append(elem)
print(v1)
print(v2)
v3=[]
for i in range(0,n):
    for j in range(0,m):
        if v1[i]==v2[j]:
            temp=v1[i]
            v3.append(temp)
v3.sort()
print(v3)
    







