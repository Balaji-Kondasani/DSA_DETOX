class ListNode:
    def __init__(self, data):
        self.data=data
        self.next=null
        
class SinglyLinkedList:
    def __init__(self):
        self.head=None
          
    def insert_at_beginning(self, data):
        first_node=ListNode(data)
        if self.head is None:
            self.head=first_node
            
        self.head=first_node.next
        self.head=first_node
        
    def insert_at_end(self, data):
        last_node=ListNode(data)
        if self.head is None:
            self.insert_at_beginning(data)
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=last_node
        
    def insert_at_position(self, data, position):
        
    
    def delete_by_value(self, data):
        """Delete the first occurrence of a node with given data"""
        # TODO: Find and delete node with matching data
        # Return True if deleted, False if not found
        pass
    
    def delete_at_position(self, position):
        """Delete node at the specified position (0-indexed)"""
        # TODO: Delete node at given position
        # Handle edge cases: position < 0, position >= length, empty list
        pass
    
    def delete_at_beginning(self):
        """Delete the first node"""
        # TODO: Delete head node
        # Handle empty list case
        pass
    
    def delete_at_end(self):
        """Delete the last node"""
        # TODO: Delete tail node
        # Handle empty list and single node cases
        pass
    
    def update_at_position(self, position, new_data):
        """Update data of node at specified position"""
        # TODO: Find node at position and update its data
        # Return True if updated, False if position invalid
        pass
    
    def update_by_value(self, old_data, new_data):
        """Update first occurrence of old_data with new_data"""
        # TODO: Find node with old_data and update to new_data
        # Return True if updated, False if not found
        pass
    
    # ============ SEARCH OPERATIONS ============
    
    def search(self, data):
        """Search for a node with given data"""
        # TODO: Return position of first occurrence (0-indexed)
        # Return -1 if not found
        pass
    
    def contains(self, data):
        """Check if list contains a node with given data"""
        # TODO: Return True if found, False otherwise
        pass
    
    def get_at_position(self, position):
        """Get data of node at specified position"""
        # TODO: Return data at position
        # Return None if position invalid
        pass
    
    # ============ UTILITY OPERATIONS ============
    
    def size(self):
        """Return the number of nodes in the list"""
        # TODO: Count and return total nodes
        pass
    
    def is_empty(self):
        """Check if the list is empty"""
        # TODO: Return True if empty, False otherwise
        pass
    
    def display(self):
        """Display the entire list"""
        # TODO: Print all nodes in format: data1 -> data2 -> ... -> None
        pass
    
    def to_list(self):
        """Convert linked list to Python list"""
        # TODO: Return Python list containing all node data
        pass
    
    def clear(self):
        """Remove all nodes from the list"""
        # TODO: Clear the entire list
        pass
    
    # ============ ADVANCED OPERATIONS ============
    
    def reverse(self):
        """Reverse the linked list in-place"""
        # TODO: Reverse the order of nodes
        pass
    
    def find_middle(self):
        """Find the middle node(s) of the list"""
        # TODO: Use slow-fast pointer technique
        # Return middle node's data (for odd length)
        # For even length, return the second middle node's data
        pass
    
    def detect_cycle(self):
        """Detect if there's a cycle in the list"""
        # TODO: Use Floyd's cycle detection algorithm
        # Return True if cycle exists, False otherwise
        pass
    
    def remove_duplicates(self):
        """Remove duplicate nodes from the list"""
        # TODO: Remove all duplicate nodes
        # Assume list is sorted for O(n) solution
        # For unsorted list, consider using hash set
        pass
    
    def find_nth_from_end(self, n):
        """Find the nth node from the end"""
        # TODO: Use two-pointer technique
        # Return data of nth node from end
        # Return None if n is invalid
        pass
    
    def merge_sorted(self, other_list):
        """Merge this sorted list with another sorted list"""
        # TODO: Merge two sorted linked lists
        # Return new merged linked list
        pass
    
    def split_at_position(self, position):
        """Split the list at given position"""
        # TODO: Split list into two parts at position
        # Return the second part as new linked list
        pass
    
    def get_intersection(self, other_list):
        """Find intersection point of two linked lists"""
        # TODO: Find the node where two lists intersect
        # Return the intersecting node's data or None
        pass
    
    # ============ ITERATOR SUPPORT ============
    
    def __iter__(self):
        """Make the linked list iterable"""
        # TODO: Implement iterator protocol
        pass
    
    def __len__(self):
        """Return length when len() is called"""
        # TODO: Return size of list
        pass
    
    def __str__(self):
        """String representation of the list"""
        # TODO: Return string representation
        pass
    
    def __repr__(self):
        """Official string representation"""
        # TODO: Return detailed representation
        pass

# ============ USAGE EXAMPLES ============
if __name__ == "__main__":
    # TODO: Add comprehensive test cases
    
    # Create a new linked list
    ll = SinglyLinkedList()
    
    # Test insertion operations
    # ll.insert_at_beginning(1)
    # ll.insert_at_end(2)
    # ll.insert_at_position(3, 1)
    
    # Test display
    # ll.display()
    
    # Test search operations
    # print(f"Search for 2: {ll.search(2)}")
    # print(f"Contains 3: {ll.contains(3)}")
    
    # Test deletion operations
    # ll.delete_by_value(2)
    # ll.delete_at_position(0)
    
    # Test utility operations
    # print(f"Size: {ll.size()}")
    # print(f"Is empty: {ll.is_empty()}")
    
    # Test advanced operations
    # ll.reverse()
    # middle = ll.find_middle()
    # has_cycle = ll.detect_cycle()
    
    pass