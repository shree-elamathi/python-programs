'''
Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3.
If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.
'''


class Solution:
    def getMiddle(self, head):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        x = (length // 2)
        cur = head
        y = 0
        while y < x:
            y += 1
            cur = cur.next
        return cur.data
