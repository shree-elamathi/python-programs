'''
Given an array arr containing non-negative integers. Count and return an array ans where ans[i] denotes the number of
smaller elements on right side of arr[i].
'''
class Solution:
    def constructLowerArray(self,arr):
        ans=[]
        for i in range(len(arr)):
            count=0
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    count+=1
            ans.append(count)
        return ans

arr=[12, 1, 2, 3, 0, 11, 4]
print(Solution().constructLowerArray(arr))