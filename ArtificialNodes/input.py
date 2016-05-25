import networkx as nx
from  constant import DEPOSITION_EDGE
from collections import Counter
from math import pow

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

    def addNodes(self):
        for start_node, edges in self.graph.edge.iteritems():
            other_nodes = Counter(self.getOtherNodes(start_node))
            adjacent_nodes = []
            for end_node, weight in edges.iteritems():
                adjacent_nodes.append(end_node)
            adjacent_nodes = Counter(adjacent_nodes)

            missing_nodes = other_nodes - adjacent_nodes

            for node in missing_nodes:
                self.graph.add_edge(start_node, node, weight = self.getDistance(start_node, end_node))
            pass

    def getDistance(self, start_node, end_node):
        if start_node in self.graph.node and end_node in self.graph.node:
            x_diff = start_node['x'] - end_node['x']
            y_diff = start_node['y'] - end_node['y']
            distance = pow(x_diff ** 2 + y_diff ** 2, 0.5)
            return distance
        else:
            return -1

if __name__ == '__main__':
    Nodesinput = Input()
    Nodesinput.readFile()
    Nodesinput.createGraph()
    Nodesinput.addNodes()
    pass