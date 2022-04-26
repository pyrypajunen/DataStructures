"""
this is a stack data structure implementation (abstract data structure)
LIFO structure - "last in first out"
"""

class Stack:
    
    def __init__(self) -> None:
        self.stack = []
        
    # insert item into the stack // O(1)
    def push(self, data):
        self.stack.append(data)
        
    # remove the last item // O(1)
    def pop(self):
        
        if self.stack_size() < 1:
            return
        
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # return the last item of the stack
    def peek(self):
        return self.stack[-1]
    
    # return false is not full otherwise true
    def is_empty(self):
        return self.stack == []
    
    # return the size of the stack
    def stack_size(self):
        return len(self.stack)
    
    def find_max(self):
        max = self.stack[0]
        
        for num in self.stack:
            if max < num:
                max = num
                
        return max
    
    
stack = Stack()
stack.push(1)
stack.push(4)
stack.push(53)
stack.push(467)
stack.push(33)
stack.push(159)
print(stack.peek())
print(stack.stack_size())
print("This is the max",stack.find_max())