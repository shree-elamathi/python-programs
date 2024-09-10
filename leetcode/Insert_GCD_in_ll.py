'''
Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
Return the linked list after insertion.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            return
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def insertGreatestCommonDivisors(self):
        current = self.head
        while current.next:
            x = current.val
            y = current.next.val
            res = self.GCD(x, y)
            new_node = Node(res)
            link = current.next
            current.next = new_node
            new_node.next = link
            current = current.next.next

    def GCD(self, m, n):
        if m < n:
            m, n = n, m
        if n == 0:
            return m
        else:
            return self.GCD(n, m % n)

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.val, end=" ")
            current_node = current_node.next


ll1 = Linkedlist()
arr1 = [18, 6, 10, 3]
for i in arr1:
    ll1.insertAtEnd(i)
ll1.insertGreatestCommonDivisors()
ll1.printLL()
