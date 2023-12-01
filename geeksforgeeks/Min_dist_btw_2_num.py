arr=[1,2,3,5,4]
n=5
x=2
y=1
class min:
    def minDist(self,arr,n,x,y):
        ind1 = -1
        ind2 = -1
        index = []
        if x not in arr or y not in arr:
            return (-1)
        else:
            for i in range(0,len(arr)):
                if x==arr[i]:
                    ind1=i
                if y==arr[i]:
                    ind2=i
                if (ind1!=-1 and ind2!=-1):
                    index.append(abs(ind1-ind2))
        index.sort()
        return index[0]


print(min().minDist(arr,n,x,y))

