class ProgrammingTeam:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        
    def add_member(self, new_member):
        self.members.append(new_member)
        
class ProgrammingPair(ProgrammingTeam): 
    def add_member(self, _):
        raise ValueError('Cannot and members to pairs.')
        