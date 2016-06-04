from util import get_edge_cost

class Input(object):
    def __init__(self, graph):
        self.size = -1
        self.graph = graph

    def transform(self,):
        # {start : [{end, weight},{end, weight},....],... }
        self.computeNodeAlias()

        matrix = {}
        for start_node, edges in self.graph.edge.iteritems():
            start_node = self.node_alias[start_node]
            for end_node, edge_data in edges.iteritems():
                end_node = self.node_alias[end_node]
                if start_node not in matrix:
                    matrix[start_node] = {end_node : get_edge_cost(edge_data)}
                else:
                    matrix[start_node][end_node] = get_edge_cost(edge_data)

        self.size = len(matrix) + 1

        self.matrix = matrix

    def computeNodeAlias(self):
        self.node_alias = {}

        current_node_alias = 0
        for node in self.graph.node:
            self.node_alias[node] = current_node_alias
            current_node_alias += 1

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]

    def getSize(self):
        return self.size

if __name__ == '__main__':
    Input().transform()