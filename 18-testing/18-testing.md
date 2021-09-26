## IN608
## Intermediate Application Development

## Session 18 :  Testing

### Introduction
You've certainly done some testing already. If nothing else, before submitting an assessment you probably checked to be sure that your code basically worked. Perhaps you even made a small plan, enumerating a set of cases to check for correct behaviour. In professional settings, plans like this become very detailed, noting the steps to be taken to perform each test and the expected outcomes from them. And while this sort of deliberate manual testing is important, such testing is time-consuming and takes care to be done consistently. It doesn't take much imagination to see that some of this testing can be done in an automated fashion, and now most programming languages have libraries and tooling to facilitate automated testing.

Python has three main test modules:
  - `unittest`
  - `pytest`
  - `nose2`

Test modules like these provide two things: features to help write test code and *test runners* - utilities to run your tests and output the results. Since `unittest` is included in the standard library and it provides a good model for how automated testing is done, we will use it for this lab.

**Types of tests**

Automated tests used by programmers can be categorised into two types: *unit tests* and *integration tests*. Unit tests each test one very specific function in a program in isolation. These very focussed tests are useful because when a test fails it's very clear where in the code the problem must lie. But a program can pass all its unit tests and still be very buggy, since unit tests don't how the invividual parts of a program work together. Integration tests do that. The different test modules can all be used for unit and itegration tests. The difference is just in the logic of how the tests are structured.

Today we will focus on unit tests.

### Writing Tests with `unittest`

Let's jump in with an example. Suppose we have this class:

```
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, num):
        return self.factor * num
```

Let's write a test for the `multiply()` method.

```
import unittest
from multiplier.multiplier import Multiplier


class TestMultiplier(unittest.TestCase):
    def setUp(self):
        self.m = Multiplier(2)

    def test_multiply(self):
        result = self.m.multiply(2)
        self.assertIsInstance(result, (int, float, complex))
        self.assertEqual(result, 4)
```

There are a few important things to note here.
  1. We import the library `unittest`.
  2. We must organise our tests in a class. Here we use the class `TestMultiplier` to test our `Multiplier` class.
  3. We import the `Multiplier` test that we want to test.
  4. Our test class inherits from `unittest.TestCase`.
  5. We use an (optional) `setUp()` method that prepares anything we need befor we run any tests with this class.
  6. Our actual tests go in methods named `test_*`. `test_multiply` tests the `multiply()` method.
  7. Our test calls the `multiply()` method and checks the result with various `assert*` methods.

**Organising our project**

As is typical with Python projects, there is more than one way to organise a project to use `unittest`. Here is one example of a good way:

```
project_root/
          |
          |- multiplier/
          |   |
          |   |- multiplier.py
          |
          | ...
          |- tests/
              |
              |- test_multiplier.py
              | ...
```
This structure keeps our test code close to our project's source code while at the same time keeping the test code distinctly seperate.

**Running tests**

With the project organised as shown above, we run our tests from a shell by navigating to the `project_root` directory and issuing the command

```
python -m unittest tests
```

`unittest`s test runner will look for test cases in any file with names starting with `test_` in the `tests` directory and run them.
We will get output that either tells us our tests all pass, or identifying tests that fail with a brief explanation of the failure.

**Assertions**

`unittest` provides a set of assertions for use in tests. Commonly used ones are
  - `assertEqual(a,b)`
  - `assertNotEqual(a,b)`
  - `assertTrue(a)`
  - `assertNotTrue(a)`
  - `assertIs(a,b)`
  - `assertIsNot(a,b)`
  - `assertIsNone(a)`
  - `assertIsNotNone(a)`
  - `assertIn(a,b)`
  - `assertNotIn(a,b)`
  - `assertIsInstance(a,b)`
  - `assertNotIsInstance(a,b)`

---

### Programming Activity
  1. Pull the course materials repo
  2. Create a new branch, `18-practical` in your **practicals** repo.
  3. From the course materials repo, copy the contents of the `18-practical` directory.
  4. Follow the directions in the README.md file in the `18-practical` directory.

---

### Testing Exceptions

It's important when testing to not just test for successful results. We must also test for cases where we expect our code to fail, to be sure it does fail in the ways we expect. `unittest` includes ways to check that exceptions are raised.

```
def test_multiply_raises(self):
    with self.assertRaises(TypeError):
        self.m.multiply('cat')
```

In our example, this test will *fail*. Our `multiply()` method does not raise a `TypeError` when called with a string. If we want this to happen, then the test shows us that we need to modify our method to satisfy this condition.

### Skipping Tests
Sometimes you want to skip a test, or you expect a test to fail. You can decorate a test with one of these.

```
@unittest.skip(’message’)

@unittest.skipIf(condition, ’message’)

@unittest.expectedFailure
```

### Conclusions
It is probably pretty obvious that automated tests like these are valuable for ensuring that our code works properly. Ideally we would run our unit tests before every commit to make sure that things work, and especially to be sure we haven't introduced any new errors to code that worked in the past. But tests have value beyond their simple functionality.

  - Tests help us design our code. To write tests we have to think through how we expect our code to be used and what we expect it to do in very explicit terms. We can't write tests for code we don't understand.
  - Tests document our code. Other developers can read our tests and see how our code should be called and what they can expect it to do.
  - Tests encourage us to write **good** code. It's hard to write tests for badly organised code. When we're writing tests and find it's a struggle to do so, that's a strong indicator that the code we want to test is not structured very well.

### References

  - https://docs.python.org/3/library/unittest.html
