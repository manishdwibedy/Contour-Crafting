import networkx as nx
from  constant import DEPOSITION_EDGE, ROTATION_COST
from collections import Counter
from math import pow
import os
import json

class Input(object):
    def __init__(self, type):
        self.type = type
        self.directory = os.path.dirname(os.path.abspath(__file__))

    def setFileName(self, filename):
        data_location = os.path.join(self.directory, 'data')
        file_location = os.path.join(data_location, filename)
        self.file_location = file_location

    def readFile(self, filename):
        self.setFileName(filename)

        with open(self.file_location) as data_file:
            data = json.load(data_file)

        print(data)

    def parseGraph(self):
        '''
        This method would read the input from a file.
        The input would be in the form of (x,y) for every node
        '''

        nodes = {}
        edges = []

        for index in range(2):
            nodes['A'+str(index)] = {
                'x': 0,
                'y': 0
            }
            nodes['B'+str(index)] = {
                'x': 0,
                'y': 2
            }
            nodes['C'+str(index)] = {
                'x': 2,
                'y': 2
            }

            edges.append({
                'start': 'A'+str(index),
                'end': 'B'+str(index)
            })
            edges.append({
                'start': 'B'+str(index),
                'end': 'C'+str(index)
            })

        for node in ['A','B','C']:
            edges.append({
                'start': node + '0',
                'end': node + '1'
            })

        self.edges = edges
        self.nodes = nodes


    def createGraph(self):
        graph = nx.Graph()

        for label, node in self.nodes.iteritems():
            graph.add_node(label)

        for edge in self.edges:
            if edge['start'][:1] != edge['end'][:1]:
                graph.add_edge(edge['start'], edge['end'], weight = DEPOSITION_EDGE)
            else:
                graph.add_edge(edge['start'], edge['end'], weight = 0)

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
            start_node = self.nodes[start_node]
            end_node = self.nodes[end_node]
            x_diff = start_node['x'] - end_node['x']
            y_diff = start_node['y'] - end_node['y']
            distance = pow(x_diff ** 2 + y_diff ** 2, 0.5)
            return distance
        else:
            return -1

if __name__ == '__main__':
    Nodesinput = Input()
    Nodesinput.parseGraph()
    Nodesinput.createGraph()
    Nodesinput.addNodes()
    pass