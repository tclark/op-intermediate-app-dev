# Answer the questions in the comments below.



lst = [1, 2, 3, 4, 5]
itr0 = iter(lst)
itr1 = iter(lst)
print(f'Are our list iterators the same?: {itr0 is itr1}')
# Explain the output of the print above.



itr2 = iter(itr1) # What if we call iter() on an Iterator?
print(f'Looking at repeated calls to iter(): {itr2 is itr1}')
# Explain the output of the print above.



print('Some output from various calls to next():')

print(f'first next(itr0): {next(itr0)}')
print(f'second next(itr0): {next(itr0)}')

# The above calls to next() on itr0 don't effect the 
# call to next on itr1 below. That's fine; it's what we 
# generally expect.
print(f'next(itr1): {next(itr1)}') 
print(f'next(itr2): {next(itr2)}')
# But the last call to next() on itr2 does seem to be effected
# by the previous call on itr1. Why?

