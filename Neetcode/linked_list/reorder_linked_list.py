'''
You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]
Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]
Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]
You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
'''

def reorderList( head):
    #point the curr pointer at the head
    curr = head

    #traverse until the node is not None
    while curr:

        #a pointer to track the last(n-1) node
        last = head
        while last.next:
            #prev pointer to make the last previous node's next as None
            prev = last
            last = last.next

        #if last and curr pointer both points to the same node then the list is reordered
        if last == curr:
            break

        #Save the last node
        newNode = last

        #Make the last previous node's next as none to avoid cycle
        prev.next = None

        #To save the curr node's next
        prev1 = curr.next

        #Now join the prev1 to the last node
        newNode.next = prev1

        #Now attach the newNode to the curr node
        curr.next = newNode

        #now move the curr pointer to the prev1
        curr = prev1

    return head