"""
AVL tree implementation
"""

class Node:
    
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None
        self.height = 0
        
        
class AVL():
    
    def __init__(self) -> None:
        self.root = None
        
    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
            
    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            # if left_node does not None
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.calculate_height(node.left_node),
                                  self.calculate_height(node.right_node)) + 1
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calculate_height(node.left_node),
                                  self.calculate_height(node.right_node)) + 1
                
        # After evry insertion  we have to check whether the AVL properties are violated
        self.handle_violation(node) 
        
    
    def remove_node(self, data, node):
        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data, self.left_node)
        elif data > node.data:
            self.remove_node(data, self.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)
                 
                parent = node.parent
                
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                    
                if parent is None:
                    self.root = None

                del node
                self.handle_violation(node)
                
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node
                
                self.handle_violation(parent)
            
            
            
            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node
                self.handle_violation(parent)
                
                
            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
                self.handle_valiation(node)
                
    def get_predecessort(self, node):
        if node.right_node is not None:
            return self.get_predecessort(node.right_node)
        return node
    
    
    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to root node
        while node is not None:
            node.height = max(self.calculate_height(node.left_node),
                              self.calculate_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent

    # check whether the subtree is balanced with root node = node
    def violation_helper(self, node):
        
        balance = self.calculate_balance(node)
        # tree is left heavy But it can be left-right heavy or left-left heavy
        if balance > 1:
            # left right heavy situation: left rotation on parent + right rotation grandparent
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            # right rotation grandparent
            self.rotate_right(node)
            
        if balance < -1:
            if self. calculate_balance(node.right_node) > 0:
                self.rotate_right(node.right_node)
            
            self.rotate_left(node)
            
            
    def calculate_height(self, node):
        # This is when the node is a NULL
        if node is None:
            return -1
        
        return node.height
    
    def calculate_balance(self, node):
        
        if node is None:
            return 0
        
        return self.calculate_height(node.left_node) - self.calculate_height(node.right_node)
    
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
            
    def traverse_in_order(self, node):
        if node.left_node is not None:
            self.traverse_in_order(node.left_node)
            
        l = ""
        r = ""
        p = ""
        
        if node.left_node is not None:
            l = node.left_node.data
        else:
            l = "NULL"
            
        if node.right_node is not None:
            r = node.right_node.data
        else:
            r = "NULL"
        if node.parent is not None:
            p = node.parent.data
        else:
            p = "NULL"
            
        print("%s left: %s right %s parent: %s height: %s" % (node.data, l, r, p, node.height))
        
        if node.right_node:
            self.traverse_in_order(node.right_node)
        
    
    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)
        
        temp_left_node = node.left_node
        t = temp_left_node.right_node
        
        temp_left_node.right_node = node
        node.left_node = t
        
        if t is not None:
            t.parent = node
            
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node = temp_parent
        
        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
            
        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node
            
        if node == self.root:
            self.root = temp_left_node
            
        node.height = max(self.calculate_height(node.left_node), self.calculate_height(node.right_node))
        temp_left_node.height = max(self.calculate_height(temp_left_node.left_node),
                                    self.calculate_height(temp_left_node.right_node)) + 1
        
        print("tulee tänne kanssa")
        
    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)
        
        temp_right_node = node.right_node
        t = temp_right_node.left_node
        
        temp_right_node.left_node = node
        node.left_node = t
        
        if t is not None:
            t.parent = node
            
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node = temp_parent
        
        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node
            
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node
            
        if node == self.root:
            self.root = temp_right_node
            
        node.height = max(self.calculate_height(node.left_node), self.calculate_height(node.right_node))
        temp_right_node.height = max(self.calculate_height(temp_right_node.left_node),
                                    self.calculate_height(temp_right_node.right_node)) + 1
        
        
if __name__== '__main__':
    
    avl = AVL()
    avl.insert(5)
    avl.insert(3)
    avl.insert(4)