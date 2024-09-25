'''
Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        val=[]
        current=head
        while current:
            val.append(current.data)
            current=current.next
        if val==val[::-1]:
            return True
        return False
