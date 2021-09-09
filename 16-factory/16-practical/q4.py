# Implement the StringTransformFactory using the Abstract Factory pattern.
# Take the StringReverser and StringStetcher from q1 and make an abstract 
# factory that can give us objects that transform strings, in particular
# the StringReverser and StringStretcher

class StringTransformFactory:
    pass



stf = StringTransformFactory()
reverser = stf.get_reverser()
stretcher = stf.get_stretcher()
cats = 'cats'
print(reverser(cats))
print(stretcher(cats))

# expected output
# stac
# c a t s
