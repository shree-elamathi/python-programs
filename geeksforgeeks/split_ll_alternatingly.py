'''
Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the
given linked list into two smaller lists. The sublists should be made from alternating elements from the original
list.
Note:
The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.
'''


class Solution:
    def alternatingSplitList(self, head):
        cur = head
        i = 0
        h1 = None
        h2 = None
        while cur and i < 2:
            if i == 0:
                h1 = Node(cur.data)
            else:
                h2 = Node(cur.data)
            i += 1
            cur = cur.next
        arr = []
        arr.append(h1)
        arr.append(h2)
        if not cur:
            return arr
        i = 0
        cur1 = h1
        cur2 = h2
        while cur:
            if i % 2 == 0:
                cur1.next = Node(cur.data)
                cur1 = cur1.next
            else:
                cur2.next = Node(cur.data)
                cur2 = cur2.next
            i += 1
            cur = cur.next
        return arr
