## IN608
## Intermediate Application Development
---

## Session 14 :  The Observer Pattern

### Introduction

Most of the games we make at my studio are intended to be played on devices with an active Internet connection. Sometimes, however, we'd like players to be able to conitue playing when their connectivity is briefly interrupted. For this to work, various parts of the games need to know when the device loses connectivity. There's one class, the one that handles communication with remote servers, that knows when this happens. So the situation is that one class knows something, and many others classes need to get that information.

There is a design pattern that addresses this: the **Observer** (or Subject-Observer) pattern. In our example, the server communications class is the *subject*. It monitors Internet connectivity. Any other class that needs to know about about connectivity registers itself with the subject as an *observer*. Whenever the subject's state changes, it notifies all of its registered observers.

"Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically." (*GoF*)

So in this one-to-many relationship, there is one subject that notifies its many observers whenever its state changes.

This a really useful pattern and it's not hard to think of examples of these. For example. imagine a comment thread that need to notify any users who are following it. The implementation is pretty straightforward. Let's look at how we code it up.

---
### Inplementation

Here's what a `Subject` class looks like. This is the class that the observers want to observe.

```
class Subject:

    def __init__(self):
        self._observers = set()

    def register(self, observer):
        self._observers.add(observer)

    def unregister(self, observer):
        self._observers.discard(observer)

    def notify(self):
        for o in self._observers:
            o.update(self)
```
Any class that needs to observe this subjust calls `register()`, and can stop observing by calling `unregister()`. An observer must supply an `update()` method. Whenever something interesting happens to the subject, `notify()` is called and the subject updates all of its observers. The subject passes itself to the observers so that they can get whatever they need from the subject.  Sometimes, intead of passing the entire subject instance, the subject can just send the relevant bit of data to its observers.

There's not much to say about the `Observer`. It just needs to have an `update()` method.

```
class Observer:

    def update(self, subject):
        pass
```        


---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `15-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `15-practical` directory.
  4. There are two files, `q1.py` and `q2.py`. Work through them now.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q3.py` and `q4.py` after reading the section below.

---

### A Pythonic Refinement

As we saw, there's not much required of observers except that they provide an `update()` method. But since Python methods are first
class values, we don't even need need to require that. 

```
class Subject:

    def __init__(self):
        self._observers = {}  # dictionary

    def register(self observer, update_method):
        self._observers[observer] = update_method

    def unregister(self. observer):
        try:
            del(self._observers[observer])
        except KeyError:
            # We don't seem to have this observer. No worries
            pass
    
    def notify(self):
        for update in self._observers.values():
            update(self)
```

So now the observer doesn't have to have a method called `update()`. When the observer registers with the subject, it just needs to include an argument telling the subject what method should be called when it needs to be updated.

---
### Publisher-Subscriber Pattern
The Observer pattern is a one-to-many structure: one subject to many observers. There is a many-to-many variation that is usually called Publisher-Subsciber pattern.  In this pattern we have many subjects. Let's call them `Authors`.  We still have many observers that we call `Subscribers`. But to handle the connection between these, we need another object that we call a `Publisher`.

```

  ---------                                ------------
 | Author  |---                        ---| Subscriber |
  ---------    |     -----------      |    ------------
               |--->| Publisher |<----|
  ---------    |     -----------      |    ------------
 | Author  |---                        ---| Subscriber |
  ---------                                ------------
```

In this pattern, subscribers register with the publisher to get updates.  Authors also register with the publisher so that it can send it it updates. Publishers get updates from the authors and forward the information to subscribers. The publisher may also implement some additional logic to manage which subscribers get notified in certain conditions.

