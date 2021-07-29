# Implement the push, pop, empty, peek, & size methods 
# in the Stack class. the size method returns the length of 
# stack.

# Use the Stack object provided in the main function to 
# display the expected output.

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass
    
    def empty(self):
        pass
          
    def size(self):
        pass
    
    def display(self):
        """ This is not a standard stack method and is just
        included here for convenience.
        """
        print(self._stack)
    
def main():
    stack = Stack()
    stack.push('Introductory App Dev Concepts')
    stack.push('Intermediate App Dev Concepts')
    stack.push('Advanced App Dev Concepts')
    
    # Write your solution here

if __name__ == '__main__':
    main()
    
# Expected output:

# ['Introductory App Dev Concepts', 'Intermediate App Dev Concepts']
# Intermediate App Dev Concepts is at the top of the stack
# There are 2 item(s) in the stack