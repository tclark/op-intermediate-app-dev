# Below there is a collection of values. Pickle each of them with 
# pickle.dumps(). This will give you byte string representations of 
# those values. Then, "unpickle" the values and verify that they are
# restored.

import pickle

# Here are our values to pickle
a_num = 42
a_str = 'spam'
a_dict = {'a': 1, 'b': 7}

class MyClass:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return str(self.data)

an_obj = MyClass('hello')

# Pickle these values below with pickle.dumps()


# The line below clears out the values of our variables.
a_num, a_str, a_dict, an_obj = None, None, None, None

# Now unpickle the pickled data


# If you pickled/unpickled successfully, these print()s should work.
print(a_num)
print(a_str)
print(a_dict)
print(an_obj)

# Expected output:
# 42
# spam
# {'a': 1, 'b': 7}
# hello
