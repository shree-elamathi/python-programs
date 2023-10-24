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
    def pairWiseSwap(self):
        p1 = self.head
        if head.next:
            p2=self.head.next
            self.head=p2
            temp=None
            while p1.next:
                p1.next=p2.next
                p2.next=p1
                if temp:
                    temp.next=p2
                temp=p1
                if p1.next==None or p1.next.next==None:
                    break
                p1=p1.next
                p2=p1.next
        else:
            head=p1

lllist=Linkedlist()
i=int(input("Enter the no.of element to be inserted:"))
for j in range(0,i):
    n=input("Enter the element to be inserted:")
    lllist.insertAtEnd(n)
lllist.printLL()
lllist.pairWiseSwap()
print("After swapping")
lllist.printLL()
