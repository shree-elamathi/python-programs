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
#Given a singly linked list of length n. The link list represents a binary number, ie- it contains only 0s and 1s.
# Find its decimal equivalent.The significance of the bits decreases with the increasing index in the linked list.
#An empty linked list is considered to represent the decimal value 0.
# Since the answer can be very large, answer modulo 109+7 should be printed.
    def decimalvalue(self, head):
        MOD = 10 ** 9 + 7
        n = llist.getCount()-1
        ans=0
        while head:
            ans=ans+(int(head.data)*(2**n))
            head=head.next
            n=n-1
        return ans%MOD
    def getCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
#You are given two linked lists that represent two large positive numbers. From the two numbers represented
# by the linked lists, subtract the smaller number from the larger one. Look at the examples to get a
# better understanding of the task.
    def sublinkedlist(self,llist,llist1):
        temp1=""
        temp2=""
        while llist:
            temp1=temp1+llist.data
            llist=llist.next
        while llist1:
            temp2=temp2+llist1.data
            llist1=llist1.next
        temp1=int(temp1)
        temp2=int(temp2)
        if temp1>temp2:
            x=str(temp1-temp2)
        else:
            x=str(temp2-temp1)
        ll3=Linkedlist()
        for i in x:
            ll3.insertAtEnd(i)
        return ll3.head.data
#given a sorted circular linked list and given an integer and you have to insert
# the value such that the linked list remains sorted.
    def sortedinsert(self,head,data):
        new_node=Node(data)
        #case1: No node
        if head is None:
            head=new_node
            return head
        current=head
        #case2: Insert at begining
        if data<head.data:
            while current.next!=head:
                current=current.next
            current.next=new_node
            new_node.next=head
            return new_node
        #case3:Insert in the middle
        while current.next!=head:
            if current.data<=data<=current.next.data:
                new_node.next=current.next
                current.next=new_node
                return head
            current=current.next
        #case4:Insert at end
        current.next=new_node
        new_node.next=head
        return head


#Given two numbers, num1 and num2, represented by linked lists of size n and m respectively.
#The task is to return a linked list that represents the sum of these two numbers.
#For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25
#by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null.
#You are required to return the head of the linked list 2->1->5->null.
#Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the
#output list.

    def addtwolist(self,num1,num2):
        sum=Linkedlist()
        num_1=""
        num_2=""
        cnode1=num1.head
        cnode2=num2.head
        while cnode1:
            num_1+=str(cnode1.data)
            cnode1=cnode1.next
        while cnode2:
            num_2 += str(cnode2.data)
            cnode2 = cnode2.next
        val=str(int(num_1)+int(num_2))
        for i in val:
            sum.insertAtEnd(i)
        return sum

# Given a singly linked list having n nodes containing english alphabets ('a'-'z').
# Rearrange the linked list in such a way that all the vowels come before the consonants while
# maintaining the order of their arrival.
    def arrangeCV(self,head1):
        ll=Linkedlist()
        vow=['a','e','i','o','u']
        vow1=[]
        cons=[]
        while head1:
            if head1.data not in vow:
                cons.append(head1.data)
            else:
                vow1.append(head1.data)
            head1=head1.next
        for i in vow1:
            ll.insertAtEnd(i)
        for i in cons:
            ll.insertAtEnd(i)
        return (ll)
def areIdentical(head1,head2):
    while head1 or head2:
        if not head1:
            return False
        if not head2:
            return False
        if head1.data!=head2.data:
            return False
        head1=head1.next
        head2=head2.next
    return True

ll1=Linkedlist()
arr1=[1,2,3,4,5,6,7]
for i in arr1:
    ll1.insertAtEnd(i)
ll2=Linkedlist()
arr2=[1,2,3,4,5,6,7]
for i in arr2:
    ll2.insertAtEnd(i)
print(areIdentical(ll1.head,ll2.head))
