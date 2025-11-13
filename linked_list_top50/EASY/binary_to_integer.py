# converting a linked list of binary nodes to an integer number

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class SinglyLinkedList(object):
    def getCurrentDecimalValue(self,head):
        curr=head
        string=""
        while curr is not None:
            string+=(curr.val)
            curr=curr.next
        result=0
        power=len(string)-1
        for i in string:
            result+=(int(i)*(2**power))
            power-=1
        return result