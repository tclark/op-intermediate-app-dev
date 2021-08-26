## IN608
## Intermediate Application Development
---

## Session 12:  The Decorator Pattern and Python Decorators

### Introduction
In this session we will see the classic *Decorator* pattern from GoF. We also also look that the Python language feature with the same name and compare and contrast them. Even though they share the same name and general purpose, and I would argue that they are closely connected, there are important differences between the Decorator pattern and Python decorators. This is a challenging topic, both in its complexity and in the difficulty in coding it. Take the time to work through the problems and understand what is going on. Python decorators are a widely used feature in the language. In my one work I deal with them basically every day.

Here's an example: When a player of one of Runaway’s games is having trouble and raises a support issue, we enable extra logging of that player’s API calls. Then, at runtime we modify the behaviour of API calls just for that player, to log the details of the calls.

**Decorator Intent**

"Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality"  (*GoF*)

The typical way to extend or modify a class’s behaviour is to subclass it. But this modification is locked in at compile time. Sometimes we want to wait until runtime to apply the modification, perhaps to apply it selectively. The Decorator pattern allows us to do this.

Suppose we have a class `Basic`. We want to modify the behaviour of an instance of `Basic` at runtime. Here is our plan:
  - Construct a standard instance of a class. Let's call it `basic_instance`.
  - Define another class that will "decorate" `basic_instance`. Basically, it wraps `basic_instance` and keeps it as an attribute.
  - This decorator instance presents the same interface as basic, making it a replacement.
  - However, the decorator can take over some of `basic_instance`’s methods, while also leaving some unchanged.
  - We can also recover the undecorated `basic_instance`. It is unchanged by the process.
  - Also, we can selectively choose whether to apply the decorator, or choose from a range of decorators to apply.

Class Structuture
```
                     ------------------- 
                    | AbstractComponent |
                    |  + operation()    |
                     -------------------  
                             ^
                             |       
                  -----------------------
                 |                       |
         -------------------     ------------------- 
        | ConcreteComponent |   | AbstractDecorator |
        |  + operation()    |   |  - component      |
        |                   |   |  + operation()    |
         -------------------     -------------------
                                         ^
                                         |
                                 -------------------
                                | ConcreteDecorator |
                                |  - component      |
                                |  + operation()    |
                                 -------------------
 ```                                
Here's what this tells us: Everything here inherits from `Component`, so the Liskov Substitution Principle tells us that anytime we need a `Component`, we can use one of its child classes. The important property of a `Component` is that it provides teh method `operation()`.The important point of difference is that `Decorator` (and its child classes) hold onto another `Component` instance as an attribute and can modify its behaviour.



### Implementing the pattern
Let's implement an example. We are going to implement a Messenger class that produces some messages. Then we'll create a Decorator class that can modify a messenger class and change its behaviour.

First, we need a base class, which has the role of `Component` in the diagram above.
```
from abc import ABC, abstractmethod

class AbstractMessenger(ABC):
    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass

    @abstractmethod
    def tell_the_time(self):
        pass
```

This demonstrates how we can make an *abstract base class* in Python.  We can't instantiate this. It shows three methods that concrete child classes must implement. So now let's make a concrete child class.

```
import datetime

class ConcreteMessenger(AbstractMessenger):
    def say_hello(self):
        return 'Hello'

    def say_goodbye(self):
        return 'Goodbye'

    def tell_the_time(self):
        return datetime.now()
```

Notice that it implements all of the abstract methods of the parent. We can create instances of `ConcreteMessenger`.

Now let's make decorators. We'll start with another abstract base class for future decorators.

```
class AbstractDecorator(AbstractMessenger):
    def __init__(self, messenger):
        self._messenger = messenger

    def tell_the_time(self):       
        return self._messenger.tell_the_time()
```

This class tells us three things:
  1. When we create a Decorator, we pass in an instance of a Messenger. This is the instance that we are decorating.
  2. We implement `tell_the_time()` and just return the result given by our decorated instance.
  3. We don't do anything with `say_hello()` or `say_goodbye()`. We leave that for our child classes to sort out.

Ok, let's make our concrete Decorator.

