## IN608
## Intermediate Application Development
---

## Session 4: Abstract Data Types

Last time we looked at some data types in Python. We definitely spent some time considering *concrete* details about how they are implemented. Sometimes it's important to consider those concrete details to help us reason about how our code works. Sometimes, however, it's helpful to step back and consider data types abstractly.

**Abstract Data Types**
An *Abstract Data Type* (ADT) is comprised of two things:
  - The set of values which the type can represent;
  - The set of operations that can be performed with elements of the type.

When we talk about ADTs, we are not concerned about their implementations. To ADTs that represent the same values and support the same operations are the same ADT. (Of course, at some point we do have to implement them.) In programming there are a number of commonly recognised ADTs that have proven useful. Examples of ADTs include

  - Stacks
  - Queues
  - Graphs
  - Trees

  ---

### Stacks
A stack is a **last-in, first-out** structure. You can picture a stack of plates or cards where you always add items to the top and take them from the top of the stack. Stacks support two primary operations, There are some additonal common, but not strictly required, operations.

Primary operations:
  - **push**: Add an item to the stack
  - **pop**: Remove an item from the stack.

Additional operations:
  - **peek**: View the item at the top of the stack without removing it
  - **depth**: Return the number of items on the stack
  - **empty**: Return true if the stack is empty

**Implementations**
A Python `list` can be used directly as a stack. The list's `append()` method is basically `push()` by another name, and they have a `pop()`method.

```
stack = []             # []
stack.append(’apple’)  # [’apple’]
stack.append(’banana’) # [’apple’, ’banana’]
stack.append(’cherry’) # [’apple’, ’banana’, ’cherry’]
stack.pop()            # [’apple’, ’banana’]
```

But we might also opt to implement a class to provide a stack.

```
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def empty(self):
        pass


stk = Stack()
stk.push(’cat’)
stk.push('dog')
stk.pop()
```  
### Queues
The dual to a stack is a queue. A queue is a **first-in, first-out** data structure. Just picture a supermarket checkout. And just like a stack, a queue has two primary operations and some additional, optional operations.

Primary operations:
  - **enqueue**: Add an item to the end of the queue
  - **dequeue**: Remove an item from the front of the queue.

Additional operations:
  - **peek**: View the item at the front of the queue without removing it
  - **depth**: Return the number of items in the queue
  - **empty**: Return true if the queue is empty

**Implementations**
A `list` is not effecient for queue operations, but the `collections` library provides a `deque` that is suitable. It suuports `append()` (enqueue) and `popleft()` (dequeue) operations

```
from collections import deque
queue = deque([])      # deque([])
queue.append(’apple’)  # deque([’apple’])
queue.append(’banana’) # deque([’apple’, ’banana’])
queue.append(’cherry’) # deque([’apple’, ’banana’, ’cherry’]) 
queue.popleft()        # deque([’banana’, ’cherry’])
```
But again, we might want to to implement a full `Queue` class.
```
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
              
    def enqueue(self, item):
        pass

    def dequeue(self):
        pass
    
    def peek(self):
        pass

    def empty(self):
        pass
          
          
q = Queue()
q.enqueue(’cat’)
```
---

Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `04-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `04-practical` directory.
  4. There are multiple Python files, `q1.py - q7.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py`, `q2.py`, and `q3.py`. We will discuss these in about 20 minutes.

---

