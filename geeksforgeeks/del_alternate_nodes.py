'''
Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes present in even positions.
'''
class Solution:
    def deleteAlt(self, head):
        cur=head
        i=0
        while cur:
            if i%2!=0:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
            i+=1
        return head