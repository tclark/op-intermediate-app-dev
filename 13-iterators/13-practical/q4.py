# Define an Iterable class called CrazyList that just stores a list of values.
# Define an Iterator, CrazyListIterator that returns randomly chosen values
# from a CrazyList. However, keep track of how many values have been returned
# so that the Iterator stops after producing the number of values in the
# original CrazyList. 

class CrazyList:
    pass

class CrazyListIterator:
    pass


if __name__ == '__main__':
    l = list('abcdefghijklmnopqrstuvwxyz')
    crazy = CrazyList(l)
    for letter in crazy:
        print(letter)

# Expected output: Varies, but you should get 26 random letters,
# possibly including repeat values.
