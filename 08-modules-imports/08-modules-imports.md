## ID608
## Intermediate Application Development
---

## Session 8: Namespaces, Modules, and Imports

### Introduction
My name is Tom. In many parts of the world that is a very common name. So when we talk about “Tom”, who exactly do we mean?

  - In this room, I’m probably the only person named Tom.
  - I appear to be the only Tom Clark at OP, so on campus my “fully
qualified” name identifies me.
  - There are a lot of Tom Clarks in NZ, but if we say, “The Tom Clark at Otago Polytech,” we’re talking about me.

In the context of a running program, we have a similar problem.

```
import otagopolytech

tom = "A really cool guy"
def enclose():
    tom = "I guess he’s ok"
    def local():
        tom = "What a jerk"
        print(tom)
    print(tom)
    return local
enclose()
print(tom)
```

What gets printed?

---

### Namespaces

In our example, the name tom gets used over and over, but they don’t conflict because each one exists in a distinct namespace. In a running Python program several namespaces may exist at any one time.

When we use a name like tom, Python applies a set of rules for searching namespaces for that name.

### Local namespace

```
def local():
    tom = "What a jerk"
    print(tom)
```

The innermost occurrence of `tom` is in a local namespace. This version of `tom` is only meaningful in the context of executing this function.


### Enclosing namespace
```
def enclose():
    tom = "I guess he’s ok"
    def local():
        tom = "What a jerk"
        print(tom)
    print(tom)
    return local
```
The function `enclose()` defines an enclosing namespace. This version of `tom` is meaningful in the context of the function `enclose()` and it would also within the enclosed function `local()` if it were not masked by the local version of `tom`.

```
def enclose():
    tom = "I guess he’s ok"
    def local():
        # tom = "What a jerk"
        print(tom)
    print(tom)
    return local
```

### Global namespace

```
tom = "A really cool guy"
def enclose():
...
```
The first occurrence of `tom` is in a global namespace. This name is meaningful anywhere in the file. The imported module `otagopolytechnic` actually defines a seperate, distinct global namespace.

### Builtin namespace
```
import otagopolytech

tom = "A really cool guy"
def enclose():
    tom = "I guess he’s ok"
    def local():
        tom = "What a jerk"
        print(tom)
    print(tom)
    return local
enclose()
print(tom)
```

We didn't do amything to define the function `print()`, but clearly the function is defined. It is one of the names defined in the *builtin* namespace. This namespace is formed when a Python program starts executing and exists until the program exits.

### LEGB
When the Python interpreter looks for a name like tom, it searches the namespaces in the order
  1. Local
  2. Enclosing 
  3. Global
  4. Builtin

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `08-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `08-practical` directory.
  4. There are two Python files, `q1.py` and `q2.py`. Each one contains a programming problem to solve.
  5. We will discuss those two questions in about 15 minutes.
  6. The directory `q3` is a homework problem. The directions are in the file `main.py`

---

### Imports
Suppose I have two files

*mod.py*
```
num = 42
def foo():
    return ’bar’
```

*main.py*
```
import mod

print(mod.num)
baz = mod.foo()
```

`mod.py` defines a *module*. The import brings the name `mod` into main.py’s global namespace and we can access its attributes there.

We can also do this:

*mod.py*
```
num = 42
def foo():
    return ’bar’
```

*main.py*
```
from mod import num

print(num)
```
In this case we bring the name num into `main.py`’s namespace.

### Modules
Where does `import` find modules/packages?

When we use `import mod` the interpreter needs to find the module or package named `mod`. It
searches the following locations in order.

  1. `sys.modules` - a cache of loaded modules.
  2. The current working directory from which the program was invoked.
  3. Any directories listed in the `PYTHONPATH` environment variable.
  4. A list of installation-dependent directories. You can see these by inspecting sys.path.

 N.B.: These lists of locations can be modified at runtime, which is sometimes useful but also a security vulnerability if you are running untrusted code. 

### Packages
We can bundle multiple modules together in a directory, and we call this a *package*.

```
main.py
mypackage/
  |
  | mod1.py
  | mod2.py
```

The in `main.py` we can use

```
import mypackage.mod1
import mypackage.mod2
```

If `mypackage/` contains a file called `__init__.py`, anything in that file can be imported with just `import mypackage`.

```
main.py
mypackage/
  |
  | __init__.py
  | mod1.py
  | mod2.py
```

In `main.py` we can use.
```
import mypackage
import mypackage.mod1
import mypackage.mod2
```

---

### Further reading
  - https://realpython.com/python-namespaces-scope/
  - https://realpython.com/python-import/
  - https://realpython.com/python-modules-packages/

