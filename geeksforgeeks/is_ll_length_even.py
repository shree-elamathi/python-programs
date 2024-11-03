'''
Given a linked list, your task is to complete the function isLengthEven() which contains the head of the linked list,
and check whether the length of the linked list is even or not. Return true if it is even, otherwise false.
'''


class Solution:
    def isLengthEven(self, head):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if length % 2 == 0:
            return True
        return False



