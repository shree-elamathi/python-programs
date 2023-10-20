class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            return
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    def insertAtBegining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def printLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.next
    def pairWiseSwap(self, head):
        current_node = head
        # 1->cr
        if head.next:
            temp_node=current_node.next
            #2->temp
            head=temp_node
            head.next=current_node
            #2->1
            while temp_node.next.next:
                current_node.next=temp_node.next.next
                temp_node=temp_node.next
                #1->2->3->4->5
                #2->1
                #2->1->4
                #2->1->4->3->5
#1->2->2->4->5->6->7->8


lllist=Linkedlist()
ob=Solution()
i=int(input("Enter the no.of element to be inserted:"))
for j in range(0,i):
    n=input("Enter the element to be inserted:")
    lllist.insertAtEnd(n)
lllist.printLL()
