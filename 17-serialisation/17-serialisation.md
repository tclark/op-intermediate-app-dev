## IN608
## Intermediate Application Development

## Session 17 :  Serialisation

### Introduction
Sure objects are great, but sometimes we need to move them around. Maybe we want to save an object to a file so we can read it in during a later session. Perhaps we want to send the object over a network to a remote process.

To do this, we need to convert the object into a serial format, like a sequence of bytes or a string. We also need a way to convert the object from its serial format into a functioning object instance.

Today we will look at two serialisation formats.
  - Binary format: Python's `pickle` module
  - String format: Python's `json` module and related tooling

The core ideas around them apply fairly generally to other formats.

---

### Pickle
Python's standard pickle module saves Python built-in types and some custom objects in a binary format. Note that this saves *object data*. It's not a way to store arbtrary code in a binary format.

Pros:
  - Easy to use
  - Efficient

Cons:
  - Python-specific
  - Can't save/load some values
  - Security concerns

**Pickle versions**
There are currently six versions of the pickle protocol.
  - Versions 0 -2: Too old, don't care
  - Version 3: introduced in Python 3.0
  - Version 4: introduced in Python 3.4
  - Version 5: introduced in Python 3.9

New versions have improved features, but data pickled with a high version can't be unpickled in older interpreters that don't support the protocol version. You can specify the protocol version used when pickling.

**Basic pickle functions**
  - `pickle.dump()`: Saves data to a file
  - `pickle.dumps()`: Returns a byte string of pickled data
  - `pickle.load()`: Loads from a file
  - `pickle.loads()`: Loads from a byte string

**Example**
```
import pickle

class PickleMe:
    def __init__(self, data):
        self.data = data

example = PickleMe(42)

pickle.dump(example, open('save.p', 'wb'))
example = None
example = pickle.load(open('save.p', 'rb'))
print(example.data) # prints 42
```

Note that in order to un-pickle data, the code that defines classes like the `PickleMe` class above must be accessible in the scope where the un-pickling takes place.

**Security concerns**
Even though `pickle` doesn't store *arbitrary* code, loading pickled data is code exectution. Never load pickled data from an untrusted source. If you are transmitting pickled data over an untrusted network, use something like the `hmac` module to cryptographically authenticate the data.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `17-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `15-practical` directory.
  4. There are three files, `q1.py`, `q2.py`,  and `q3.py`. Work through them now.
  5. We won't discuss these problems since we're not meeting in person, but I will share solutions on teams later.
  6. Complete the problems in `q4.py` after reading the section below.

---

### JSON 

Javascript Object Notation (JSON) is a common data serialisation format. Python's `json` module has functions corresponding to those we saw in pickle.
  - `json.dump()`: Saves data to a file
  - `json.dumps()`: Returns a JSON string of pickled data
  - `json.load()`: Loads from a file
  - `json.loads()`: Loads from a JSON string

Pros:
  - Not Python-dependent
  - Easy
  - Extensible

Cons: 
  - Can't represent some Python values
  - Can't represent custom object without additional code

The last points are worth contrasting with `pickle`. Since `pickle` is integrated with Python, it can handle most Python core types and user-defined objects. With JSON we give that up, but in return get a language-independent format.

**Python values that serialise to JSON**
  - integers
  - floats
  - strings
  - booleans
  - lists (whose members also serialise)
  - dictionaries (but only with string keys)
  - `None`

**Example**
```
import json
pets = {'cat': 'Lola',
   'dog': 'Star',
   'fish': 'My fish don't have names.'
   }
json_pets = json.dumps(pets)
restored_pets = json.loads(json_pets)
```

The json library uses a default encoder that handles most cases, but when it doesn't we can create and use a custom JSONEncoder`.

```
import json

z = 1 + 2j
# z is a complex number - a type supported natively in Python but not JSON.

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        return json.JSONEncoder.default(self, obj)

json_z = json.dumps(z, cls=ComplexEncoder)
```

**Adding serialisation to a class**
Since the `json` module can't handle custom classes, a typical approach is to add serialisation methods to the class.

```
class Foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dumps(self):
        return json.dumps({'a': self.a, 'b': self.b})

    @classmethod
    def loads(cls, js):
        data = json.loads(js)
        return cls(data['a'], data['b'])

foo = Foo(6, 'spam')
json_foo = foo.dumps()
restored_foo = Foo.loads(json_foo)
```

**More robust serialisation**
The pip-installable module `marshmallow` provides a more robust approach to JSON (and other) serialisation.

```
from marshmallow import Schema, fields, post_load

class Foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class FooSchema(Schema):
    a = fields.Str(required=True)
    b = fields.Integer()

    @post_load
    def make_foo(self, data, **kwargs):
        return Foo(**data)

foo = Foo(’hello’, 6)
foo_schema = FooSchema()
serialised = foo_schema.dump(foo)  # returns a dict, not json
deserialised = foo_schema.load(serialised)
```

The idea here is that we want to serialise/deserialise objects of type `Foo`. We define the `FooSchema` class so that `marshmallow` can use it to work with out `Foo` class.

***Security concerns***

We should notice that JSON is a much more limited serialisation format than pickle. It simply can't represent the same range of values. But that also means that JSON is a bit safer to handle. That general principle holds up in general. More expressive formats must be handled more carefully. Programmers commonly treat serialisation/deserialisation as routine and even boring, but it is critically important to research the formats and tools we use and make sure that we handle serialised data safely.

### References

  - https://docs.python.org/3/library/pickle.html
  - https://docs.python.org/3/library/json.html
  - https://marshmallow.readthedocs.io/en/stable/index.html
