def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


def factorial_Approach2(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

x=eval(input("Enter the number: "))
# print("factorial(",x,")=",factorial(x))
print("factorial Approach 2(",x,")=",factorial_Approach2(x))
