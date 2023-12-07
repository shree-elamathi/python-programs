class fol:
    def frequencycount(self,arr,N,P):
        arr.sort()
        for i in arr:
            print(i)
        for i in arr:
            print("i",i)
            for j in range(1,P+1):
                print("j",j)
                if i!=j:
                    arr[j-1]=0
                    print("list value",arr[j-1])
                else:
                    a=1
                    print("i after",i)
                    for k in range(j,len(arr)):
                        if i==k:
                            a=a+1
                    arr[i-1]=a
        return arr
arr=[2,3,2,3,5]
N=5
P=5
fol().frequencycount(arr,N,P)
for i in arr:
    print(i,end=" ")
