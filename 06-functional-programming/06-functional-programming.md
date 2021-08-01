## IN608
## Intermediate Application Development
---

## Session 6: Functional Programming

Most of us are primarily familiar with object-oriented programming. It’s principal abstractions are around classes and objects. Objects are frequently used to maintain state. In this paper we are considering object-oriented programming almost exclusively. Python is an object-oriented language.

There are completely different types of programming and programming languages. One that is used today is *functional programming*. In functional programming the principal abstraction is the concept of functions, and strictly defined ones at that. Examples of functional programming languages include Lisp, Haskell, and Javascript.
Python does support some functional programming features.

---

### Key Idea: Pure Functions

A pure function has two properties.
  1. It always returns the same result when given the same arguments;
  2. It has no side effects.

Here is an example of a pure function.
```
    def square(x):
        return x * x
```

Functional programming relies on pure functions. Pure functions are relatively easy to reason about and to test.

**Impure Functions**

In contrast, this function is not pure:

`random.randint(0, 100)`

Given the same arguments (0, 100) it will not always return the same result.

Neither is this one

```
l = [1, 2, 3]
l.pop()
```

Besides returning the last item on the list, it also changes the list by removing the last item. This is a side effect.

---

### Key Idea: First Class Functions

Functions in Python are first-class values.

  - We can assign a function’s value to a variable.
  - Functions can be passed as arguments to other functions. 
  - Functions can be returned from other functions.

First class functions are not required for functional programming, but they make it easier. Also, in some languages we can do some of the things on this list even though functions are not first class values in those languages. But with first class functions these things are easier and are done more routinely.

Some examples:
```
def double(x):
    return x * 2
      
times_two = double # notice the lack of brackets
print(times_two(2)) 

def apply_twice(fn, arg):
    return fn(arg), fn(arg)
      
apply_twice(double, 2)  # returns 4, 4
      
def make_multiplier(factor):
    def mult(x):
        return x * factor
    return mult

times_two = make_multiplier(2)
```

**Sidebar: Closures**

Hey, wait.

```
def make_multiplier(factor):
    def mult(x):
        return x * factor
    return mult
```

Notice how the inner function `mult()` uses the local variable `factor` that goes out of scope when the function `make_multiplier()` exits? The function encloses its lexical scope at the time it is defined. That is, it caputures and retains values that are in scope at the time the function is defined. We call this a closure.

---

### Another Idea: Lambdas

Sometimes we need a small function in a very specific context. The following are equivalent
```
def double(x):
    return x * 2
      
double = lambda x: x * 2    Note the lack of "return".
```

Often we use lambdas when we need a function as an argument to another function, like this

`foo(lambda x: x * 6, [2, 7, ’cat’])`

Another name for lambda is anonymous function.

N.B.: In Python lambdas are limited to only one expression.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `056practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `05-practical` directory.
  4. There are several Python files, `q1.py` - `q10.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py`, `q2.py`, and `q3.py`. We will discuss it in about 20 minutes.

---

### Map
`map(function, iterable) -> iterator`

`map()` returns an iterator which applies function to elements of `iterable`, yielding the results. Basically, we can apply it to a list and get back a new list where the values come from applying a function to each element in the original list.

```
nums = [1, 2, 3, 4, 5]
cubes = map(lambda x: x ** 3, nums)
print(cubes)  # [1, 8, 27, 64, 125]
```

### Filter
`filter(function, iterable) -> iterator`

`filter()` returns iterator which yields elements of iterable for which `function` returns `True`. So, we can pass in a boolean function and a list. `filter()` will apply the function to each value in the list and give back a new list containing only the values for which the function returned `True`.

```
def is_odd(num):
    return x % 2 == 1
      
nums = [1, 2, 3, 4, 5]
odds = filter(is_odd, nums)
print(odds) # [1, 3, 5]
```

### Reduce
`reduce(function, iterable) -> value`

`reduce()` applies a function of two arguments cumulatively to elements of iterable from left to right, reducing the iterable to a single value. It's found in the `functools` module.

```
from functools import reduce
      
def add(x, y):
    return x + y
      
nums = [1, 2, 3, 4, 5]
sum_nums = reduce(add, nums)
print(sum_nums) # 15
```

### List (and other) Comprehensions
The functionality of `map()` and `filter()` are combined in a *list comprehension*. This is why it’s somewhat rare to see map and filter in Python code.

```
string = ’123 Hi 456’
nums = [int(s) for s in string if s.isdigit()]
print(nums)  # [1, 2, 3, 4, 5, 6]
```

This is equivalent to 

```
string = ’123 Hi 456’
nums = []
for s in string:
    if s.isdigit():
        nums.append(int(s))
```

There are also set comprehensions and dictionary comprehensions that work in similar ways.

### Partial

`partial(function, *args) -> partial object`

`partial()` returns a function-like object (basically a function). This new function behaves like the original function with *args supplied to it. It is imported from the `functools` module.

```
from functools import partial

def add(x, y):
    return x + y
      
add_two = partial(add, 2) # add_two is like add(2, x)
add_two(3)  # returns 5
```
