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
  4. There are multiple Python files, `q1.py - q6.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py` and `q2.py`. We will discuss these in about 20 minutes.

---
### Some more ADTs

### Circular Queue
Sometimes we want a queue with a maximum length. If we try to add an item that puts if over the maximum, we have two choices. We could just refuse to add the item, possibly raising an exception. On the other hand, we could remove the oldest item from the queue to make room for the new item. Which is correct? It depends on the problem we are trying to solve. If we are implementing the second case, a *circular queue* can be a good structure.

Suppose we want a queue with no more than 4 items. We will make a 4-element list to start:

```         
q = [None, None, None, None]
q_front = 0
q_back = 0
```
The queue is empty, so all the values are `None`. `q_front` is the location from which we would removes items, but there arent any right now.. `q_back` is the location where we will add the next item. 

Let's add the value 'a' to the queue.
```
q[q_back]  = 'a'
q_back = (q_back  + 1) % 4  # modulo 4
```
We adjusted `q_back` since the next time we add something it will go in location 1. Now suppose we add 'b', 'c', and 'd', adjusting `q_back` each time. At this point the list will look like `['a', 'b', 'c', 'd']`. `q_front` is still `0`, since that's the location of the oldest item, and hence the one we should remove next. But `q_back` is also `0`, since the next we we want to add something, that's where it should go. After enqueuing these four items our queue looks like this:

```
q == ['a', 'b', 'c', 'd']
q_front == 0
q_back == 0
```

Now let's take something out of the queue. We get the item at the index indicated by `q_front` and return its value `'a'`. We also add one to `q_front`, since the next time we want to remove an item it will have to come from the next position over.

If we add 'd' to the queue, then we at it at position `0`, as indicated by `q_back` and then we set `q_back` to `1`. We overwrite the value `'a'`, but that's fine since it's no longer in the queue. Now let's add another value, `'e'`. The value of `q_back` tells us to place it in position `1`, but that would overwite the `'b'` at the front of the queue. What should be do?

One approach is to decline to add the new item because the queue is full. In this case we might raise an exception. But in some applications we might conclude that the value `'b'` at the front of the queue is too "stale" to be relevant any longer. In this case we overwrite that value and increment `q_front` to point at `'c'` since it's now the oldest value in the queue. Which approach is correct depends on the problem we're trying to solve.


### Graphs
Graphs are extremely common data structures. In fact there are special cases of graphs you may have seen, like linked lists or trees. A graph is just a collection of *nodes* and *edges*.  The nodes hold some piece of data. An edge joins two nodes to represent some sort of connection between them

![A graph with six nodes and seven edges (User:AzaToth, Public domain, via Wikimedia Commons)](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/333px-6n-graf.svg.png "Undirected Graph")

Graphs can be *directed* or *undirected*. In a directed graph, each edge has a direction, e.g. from NodeA to NodeB, but not necessarily in the other direction. In an undirected graph, there's no direction to an edge. The relationship metween the two nodes can be considered symmetrical.

![A directed graph (Johannes Rössel, Public domain, via Wikimedia Commons)](https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Directed_acyclic_graph_2.svg/305px-Directed_acyclic_graph_2.svg.png "Directed Graph")

Graphs are frequently used data structures. Some of the well-known special cases of graphs include *trees* and *linked lists*

![A tree (Paddy3118, CC BY-SA 4.0 via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tree_%28computer_science%29.svg/258px-Tree_%28computer_science%29.svg.png "Tree")

To represent a graph in code, there are multiple possible approaches. Abstractly, a graph is just a list of nodes and a list of edges. A node could be just about any opject, and an edge could be a tuple  of the two nodes it joins.  We could then write a `Graph` class that has two lists, one for nodes and one for edges. This approach works well for undirected graphs. For directed graphas it's often useful to make a `Node` class that does a lot of the work. Such a `Node` would have one attribute for its data and another with a list of the `Nodes`'s *outgoing* edges (probably really a list of the `Node`s to which it is joined by an edge.) In any case, the "correct" approach is one that leads to easily understood and maintained code.

