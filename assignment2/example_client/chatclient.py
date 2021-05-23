""" Provides a (very basic) chat client for testing."""
import json
import pprint
from datetime import datetime


pp = pprint.PrettyPrinter(indent=4) # prints dicts nicely


class Client:
    """ The Client class basically performs the four actions (login,
    get, send, logout). It
      - prepares the outgoing message body as a dict
      - passes the message body to its ChatServer for sending
      - receives the response from the Chatserver (a dict)
      - prints the response.

    The client holds a reference to a ChatServer instance. This
    instance prepares the messages data, adding headers, sends the
    data, and returns the response to the client.
"""
    def __init__(self):
        """ Creates Client instance with initial state. """
        self.last_read = None
        self.logged_in = False
        self.name = None
        self.server = None

    def login(self, name):
        """ Connects to the server and logs in a user with the supplied
        name. Prints the response.  If the user is already logged in,
        it prints a message and exits.
        """
        if self.server and not self.logged_in:
            self.server.connect()
            self.name = name
            message = {
                'action': 'login',
                'params': {'name': name}
                }
            login_req = json.dumps(message)
            resp = self.server.send(login_req)
            pp.pprint(resp)
            self.logged_in = True
        else:
            if self.server:
                print(f'Already logged in as {self.name}')

    def logout(self):
        """ Logs the user out and closes the connection to the
        server.
        """
        if self.server and self.logged_in:
            message = {
                'action': 'logout',
                'params': None
                }
            logout_req = json.dumps(message)
            resp = self.server.send(logout_req)
            pp.pprint(resp)
            self.server.close()
        self.logged_in = False

    def send(self, messages):
        """ Takes a list of messages (dicts) and sends them to the
        server.
        """
        if self.server and self.logged_in:
            message = {
                'action': 'send_messages',
                'params': {'messages': messages}
                }
            send_req = json.dumps(message)
            resp = self.server.send(send_req)
            pp.pprint(resp)

    def get(self):
        """ Gets a list (possibly empty) of messages for the user.
        If the last_read parameter is supplied, then it only requests
        messages send after that time. Updates last_read.
        """
        if self.server and self.logged_in:
            last = self.last_read and self.last_read.isoformat()
            message = {
                'action': 'get_messages',
                'params': {'last_read': last}
                }
            get_req = json.dumps(message)
            resp = self.server.send(get_req)
            self.last_read = datetime.utcnow()
            pp.pprint(resp)
