'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
'''

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr= nextNode
        return prev