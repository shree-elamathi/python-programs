'''
Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.
'''
class Solution:
    def count(self, head, key):
        key_count=0
        cur=head
        while cur:
            if cur.data==key:
                key_count+=1
            cur=cur.next
        return key_count

