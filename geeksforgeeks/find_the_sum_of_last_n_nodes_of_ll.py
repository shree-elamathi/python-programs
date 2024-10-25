'''
Given a single linked list, calculate the sum of the last n nodes.
Note: It is guaranteed that n <= number of nodes.
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        cur=head
        arr=[]
        while cur:
            arr.append(cur.data)
            cur=cur.next
        x=len(arr)-n
        arr=arr[x:]
        y=sum(arr)
        return y