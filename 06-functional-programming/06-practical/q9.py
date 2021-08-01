# Using the randrange function, create a list comprehension called rand_nums
# which generates five numbers between 1 & 100. Use rand_nums, reduce
# function & lambda function to return the sum of rand_nums. 
#
# Note: your outputs will be different than what is shown below.

from functools import reduce
from random import randrange

rand_nums = # Write your solution here
sum_rand_nums = reduce('''Write your lambda function here''')
print(f'Random numbers: {rand_nums}')
print(f'Sum of random numbers: {sum_rand_nums}')

# Expected output:
# Random numbers: [25, 65, 75, 9, 57]
# Sum of random numbers: 231
