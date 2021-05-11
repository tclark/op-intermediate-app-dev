import datetime
import random

ALLOWED_COLOURS = {'red', 'blue', 'green', 'yellow'}

class Practical18:

    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.colours = set() # we'll add to this later

    def __str__(self):
        return f'{self.name}: {self.num}'

    def add_stuff(self, x):
        return x + self.num

    def add_colour(self, colour):
        if colour in ALLOWED_COLOURS:
            self.colours.add(colour)
        else:
            raise ValueError(f'{colour} is not an allowed colour')

    def clear_colours(self):
        self.colours.clear()

    def strange_number(self):
        return self.num + random.randint(0, 100)

    def uppername(self):
        return self.name.upper()

    def is_it_the_weekend(self):
        today = datetime.datetime.now()
        return today.weekday() > 5 # Mon == 1, Sun == 7

    def side_effect(self, x, y):
        self.colours.add('pink')
        return x + y

if __name__ == '__main__':
    p18 = Practical18('example', 4)
    print(p18)
