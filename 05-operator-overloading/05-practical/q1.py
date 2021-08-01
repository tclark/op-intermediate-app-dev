#  Flocks of sheep
#  Define the dunder methods of the Flock class below.

class Sheep:
    def __init__(self, tag): # a tag is a string that identifies a sheep
        self.tag = tag
        
    def __repr__(self):
        return f'Sheep({self.tag})'
        
class Flock:
    def __init__(self, sheep): #tags is a list of id tag numbers
        self.sheep = sheep
    
    def __add__(self, other):
        # this should combine the flocks by
        # merging their sets of tags
        pass
    
    def __eq__(self, other):
        # two flocks compare == if they have the same number of shhep
        pass
    
    def __lt__(self, other):
        # self < other if other has more sheep
        pass
    
    
def main():
    sheep1 = [Sheep(str(i)) for i in range(1, 10)] 
    sheep2 = [Sheep(str(i)) for i in range(20, 34)]
    flock1 = Flock(sheep1)
    flock2 = Flock(sheep2)
    print(flock1 == flock2)
    print(flock1 != flock2)
    print(flock1 < flock2)
    print(flock1 > flock2)
    flock3 = flock1 + flock2
    print(flock3.sheep)
   

if __name__ == '__main__':
    main()
    
# Expected output:
# [Sheep(1), Sheep(2), Sheep(3), Sheep(4), Sheep(5), Sheep(6), Sheep(7), Sheep(8), Sheep(9)]
# False
# True
# True
# False
# [Sheep(1), Sheep(2), Sheep(3), ... (you get the idea) ..., Sheep(33)]

# Question: We only handled == and <. Why do != and > also work?
