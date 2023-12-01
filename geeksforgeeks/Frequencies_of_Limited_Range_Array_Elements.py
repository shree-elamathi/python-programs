class fol():
    def __init__(self,N,P,arr):
        self.arr = arr
        self.P=P
        self.N=N
    def get_arr(self,N):
        for i in range (0,N):
            a=int(input("Enter the elements of arr:"))
            arr.append(a)
    def print_arr(self,arr):
        for i in arr:
            print(i,end=" ")
    def frequencycount(self,arr,N,P):
        print(N)
        newarr=[]
        if N>0:
            a=0
            for i in arr:
                if i==N:
                    a=a+1
            newarr.append(a)
            ob.frequencycount(arr,N-1,P)
        for i in newarr:
                print(i,end=" ")



arr=[]
N=int(input("Enter N value:"))
P=int(input("Enter P value:"))
ob=fol(N,P,arr)
ob.get_arr(N)
ob.print_arr(arr)
ob.frequencycount(arr,N,P)

#another method
#with reduced time complexity
#inside the frequency function
#newarr=[]
#for i in range(1,N+1):
#a=0
#for j in arr:
#if i==j:
#a=a+1
#newarr.append(a)
#arr=newarr
#ob.print_arr(arr)