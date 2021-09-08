# Using the Factory Method pattern, implement the StringTransformer below. 

class StringReverser:
    def transform(self, string):
        return string[::-1]
    
class StringStretcher:
    def transform(self, string):
        return ' '.join(list(s))
    
class StringTransformer:
    def transform(self, string, transform_type):
        pass
    
transformer = StringTransformer()
s = 'cats'
print(transformer.transform(s, 'reverse'))
print(transformer.transform(s, 'stretch'))

# expected output
# stac
# c a t s
