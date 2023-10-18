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

lllist=Linkedlist()
i=int(input("Enter the no.of element to be inserted:"))
for j in range(0,i):
    n=input("Enter the element to be inserted:")
    lllist.insertAtEnd(n)
lllist.printLL()