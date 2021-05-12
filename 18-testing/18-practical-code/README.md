# Practical  18: Testing

Complete the exercises below by adding code to the file `tests/test_practical.py`.

## Using `unittest`

1. Write a unit test that tests `Practical18`'s `__str__()` method.

2. Write a unit test that tests `Practical18`'s `add_stuff()` method.

3. Write a unit test that tests `Practical18`'s `add_colour()` method.

4. Write a unit test that shows `Practical18`'s `add_colour()` method  raises an exception if a 
disallowed colour is added.

**Stop here**. We will discuss solutions in class.

## Homework

5. Write unit tests for the remaining methods of the `Practical18` class. For methods
that use `random` or `datetime`, use `patch()` and mocks to mock the behaviours of those modules.

Be sure to cover every (reasonable) test case.
.


You can run your tests with the command

  python -m unittest tests/test_practical.py

or 

  python -m unittest tests/test_practical.py -v  (for verbose)

from this directory
