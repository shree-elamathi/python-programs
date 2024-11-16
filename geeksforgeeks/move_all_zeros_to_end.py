'''
Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the
order of non-zero elements. Do the mentioned change in the array in place.
'''


class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        left = 0
        right = 1

        while left < n and right < n:
            if arr[left] == 0:
                while right < n and arr[right] == 0:
                    right += 1

                if right == n:  # Exit if no non-zero element is found
                    break

                # Swap the zero at 'left' with the non-zero at 'right'
                arr[left], arr[right] = arr[right], arr[left]

            # Move left pointer forward if the current element is non-zero
            if arr[left] != 0:
                left += 1

            # Ensure right pointer is ahead of left
            right = max(right, left + 1)

        return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(Solution().pushZerosToEnd(arr))
