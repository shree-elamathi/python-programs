def GCD(m,n):
    if m<n:
        m,n=n,m
    if n==0:
        return m
    else:
        return GCD(n,m%n)

x=eval(input("Enter the 1st number: "))
y=eval(input("Enter the 2nd number: "))
print("GCD is",GCD(x,y))
