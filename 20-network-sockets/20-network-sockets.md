## IN608
## Intermediate Application Development

## Session 20 :  Network Sockets

### Introduction
Today it seems like just about any application we write involves some degree of network interaction. Our processes communicate with each other using network sockets. These sockets are really just one (very common) form of interprocess communication. The general principles we apply in this case apply across interprocess communiction in general.

It's useful to think about the TCP/IP network model.

  - Application layer
  - Transport Layer (TCP, UDP)
  - Internet Layer (IPv4, IPv6)
  - Link layer

We will look at application layer considerations in the next session. As programmers, most of our attention is there. Today we will look at the transport and internet layers. We will focus on TCP and IPv4, but the main ideas hold for other protocols like UDP or IPv6. We aren't especially concerned with the link layer, since that is handled by the operating system.

** Servers and Clients **

We will discuss writing both client and server applications. There isn't one universal set of definitions for these, but for our purposes

  - A _server_ application listens for incoming requests and responds to them;
  - A _client_ initiates communication by opening a connection to a server.

A particular application may act like a server at some times and like a client at other times.

### Network socket flow

  1. The server creates a socket.
  2. The server binds the socket to an address/port.
  3. The server listens for connections to the socket.
  4. The client creates a socket.
  5. The client connects to the server’s socket.
  6. The server accepts the client connection.
  7. The client and server send and receive data.
  8. The client closes its connection, notifying the server.
  9. The server closes its connection.

Here's what this looks like in code:

** Server **
```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1
s.bind((’127.0.0.1’, 65432))                           # 2
s.listen()                                             # 3
conn, addr = s.accept()                                # 6 
data = conn.recv(1024)                                 # 7.2 
conn.sendall(b’received’)                              # 7.3
data = conn.recv(1024)                                 # 8.2
conn.close()                                           # 9
```

** Client **
```
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 4
s.connect((’127.0.0.1’, 65432))                        # 5
s.sendall(b’Hello’)                                    # 7.1
data = s.recv(1024)                                    # 7.4
s.close()                                              # 8.1
```

---
### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `20-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `20-practical` directory.
  4. Follow the directions in the README.md file in the `20-practical` directory.
---

### Concurrency
Our server above can only handle one connection at a time. While it’s servicing that connection, other clients just queue up and wait. In particular, calls to `accept()` and `recv()` block waiting on data from the socket. Realistically, our application code needs some sort of concurrency mechanism to handle multiple clients.

We will cover concurrency in more detail next week, but briefly our options are
  - Threading
  - Forking
  - Asyncio
  - Selectors

We will use selectors today.  

** Server: setting up the socket and selector **
```
import socket
import selectors

# We will add some functions here later

clients = selectors.DefaultSelector()
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind((host, port))
listener.listen()
listener.setblocking(False)
clients.register(listener, selectors.EVENT_READ, data=None)
```

Two things are going on here:
  1. We use `setblocking(False)` so that, when we call `accept()` later, our code won’t block waiting on a connection.
  2. We register our listener with our selector, telling the selector to notify us if the listener receives data.

Now that our socket is set up waiting for connections, we can add a simple event loop. Basically, the selctor will raise and event when a client socket has received some data for us to process.

```
while True:
    events = clients.select(timeout=None)
    for event, mask in events:
    if event.data is None:
        accept_connection(event.fileobj, clients)
    else:
        service_connection(event, mask, clients)
```

When we registered the listener, we set `data=None`. This is why `event.data` is `None` for a new connection. Now we just need to define the functions `accept_connection()` and `service_connections`.

** Accept connection **

When a new client connects to the server, this function handles accepting the connection and setting up the client socket.
```
def accept_connection(sock, clients):
    conn, addr = sock.accept()
    conn.setblocking(False)
    data = {’addr’: addr, ’buffer’: b’’}
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    clients.register(conn, events, data=data)
```

Again, notice that we set the connection to be nonblocking once we establish it. We register the newly established connection with our clients selector.

** Service connection **

When a client with an established connection sends data to the server, or when the server has data to send to the client, this function handles it.

```
def service_connection(event, mask, clients):
    sock = event.fileobj
    data = event.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data[’buffer’] = recv_data
        else:
            client.unregister(sock)
            sock.close()
        if mask & selectors.EVENT_WRITE:
            if data[’buffer’]:
                sent = sock.sendall(data[’buffer’])
                data[’buffer’] = b’’

```

If we received data, we save it in the buffer to use later. If we’re ready to write to client and we have data in buffer, we send it.

### References

  - `socket` library: https://docs.python.org/3/library/socket.html
  - `selectors` library: https://docs.python.org/3/library/selectors.html
  - RealPython article on socket programming: https://realpython.com/python-sockets/
  

