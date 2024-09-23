'''
Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n} is missing and one number
'B' occurs twice in array. Find numbers A and B.
'''
class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        S = n * (n + 1) // 2  # Sum of first n natural numbers
        P = n * (n + 1) * (2 * n + 1) // 6  # Sum of squares of first n natural numbers

        sum_arr = sum(arr)
        sum_squares_arr = sum(x * x for x in arr)

        # Equations:
        diff = S - sum_arr  # A - B
        sum_ab = (P - sum_squares_arr) // diff  # A + B

        A = (diff + sum_ab) // 2
        B = sum_ab - A

        return A, B


solution = Solution()
arr =  [2, 2]
print(solution.findTwoElement(arr))