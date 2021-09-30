import datetime
import random


class Practical19:

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def __str__(self):
        return f'{self.name}: {self.num}'

    def strange_number(self):
        return self.num + random.randint(0, 100)


    def is_it_the_weekend(self):
        today = datetime.datetime.now()
        return today.weekday() > 5 # Mon == 1, Sun == 7


if __name__ == '__main__':
    p19 = Practical19('example', 4)
    print(p19)
