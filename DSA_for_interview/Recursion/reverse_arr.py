'''
Given a array reverse it using recursion
'''


class Solution:
    def reverse(self, arr, n):
        def fun(l,r):
            if (l>=r):
                return
            arr[l], arr[r] = arr[r], arr[l]
            fun(l+1, r-1)

        fun(0, n-1)
        return arr


n=5
arr = [1,2,3,4,5]
print(Solution().reverse(arr,n))