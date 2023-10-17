##n=eval(input("Enter the value of N?"))
##n1=-1
##n2=1
##print("The first",n,"fibonacci series are:")
##for i in range (n):
##    n3=n1+n2
##    print(n3,end="\t")
##    n1=n2
##    n2=n3
n=17
n1=-1
n2=1
for i in range(n+1):
    n3=n1+n2
    n1=n2
    n2=n3
print(n3)
