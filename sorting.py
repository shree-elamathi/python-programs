n=eval(input("How many names?" ))
a=[]
print("enter",n,"names one by one")
for i in range(n):
    a.append(input())
print('before sort, the names are')
print(a)
a.sort()
print('after sort, the names are')
print(a)
