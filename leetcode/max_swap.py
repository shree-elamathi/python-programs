'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
'''


class Solution:
    def maximumSwap(self, num):
        num_list = list(str(num))
        n = len(num_list)
        last = {int(d): i for i, d in enumerate(num_list)}
        for i in range(n):
            for d in range(9, int(num_list[i]), -1):
                if last.get(d, -1) > i:
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int("".join(num_list))
        return num


num = 2736
print(Solution().maximumSwap(num))