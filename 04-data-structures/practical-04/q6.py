# Implement the methods in the Graph class below. Please comment 
# your code as appropriate. It helps us understand your implementation.

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []
        
    def add_node(self, node_value):
        pass
    
    def add_edge(self, node1, node2):
        # Create an edge between node1 and node2.
        # An edge is just a tuple with two node values in it.
        # Duplicate edges are allowed.
        pass
    
    def remove_node(self, node_value):
        # Don't forget to remove edges!
        pass
    
    def remove_edge(self, node1, node2):
        # remove one edge between node1 and node2
        pass
    
    def get_node(self, node_value):
        # Return a tuple whose first element is the node value
        # and whose second value is a list of edges connected 
        # to the node
        pass
    
def main():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    print(graph.get_node('a'))
    graph.remove_node('b')
    print(graph.get_node('c'))
    
if __name__ == '__main__':
    main()
    
# Expected output:
    
# ('a', [('a', 'c')])
# ('c', [('a', 'c')])  