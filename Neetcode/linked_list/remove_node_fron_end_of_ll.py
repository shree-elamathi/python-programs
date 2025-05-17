'''
You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.
'''

class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        cur = head

        #To calculate the length of the list
        while cur:
            count += 1
            cur = cur.next

        cur = head
        count = count - n

        #If the count is 0 then we need to remove head so return head.next
        if count == 0:
            return head.next

        #If not then move until the n-1 node from the last
        for _ in range(count - 1):
            cur = cur.next

        #Now remove the nth node and return the head
        cur.next = cur.next.next

        return head




