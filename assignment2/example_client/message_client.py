#! /usr/bin/env python3
""" A basic chat client for testing and debugging. It sends chat
requests to a server and prints the full response that the server
sends in reply.

Actions:

  login <username> : Starts a session for the given user.

  get : Gets any messages for the logged in user. The first time
  it gets messages for a user it will request all the messages the
  server has for the user. On subsequent requests it will send a
  'last_read' datetime parameter and should only receive messages
  sent after that time.

  send: The client will prompt for messages. After the user indicates that
  all messages have been entered, it will send the list of messages to the
  server.

  logout: Logs the user out.

  quit: Exits the program, logging the user out if necessary.

It's not a very user-friendly program. If you enter commands that
can't be performed, like sending messages before logging in, it just
doesn't perform the action.
"""
import sys

from chatservice import ChatService
from chatclient import Client


def get_action():
    """ Prompts the user for a command with possible
    arguments and returns them as a list of str.
    """
    return input('action > ').split()


def end_session(client):
    """ Logs the client out and exits the program."""
    client.logout()
    sys.exit(0)


def get_msg_list():
    """ Prompts the user to enter a series of messages,
    forming them into a list of dicts that can be sent to
    the client.
    """
    another = True
    msg_list = []
    while another:
        msg_to = input('To: ').strip()
        txt = input('Message: ').strip()
        msg_list.append({'to': msg_to, 'msg': txt})
        again = input('Send another(y/N): ').strip()
        another = again[:1].lower() == 'y'
    return msg_list


def main():
    """ Main program loop"""
    client = Client()
    client.server = ChatService('127.0.0.1', 65432)
    while True:
        action = get_action()
        if action[0] == 'quit':
            end_session(client)
        elif action[0] == 'login' and action[1]:
            client.login(action[1])
        elif action[0] == 'logout':
            client.logout()
        elif action[0] == 'send':
            mesgs = get_msg_list()
            client.send(mesgs)
        elif action[0] == 'get':
            client.get()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
