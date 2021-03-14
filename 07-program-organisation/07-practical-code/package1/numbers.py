import random

def various_numbers():
    for _ in range(10):
        yield random.uniform(0, 16)
