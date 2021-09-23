# For the SerialiseMe class below:
# Part 1: Write a custom JSON Encoder that can be used with json.dumps()
# to serialise objects of this type to JSON.
#
# Part 2: Write a marshmallow schema and use it to serialise and
# deserialise objects of this type. Note that these produce and
# read dictionaries, not JSON strings (but the dictionaries are easily
# converted to/from JSON).

import json
from marshmallow import Schema, fields # you will need to pip install marshmallow

class SerialiseMe:
    def __init__(self, my_str, my_int, my_bool):
        self.my_str = my_str
        self.my_int = my_int
        self.my_bool = my_bool

sample = SerialiseMe('spam', 42, False)        
        
