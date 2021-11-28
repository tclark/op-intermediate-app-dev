# Earlier in the semester we implemented Queue classes. Take your earlier 
# Queue class and add to it so that we can treat it as an immutable sequence.
# The rationale is that this will let us inspect items in the queue
# but we can only modify the queue with the typical push() and pop().
# methods. Your new Queue should implement collections.abc.Sequence.
# Include an "if __name__ == '__main__':" section demonstrating
# the sequence properties.


class Queue:
    pass


if __name__ == '__main__':

    q = Queue()
    for i in range(10):
        q.enqueue(i)

    print(q[5])
    q_slice = q[3:6]
    if isinstance(q_slice, Queue):
        print('A slice of a Queue is also a Queue')
    else:
        print('Something is not right.')
    print(q_slice[1])    
