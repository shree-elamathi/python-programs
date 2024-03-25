#Another sorting method, the counting sort, does not require comparison. Instead, you create an
# integer array whose index range covers the entire range of values in your array to sort. Each time a
# value occurs in the original array, you increment the counter at that index. At the end, run through
# your counting array, printing the value of each non-zero valued index that number of times.
#we are going to return the frequency list
class Solution():
    def CountingSort(self,arr):
        val=[]
        fre=[]
        for i in range(0,100):
            val.append(i)
            fre.append(0)
        for j in arr:
            for k in range(len(val)):
                if j==val[k]:
                    fre[k]+=1
                    break
        print(len(fre))
        return fre
arr=[1,1,3,2,1]
print(Solution().CountingSort(arr))