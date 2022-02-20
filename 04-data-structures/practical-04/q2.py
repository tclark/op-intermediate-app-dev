# Implement the enqueue, dequeue, peek, empty, & length 
# methods in the Queue class. the length method returns the 
# length of queue.

# Use the Queue object provided in the main function to 
# display the expected output.

from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque([])

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass
    
    def empty(self):
        pass
    
    def length(self):
        pass
    
    def display(self):
        """Again, not a standard queue method."""
        print(self._queue)

def main():
    queue = Queue()
    queue.enqueue('Introductory App Dev Concepts')
    queue.enqueue('Intermediate App Dev Concepts')
    queue.enqueue('Advanced App Dev Concepts')
    
    # Write your solution here

if __name__ == '__main__':
    main()
    
# Expected output:
    
# There are 3 item(s) in the queue
# ['Intermediate App Dev Concepts', 'Advanced App Dev Concepts']