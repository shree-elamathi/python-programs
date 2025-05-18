'''
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional
pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of
[val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or
null if it does not point to any node.
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        head1 = Node(head.val)
        curr1 = head1

        #maintain a hashmap to store the alternates of old node to new node
        hash = {head:head1}

        #Form the new ll without random pointer
        while curr.next:
            curr1.next = Node(curr.next.val)
            hash.update({curr.next:curr1.next})
            curr = curr.next
            curr1 = curr1.next

        curr = head
        curr1 = head1

        #Now traverse both the old and new list at the same time
        #find where the random pointer points in the old list (old node)
        #find the alternate for old node in the hash map
        #Now point the random pointer of the new node to the alternate node
        while curr:
            if curr.random:
                curr1.random = hash[curr.random]
            curr = curr.next
            curr1 = curr1.next

        #Now return the head
        return head1