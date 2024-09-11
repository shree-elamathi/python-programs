'''
Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope.
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.
'''
import bisect
class solution:
    def minCost(self,arr):
        tot_cost=0
        if len(arr)==0:
            return tot_cost
        arr.sort()
        while len(arr)>1:
            first=arr.pop(0)
            second=arr.pop(0)
            cost=first+second
            tot_cost+=cost
            bisect.insort(arr, cost)
        return tot_cost



arr=  [4, 2, 7, 6, 9]
#  2, 4, 6, 7, 9
print(solution().minCost(arr))



