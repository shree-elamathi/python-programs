'''
Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the
order of non-zero elements. Do the mentioned change in the array in place.
'''


class Solution:
    def pushZerosToEnd(self, arr):
        count=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[count]=arr[count],arr[i]
                count+=1
        return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(Solution().pushZerosToEnd(arr))
