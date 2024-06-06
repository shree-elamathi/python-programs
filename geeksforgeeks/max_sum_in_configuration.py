'''
Given an integer array(0-based indexing) a of size n. Your task is to return the maximum value of the sum
of i*a[i] for all 0<= i <=n-1, where a[i] is the element at index i in the array. The only operation
allowed is to rotate(clockwise or counterclockwise) the array any number of times.
'''
class Solution:
    def max_sum(self,a,n):
        max_sum=0
        for i in range(n):
            j=0
            a.append(a[j])
            a.remove(a[j])
            new_sum=0
            for i in range(n):
                val=i*(a[i])
                new_sum+=val
            max_sum=max(max_sum,new_sum)
        return max_sum

a=[10, 1, 2, 3, 4]
n=5
print(Solution().max_sum(a,n))