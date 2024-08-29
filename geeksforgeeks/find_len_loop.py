'''
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number
of nodes in the loop, otherwise return 0.
'''
class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                count = 1
                while slow.next!=fast:
                    count+=1
                    slow=slow.next
                return count
        return 0