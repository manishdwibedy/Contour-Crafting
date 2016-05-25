import networkx as nx
from  constant import DEPOSITION_EDGE

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
        graph = nx.Graph()

        for node in self.nodes:
            graph.add_node(node['id'])

        for edge in self.edges:
            graph.add_edge(edge['start'], edge['end'], weight = DEPOSITION_EDGE)

        self.graph = graph

    def getOtherNodes(self, node):
        node_list = []
        for node_object in self.graph.node:
            if node != node_object:
                node_list.append(node_object)

        return node_list

if __name__ == '__main__':
    Nodesinput = Input()
    Nodesinput.readFile()
    Nodesinput.createGraph()
    Nodesinput.addNodes()