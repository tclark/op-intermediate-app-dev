# Implement the Observer pattern so that the observer 
# prints the expected output.

from random import randint
from time import sleep

class Observer:
    
    def update(self, subject):
        print(f'subject state: {subject.state}')

class Subject:
    def __init__(self):
        self.state = 'awake'
        
    def snooze(self):
        sleep_time = randint(1, 6)
        self.state = f'sleeping for {sleep_time} seconds'
        sleep(sleep_time)
        self.state = 'awake'


sub = Subject()
obs = Observer()
#sub.register(obs1)
sub.snooze()

# expected output (Order may vary)
# subject state: sleeping for 3 seconds
# subject state: awake
