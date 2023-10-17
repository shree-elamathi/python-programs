v=[]
k=4
while (len(v)<=10):
    isprime=True
    for i in range (2,int(k/2)+1):
        if (k%i==0):
            isprime= False
            break
    if(isprime):
        v.append(k)
    k+=1

print(v)
