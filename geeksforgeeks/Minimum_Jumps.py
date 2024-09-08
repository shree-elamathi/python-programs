'''
Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can
be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0,
then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.
'''


class Solution:
    def minJumps(self, arr):
        if len(arr) == 1:
            return 0
        x = arr[0]
        ind = 0
        jump = 1
        while x < (len(arr) - 1) - ind:
            if x == 0:
                return -1
            max_ind = ind + 1
            for i in range(2, x):
                print("Verifying index ", max_ind+i)
                if (arr[ind + i + 1] + i) >= max_ind:
                    max_ind = ind + i + 2
            x = arr[max_ind]
            print("jump to", x)
            ind = max_ind
            jump += 1
        return jump

arr = [1, 4, 3, 2, 6, 7]
# arr = [9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]
print(Solution().minJumps(arr))

# arr= [1, 1,1,1]
# arr= [1,2,1,1,1]
# arr= [10,9,8,7,6,5,4,3,2,1,1,0]
# arr= [9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]
