class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

# we need to find the common node of both the lists
# nodes when created are assigned a memory address after getting stored in a memory location
# so in both the lists we need to find if any of the nodes are pointing to (same node)same memory location
# in both the lists

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        
        #Brute Force -- store the complete node as key in hashmap
        curr=headA
        hashmap={}
        while curr is not None:
            hashmap[curr]=1
            curr=curr.next
        temp=headB
        while temp is not None:
            if temp in hashmap:
                return temp
        return None
    
        #Better Solution -- calculate length difference of both nodes , make both pointers start 
        # same node , if two pointers are equal --> intersectig point
        
        curr=headA
        length1=0
        while curr is not None:
            length1+=1
            curr=curr.next
        temp=headB
        length2=0
        while temp is not None:
            length2+=1
            temp=temp.next

        if length1>length2:
            diff=length1-length2
            curr=headA
            while diff!=0:
                curr=curr.next
                diff-=1
            temp=headB
            while curr is not None and temp is not None:
                if curr==temp:
                    return curr
                curr=curr.next
                temp=temp.next
            return None
        else:
            diff=length2-length1
            temp=headB
            while diff!=0:
                temp=temp.next
                diff-=1
            curr=headA
            while curr is not None and temp is not None:
                if curr==temp:
                    return curr
                curr=curr.next
                temp=temp.next
            return None
        
        #Optimal Solution -- 
