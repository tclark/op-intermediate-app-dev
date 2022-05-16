## IN608
## Intermediate Application Development

## Session 19 :  (More) Testing

### Introduction

Last time we looked at *unit testing*. The critical thing about unit testing is that each test only tests one part of our code, in isolation. If we do this, then whenever a test fails it will be clear where, and thus why, it fails. But there's a problem with this.

This code from last timeis easy to unit test:

```
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, num):
        return self.factor * num
```

It's easy to test because it doesn't depend on anything outside the core language. It also is plainly deterministic and has no side effects. To be clear, that's a **good thing**. Code like this, that is easy to test, is likely to be reliable and easy to use. But we often need to write code that is more complicated thatn this. Consider this code:


```
import random

class Multiplier:

    def multiply(self, num):
        return random.randint(-10, 10) * num
```

This is only a tiny bit more complicated than the first example, but it's much harder to test precisely. It depends on the `random` library, which is in the standard library and so is pretty reliable, but it could still have its own bugs.
But most importantly, the behaviour of `multiply()` is less pridictable than the first version.

### Mocking

The problem with our `multiply()` method is this call:

```
random.randint(-10, 10)
```

If we could replace it with something predictable our method would be easy to test.

```
    def multiply(self, num):
        # The line below is commented out for testing.
        # BE SURE to replace it before release!
        #return random.randint(-10, 10) * num
        return 2 * num
```

Ok, this is now easy to test, but how long do you think it will be before we accidentally forget to restore the correct code before releasing it? What we really want it to to write our tests in such a way that we accoplish the same thing without changing the code we want to test. Luckily, the `unittest.mock` libaray lets us do that.

```
import unittest
from unittest.mock import patch
from multiplier.multiplier import Multiplier


class TestMultiplier(unittest.TestCase):
    def setUp(self):
        self.m = Multiplier()

    @patch('multiplier.multiplier.random')
    def test_multiply(self, mock_random):
        mock_random.randint.return_value = 2
        result = self.m.multiply(2)
        self.assertEqual(result, 4)
```

There is a lot going on here. 
  - We import the `patch` decorator from `unittest.mock`
  - We import the Multiplier class like normal.
  - We decorate our test, telling it that when it loads the `multiplier` module, it should replace the standard `random` module with a `Mock` object that we refer to as `mock_random` in the test method.
  - We basically tell our `mock_random` object that it should respond to calls to a `randint` method by always returning 2.
  - Now we can test our method with the assumption that its random factor has the value 2.

**A slightly more complex example**

Consider this code:

```
from my_db_lib import db

class UserManager:
    def get_user_name(self, user_id):
        user  = db.get_user(user_id)
        return user.name
```
There are multiple issues with testing this code.
  1. It relies on the `my_db_lib` module.
  2. Presumably that library is used to connect to a database.
  3. That database needs to have a user with a given `user_id` and `name`.
  4. the `db.get_user()` method appears to return some sort of user object.

Again, the `unittest.mock` module helps us. Here's a test:

```
from unittest.mock import Mock, patch
import user_manager

class TestUserManager:
    @patch(’user_manager.db’)
    def test_get_user_name(self, mock_db):
        testuser = Mock()
        testuser.name = ’Joe Bloggs’
        mock_db.get_user.return_value = testuser
        assertEqual(self.usermanager.get_user_name(1),
            ’Joe Bloggs’)
```

In this test we use `patch` just like in the previous example. We also use `unittest.mock`'s `Mock` class. A `Mock` object can act as a stand in for virtually any other kind of object. We can give a `Mock` object whatever attributes it needs for our test. So in this case me make a mock user object, give it a `name` attribute, and then use `patch` so that our `get_user()` call returns the mock object.

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `19-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `19-practical` directory.
  4. Follow the directions in the README.md file in the `19-practical` directory.
---

### References

  - https://docs.python.org/3/library/unittest.mock.html
  - https://realpython.com/python-mock-library/

