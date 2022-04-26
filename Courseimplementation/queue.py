"""
basic implementation of queue structure
FIFO structure - first in first out
"""



class Queue:
    
    
    def __init__(self) -> None:
        self.queue = []
    
    # check if queue is empty
    def is_empty(self):
        return self.queue == []
    
    # add itmes
    def enqueue(self, data):
        self.queue.append(data)
    
    # return first item and delete it
    def dequeue(self):
        if self.size_queue() < 1:
            return
        
        data = self.queue[0]
        del self.queue[0]
        return data
    
    # returns the last item of the qeue
    def peek(self):
        return self.queue[0]
    
    def size_queue(self):
        return len(self.queue)
    
    
    
que = Queue()
que.enqueue(7)
que.enqueue(8)
que.enqueue(7)
que.enqueue(5)
que.dequeue()
print(que.size_queue())