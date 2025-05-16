'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
'''

class Solution:
    def reverseList(self, head):

        #have a cur pointer
        curr = head

        #to store the previous node
        prev = None

        #runs until the last node
        while curr is not None:

            #save the next node
            nextNode = curr.next

            #Now add the prev node to the next node
            curr.next = prev

            #now change the previous node to the current node
            prev = curr

            #now current is moved to the previously save next node
            curr= nextNode

        #now return the previous node
        return prev