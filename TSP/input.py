
class Input(object):
    def __init__(self):
        pass

    def getInput(self):
        self.input = [(0, 1, 3), (0, 2, 12), (0, 3, 6), (1, 2, 5), (1, 3, -4), (2, 3, -4)]

    def transform(self):
        self.getInput()
        # {start : [{end, weight},{end, weight},....],... }
        matrix = {}
        for input in self.input:
            (start, end, weight) = input
            if start in matrix:
                matrix[start][end] = weight
            else:
                matrix[start] = {end : weight}

        size = len(matrix) + 1

        for row in range(size):
            if row in matrix:
                row_value = matrix[row]
                for column in range(size):
                    if row == column:
                        row_value[column] = 0
                    if column not in row_value:
                        row_value[column] = matrix[column][row]
                        # matrix[column][row] = matrix[row][column]
            else:
                row_value = {}
                for column in range(size):
                    if row == column:
                        row_value[column] = 0
                    if column not in row_value:
                        row_value[column] = matrix[column][row]
                        # matrix[column][row] = matrix[row][column]
                matrix[row] = row_value
        self.matrix = matrix

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]

if __name__ == '__main__':
    Input().transform()