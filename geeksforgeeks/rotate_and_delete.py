'''
Given an array arr integers. Do the following operation until a single element left. For every kth operation:
Right, rotate the vector clockwise by 1.
Delete the kth element from the last.
Now, find the element which is left at last.
'''


class Solution:
    def rotate(self, arr):
        x = arr.pop()
        arr.insert(0, x)
        return arr

    def rotateDelete(self, arr):
        k=1
        while len(arr) > 1:
            arr = self.rotate(arr)
            arr.pop(-k)
            k+=1
            if k>len(arr):
                k=len(arr)
        return arr[0]


arr = [1, 2, 3, 4]
print(Solution().rotateDelete(arr))