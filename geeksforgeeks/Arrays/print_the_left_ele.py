'''
Given a array of length N, at each step it is reduced by 1 element. In the first step the maximum element
would be removed, while in the second step minimum element of the remaining array would be removed, in the
third step again the maximum and so on. Continue this till the array contains only 1 element. And find the
final element remaining in the array.
'''
class Solution:
    def leftElement(self, arr, n):
        for i in range(n):
            if len(arr)==1:
                return arr[0]
            if len(arr)==2:
                arr.remove(max(arr))
                return arr[0]
            arr.remove(max(arr))
            arr.remove(min(arr))
arr=[7, 8, 3, 4, 2, 9, 5]
n=7
print(Solution().leftElement(arr,n))