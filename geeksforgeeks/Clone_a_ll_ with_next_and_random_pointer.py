'''
You are given a special linked list where each node has a next pointer pointing to its next node. You are also given
some random pointers, where you will be given some pairs denoting two nodes a and b i.e. a->random = b (random is a
pointer to a random node).
Construct a copy of the given list. The copy should consist of the same number of new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the original and copied list pointers represent the same list
state. None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes x and y in the original list, where x->random = y, then for the corresponding two
nodes xnew and ynew in the copied list, xnew->random = ynew.
Return the head of the copied linked list.
NOTE :
1. If there is any node whose arbitrary pointer is not given then it's by default NULL.
2. Don't make any changes to the original linked list.
'''


class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        new_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return new_head
