## IN608
## Intermediate Application Development
---

## Session 7: Exceptions and Exception Handling

### The Problem
You may have noticed that things don’t always go quite to plan when programming.
```
def get_item(i):
    stuff = [1, 2, 3, 4, 5]
    return stuff[i]
```
What could possibly go wrong?  No, really, what could go wrong?
  - We could call `get_item()` with an index that is out of range.
  - We could call `get_item()` With an argument of the wrong type.

### One solution:
We could guard against these problems by adding some extra checks before we try to retrieve a list item.
```
def get_item(i):
    stuff = [1, 2, 3, 4, 5]
    if type(i) is int and 0 <= i < len(stuff):
        return stuff[i]
    else:
        return None
```
This is ok, but now we’ve devoted a good chunk of our login to handling cases that we don’t expect to happen - to *exceptional* cases.

### Exceptions
Many programming languages deal with this by providing *Exceptions*, a sort of built in event and event handling to deal with these error cases.
```
def get_item(i):
    stuff = [1, 2, 3, 4, 5]
    return stuff[i]  # Exceptions can be raised here.
```
  - If the argument `i` is not an integer, A `TypeError` is raised.
  - If `i` is an integer outside the range of valid indices for our list, an `IndexError` is raised.

### Exception Handling
Basic exception handling is done with a `try/except` block.
```
def get_item(i):
    stuff = [1, 2, 3, 4, 5]
    try:
        return stuff[i]
    except IndexError:
        return None
```
 Notice that we’re not handling the possible `TypeError`. If we don’t have a plan for how to recover from an exception, it's better to let it propagate.       

 We can access the Exception object created when the error occured. We also have the opportunity to take some action in the case of an exception and then re-raise it to pass it up the stack.

 ```
 def get_item(i):
    stuff = [1, 2, 3, 4, 5]
    try:
        return stuff[i]
    except IndexError:
        return None
    except TypeError as e:
        logger.error(e)
        raise e
```
### Full `try/except` Structure
```
try:
    ...code...
except ErrorType:
    ...handle ErrorType...
except AnotherError as e:
    ...handle AnotherError with access to exception
else:
    ...executed if no exceptions are raised...
finally:
    ...aways executed after all other blocks complete...
```

---

### Programming Activity
### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `07-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `07-practical` directory.
  4. There are several Python files, `q1.py` - `q5.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py` through`q4.py`. We will discuss it in about 15 minutes.
  6. `q5.py` is left as homework.

---

### User-Eefined Exceptions
  - It’s generally preferable to use a built in exception when it suits the error. 
  - Exceptions are just special classes.
  - Exception names should end in `Error`.
  - A user-defined exception must derive from Exception or one of its subclasses.
  - You can do just about anything, but in general they are simple classes that hold information about the error.
  - User-defined exceptions must be explicitly raised in application code.

  ```
class IN608Error(Exception):
    pass

class InputError(IN608Error):
    def __init__(self, badinput, message):
        self.input = badinput
        self.message = message
    
    def __str__(self):
        return f'InputError: {self.message}'
```

### Conclusions
  - Exceptions let us extract error handling from core logic.
  - They are best used for handling things you don’t expect to happen.
  - You don’t have to handle every exception. It’s generally bad practice to try.

Good reasons to handle exceptions include
  - It’s possible to recover from the error and continue execution.
  - The error is unrecoverable, but there are important actions to complete before halting execution.

  References:
    - https://docs.python.org/3/library/exceptions.html
    - https://realpython.com/python-exceptions/
        
