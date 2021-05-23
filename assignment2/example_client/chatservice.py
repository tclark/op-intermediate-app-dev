""" Provides ChatService, a class that handles sending data to and
receiving data from a chat server.
"""
import json
import socket
import struct

MAX_HEADER_SIZE = 2 ** 16 - 1
PREHEADER_SIZE = 2

class ChatService:
    """ The ChatService class handles network communication between the
    client and the server. Public methods:
      - connect()
      - send()
      - receive()
      - close()
    Note that chat servers only send data in response to a client
    request, so at this time there's no reason to call receive().
    It's included as a public method for now in case the protocol
    specification changes.
    """

    def __init__(self, host, port):
        """ Sets up the server object with specified IPv4 address and
        port. Sets some default values for outgoing headers.
        """
        self.host = host
        self.port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # some default header values for sending
        self.send_header = {
            'Content-type': 'application/json',
            'Content-encoding': 'utf-8'
            }
        self._read_buffer = b''

    def connect(self):
        """ Pretty much does what it says."""
        self._sock.connect((self.host, self.port))

    def receive(self):
        """ Reads a message from the chat server, returning a dict
        with the header, the body processed as a dict, and the raw
        body string.
        """
        header_len = self._read_preheader()
        header = self._read_header(header_len)
        body = self._read_body(header)
        return {
            'header': header,
            'body': body[0],
            'raw_body': body[1]
            }


    def send(self, msg):
        """ Send msg to the server. The message should be a json
        formatted string. Returns the processed response.
        """
        body = bytes(msg.encode('utf-8'))
        header = self._header(len(body))
        preheader = self._preheader(len(header))
        message = preheader + header + body
        # send the message
        self._sock.sendall(message)
        # return the response
        return self.receive()

    def close(self):
        """ Closes the connection to the server."""
        self._sock.close()

    def _preheader(self, length):
        if length > MAX_HEADER_SIZE:
            raise ValueError('Header size {length} is too big.')
        return struct.pack('>H', length)

    def _read_preheader(self):
        ph_bytes = self._read(PREHEADER_SIZE)
        return struct.unpack('>H', ph_bytes)[0]

    def _header(self, body_length):
        hdr = self.send_header
        hdr['Content-length'] = body_length
        hdr_str = json.dumps(hdr)
        return bytes(hdr_str.encode('utf-8'))

    def _read_header(self, length):
        hdr_bytes = self._read(length)
        hdr_str = hdr_bytes.decode('utf-8')
        return json.loads(hdr_str)

    def _read_body(self, header):
        body_len = header.get('Content-length')
        body_bytes = b''
        body_str = ''
        body = None
        if body_len:
            body_bytes = self._read(body_len)
        else:
            raise ValueError('Content-length header missing')
        body_enc = header.get('Content-encoding')
        if body_enc == 'utf-8':
            body_str = body_bytes.decode('utf-8')
        else:
            raise ValueError(f'Unsupported Content-encoding: {body_enc}')
        body_type = header.get('Content-type')
        if body_type == 'application/json':
            body = json.loads(body_str)
        return body, body_str

    def _read(self, length):
        while len(self._read_buffer) < length:
            self._read_sock()
        result = self._read_buffer[:length]
        self._read_buffer = self._read_buffer[length:]
        return result

    def _read_sock(self):
        self._read_buffer += self._sock.recv(1024)
