'''
You are given a Linked List. Sort the given Linked List using quicksort.
'''


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def getTail(node):
    while node and node.next:
        node = node.next
    return node


def partition(head, end):
    pivot = end
    prev, curr = None, head
    tail = pivot
    new_head, new_end = head, end

    # Partitioning around the pivot
    while curr != pivot:
        next_node = curr.next  # Save the next node to avoid NoneType error
        if curr.data < pivot.data:
            if not new_head:
                new_head = curr
            prev = curr
        else:
            # Move nodes greater than pivot to the end
            if prev:
                prev.next = next_node
            else:
                new_head = next_node  # Update new head if the first element is moved
            tail.next = curr
            curr.next = None
            tail = curr
        curr = next_node

    if not new_head:
        new_head = pivot
    new_end = tail

    return pivot, new_head, new_end


def quickSortRecur(head, end):
    if not head or head == end:
        return head

    pivot, new_head, new_end = partition(head, end)

    # Sort left side if there's a portion to the left of the pivot
    if new_head != pivot:
        temp = new_head
        while temp.next != pivot:
            temp = temp.next
        temp.next = None  # Temporarily disconnect

        # Recursively sort the left side and reconnect pivot
        new_head = quickSortRecur(new_head, temp)
        temp = getTail(new_head)
        temp.next = pivot

    # Recursively sort the right side of pivot
    pivot.next = quickSortRecur(pivot.next, new_end)
    return new_head


def quickSort(head):
    end = getTail(head)
    return quickSortRecur(head, end)


# Helper function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


# Example usage
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(8)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(10)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)

sorted_head = quickSort(head)
print("Sorted Linked List:")
printList(sorted_head)
