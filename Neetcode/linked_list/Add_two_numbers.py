''''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Return the sum of the two numbers as a linked list.
'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        i = 1
        cur1 = l1
        head3 = None

        #store the number represented by ll1
        while cur1:
            temp = cur1.val * i
            num1 += temp
            #since the number is in reverse
            i = i * 10
            cur1 = cur1.next

        num2 = 0
        i = 1
        cur2 = l2

        # store the number represented by ll2
        while cur2:
            temp = cur2.val * i
            num2 += temp
            # since the number is in reverse
            i = i * 10
            cur2 = cur2.next

        #Now add both the numbers
        newNum = num1 + num2

        #If the newNum is 0 then return New node with value 0
        if newNum == 0:
            return ListNode(0)

        #We should return the sum in reverse
        #So remove digits from last and make it a node and add it
        while newNum > 0:
            temp = newNum % 10
            newNode = ListNode(temp)
            newNum = int(newNum / 10)
            if head3 is None:
                head3 = newNode
                cur3 = head3
            else:
                cur3.next = newNode
                cur3 = cur3.next

        #now return the head of the newly formed ll
        return head3