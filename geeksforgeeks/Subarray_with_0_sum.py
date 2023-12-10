#Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need
# to return true/false depending upon whether there is a subarray present with 0-sum or not.
# Printing will be taken care by the driver code.
class solution:
    def subarray(self,arr,n):
        for i in arr:
            if i==0:
                return True
            else:
                if i<0:
                    m=i
                    arr.remove(i)
                    if tofindsum(arr,m):
                        return True
                    else:
                        return False

def tofindsum(arr,m):
    for i in range(0,len(arr)):
        if arr[i]+m==0:
            return True
        else:
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]+m==0:
                    return True


arr=[5,-4,-3,-1]
n=4
print(solution().subarray(arr,n))