```
class UppercaseDecorator(AbstractDecorator):

    def say_hello(self):
        msg = self._messenger.say_hello()
        return msg.upper()

    def say_goodbye(self):
        msg = self._messenger.say_goodbye()
        return msg
 ```

 When we use an `UppercaseDecorator` to decorate a `ConcreteMessenger`, we take the results from `say_hello()` and `say_goodbye()` and convert them to upper case before returning them.  

```           
basic_messenger = ConcreteMessenger()
print(basic_messenger.say_hello()) # prints ’Hello’

upper_messenger = UppercaseDecorator(basic_messenger)
print(upper_messenger.say_hello()) # prints ’HELLO’
```

Notice that we didn't change `basic_messenger`. We made a new. decorated version, `upper_messenger`.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `12-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `12-practical` directory.
  4. There are two Python files, `q1.py` and `q2.py`. Each one contains a programming problem to solve.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q3.py` and `q4.py` after reading the section below.

---

### Python decorators

Python has a core language feature called a decorator. You’ve seen them already.

```
@abstractmethod  # There's one!
def say_hello(self):
    pass
```

A lot of literature on the topic will go out of its way to point out that Python decorators are not the same thing as the Decorator pattern. Except they kind of are. I mean, they’re not... but sometimes they are.

**Decorating functions**

In practice, Python decorators are usually applied to functions rather than clases, although we definitely can decorate classes.

```
@abstractmethod
def say_hello(self):
    pass
```

There are many decorators built into the language or provided in the standard library. We’ve already seen some like `@property` and `@classmethod`. The decorator `@abstractmethod` modifies the behaviour of the function `say_hello()`. This is one big point of difference. This classic Decorator pattern modifies objects, and through them can modify their methods. This is because the authors of GoF were working with a language that did not let them easily modify functions.


### Implementing decorators

A decorator is just a function that takes another function as an argument and returns a modified version of that function. It generally "wraps" its decorated function.

```
import functools

def shouty(wrapped_fn):
    @functools.wraps(wrapped_fn) 
    def wrapper(*args, **kwargs):  # *args, **kwargs lets us capture the arguments to our decorated function
        msg = wrapped_fn(*args, **kwargs)  # call the decorated function, get its result
        return msg.upper()  # return a modified result
    return wrapper  # return the modified function

```

We could use shouty to modify a function like this:

```
def hello():
    return 'hello'

hello = shouty(hello)
```

But in Python there's a shorter way to do this:

```
@shouty
def hello():
    return 'hello'
```


### Decorators with arguments
Warning: This next bit will do your head in the first couple of times you look at it. There's no avoiding it. Sometimes you just have to do the mahi.

Above we defined `shouty()`, a function that takes a function and returns a modified version of it. Using it is a little different than the classic Decorator patterns since the decorating effect is locked in before runtime. But there is a way to get the runtime behaviour we want.

  1. We write a function that takes some arguments and returns a new function.
  2. The function we return will na a function like `shouty()` - a function that takes in a function as an argument and returns a modified version of it.

 Here's an example (deep breath):

 ```
 def shouty_or_not(choice):  # We will take a boolean argument
    def maybe(wrapped_fn):
        @functools.wraps(wrapped_fn)
        def wrapper(*args, **kwargs):   # this function is like shouty(), above
            msg = wrapped_fn(*args, **kwargs)
                if choice:
                    return msg.upper()
                else:
                    return msg
        return wrapper
    return maybe
```

Here's how we use it:

```
@shouty_or_not(True)
def hello():
    return 'hello'

@shouty_or_not(False)
def goodbye()
    return 'goodbye'
```

Our decorator will transform the output of `hello()` into uppercase, but it leaves the output of `goodbye()` unchanged.

### Class decorators
*Real Python* has a nice example of a class decorator that make a class into a Singleton. It's better than what I would have written, so I'll just give you the link.

https://realpython.com/primer-on-python-decorators/#creating-singletons

### Conclusions

Recall the intent of the Decorator pattern:

"Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality"

  - Python decorators have several uses, some of which don’t satisfy this intent.
  - They also have uses that **look** very different in their implementation than the textbook pattern, but nonetheless do satify the intent.
   - Regardless of which type, Python decorators are handy and widely used.
