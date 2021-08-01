## IN608
## Intermediate Application Development
---

## Session 4: Operator Overloading and Dunder Methods

Let's add two integers, say 2 and 3. Integer addition is a function that takes two arguments and returns their sum We might expect to write it this way:
```
add(2, 3)
```
or, if we’re feeling particularly object oriented,
```
2.add(3)
```
But we don’t do that. We generally we write it this way:
```
2 + 3
```
because somebody did it like that in 1360 and people liked it. The “+” symbol in this expression is an operator.

Wow, that's handy!  The `+` operator notation is so handy that we use it in other places
```
> [3, 1, 4] + [22, 11]
[3, 1, 4, 22, 11]
```    
And it’s not just `+` that gets this treatment.
```
> 3 * 'cat'
'catcatcat'
```
What if we wanted to do this for our own classes?

---
### Dunder Methods
Every object in Python inherits some "dunder" methods, also commonly called "magic methods". We’ve already seen two of these, `__init__()` and `__str__()`. There are also other such methods that we can choose to implement.

It’s bad practice to define new dunder methods, and it won’t generally do what we want anyway. The interesting thing about them is that we almost never explicitly call dunder methods. They are automatically invoked by the interpreter in various contexts. Also, it’s possible to abuse dunder methods by implementing them in unexpected ways. Don’t do that.


---
### Operator Overloading

Suppose we define a class and would like to be able to add two objects of that class using `+`. This would be an example of **opertator overloading**.

```
class Bill:
    def __init__(self, items):
        self.line_items = items # a list of item objects

     def __add__(self, other):
          new_list = self.line_items + other.line_items
          return Bill(new_list)

b1 = Bill(some_items)
b2 = Bill(some_other_items)
b3 = b1 + b2
```

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `05-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `05-practical` directory.
  4. There are two Python files, `q1.py` and  `q2.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py`. We will discuss it in about 15 minutes.

---

### Other Dunder Methods
There are other handy dunder methods to implement that aren’t strictly used for operator overloading

### `__str__()` and `__repr__()`
We’ve already seen that we can use the `__str__()` method to control what happens when our object is passed as an argument to `print()`. The general idea is that `__str__()` should return a user-friendly string. `__repr__()` is similar, but it should return a programmer-friendly string. A good idea is to return a string that matches a call to the constructor method that returns the given object.

```
class Cat:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f’Cat("{self.name}")’
    
    c  = Cat("Larry")
```
If a class does not implment `__str__()`, then the `__repr__()` method is used in its place. It's good practice to always implement a `__repr__()` method.


### `__bool__()`
Often it's handy to be able to evaluate an object on a boolean context. For example, it's common to do this with strings or lists. We can support the same functionality in our classes with the `__bool__()` method.

```
class Flock:
    def __init__(self, sheep):
        self.sheep = sheep

    def __bool__(self):
        return len(self.sheep) > 0

 fl = Flock(some_sheep)
 if fl:
     print('There are sheep in this flock.')
 else:
     print('There are no sheep.')
```

Note the we should only implement `__bool__()` if there is a reasonable boolean interpretation of the objects in question.

### `__len__()`
We have seen that we can call `len()` on a list or string to get its length. If we want to make this work for our own classes, we implement `__len__()`.

```
class Bill:
    def __init__(self, items):
        self.line_items = items # a list of item objects
        
    def __len__(self):
        return len(self.line_items)


bill = Bill(items)
print(f'There are {len(bill)} items in the bill.')
```

### Some Conclusions
Operator overloading is somewhat controversial. Not all languages support it and some programmers think it’s a bad idea. I find it to be useful.

Implementing appropriate dunder methods is a very “Pythonic” way to do things. Well implemented dunder methods can make your classes easy and productive to use.

Some refs:
  https://dbader.org/blog/python-dunder-methods 
  https://docs.python.org/3/reference/datamodel.html#special-method-names

