# The code below takes input from the user. The only permitted inputs are
# "load", "save", "save as", and "close". If the user enters anything else,
# an exception is raised. Refactor this code using a try/except and the
# InputError from the lecture to recover from the error.

def get_input():
    inp = input('>')
    return inp

def do_command(c):
    actions = {
        'load': 'loading',
        'save': 'saving',
        'save as': 'saving as',
        'close': 'closing'
    }
    return actions[c]

def main():
    supported_commands = ['load', 'save', 'save as', 'close']
    entered_command = None
    while entered_command != 'close':
        entered_command = get_input()
        print(do_command(entered_command))

if __name__ == '__main__':
    main()
