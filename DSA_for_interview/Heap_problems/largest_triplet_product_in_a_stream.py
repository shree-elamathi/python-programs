'''
Given a stream of integers represented as arr[]. For each index i from 0 to n-1, print the multiplication of
largest, second largest, third largest element of the subarray arr[0…i]. If i < 2 print -1. Given a stream of
integers represented as arr[]. For each index i from 0 to n-1, print the multiplication of largest, second largest,
third largest element of the subarray arr[0…i]. If i < 2 print -1.
'''

from queue import PriorityQueue


class Solution:
    def LargestTripletMultiplication(self, arr, n):
        q = PriorityQueue()
        for i in range(n):
            q.put(-arr[i])
            if (q.qsize() < 3):
                print(-1)
            else:
                x = q.get()
                y = q.get()
                z = q.get()

                ans = x * y * z

                print(-ans)

                q.put(x)
                q.put(y)
                q.put(z)


arr = [1, 2, 3, 4, 5]
n = len(arr)
Solution().LargestTripletMultiplication(arr, n)
