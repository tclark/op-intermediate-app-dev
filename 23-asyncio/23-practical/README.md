# Practical  23: Async IO
To perform today's lab it will be necesary to `pip install sqlalchemy`.

1. Write a program that reads in this README file to a list of lines and 
then prints the text with the order of the lines reversed and the text
in each line reversed. Use the `aiofiles` library to read and write the 
files. The basic structure of your program should include
  - a coroutine that reads in this README file
  - a coroutine that writes the reversed output to a new file
  - a coroutine that calls the ones above, chaining them together
  - a main section that invokes `asyncio.run()`.

**Stop here**. We will discuss solutions in class.

## Homework

2. Write a program using `asyncio` to count the number of "o"s in this file.
Use the producer/consumer pattern. 
  - Use one producer to read in lines and put them in a queue.
  - Use two consumers to take lines from the queue and count the "o"s.
    place the count of "o"s on a line in a list that is shared between
    the consumers.
  - Once the producers and consumers are done, sum that list to get the total.
