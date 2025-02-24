'''
The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to
calculate the span of stock price for all days. The span arr[i] of the stocks price on a given day i is defined as
the maximum number of consecutive days just before the given day, for which the price of the stock on the given day
is less than or equal to its price on the current day.
'''


class Solution:
    def check(self, arr, i, count):
        j = i - 1
        while j >= 0:
            if arr[j] <= arr[i]:
                count += 1
                j -= 1
            else:
                return count
        return count

    def calculateSpan(self, arr):
        ans = [1]
        count = 1
        for i in range(1, len(arr)):
            ans.append(self.check(arr, i, count))
        return ans


arr = [100, 80, 60, 70, 60, 75, 85]
print(Solution().calculateSpan(arr))
