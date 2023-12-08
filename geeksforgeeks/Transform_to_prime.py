#Given an array of n integers. Find the minimum positive number to be inserted in array,
# so that sum of all elements of array becomes prime.
class solution:
    def minnumber(self,arr,n):
        a=0
        for i in arr:
            a=a+i
        if isprime(a):
            return 0
        else:
            ans=find_next_num(a)
            val=ans-a
            return val
def find_next_num(a):
    next_num=a+1
    while True:
        if isprime(next_num):
            return next_num
        next_num+=1

def isprime(a):
    if a<=1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a%i==0:
            return False
    return True

arr=[2, 4, 6, 8, 12]
n=len(arr)
print(solution().minnumber(arr,n))