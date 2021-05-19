# Practical  20: More sockets


##  Echo client and server
In today's exercise we will extend the echo client and servers that we wrote 
for practical 19. You need to have completed at least questions 1 and 2 from 
practical 19 before starting today's questions.

1. **Echo client**: Extend your echo client to use `send()` and `receive()` 
functions that add and process our basic two-byte length header, repectively.

2. **Echo server**: Extend your echo server to use `send()` and `receive()` in 
the same way. You should be able to write those functions so that they can be
used in both the client and the server.

**Stop here**. We will discuss solutions in class.

## Homework
The homework problems just continue in the same vein.

3. Extend your echo client and server from the first two question to use
full application headers. At this point you will need to write a full 
`Message` class. To be clear, when you submit you only need to provide this
version, not the versions from the above questions.

4. Finally, extend your multi-client echo server to use our application headers.
To do this you will need to build up the `Message` class to be more of an event 
handler. Here's an outline of how this could work:

    - We set up our listening socket and register it with the 
    selector, just like before.

    - When a connection is initiated by a client, accept the connection and 
    register the client socket with the selector. Set the `data` argument to 
    be a new `Message` object.

    - When a read event happens, the `Message` object can process the incoming 
    client request. Then, modify the selector event to look for the write event.

    - When the write event fires, your `Message` prepares and writes the response.
    Then your work is done, so deregister the socket from the selector and close 
    the socket.

For all this to work, your `Message` class needs to maintain a bunch of fields so
it can access the socket and selector, as well as tracking its own state. The 
Real Python article referenced in the last class actually has an example of all this, 
but it's a bit hard to follow. Honestly, it's probably easier to think it 
through yourself. Just take it one step at a time.                       


