'''
Find the smallest index where the element is greater than the target
'''

class Solution:
    def upperBound(self, arr, x, n):
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] > x:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans

arr = [1,2,3,4,5,8,8,10,10,11,11,11]
x = 10
n = len(arr)
print(Solution().upperBound(arr,x,n))