'''
Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key.
Return -1 if the key is not found.
'''


class Solution:
    def search(self, arr, key):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (key == arr[mid]):
                return mid
            if (arr[mid] >= arr[lo]):
                if (key >= arr[lo] and key < arr[mid]):
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if (key > arr[mid] and key <= arr[hi]):
                    lo = mid + 1

                else:
                    hi = mid - 1
        return -1

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 10
print(Solution().search(arr,key))
