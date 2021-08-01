# Vector Class
#
# Below is the start of a class that can represent vectors in n-dimensional
# spaces. Implement the dunder methods to get the expected output.
#
# Question: We implement a length() method and also a __len__() method
# and they are quite different. Why don't we just use length() for
# __len__(). Hint: There are actually two reasons.

from math import sqrt

class Vector:
    def __init__(self, *args):
        self.coords = tuple(args)
        
    def length(self):
        # this is the geometric length of the vector.
        return sqrt(sum(map(lambda x: x * x, self.coords)))
    
    def __len__(self):
        # len is the number of items in the coordinates tuple
        pass
    
    def  __str__(self):
        return ''
    
    def __repr__(self): 
        return ''
    
    def __add__(self, other):
        # add two vectors by adding their coordinates pointwise, e.g.
        # (1, 2, 3) + (1, 1, 2) = (2, 3, 5)
        pass
    
    def __eq__(self, other):
        # two vectors compare == if the have the same len() and the same length()
        pass
    
    def __lt__(self, other):
        # similar to ==
        pass
    
    def __mul__(self, other):
        # You can multiply a vector by a number (scalar), e.g.,
        #(1, 2, 3) * 2 = (2, 4, 6)
        pass
    
    # a problem: With __mul__() we can do v * 3 for a Vector v,
    # but not 3 * v. There's a way to do that, and you need to implement it.
    

def main():
    v1 = Vector(1, 1)
    v2 = Vector(2, 2)
    v3 = Vector(1, 2, 3)
    
    print(v1)
    print(repr(v1))
    print(len(v3))
    print(v1 == v2)
    print(v1 < v2)
    print(v1 != v3)
    print(v1 + v2)
    #print(5 * v1)
    print(v1 * 2)
    

if __name__ == '__main__':
    main()

# Expected output:
# (1, 1)
# Vector(1, 1)
# 3 
# False
# True
# True
# (3, 3)
# (5, 5)
# (2, 2)
