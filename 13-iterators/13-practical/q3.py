# In Python, file objects, like the variable "file" below, are 
# Iterators. With that in mind, explain the behaviour of the 
# code below.


with open('testfile') as file:
    file_itr0 = iter(file)
    file_itr1 = iter(file)
    print(f'File iterators the same: {file_itr0 is file_itr1}')
    print(f'File iterators the same as the file object: {file_itr0 is file}')
    # What's going on here? Can you explain why file, file_itr0, and file_itr1
    # are all the same object?

wit open('testfile') as file:
    while True:
        line = next(file)
        print(line[:-1])    # The -1 is just to trim a trailing newline.
        if line == 'cat\n':
            print('====Found a cat.====')
            break

    print('Exited the first loop')        

    for line in file:
        print(line[:-1])

# Notice that we have two different loops, but the second loop just seems to be 
# a continuation of the first. Why does it work in this way?
