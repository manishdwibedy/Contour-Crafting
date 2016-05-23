
class Input(object):
    def __init__(self):
        self.matrix = {
            0: {0: 0,1: 3,2:12,3:6},
            1: {0: 3,1: 0,2:5, 3:-4},
            2: {0: 12,1: 5,2:0, 3:-4},
            3: {0: 6,1: -4,2:-4, 3:0},
        }

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

        self.matrix = {}

        size = len(matrix)

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]

if __name__ == '__main__':
    Input().transform()