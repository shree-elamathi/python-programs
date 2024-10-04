'''
Given a Circular Linked List. The task is to delete the given node, key in the circular linked list, and reverse the
circular linked list.
Note:
You don't have to print anything, just return the head of the modified list in each function.
Nodes may consist of Duplicate values.
The key may or may not be present.
'''


class Solution:
    def reverse(self, head):
        if head is None or head.next == head:
            return head
        prev = None
        current = head
        next_node = None
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == head:
                break
        head.next = prev
        head = prev
        return head
    def deleteNode(self, head, key):
        if head is None:
            return None
        if head.data == key and head.next == head:
            return None
        current = head
        prev = None
        if head.data == key:
            while current.next != head:
                current = current.next
            current.next = head.next
            head = head.next
            return head
        current = head
        while current.next != head and current.next.data != key:
            current = current.next
        if current.next.data == key:
            current.next = current.next.next
        return head