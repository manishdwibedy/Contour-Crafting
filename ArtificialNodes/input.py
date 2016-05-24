import networkx as nx

class Input(object):
    def __init__(self):
        pass

    def readFile(self):
        '''
        This method would read the input from a file.
        The input would be in the form of (x,y) for every node
        '''

        nodes = []
        edges = []

        nodes.append({
            'id': 'A',
            'x': 0,
            'y': 0
        })
        nodes.append({
            'id': 'B',
            'x': 0,
            'y': 2
        })
        nodes.append({
            'id': 'C',
            'x': 2,
            'y': 2
        })

        edges.append({
            'start': 'A',
            'end': 'B'
        })
        edges.append({
            'start': 'B',
            'end': 'C'
        })
        self.edges = edges
        self.nodes = nodes


    def createGraph(self):
        G=nx.Graph()

        for node in self.nodes:
            G.add_node(node['id'])

        for edge in self.edges:
            G.add_edge(edge['start'], edge['end'], weight = -100)

        print G.number_of_nodes()
        print G.number_of_edges()

if __name__ == '__main__':
    Nodesinput = Input()
    Nodesinput.readFile()
    Nodesinput.createGraph()