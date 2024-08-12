'''
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less
than or equal to 1.
'''
class Soluiton:
    def pickingNumbers(self,a):
        arr=[]
        a.append(0)
        count=1
        for i in range(len(a)-1):
            val=abs(a[i]-a[i+1])
            print(count)
            if val>1:
                arr.append(count)
                count=1
            else:
                count+=1
        return max(arr)
a=[4,6,5,3,3,1]
print(Soluiton().pickingNumbers(a))