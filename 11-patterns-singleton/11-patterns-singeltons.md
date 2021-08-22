## IN608
## Intermediate Application Development
---

## Session 11:  Design Patterrns and the Singleton

### Introduction

Last time we talked about the development of a body of knowledge around Object Oriented Design that included SOLID Principles.
Another major part of that project is the idea of Design Patterns. The principal reference on that topic is the 1995 book *Design Patterns: elements of reusable object-oriented software* by Gamma, et al. (Typically known of Gang of Four or GoF). The book describes 23 patterns.

A design pattern is not code. It’s a description of how code (typically a class or group of classes) should function. It describes a broadly useful approach to solving a common problem. Patterns are generally language-independent, although their implementations are not. They are typically language paradigm-dependent, so that OO patterns might not apply to other language types. A lot of the "classic patterns" came from C++, and they reflect the nature of that language.

The primary test of the utility of a particular design pattern is that it works. It solves the problem it’s intended to solve. When you’re confronted by a problem that is probably pretty common, look to see if there is a well known pattern that solves it. 
The primary test of the utility of a particular design pattern is that it works. It solves the problem it’s intended to solve. When you’re confronted by a problem that is probably pretty common, look to see if there is a well known pattern that solves it. Conversely, it’s good to know about common patterns so that you recognise common problems when you see them. Using a well-known pattern also helps other programmers understood what you are doing with your code.

With that said, there are critisms of design patterns. In particular,
  - Design patterns merely point out shortcomings in particular languages.
  - Patterns lead to needless complexity in software design.

The first point isn't much of a criticsm in my opinion. All programming languages have shortcomings and well-understood ways of working around them are good things. Moreover, a widely used pattern could point out a shortcoming that should be addressed in future versions of a language, or could server as a cue to designers of new languages. 

The second point is valid. I have seen code in which the developers used design patterns where they were unecessary or a poor fit because they regarded their use as some sort of best practise. But that goes against the intent of the patterns and really, against the intent of software design at all. The key is to be familiar enough with design patterns and software design to make deliberate and well-reasoned decision about how to write good quality code.

With that said, we're going to consider some well known design patterns over the next few weeks for two reasons. First, the patterns themselves have utility. Second, because working with these patterns gives us opportunities to think about and experiment with software design. We'll start by looking at the *Singleton* pattern today.

---
### The Singleton Patttern
"Ensure a class only has one instance and provide a global point of access to it" (*GoF*)

The description above is pretty clear and helpful, which can't be said of all the descriptions in *GoF*. Both points are important:
  - We only want to have one instance of a singleton object.
  - We want to be able te access this object easily anywhere in our code.

In Python, `None` is a singleton.

Typically we implement a singleton by implementing the class' constructor so that it always returns int eh same instance.  The authors of *GoF* didn't do it that way, becuase they were working with a version of C++ that made this impossible. Instead, they took the following approach:

```
class SoloGoF:
    _instance = None  # This is a class variable
    
    def __init__(self):
        raise RuntimeError(’Use instance() instead.’)
        
    @classmethod
    def instance(cls):
        if not cls._instance:
            # We haven't created one of these yet, so do it now.
            cls._instance = cls.__new__(cls)
            # extra initialisation can happen here
        # Either we're returning the object we just created, or one that we created
        # earlier and saved in _instance. But we'll always return the same instance of this
        # oject, now matter what.    
        return cls._instance
        
        
solo = SoloGoF.instance()
```
There's a lot going on here. Let's hit the key points.

`_instance` is a *class variable*. This means that every instance of this class will share the exact same value.

We don't want people using the ordinary constructor, so we have `__init__()` raise an exception to prevent people from doing so. We want them to use `instance()` instead.

`instance()` is a *class method*. Usually we use *instance methods* by mmaking an instance of a class, say `inst` and calling its methods like this: `inst.method_name()`. With a class method we don't need an instance. We call it with its class name, like this: `SoloGoF.instance()`. In the definition of the class method we use the local variable `cls` instead of `self`. And note that `cls` refers to the class itself.

The end result of all this is that any tiime we need to get at the `SoloGoF` object we can just call `SoloGFoF.instance()` and we always get the exact same instance.

---

Remeber that I said that the *GoF* authors were working with a language that didn't let them implement a constructor that did what they wanted, so they had to use the special `instance()` methos above.  In Python we don;t have that limitation, so we can writs a more Pythonic version like this:

```
class SoloPy:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SoloPy, cls).__new__(cls)
            # extra initialisation can happen here
        return cls._instance


solo = SoloPy()
```
This isn't much different than the first version, except we didn't need to write a special `instance()` method. There are two interesting things to notice, however. 

From the definition of `__new__()`, it looks like a class methos, but it lacks the `@classmethos` decorator. That's because `__new__()` is always a class method, so it doesn't need the decorator.

Recall that I said that `__init__()` is not a constructor, even though we seem to treat it like one. In fact, `__new__()` is the constructor. We almost never override it because there rarely a reason to do so. In fact, notice that we call `SoloPy`'s super class constructor explicitly so that we can get its default behaviour.

The tl;dr: of all this is that we can call `SoloPy()` to get this object any time we need it and we always get the same instance back. Take a minute to notice that we have met both of our goals: We only make one instance of `SoloPy`, and we can get at it anywhere in our code just by calling `SoloPy()`.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `11-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `11-practical` directory.
  4. There are two Python files, `q1.py` and `q2.py`. Each one contains a programming problem to solve.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problem in `q3.py` after reading the section below.


---

### Criticisms of the Singleton

If you Google for "singleton antipattern" you will get many results.

**"It's too complicated. If you only need one instance, then just make only one instance."**

This is fair. Earlier I said one problem with patterns was that sometime programmers use them without thinking about whether they need to do so. If your problem is easily soled by "hust making one" instance, then you don't need a singleton.

**Singletons are inflexible. What if you really need two?**

Again, if you might need more than one, don't use singletons. In fact, you should only use them when  it's really important to only create one instance.

**Singeltons are thinly diguised globals.**

The problem with globals is that they are these values flying around in your code that aren't well controlled. The same problem can arise with singeltons. However, with a singelon object you can use things like encapsualtion to excersice some control over how the object is used.

**It's diffeicult to test code with singeltonss because you can't control their construction.**

This is a valid and important criticism. It's best to use singeltons in ways that are fairly simple and easy to test. When we do test with singletons, we need to be sure that we can reiably predict their states when testing.

---

### Singelton using modules

The singleton implementations above are interesting as examples of how we can slove this problem, but the truth is that neither are examples of how I would implement a singleton in Python. There's a way that is simpler and that address some of the criticisms.

Recently we looked at Python modules. Recall that we can import a module's contents into our namespaces easily, and also that a modfule's code is only excuted **one time** when it is first imported. Subsequent imports used the cached result. We can exploit this to make a singleton

File: *solomod.py*:
```
 class _SoloMod:
    # The leading underscore means that this class is private to 
    # the module and should not be imported.
    def __init__(self):
        # do some init stuff, idk
        pass
      
# This code below is only excuted one time when the module is 
# first imported, so it gives us one instance to use.      
soloinstance = _SoloMod()
```

Then in other code we can just use `from solomod import soloinstance` and we get one consistent instance to use.  At the same time, `_SoloMod` is just a plain vanilla class and we can test it like any other class.


