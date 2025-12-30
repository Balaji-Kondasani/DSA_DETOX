from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque([])
    def push(self,elem):
        self.stack.append(elem)
        print(f"element {elem} was added to stack")
    def pop(self):
        if(len(self.stack)==0):
            print("Stack underflow, no elements exist to be deleted")
        else:
            popped_element=self.stack.pop()
        print(f"element {popped_element} was popped from stack")
    def top(self):
        if(len(self.stack)==0):
            print("Stack empty , no elements exist")
        else:
            print(f"Top element of stack is {self.stack[-1]}")
    def size(self):
        if(len(self.stack)==0):
            print("Stack empty , no elements exist")
        else:
            print(f"The size of stack is {len(self.stack)}")  
    def traversal(self):
        if(len(self.stack)==0):
            print("Stack empty , no elements exist")
        else:
            print("Elements in lifo order are")
            for elem in range(len(self.stack)-1,-1,-1):
                print(self.stack[elem],end=" ")
            
st=Stack()
operations=True
while operations:
    print("Enter your choice\n 1.PUSH 2.POP 3.TOP 4.SIZE 5.TRAVERSAL 6.EXIT")
    choice=int(input())
    if choice==1:
        num=int(input("enter an element to push to stack\n"))
        st.push(num)
    elif choice==2:
        st.pop()
    elif choice==3:
        st.top()
    elif choice==4:
        st.size()
    elif choice==5:
        st.traversal()
    elif choice==6:
        print("stack operations ended......")
        operations=False
    else:
        print("Enter correct choice")
        
        