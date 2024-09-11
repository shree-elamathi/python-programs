'''
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1
to 0.
For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not
shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get
101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
'''


class solution:
    def minBitFlips(self, start, goal):
        s_bin = bin(start).replace("0b", "")
        g_bin = bin(goal).replace("0b", "")
        min_flip = 0
        if len(g_bin) > len(s_bin):
            x = len(g_bin) - len(s_bin)
            for i in range(x):
                s_bin = "0" + s_bin
        elif len(s_bin) > len(g_bin):
            x = len(s_bin) - len(g_bin)
            for i in range(x):
                g_bin = "0" + g_bin
        for i in range(len(s_bin)):
            if s_bin[i] != g_bin[i]:
                min_flip += 1
        return min_flip


start = 3
goal = 4
print(solution().minBitFlips(start, goal))
