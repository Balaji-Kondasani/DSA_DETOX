class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class DoublyLinkedList:
    count_nodes=0
    def __init__(self):
        self.head=None
    def add_at_beginning(self,data):
        newnode=Node(data)
        DoublyLinkedList.count_nodes+=1
        if self.head is None:
            self.head=newnode
        else:
            newnode.right=self.head
            self.head=newnode
    def add_at_end(self,data):
        DoublyLinkedList.count_nodes+=1
        if self.head is None:
            self.add_at_beginning(data)
        else:
            newnode=Node(data)
            temp=self.head
            while temp.right!=None:
                temp=temp.right
            temp.right=newnode
            newnode.left=temp
    def add_at_specified_position(self,pos,data):
        if pos==0:
            self.add_at_beginning(data)
            DoublyLinkedList.count_nodes+=1
        else:
            newnode=Node(data)
            temp=self.head
            counter=0
            while counter<pos-1:
                temp=temp.right
                pos=pos-1
            newnode.right=temp.right
            temp.right=newnode
            newnode.left=temp
            DoublyLinkedList.count_nodes+=1
    def get_total_nodes(self):
        print(f"The total no of nodes in list are {self.count_nodes}")
                
    def traverse_nodes(self):
        if self.head is None:
            print("Linked List is currently empty")
        else:
            temp=self.head
            while temp.right is not None:
                print(temp.data,end="->")
                temp=temp.right
            print(temp.data)
dll=DoublyLinkedList()
operations=True
while operations:
    print("Enter your choice\n 1.ADD AT BEGINNING 2.ADD AT END 3.ADD AT SPECIFIED POSITION 4.TRAVERSAL 5.SIZE 6.EXIT")
    choice=int(input())
    if choice==1:
        num=int(input("enter an element to add at beginning of list\n"))
        dll.add_at_beginning(num)
    elif choice==2:
        num=int(input("enter an element to add at ending of list\n"))
        dll.add_at_end(num)
    elif choice==3:
        print(f"We have {dll.count_nodes} in the list, so enter position accordingly")
        pos=int(input("enter position (0_based_indexing)"))
        if pos>DoublyLinkedList.count_nodes-1:
            print(DoublyLinkedList.count_nodes)
            print("Cannot insert node (out of bounds)")
        else:
            num=int(input(f"enter an element to add at {pos} position of list\n"))
            dll.add_at_specified_position(pos,num)
    elif choice==4:
        dll.traverse_nodes()
    elif choice==5:
        dll.get_total_nodes()
    elif choice==6:
        print("linked list operations ended......")
        operations=False
    else:
        print("Enter correct choice")
        
        