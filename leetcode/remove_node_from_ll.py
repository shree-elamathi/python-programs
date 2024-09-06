'''
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list
after removing all nodes from the linked list that have a value that exists in nums.
'''
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        prev = None
        cur_node = head
        while cur_node:
            if cur_node.val in nums_set:
                if prev is None:
                    head = cur_node.next
                else:
                    prev.next = cur_node.next
            else:
                prev = cur_node
            cur_node = cur_node.next
        return head