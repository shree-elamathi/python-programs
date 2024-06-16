v1=[]
v2=[]
v3=[]
n=int(input("Enter the number of elements in V1: "))
for i in range(0,n):
    ele=int(input("Enter the elements of V1: "))
    v1.append(ele)
m=int(input("\nEnter the number of elements in V2: "))
for i in range(0,m):
    elem=int(input("Enter the elements of V2: "))
    v2.append(elem)
for i in v1:
    if i in v2:
        v3.append(i)

v3.sort()
print(v3)
    

    



