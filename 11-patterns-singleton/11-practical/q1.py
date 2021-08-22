# Implement the RandomNumberGen class as a singelton. It should provide a number() method that returnsxi
# a randomly generated integer.


class RandomNumberGen:
	    pass



rng = RandomNumberGen()
print(f'Random number: {rng.number()}')
rng1 = RandomNumberGen()
print(rng is rng1)

# expected output

# Random number: 42  (Numbers will vary, you know, randomly.)
# True

