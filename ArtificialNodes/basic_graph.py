import networkx as nx

class BasicGraph(object):
    def __init__(self, data):
        self.data = data

    def createBasicGraph(self):
        '''
        Creating a basic graph, if data about the graph exists.
        '''
        self.graph = None
        # If graph data exists
        if self.data:
            self.graph = nx.Graph()

            nodes = self.data['nodes']
            edges = self.data['edges']

            for node in nodes:
                self.graph.add_node(node['id'], X = node['X'], Y = node['Y'])

            for edge in edges:
                self.graph.add_edge(edge['start'], edge['end'], DEPOSITION_EDGE = True)