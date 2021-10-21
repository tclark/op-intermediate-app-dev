## IN608
## Intermediate Application Development

## Session 21 :  Network Sockets - part 2

### Introduction
Last time we saw how to get network sockets working from the client and the server side. Our basic implementations had a lot of problems. One of them was that our server could only respond to one client at a time. We overcame that by using selectors to multiplex over our client sockets. This time we will see how to overcome another big problem.

It's useful to think about the TCP/IP network model again. Last time we focussed on the Transport and Link Layers. The underlying network protocols pretty much determined what we did. Today our focus is the appliaction layer, where we are much more free to make our own choices.

  - **Application layer**
  - Transport Layer (TCP, UDP)
  - Internet Layer (IPv4, IPv6)
  - Link layer


**The problem**

Last time we wrote code like this

```
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 65432))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024)
```

But what if we want to send longer (or shorter) messages? How can we tell how long an incoming message is? The lower level protocols don't help in this regard. Basically we have two options:

  1. Require that our application uses fixed-length messages.
  2. Make the messages indicate how long they are.

Both of these options work and both are used in real world application. The first option is kind of limiting, but is easy to implement. The second option is more flexible. To make this work, we need to start our messages with *application headers*. Here is a very simple one:

```
 |----------|---------------|
 |   12     | Hello, world  |
 |----------|---------------|
   Header      Body
   (2 bytes)   (Variable) 
```

Our application protocol is that every message starts with a 2-byte header, which contains an unsigned integer. The value of this integer is the number of bytes in the body. This means that our bodies can be up to 65,535 bytes long. The process of reading a message is now

  1. Read in two bytes
  2. Decode the bytes into an integer value
  3. Read in the number of bytes indicated by the header value.

To send a message
  1. Compose the message body.
  2. Convert it to bytes, if necessary and determine its length.
  3. Encode the length value into a two-byte header.
  4. Concatenate the header and body.
  5. Send the data.


### Example Code

The natural thing to do at this point is to write two functions, one to send messages and one to receive them

**Send**

```
import struct

def send(txt, sock):
  msgbody = bytes(txt.encode('utf-8'))
  msglen = len(msgbody)
  header = struct.pack('>H', msglen) # 2-byte unsigned int
  message = header + msgbody
  sock.sendall(message)                                       # 9
```

**Receive**

```
def receive(sock):
    data = b''
    while len(data) < 2:
        data += sock.recv(4)
    body_length  = struct.unpack('>H', data[:2])[0]
    data = data[2:]
    while len(data) < body_length:
        data += sock.recv(4)
    return data.decode('utf-8')       
```

(Yes, calling sock.recv(4) is a bit silly, but it demonstrates our process.)

---
### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `21-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `21-practical` directory.
  4. Follow the directions in the README.md file in the `21-practical` directory.
---

### More cowbell

We now have a de facto “application protocol” that lets us send and receive utf-8 strings of up to about 64kb length. We can do better. If we could define a larger header with multiple fields, then we could attach more metadata to our application messages.

It’s our application, so we can do anything we want with the header. We probably want it to be text. Using JSON makes it easy to parse.

**Example header**

```
{
    'Context-type': 'text/plain',
    'Content-encoding': 'utf-8',
    'Content-length': 46
   }
```
We put a header like this before our body. An application can use this to determine how to process the body. Now we have a new problem. How long is the header? But we already solved this.


```
 |----------|---------------|--------------------|
 |   48     | { ... }       | "Hello, world"     |
 |----------|---------------|--------------------|
   Preeader    Header          Body
   (2 bytes)   (Variable)      (Variable)
```

The preheader tells us how long the header is. The header tells us how long the body is

### Sending a message
The process of writing a message is now

  1. Get your message body and convert it to bytes.
  2. Prepare your header, now that you know how long the body is, and convert it to bytes.
  3. Prepare your preheader with the length of your header.
  4. Assemble the three parts.
  5. Send the message.

### Receiving a message

The process of reading a message is now
  1. Get at least two bytes in an input buffer.
  2. Process the preheader and remove it from the buffer.
  3. Collect enough bytes in the buffer to hold the header.
  4. Process the header and remove its bytes from the buffer. 
  5. Collect the bytes for the body and process it.

At this point we probably have enough structure to warrant a `Message` class. What methods should it have?
