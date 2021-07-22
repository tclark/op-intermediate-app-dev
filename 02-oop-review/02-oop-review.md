
## IN608
## Intermediate Application Development
---

## Session 2: OOP Review

Like other languages you have studied at OP, Python is an *object oriented* language. However, unlike other languages you have seen, it is *dynamically typed*. So most of the things we will review in this lab are likely to be familiar to you, albeit with some differences.

### Classes
Classes in Python are defined like this
```
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        return f'Meow, my name is {self.name}'
```

To instantiate an object of type `Cat`, we use

```
my_cat = Cat('Lola', 'Burmese')
```
And we can invoke the `meow()` method like this
```
print(my_cat.meow())
```

We might infer from this that `__init__()` is the constructor, but that's not strictly true. It's more correct to call in the initialiser. We'll look at this in more detail later in the semester. For now it's just important to know that any setup you want to accomplish when creating an object instance is generally done in its class's `__init__()` method.

---
### Sidebar: Functions and arguments
Python handles arguments in a pretty flexible manner.

**Positional arguments:** These work in the same way that arguments work in most languages. If we have a function
```
def add(x,y):
    return x + y
```
then when we call it with arguments like this
```
result = add(1, 2)
```
the value 1 is bound to `x` and 2 is bound to  `y` in the scope of the function `add()`. That's pretty clear, but how do we explain the methonds  in the `Cat` class above? For example, the `meow()` method seems to take one positional argument, `self`. But we call it like this: `my_cat.meow()`. In this case, the instance value `my_cat` is passed to the `meow()` method as the first positional argument and bound to `self`.

**Keyword arguments:** Python also lets us use what we call *keyword* arguments. Here's an example.
```
def cat(a='a', b='b'):
    return a + b
```
We can tell that `a` and `b` are keyword arguments because we've assigned them the default values "a" and "b" respecively. We can call the function in various ways, including
```
cat(a='Hello ', b='world')
cat(b='world', a='Hello')
cat(b='bcde')
```
Note that in the last example we don't even need to supply a value for the argument a, since it has a default value, "a". On the other hand, we must supply values for any and all positional arguments.

**Mixed arguments:** Finally, we can mix positional and keyword arguments in a single function definition. 
```
def mixed(x, y, z=0):
    return x + y + z
```

Typically we use this when some arguments must be provided by the caller and other arguments are optional and only need to be supplied to override the defaults. Note that in this case positional arguments must come before any keyword arguments when both defining and calling the function. 

---

### Classes: access
Let's look at our `Cat` class again.
```
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        return f'Meow, my name is {self.name}'
```
This class has two attributes, `name` and `breed` and one method, `meow()`. All three of these are public, since that's the only option in Python. There are no mechanisms to enforce access controls.  We can change a `Cat`'s name, for example.
```
my_cat = Cat('Lola', 'Burmese')
my_cat.name = 'Freya'
```
If we want a method or attribute to be treated as private, the convention is to prefix its name with an underscore, like this:
```
class Cat:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
```
We can still modify these attributes; the language doesn't stop us. The leading underscores just tell us that we *shouldn't*.

A slightly stronger form of this is to use two underscores.
```
class Cat:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
```
This sneakily changes the names  of the attributes to `_Cat__name` and `_Cat__breed`, but we can still access the attributes using this modified names. In practice, this form isn't often used.

### Classes: encapsulation
Suppose we start with the `Cat` class at the beginning of the lecture.
```
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```
Since the attributes are public we can access them directly.
```
print(my_cat.name)
my_cat.breed = 'DSH'
```
But then we decide we'd like to have setters/getters so that we
can control access more carefully. Maybe we want to be sure that we only assign recognised breeds to our cats' `breed` attributes. That's fine, but we also want to keep our class's interface consistent so that we don't break client code. Python lets us do that with *properties*. let's refactor the `Cat` class.
```
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self._breed = breed
    
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed): 
        if breed in RECOGNISED_BREEDS:
            self._breed = breed
        else:
            raise ValueError(f'{breed} is not recognised')        
```
We did two things here. First, we replaced `self.breed` with `self._breed`, a private attribute. Second, we defined a property setter and getter. To users of the class, the change is transparent.
```
print(my_cat.breed) # calls the property's getter
my_cat.breed = 'DSH' # calls the setter
```

---
### Classes: inheritance
Classes in Python can inherit from other classes.
```
class PurebredCat(Cat):
    def __init__(self, name, breed, breeder):
        super().__init__(name, breed)
        self.breeder = breeder
``` 
`PurebredCat` inherits from `Cat`, and we have overridden `Cat`s `__init__()` method. In the new `__init__()` method we use `super()` to call the original `_init__()` method from `Cat`, but that's not a requirement. It's simply useful in this case to avoid repeating the code already supplied by the parent class.

We have not overridden `Cat`'s `meow()` method, so when we call `meow()` on a `PurebredCat` it will just use the parent's method.
---
### Classes: polymorphism and duck typing
Suppose we have the following classes.
```
class Cat:
    def meow(self):
        return 'Meow, I am a cat.'


class HouseCat(Cat):
    def meow(self):
        return 'Meow, I am a house cat.'


def AlleyCat(Cat):
    def meow(self):
        return 'Meow, I am an alley cat.'


cats = [Cat(), HouseCat(), AlleyCat] 
for cat in cats:
    print(cat.meow())
```
This code works fine, because all the objects are of type `Cat` and all `Cat`s provide an approriate `meow()` method. Which versions of `meow()` is actually called will be resolved at run time. This is classical object-oriented polymorphism.

But on the other hand, consider this example.
```
class Cat:
    def meow(self):
        return 'Meow, I am a cat.'


class HouseCat:
    def meow(self):
        return 'Meow, I am a house cat.'


def AlleyCat:
    def meow(self):
        return 'Meow, I am an alley cat.'


cats = [Cat(), HouseCat(), AlleyCat] 
for cat in cats:
    print(cat.meow())
```
In this case, `Cat`, `HouseCat`, and `AlleyCat` are all distinct types. But the code functions identically because all three types provide `meow()` methods. Since Python is dynamically typed, it's not particularly important what type an object has as long as it has the necessary functionality. This is called *duck typing* and it's very common in Python.


--
### Programming activity
  1. Pull the course materials repo.
  2. Create a new branch, `02-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `02-lab` directory into your practicals repo's `02-practical subdirectory`.
  4. Follow the directions in the included README file. 