'''
Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number
of nodes in the linked list.
'''
class Solution:
    def getCount(self, head):
        cur=head
        c=0
        while cur:
            c+=1
            cur=cur.next
        return c