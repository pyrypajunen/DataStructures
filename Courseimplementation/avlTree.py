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
                node.height = max(self.calc_height(node.left_node),
                                  self.calc_height(node.right_node)) + 1
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node),
                                  self.calc_height(node.right_node)) + 1
                
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
                        parent.left_node = node.left_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node
                
                self.handle_violation(node)
            
            
            
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
                self.handle_violation(node)
                
                
            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
                self.handle_valiation(node)


            
            
        