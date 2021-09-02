## IN608
## Intermediate Application Development
---

## Session 14 :  Sequences

**Introduction**

Since we looked at iterables and iterators last time, it's pretty natural to move on and talk about sequences now. But first I have to point out something. Unlike iterators, there is no classical sequence pattern. That's because the authors of *GoF* where thinking in the context of languages where a sequence pattern wouldn't make sense. They basically had only one type of sequence: an array. And arrays are not nearly as feature-rich as collections like Python's list type. But today we don't have the same limitations, so we can talk about sequences, and we will do so today.

### Sequence types
like iterables, sequence types hold collections of objects. Basically all sequence types are also iterables, since it makes sense to access their elements one at a time. The critical difference is that sequence types must have an order to the elements. Iterables do not alwasy have an order. A Python set is an iterable, but it makes no sense to talk about the first item in a set because sets are not ordered. When we iterate over the elements of a set we don't know in what order we will get them. A list, on the other hand, is a sequence and it's elements are clearly ordered.

Examples of built-in sequences:
  - Lists
  - Tuples
  - Strings
Examples of built-in interable that are **not** sequences:
  - Sets
  - Dictionaries

  We'll mainly use strings as examples, since they are easy to visualise.

### Accessing sequence elements by index

The key thing that makes a sequence a sequence is that you can access its elements by integer *index*, where the index indicates an element's position in the sequence. We start at zero, of course. Suppose we have a string
```
cat = 'My cat is black.'
```

Then each character in the string has an index.
```
Index    Character
 0         M          
 1         y
 2        <space>
 3         c
 4         a
 5         t
 6        <space>
 7         i
 8         s
 9        <space>
 10        b
 11        l
 12        a
 13        c
 14        k
 15        .
 ```       

 and we can access any individual character by its index like this: `cat[3]`, which has the value `'c'`. If we try to access an element using an index outside of the sequence's range, e.g., `cat[42]` an `IndexError` exception is raised.  That's not surprising. It's a little surprising to learn that Python sequence elements can also be accessed by *negative* indices.

 ```
Index    Character
 -16       M          
 -15       y
 -14      <space>
 -13       c
 -12       a
 -11       t
 -10       <space>
 -9        i
 -8        s
 -7       <space>
 -6        b
 -5        l
 -4        a
 -3        c
 -2        k
 -1        .
 ```       
So `cat[-13]` has the value `'c'` since it's the same element as `cat[3]`.

### Accessing subsequences with slices

Accessing elements by integer index is pretty ordinary. But with Python we can also access elements with something called a *slice*. Here's an example to start.

```
print(cat[3:6:1])
```
The expression `3:6:1` is a slice. It basically says "start at the element at index 3 and step 1 element at a time up to, but not including the element at index 6." So the code above prints "cat". The basic form of a slice is `start:stop:step`. It's important to note, however, that each of the three parts has a default.

  - The default step is 1, so we can leave off the step value and say `cat[3:6]` and get the same result. Note we can also leave off the trailing `:` in this case too.
  - While we're at it, steps can be *negative* which means "step backwards". `cat[3:6:-1]` is `'tac'`.
  - The default start is 0, i.e. the start of the sequence. `cat[:6:1]` or `cat[:6]` is `'My cat`. Note that we can **never** omit the first `:` in a slice expression.
  - The default stop is the highest valid index, i.e. the end of the collection. `cat[3::1]` or `cat[3:]` is `'cat is black.'`

With the above in mind, what is `cat[::]`?

Three more important things: 
  1. When we apply a slice in a sequence, we get a *copy* of the selected values from the sequence. `cat[3:6]` is a completely different string from `cat`. It's not a view into the original string.
  2. When we obtain a slice of a sequence, we get back the same type as the original sequence. A slice from a string is a string. A slice from a list is a list. (This will be important for the homework.)
  3. With iteger indices, using an index out of range raise an exception. That's not true with slices. It just ignores the values that don't exist. `cat[72:112]` is just an empty string.


---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `14-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `14-practical` directory.
  4. There are two files, `q1.py` and `q2.py`. Work through `q1.py` now and do `a2.py` after reading the section below.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q4.py` after reading the section below.

---

### Implmenting sequences in classes.

Last time we saw that we could make our classes into iterables by implementing the required dunder methods. Shockingly, this is also true for sequences. The critical methods we must implement are `__len__()` and `__getitem__()`. But first some preliminaries.

When implementing a sequence class first we have to decide if the sequence is *mutable* or *immutable*. For example, a string is an *immutable* sequence. We can access its elements, but we can't change their values or remove them. A list is a mutable sequence. We can do those things with a list. Implementing a mutable sequence means we need to implement additional dunder methods, in particular, `__setitem__()` and `__delitem__()`. The standard library module `collections.abc` (https://docs.python.org/3/library/collections.abc.html) provides the abstract base classes `Sequence` and `MutableSequence` that serve as good guides, although you don't have to use them to implement a sequence. Also, those classes provide *abstract methods* and *mixin methods*. Recall that we **must** override abstract methods in concrete child classes. We don't have to override mixin methods. The base classes provide implmentations, but they may not be ideal in some cases.


Let's see how to do this by working through an example. The first, more common, and easier, case to consider is a class that stores values
in a field that is itself a sequence.

```
class Cattery(collections.abc.MutableSequence):

    def __init__(self, cats):
        # _cat_list is a list of cats
        self._cat_list = cats
```
Why are the cats ordered? Because some cats are better than others. 

Since we inherit from `collections.abc.MutableSequence` we must override the abstract methods.  The first one is easy.

```
    def __len__(self):
        return len(self._cat_list)
```

But the next one is the hardest.

```
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._cat_list[key]
        elif isinstance(key, slice):
            return Cattery(self._cat_list[key])
        else:
            raise TypeError('Sequence access requires an int or a slice')        
```

What's going on here? If we use `my_cattery[3]`, then `key` in `__getitem__()` is an int. We just return that value from the internal list.  If it's a slice, we can get a slice from the internal list. But remember that a slice needs to return an object of the same type as the original value. So, we take our slice from the internal list, use it to construct a new `Cattery` instance, and return the instance.

If this was an immutable sequence, we'd be done. But this is going to be a mutable sequence, so we need to add three more methods.

```
    def __setitem__(self, index, value):
        # handles cattery[4] = socks
        self._cat_list[index] = value

    def __delitem__(self, index):
        # removes the cat at position index
        del self._cat_list[index]    
    
    def insert(self, index, value):
        # inserts value at postion index, moving other elements down if necessary
        self._cat_list.insert(index, value):

```

Now our `Cattery` is a sequence, so we can do things like this:

```
my_cattery = Cattery(cats)

mittens = my_cattery[2]
my_cattery[6] = princess
bad_cats = my_cattery[7:11]
del my_cattery[4]  # Don't worry, she went to live on a farm in Southland.
```

All of this was pretty easy because we just had to pass off the hard work to the internal list, but this actually covers most of the real-world cases. If our classes are legitamate sequences, then we're probably using a sequence type in its internals. But what if we're not? (Spoilers). In that case you'll need some sort of logic, probably a loop, to get at the item with a given index. When dealing with slices you will have to pull apart the slice object (e.g. `[3:6:1]`) get at its values and then provide some logic to get at the values required for the slice.

