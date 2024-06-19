'''
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly
one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is
impossible to make m bouquets return -1.
'''
class Solution:
    def minDays(self,bloomDay,m,k):
        def canMakebouquets(days):
            bouquets, flowers = 0, 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakebouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left if canMakebouquets(left) else -1
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(Solution().minDays(bloomDay,m,k))
