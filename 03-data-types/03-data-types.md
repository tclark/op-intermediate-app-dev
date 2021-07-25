## IN608
## Intermediate Application Development
---

## Session 3: Data Types and Variables

Last time we talked a bit about strong vs. weak and static vs. dynamic typing. I decided to fact check myself and see if what I said was accurate. It turns out that there really isn't a unversally agreed upon definition for these terms, so what I said was vacuously true. Just to be clear, here's what I meant:

  - Strong typing generally prevents you from treating values of one type as if they are values of other types. Weak typing allows this.
  - Static typing means that the types of values can be determined before run time (e.g., at compile time). Dynamic typing means that types can't be reliably determined until run time.

But others may use these terms differently.

---

### Core ideas
Python has most of the types with which you're already familiar. Its built in collection types are a bit more powerful and flexible than those seen in other languages, so we'll mostly talk about them. First, though, we need to talk about three core ideas:

  - Variables
  - Mutability vs. Immutablity
  - Equality vs. Identity
  
---

**Variables**
A Python variable is a reference, or pointer, to an object. When we type

`a = 4` 

the variable `a` is made to point to the object `4`. If we now type 

`a = 'cat'`

then `a` no longer points to `4`. Now it points to the string object `'cat'`. If we type

`b = a`

then `b` points to the same object that `a` points to: the value `'cat'`. `b` isn't connected to `a`, it's connected to the value that `a` points to at the time of `b`'s assignment. We can make changes to `a`, for example by typing 

`a = 4`

and now `a` points to the value `4` again. But `b` is unchanged; it continues to point to `'cat'`. Understanding the way that variables behave in a language will give you a better feel for what code does.

---

**Immutable values**
Many of the built in types in Python are *immutable*, i.e., their values can't be changed. Integers are an obvious example. If we type
```
a = 4
a = 5
```
we aren't changing the value of 5. We're just making the variable `a` point to a different value. Numeric types, booleans, and strings are immutable in Python. In general immutable types are good because they're easy to reason about.

**Mutable values**
Other types in Python are *mutable*, meaning that their values can change. An example of a mutable type is a `List`. (We'll talk about them in more detail later.) Here's an example:

`a = [1, 2, 3]`

`a` refers to a list that currently holds the values `1`, `2`, and `3`. We can add a value to this list.

`a.append(4)`

Now the list to which `a` refers holds  `1`, `2`, `3`, and `4`. But it's still the same list. Think of it like a bucket. We can add things to or remove things from the bucket, but it's still the same bucket. What's more, if we type 

`b = a`

then `a` and `b` point to the same list. If we change `a`

`a.append(5)`

then we change `b` as well, since it's the same list. On the other hand, if we reassign `b`

`b = True`

we don't change the value of `a`, we just made `b` refer to a different value.

---

**Equality vs. Identity**
There are two ways to compare values in Python.

`a == b` 

Describes whether `a` and `b` refer to the same value.

`a is b`

Describes whether a and b refer to the same object. Sometimes these two things are equivalent, but sometimes they are not. When comparing values it's important to know which comparison you want to make. Sometimes the results are very surprising.

```
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
a == b  # True
a is b  # False
```

This makes sense. `a` and `b` have equivalent values, but they are definitely different lists. On the other hand, 

```
a = 5
b = 5
a == b  # True
a is b  # True, ok I guess?
c = 5555
d = 5555
c == d # True, good.
c is d # True, wat?
```

It turns out that Python interpreters reuse small values sometimes, provided the values are immutable.

---

Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `03-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `03-practical` directory.
  4. There are multiple Python files, `q1.py - q7.py`. Each one contains a programming problem to solve.
  5. Work through `q1.py`, `q2.py`, and `q3.py`. We will discuss these in about 15 minutes.


---
### Collection types
Python has a powerful and flexible set of collection types built in. These types are sufficient to solve a large range of problems that might require custom classes in other languages that lack such collections. Before you write a new class or a complex algorithm, it's often worthwhile to stop and ask whether you can solve a problem with these built in types.

**Lists**
  - Ordered collection of values
  - Can be indexed by integer position
  - Mutable
  - Grow and shrink dynamically

```  
nums = [1, 2, 3, 4, 5] # Homogeneous
nums[2]  # 3
hetero = [1, 'C#', True, 2, 'Java'] # Heterogeneous
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Tuples**
  - Ordered collection of values
  - Can be indexed by integer position
  - Immutable, BUT can contain mutable values, e.g., lists

```  
nums = (1, 2, 3, 4, 5) # Homogeneous
nums[2]  # 3
hetero = (1, 'C#', True, 2, 'Java') # Heterogeneous
with_list = (1, [2, 3, 4]) # List's value can change!
```

**Sets**
  - Unordered collection of values
  - Doesn't contain duplicate values
  - Mutable

```
nums = {1, 2, 3, 4, 4} # Homogeneous
hetero = {1, 'C#', True, 2, 2} # Heterogeneous
print(nums) # {1, 2, 3, 4}
print(hetero) # {'C#', 1, 2}
```

Why doesn't True appear in the values when we print hetero?


**Dictionaries**
  - Unordered collection of key/value pairs
  - Mutable
  - Keys can be any immutable object

```  
ig_user_one = {'username': 'john_doe', 'active': False, 'followers': 150}
ig_user_two = {'username': 'jane_doe', 'active': True, 'followers': 500}
print(ig_user_one['username']) # john_doe
print(ig_user_two['followers']) # 500
```


**Strings**
  - Ordered collection of unicode character values
  - Can be indexed by integer position
  - Immutable
  - They print nicely

```  
st = 'I have a cat named Lola.'
st[5] # 'e'
```

Strings and other sequence types can also be *sliced*. We won't go into that here, but you should investigate this because you will find it useful this semester.

```
st = 'I have a cat named Lola.'
st[9:12]  # cat
```