class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertAtBegining(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def insertAtIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        position=0
        if position==index:
            self.insertAtBegining(data)
        else:
            while(current_node!=Node and position+1 !=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print("Index does not exist")
    def insertAtEnd(self,data):
        new_node=Node(data)
        current_node=self.head
        if self.head is None:
            self.head=new_node
            return
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node
    def updateNode(self,data,index):
        current_node=self.head
        position=0
        if position==index:
            current_node.data=data
        else:
            while(current_node!=None and position!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                current_node.next=data
            else:
                print("Index does not exist")
    def remove_first_node(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next
    def remove_last_node(self):
        current_node=self.head
        if self.head is None:
            return
        else:
            while current_node.next.next:
                current_node=current_node.next
            current_node.next=None
    def removeatindex(self,index):
        if self.head is None:
            return
        current_node=self.head
        position=0
        if position==index:
            self.remove_first_node()
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                current_node.next=current_node.next.next
            else:
                print("Index does not exist")
    def remove_node(self,data):
        current_node=self.head
        while current_node!=None and current_node.next.data!=data:
            current_node=current_node.next
        if current_node==None:
            return
        else:
            current_node.next=current_node.next.next
    def sizeofLL(self):
        size=0
        if (self.head):
            curent_node=self.head
            while(curent_node):
                size=size+1
                curent_node=curent_node.next
            return size
        else:
            return 0
    def printLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.next

llist=Linkedlist()
llist.insertAtBegining("1")
llist.insertAtEnd("2")
llist.insertAtEnd("3")
llist.insertAtEnd('4')
llist.insertAtEnd('5')
llist.printLL()









            




