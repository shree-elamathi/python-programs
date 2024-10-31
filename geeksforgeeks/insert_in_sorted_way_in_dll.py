'''
Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position
in the sorted Doubly linked list(DLL).
Note: The DLL is sorted in ascending order
'''


class Solution:
    def sortedInsert(self, head, x):
        new_node = Node(x)
        if not head:
            return new_node

        if x < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node

        cur = head
        while cur:
            if x >= cur.data:
                if not cur.next or x < cur.next.data:
                    new_node.next = cur.next
                    new_node.prev = cur
                    if cur.next:
                        cur.next.prev = new_node
                    cur.next = new_node
                    break
            cur = cur.next
        return head