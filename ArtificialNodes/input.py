import networkx as nx

class Input(object):
    def __init__(self):
        pass

    def readFile(self):
        '''
        This method would read the input from a file.
        The input would be in the form of (x,y) for every node
        '''
        input = []
        input.append({
            'x': 0,
            'y': 0
        })
        input.append({
            'x': 0,
            'y': 2
        })
        input.append({
            'x': 2,
            'y': 2
        })
        self.input = input

    def createGraph(self):
        G=nx.Graph()

        for node in self.input:
            G.add_node(node)

        print G.number_of_edges()
        print G.number_of_nodes()