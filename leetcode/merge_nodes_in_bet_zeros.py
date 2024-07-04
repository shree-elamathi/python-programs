'''
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning
and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is
the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_Node=Node(data)
        current_Node=self.head
        if self.head is None:
            self.head=new_Node
            return
        while current_Node.next:
            current_Node=current_Node.next
        current_Node.next=new_Node
    def mergeNodes(self):
        temp=self.head
        prev=None
        sum=0
        while temp:
            if temp.data==0:
                if prev is None:
                    prev=temp
                else:
                    prev.next=temp
                    prev=temp
                if sum!=0:
                    prev.data=sum
                sum=0
                temp=temp.next
            else:
                sum+=temp.data
                temp=temp.next
        return self.head.next

    def printNode(self,head):
        cur_node=head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
ll=LinkedList()
arr1=[0,3,1,0,4,6,2,0]
for i in arr1:
    ll.insert(i)
ans=ll.mergeNodes()
ll.printNode(ans)
