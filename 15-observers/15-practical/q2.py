# Usually a Subject calls its own notify() method when its own 
# state changes. Implement that below.

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f'{self.name} - subject state: {subject.state}')

class Subject:
    def __init__(self, state):
        self._state = state
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state
        

sub = Subject('eggs')
obs1 = Observer('Observer 1')
obs2 = Observer('Observer 2')
sub.register(obs1)
sub.register(obs2)
sub.state = 'spam'

# expected output (Order may vary)
# Observer 1 - subject state: spam
# Observer 2 - subject state: spam   
