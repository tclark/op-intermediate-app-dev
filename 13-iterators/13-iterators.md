## IN608
## Intermediate Application Development
---

## Session 13 :  The Iterator Pattern

### Introduction
In Python we do this all the time:

```
for thing in aggregate:
    do_stuff_with(thing)
```

Which leads to two questions.
  1. What kind of object is `aggregate`, anyway?
  2. How does all this work, anyway?

Objects like `aggregate` that can be used in loops like this are called *interables*. This means that they are capable of supplying *iterators*. In other words, they implement the **Interator Pattern**. 

"Provide a way to access the elements of an aggregate object sequentially without exposing its underlying implementation." (*GoF*)

This pattern is so fundamental that it is supported in the core Python language. Many common objects implement Iterator, and it is easy to make your own objects that support it too. Incidetally, while last time we havde to discuss the differences between Python decorators and the Decotrator Pattern, in this case it turns out the Python implentation and the classic pattern line up closely.

Examples of common interables include
  - Lists
  - Dictionaries
  - Sets
  - Files

---

### Iterators in practice

Here's a concrete example:

```
ls=[1,2,3] #lsisanIterable
itr = iter(ls)   # itr is a list Iterator 
print(next(itr)) # prints 1
print(next(itr)) # prints 2
print(next(itr)) # prints 3
print(next(itr)) # raises a StopIteration exception
```

What's going on here?
  1. A list is an example of an *iterable*.
  2. Calling `iter()` on the list causes it to produce an *iterator*
  3. Once we have the iterator, we can call `next()` on it repeatedly and it gives us one value from the aggregate each time.
  4. If we call `next()` on an iterator that has yielded all its values, it raises a `StopIteration` exception.

The reason this code is unfamiliar is that we usually accomplsh this with a loop like this:

```
ls = [1, 2, 3]
for i in ls:
    print(i)
```

Perhaps the conection is more clear when we look at the following equivalent loop"

```
itr = iter(ls)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
```        

So in other words, when we loop over an iterable, we start by obtaining am instance of its iterator. Them we call `next()` on the iterator until it raises a `StopIteration` exception, and then we exit the loop.

**Why a seperate iterator?**

At this point it might seem odd that the **iteraable** and the **interator** are distinct objects. There's a good reason for this. Suppose we have a list and we are looping over it in two different threads. It's important that each thread has its own iterator instances so that iterations within one loop don't effect iterations in the other. But there are exceptions to this. For example, a `File` object is its own iterator. This is because we expect to be able to read from file, perhaps in a loop, then stop. Later when we resume reading from the file we expect to pick up frm where we left off in the file. So keep in mind thaat usually an iterable produces distinct iterators, but sometimee we have iterables that are their own iterators - essentially they return themselves when asked for an iterator - when we want different behaviour.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `13-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `12-practical` directory.
  4. There are three Python files, `q1.py`, `q2.py`, and `q3.py`. Each one contains a programming problem to solve.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q4.py` after reading the section below.

---

### Making our classes interables


We make a class iterable by implementing the `__iter__()` method. It must return an Iterator.

```
class Cattery:

    def __init__(self, cats):
        self._cats = set(cats)

    def __iter__(self):
        return iter(self._cats)
```

In the case above we didn't have to do much work. That's because the private attribute `_cats` is a `set`. These are iterables themselves, so when we call `iter(self._cats)` we just get the iterator provided by the set. But we don't always have it that easy. Sometime we need to implement our own iterator class.  To make a class in iterator, we need to implement a suitable `__next__()` method.

```
class SkippingIterator:

    def __init__(self, list_):
        self._list = list_
        self._next_index = 0

    def __next__(self):
        try:
            result = self._list[self._next_index]
            self._next_index += 2
            return result
        except IndexError:
            # We've run out of list. We need to raise a
            # StopIteration exception to satisfy the requirements
            # of an Iterator
            raise StopIteration        
```

So now an iterable could produce a `SkippingIterator`.

```
class Skipper:

    def __init__(self, list_):
        self._list = list(items)

    def __iter__(self):
        return SkippingIterator(self._list)
```

Notice how our interable and iterator are tightly coupled. That's typical of this pattern.

Now we can use our iterable/iterator like this:

```
skippy = Skipper(range(6))
for value in skippy:
    print(value)
```
What does this print?    



