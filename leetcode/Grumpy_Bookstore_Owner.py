'''
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter
the store. You are given an integer array customers of length n where customers[i] is the number of the
customer that enters the store at the start of the ith minute and all those customers leave after the end of
that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if
the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are
satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes,
but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
'''
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        total_satisfied = sum([customers[i] for i in range(len(customers)) if grumpy[i] == 0])
        max_increase = 0
        window_sum = 0
        for i in range(len(customers)):
            window_sum += customers[i] if grumpy[i] == 1 else 0
            if i >= minutes:
                window_sum -= customers[i - minutes] if grumpy[i - minutes] == 1 else 0
            max_increase = max(max_increase, window_sum)
        return total_satisfied + max_increase
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
print(Solution().maxSatisfied(customers,grumpy,minutes))