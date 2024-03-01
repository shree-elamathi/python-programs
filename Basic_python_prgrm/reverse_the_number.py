rev=0
n=eval(input("Enter number to reverse: "))
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("The reverse of the number: ",rev)
    
