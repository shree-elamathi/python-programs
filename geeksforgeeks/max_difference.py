'''
Given an integer array arr of integers, the task is to find the maximum absolute difference between the nearest left
smaller element and the nearest right smaller element of every element in array arr. If for any component of the arr,
the nearest smaller element doesn't exist then consider it as 0.
'''


class Solution:
    def maxAbsDifference(self, arr):
        n = len(arr)

        # Arrays to store the nearest smaller elements on the left and right
        left_smaller = [0] * n
        right_smaller = [0] * n

        # Stack to find nearest smaller to the left
        stack = []

        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            left_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])

        # Clear the stack to reuse for finding nearest smaller to the right
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            right_smaller[i] = stack[-1] if stack else 0
            stack.append(arr[i])

        # Calculate the maximum absolute difference
        max_difference = 0
        for i in range(n):
            max_difference = max(max_difference, abs(left_smaller[i] - right_smaller[i]))

        return max_difference


# Example usage:
solution = Solution()
arr = [2, 1, 8, 7, 6, 5]
print(solution.maxAbsDifference(arr))  # Output: 6
