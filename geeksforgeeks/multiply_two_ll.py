'''
Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.
Note: The output could be large take modulo 109+7.
'''
class Solution:
    def multiply_two_lists(self, first, second):
        MOD=1000000007
        num1=""
        num2=""
        cur1=first
        cur2=second
        while cur1:
            num1+=str(cur1.data)
            cur1=cur1.next
        while cur2:
            num2+=str(cur2.data)
            cur2=cur2.next
        num1=int(num1)
        num2=int(num2)
        res=num1*num2
        return res%MOD
