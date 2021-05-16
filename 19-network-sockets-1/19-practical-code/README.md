# Practical  19: Network sockets


##  Echo client and server
The network programming equivalent of "Hello, world" is an echo server. The
server just receives a text message from the client and then echoes the message
back to it.

1. **Echo client**: The client isn't much different from the example client code we just saw. Write a client that
    1. connects to a server on the localhost;
    2. gets a message from user input;
    3. sends the message to the server;
    4. receives the echoed response from the server;
    5. prints the response;
    6. closes the connection.

2. **Echo server**: The echo server needs just a bit more capability than the example code. Write a server that
    1. sets up a socket listening on the localhost interface (IPv4);
    2. accepts the incoming client connection;
    3. in a loop, receives data from the client and sends the same data back;
    4. exits the loop when it receives empty data (this indicates that the client closed the connection);
    5. closes its connection.

This server can be left running while you run the client multiple times.

3. Experiment with your client and server. What happens if you run two clients at once? What happens if you send a very long message? (Try using a smaller buffer size than the 1024 bytes we used in the example). 


**Stop here**. We will discuss solutions in class.

## Homework

4. Write a more capable version of your echo server using selectors to service concurrent requests. Include a function to establish incoming client connections and one or more functions to handle reading from and writing to established client connections.

We will pick up from here in the next class session, so you should try to complete these before the next class.

