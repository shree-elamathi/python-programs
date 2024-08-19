'''
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth
smallest element in the given array. It is given that all array elements are distinct.
Follow up: Don't solve it using the inbuilt sort function.
'''
class Solution:
    def kthSmallest(self, arr,k):
        sorted_arr=self.bubbleSort(arr,len(arr))
        return sorted_arr[k-1]
    def bubbleSort(self,arr, n):
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(Solution().kthSmallest(arr,k))