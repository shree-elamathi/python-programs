#print n fibonacci numbers using for loop
def fibonacci(n):
    num1=0
    num2=1
    print(num1)
    print(num2)
    for i in range(n):
        num3=num1+num2
        print(num3)
        num1=num2
        num2=num3
#fibonacci(4)

#printing n fibonacci numbers using recursion
#print(0)
#print(1)
def fibo(num1,num2,count):
    if count<=19:
        num3=num1+num2
        print(num3)
        num1=num2
        num2=num3
        count+=1
        fibo(num1,num2,count)
    else:
        return
#fibo(0,1,2)

#printing nth fibonacci number using recursion
def F(n):
    if n<=1:
        return n
    else:
        return F(n-1)+F(n-2)

print(F(19))