'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
'''


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #create a dummy node in order to add the other nodes
        dummy = ListNode()
        curr = dummy

        #this loop traverses until 1 list reaches the end
        while list1 is not None and list2 is not None:

            #find the smallest node and add it to the dummy node
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        #if list1 has remaining nodes then add it to the dummy node
        if list1 is not None:
            curr.next = list1

        #else add the list2 to the dummy
        else:
            curr.next = list2

        #since the first node is dummy return the next node
        return dummy.next
