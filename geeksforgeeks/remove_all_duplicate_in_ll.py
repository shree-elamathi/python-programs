'''
Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only
numbers that appear once in the original list, and return the head of the modified linked list.
'''
class Solution:
    def removeAllDuplicates(self,head):
        temp=head
        prev=None
        while temp:
            n=temp.next
            f=False
            while n and temp.data==n.data:
                n=n.next
                f=True
            if f:
                if prev is None:
                    head=n
                else:
                    prev.next=n
                temp=n
            else:
                prev=temp
                temp=temp.next
        return head