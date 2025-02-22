'''
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product
of lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters.
'''


def maxProd(n):
    if (n == 0 or n == 1):
        return 0
    max_val = 0
    for i in range(1, n - 1):
        max_val = max(max_val, max(i * (n - i), maxProd(n - i) * i))
    return max_val

n = 10
print(maxProd(n))