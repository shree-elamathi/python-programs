'''
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will
set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
'''


class Solution:
    def hasCycle(self, head):
        # Using Floyd's cycle detection using slow and fast pointer
        slow = head
        fast = head

        #slow pointer moves 1 step ahead
        #fast pointer moves 2 step ahead
        #if they both meet then cycle is detected
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


