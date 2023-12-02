class Solution:
    def isRepresentingBST(self, arr, N):
        a=list(arr)
        a.sort()
        if (arr==a):
            return 1
        else:
            return 0

arr=[2, 4, 1]
N=3
print(Solution().isRepresentingBST(arr,N))