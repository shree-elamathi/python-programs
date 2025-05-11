'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the
ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears
on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set
result[i] to 0 instead.
'''

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)

        # stack is used to track the largest element
        st = deque()

        # Iterate through the list from the last
        for i in range(len(temperatures)-1, -1, -1):

            # to maintain the dist ---> val is used
            val = 0

            # If the stack is empty then there is no larger values than that
            # So apply 0 to the current index
            if len(st) == 0:
                res[i] = 0

            # While to access the st until we find the largest element
            # Iterate until we find it or the stack becomes empty
            while len(st) > 0:

                #if the top val in stack is add 1 to the val
                # if found the largest element then break
                if st[-1][0] > temperatures[i]:
                    val += 1
                    break

                # If it is smaller add the val of that temperature and pop the top element
                val += st[-1][1]
                st.pop()

            # If the st is empty then there is no larger element so val is 0
            if len(st) == 0:
                res[i] = 0

            # If st is not empty then add the val to the res
            else:
                res[i] = val

            #while appending the element to the st append it along with its value
            # for easy access during the st pop and val update
            st.append([temperatures[i],val])

        return res


temperatures =  [55,38,53,81,61,93,97,32,43,78]
print(Solution().dailyTemperatures(temperatures))
