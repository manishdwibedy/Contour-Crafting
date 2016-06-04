from util import get_edge_cost

class Input(object):
    def __init__(self, graph):
        self.size = -1
        self.graph = graph

    def transform(self,):
        # {start : [{end, weight},{end, weight},....],... }
        matrix = {}
        for start_node, edges in self.graph.edge.iteritems():
            for end_node, edge_data in edges.iteritems():
                if start_node not in matrix:
                    matrix[start_node] = {end_node : get_edge_cost(edge_data)}
                else:
                    matrix[start_node][end_node] = get_edge_cost(edge_data)

        self.size = len(matrix) + 1

        self.matrix = matrix

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]

    def getSize(self):
        return self.size

if __name__ == '__main__':
    Input().transform()