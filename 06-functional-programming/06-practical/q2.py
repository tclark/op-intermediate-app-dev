# The function middle() takes a string and returns the string produced by
# removing its first and last characters. Write the body of upper_arg so
# that it takes a function of a string (like middle) and returns a new
# function that first converts its argument to uppercase and then calls the
# original function. So in the code below, calling MIDDLE('cats') is like
# calling middle('CATS').

def middle(s):
    return s[1:-1]

def upper_arg(fn):
    pass


print(middle('cats'))
MIDDLE = upper_arg(middle)
print(MIDDLE('cats'))

# Exppected output:
# at   
# AT
