# Examples 1 and 2 are adapted from 
# https://python-patterns.guide/gang-of-four/singleton/

# 1. Classical GoF implementation

class SoloGoF:
    _instance = None  # This is a class variable

    def __init__(self):
        raise RuntimeError('Use instance() instead.')

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
            # extra initialisation can happen here
        return cls._instance

solo1 = SoloGoF.instance()
solo2 = SoloGoF.instance()
print(f"solo1's id: {id(solo1)}")
print(f"solo2's id: {id(solo2)}")
print(solo1 is solo2)

# A somewhat more Pythonic version

class SoloPy:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SoloPy, cls).__new__(cls)
            # extra initialisation can happen here
        return cls._instance
  
solo3 = SoloPy()
solo4 = SoloPy()
print(f"solo3's id: {id(solo3)}")
print(f"solo4's id: {id(solo4)}")
print(solo3 is solo4)

# Since a module is only imported once (usually), the module
# approach implements the singleton patter nicely.

import solomod
solo5 = solomod.solomod
solo6 = solomod.solomod
solo7 = solomod.SoloMod()
print(f"solo5's id: {id(solo5)}")
print(f"solo6's id: {id(solo6)}")
print(f"solo7's id: {id(solo7)}")
print(solo5 is solo6 is solo7)


