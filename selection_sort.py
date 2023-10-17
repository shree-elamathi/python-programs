a=input("Enter a list:\n").split()
a=list(map(eval,a))
for i in range(0,len(a),1):
    smallest=min(a[i:])
    sindex=a.index(smallest)
    a[i],a[sindex]=a[sindex],a[i]
print(a)
