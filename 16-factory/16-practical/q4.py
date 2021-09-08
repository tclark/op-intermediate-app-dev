# Implement the StringTransformFactory using the Abstract Factory pattern.

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
