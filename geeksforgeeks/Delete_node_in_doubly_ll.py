''''
Given a doubly Linked list and a position. The task is to delete a node from a given position (position
starts from 1) in a doubly linked list and return the head of the doubly Linked list.
'''
class Solution:
    def delete_node(self, head, x):
        if head is None or x<=0:
            return head
        cur=head
        if x==1:
            head=cur.next
            if head:
                head.prev=None
            cur=None
            return head
        for _ in range(x-1):
            cur=cur.next
            if cur is None:
                return head
        if cur.next:
            cur.next.prev=cur.prev
        if cur.prev:
            cur.prev.next=cur.next
        cur=None
        return head