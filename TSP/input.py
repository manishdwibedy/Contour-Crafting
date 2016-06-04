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

        for row in range(self.size):
            if row in matrix:
                row_value = matrix[row]
                for column in range(self.size):
                    if row == column:
                        row_value[column] = 0
                    if column not in row_value:
                        row_value[column] = matrix[column][row]
                        # matrix[column][row] = matrix[row][column]
            else:
                row_value = {}
                for column in range(self.size):
                    if row == column:
                        row_value[column] = 0
                    if column not in row_value:
                        row_value[column] = matrix[column][row]
                        # matrix[column][row] = matrix[row][column]
                matrix[row] = row_value
        self.matrix = matrix

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]

    def getSize(self):
        return self.size

if __name__ == '__main__':
    Input().transform()