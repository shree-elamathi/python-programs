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
            max_ind = ind + x
            temp_ind = ind + 1
            val = arr[ind + 1]
            for i in range(1, x+1):
                if arr[ind + i] + temp_ind > max_ind:
                    val = arr[ind + i]
                    max_ind=arr[ind + i] + temp_ind
                    actual_ind=temp_ind
                temp_ind += 1
            x = val
            ind = actual_ind
            jump += 1
        return jump


arr= [9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]
print(Solution().minJumps(arr))

#arr = [1, 4, 3, 2, 6, 7]
#arr = [9, 8, 2, 2, 0, 2, 2, 0, 4, 1, 5, 7, 9, 6, 6, 0, 6, 5, 0, 5]
#arr= [1, 1,1,1]
# arr= [1,2,1,1,1]
# arr= [10,9,8,7,6,5,4,3,2,1,1,0]
