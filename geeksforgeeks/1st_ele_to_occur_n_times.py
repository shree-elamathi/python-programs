#Given an array of n integers. Find the first element that occurs atleast k number of times. If
# no such element exists in the array, then expect the answer to be -1.
def firstelektime(n,k,a):
    res = {}
    for i in range(n):
        if res.get(a[i]) and res[a[i]] + 1 == k:
            return a[i]
        elif res.get(a[i]):
            res[a[i]] += 1
        else:
            res[a[i]] = 1
    return -1



n=7
k=2
a=[1, 7, 4, 3, 4, 8, 7]
print(firstelektime(n,k,a))