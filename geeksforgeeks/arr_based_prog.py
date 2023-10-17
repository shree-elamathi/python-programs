##Array and list based programs
##Shortest in list
a= [20, 10, 20, 4, 100]
a.sort()
print("The smallest element is",a[0])


##Largest in list
arr=[20, 10, 20, 4, 100]
i=len(arr)-1
arr.sort()
##print(arr)
##print(i)
print("The largest element is",arr[i])


##second largest in a list
arr=[20, 10, 20, 4, 100]
i=len(arr)-2
arr.sort()
print("The second largest element is",arr[i])

##split and add arr
a=[12, 10, 5, 6, 52, 36]
b=[]
k=2
while (len(b)<=k-1):
        for i in a:
            b.append(i)
            print(i)
            a.remove(i)
            break
print(a)
print(b)
print(a+b)


##to swap first and last element
a=[12, 35, 9, 56, 24]
print(a)
a[0],a[-1]=a[-1],a[0]
print(a)

##To swap required positions
a = [23, 65, 19, 90]
##pos1=int(input("Enter the first position: "))
##pos2=int(input("Enter the second position: "))
pos1 = 1
pos2 = 3

a[pos1-1],a[pos2-1]=a[pos2-1],a[pos1-1]
print(a)


##Arr addition
arr= {15, 12, 13, 10}
sum=0
for i in arr:
    sum=sum+i
print("The sum is:",sum)

##arr multiplication and divide by n
a= [100, 10, 5, 25, 35, 14]
n = 11
mult=1
for i in a:
    mult=mult*i
print(mult)
print(mult%n)

##Arr multiplication
a=[3, 2, 4] 
mul=1
for i in a:
    mul=mul*i

print("The multiplication is",mul)

##Arr is monotonic
a=[5,15,20,10]
b=len(a)
x,y=[],[]
x.extend(a)
y.extend(a)
x.sort()
y.sort(reverse=True)
if(x==a or y==a):
    print("True")
else:
    print("False")


##To find N largest elements
a=[4, 5, 1, 2, 9]
N=2
a.sort(reverse=True)
for i in range(0,N):
    print(a[i])
##print(a)

##To print even number in the list
a=[2, 7, 5, 64, 14]
b=[]
for i in a:
    if i%2==0:
        b.append(i)

print(b)

##To print odd num in array
a=[2, 7, 5, 64, 14]
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
print(b)

##To print all even&odd num in range
a=2
b=22
c=[]
d=[]
for i in range(a,b+1):
    if i%2==0:
        c.append(i)
    else:
        d.append(i)

print("The even numbers are",c)
print("The odd numbers are",d)

##To print pos&neg num in list
a=[12, -7, 5, 64, -14]
b=[]
c=[]
for i in a:
    if i>=0:
        b.append(i)
    else:
        c.append(i)

print("The pos num are",b)
print("The neg num are",c)

##To print pos&neg num in range
a=-4
b=5
c=[]
d=[]
for i in range(a,b+1):
    if i>=0:
        c.append(i)
    else:
        d.append(i)

print("The positive numbers are",c)
print("The negative numbers are",d)

##To delete multiple elements in a list
a=[12, 15, 3, 10]
n=int(input("Enter the number of elements to be removed: "))
for i in range(0,n):
    i=int(input("Enter the elements: "))
    if i in a:
        a.remove(i)

print(a)

##cumulative sum of list
a=[10, 20, 30, 40, 50]
b=[]
sum=0
for i in a :
    sum=sum+i
    b.append(sum)
print(b)


