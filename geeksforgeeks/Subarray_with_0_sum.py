#Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need
# to return true/false depending upon whether there is a subarray present with 0-sum or not.
# Printing will be taken care by the driver code.
class solution:
    def subarray(self,arr,n):
        for i in arr:
            if i==0:
                return True
        else:
            sp = 0
            ep = sp + 1
            if tofindsum(arr, sp):
                return True
            else:
                return False

def tofindsum(arr,sp):
    if sp<len(arr):
        ep=sp+1
        a=0
        while ep<len(arr):
            sum=0
            for i in range(sp,ep+1):
                sum=sum+arr[i]
            if sum==0:
                a=a+1
                break
            else:
                ep = ep + 1
        if a>0:
            return True
        else:
            return tofindsum(arr,sp+1)



arr=[6,-10,-4,-6]
n=3
print(solution().subarray(arr,n))