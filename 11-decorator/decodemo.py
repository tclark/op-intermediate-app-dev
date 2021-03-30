""" This module demonstrates an application of the Decorator Pattern
in a pretty by-the-book manner.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class AbstractMessenger(ABC):
    """The abstract base class defines our messenger interface and
    is the base of all our following classes. Note that any concrete
    subclasses must override any methods marked as abstract.
    """
    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass

    @abstractmethod
    def tell_the_time(self):
        pass

class ConcreteMessenger(AbstractMessenger):
    """This class must implement the thee abstract methods in its parent."""

    def say_hello(self):
        return 'Hello'

    def say_goodbye(self):
        return 'Goodbye'

    def tell_the_time(self):
        return datetime.now()

class AbstractDecorator(AbstractMessenger):
    """Concrete subclasses of this class can decorate ConcreteMessenger instances.
    This class does not override the abstract messages of its parent, so it
    is also an abstract base class."""

    def __init__(self, messenger):
        """This object needs to hold a reference to the messenger object it
        decorates."""
        self._messenger = messenger

    def tell_the_time(self):
        """We're only going to alter the behaviour of methods that return strings.
        tell_the_time() returns a datetime, so we'll pass its behaviour straight
        through.
        """
        return self._messenger.tell_the_time()

class ReversingDecorator(AbstractDecorator):
    """This decorator will reverse any string values returned from a
    Messenger's methods. Note that we only need to override those
    string methods here, since the parent handled tell_the_time().
    """

    def say_hello(self):
        msg = self._messenger.say_hello()
        return msg[::-1]

    def say_goodbye(self):
        msg = self._messenger.say_goodbye()
        return msg[::-1]

class UppercaseDecorator(AbstractDecorator):
    """This decorator will convert any string values returned from a
    Messenger's methods to uppercase.
    """

    def say_hello(self):
        msg = self._messenger.say_hello()
        return msg.upper()

    def say_goodbye(self):
        msg = self._messenger.say_goodbye()
        return msg.upper()

if __name__ == '__main__':

    basic_messenger = ConcreteMessenger()
    print('Standard Messenger output:')
    print(basic_messenger.say_hello())
    print(basic_messenger.tell_the_time())
    print(basic_messenger.say_goodbye())
    print()

    # Notice that we pass in basic_messenger, because we are decorating it.
    reverse_messenger = ReversingDecorator(basic_messenger)
    print('Output when decorated with ReversingDecorator:')
    print(reverse_messenger.say_hello())
    print(reverse_messenger.tell_the_time())
    print(reverse_messenger.say_goodbye())
    print()

    # Notice that we pass in basic_messenger, because we are decorating it.
    upper_messenger =  UppercaseDecorator(basic_messenger)
    print('Output when decorated with UppercaseDecorator:')
    print(upper_messenger.say_hello())
    print(upper_messenger.tell_the_time())
    print(upper_messenger.say_goodbye())
    print()


    print("Note that the original messenger didn't change:")
    print(basic_messenger.say_hello())
    print(basic_messenger.tell_the_time())
    print(basic_messenger.say_goodbye())
    print()

    # And now for something completely different.
    print('We can even stack the decorators:')
    double_decorated_messenger = ReversingDecorator(
        UppercaseDecorator(basic_messenger)
    )
    print(double_decorated_messenger.say_hello())
    print(double_decorated_messenger.tell_the_time())
    print(double_decorated_messenger.say_goodbye())
    print()
