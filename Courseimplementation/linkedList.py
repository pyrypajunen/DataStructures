
# Represent current node of the list
class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        
    def __repr__(self) -> str:
        return str(self.data)
        
class LinkedList:
    
    def __init__(self) -> None:
        # this is the first node
        self.head = None
        self.num_of_nodes = 0
        
        
    def reverse_linked_list(self):
        
        # helper pointers
        actual_node = self.head
        previous_node = None
        next_node = None
        
        while actual_node is not None:
            next_node = actual_node.next_node
            actual_node.next_node = previous_node
            previous_node = actual_node
            actual_node = next_node
            
        self.head = previous_node
        
        
    def get_middle_node(self):
        
        fast_pointer = self.head
        slow_pointer = self.head
        
        while fast_pointer.next_node and slow_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
            
        return slow_pointer
            
        
    def insert_start(self, data):
        # this insert data beginning of the linked list
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        
        else:
            new_node.next_node = self.head
            self.head = new_node
            
    def insert_end(self, data):
        # this insert data end of the linked list
        self.num_of_nodes += 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            
            actual_node.next_node = new_node
            
        
    def size_of_list(self):
        return self.num_of_nodes
    
    # O(N) linear running time
    def traverse(self):
        
        actual_node = self.head
        
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node
        
    def remove(self, data):
        
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None
        
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
            
        if actual_node is None:
            return
        
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node
            

        
        
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Pyry')
    linked_list.insert_start(6.5)
    linked_list.insert_start(16.5)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()
    print("-------------")
    linked_list.remove(1000)
    linked_list.remove('Pyry')
    linked_list.traverse()
    print("-------------")
    linked_list.reverse_linked_list()
    linked_list.traverse()
    
        
        
        
        
        
        
        
        
        