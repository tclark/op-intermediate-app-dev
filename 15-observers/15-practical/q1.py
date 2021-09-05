# Implement the methods of the Subject and Observer classes below 
# to complete the Observer pattern/ 


class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        pass
    
class Subject:
    def __init__(self):
        pass
    
    def register(self, observer):
        pass
    
    def unregister(self, observer):
        pass
    
    def notify(self):
        pass
        
sub = Subject()
obs1 = Observer('Observer 1')
obs2 = Observer('Observer 2')
sub.register(obs1)
sub.register(obs2)
sub.notify()
sub.unregister(obs1)
sub.notify()

# expected output (Order may vary)
# Observer 1 notified
# Observer 2 notified
# Observer 2 notified
