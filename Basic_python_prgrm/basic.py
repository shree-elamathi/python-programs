a=[100,278,153,784,105,632,147,118,39,410]
b=sorted(a)
print(b)
x=eval(input("Enter the number"))
pos=int(len(b)/2)
while (pos<len(b)):
    if x==b[pos]:
        print("true")
        break
    elif x>b[pos]:
        pos=int(pos+len(b)/2)
