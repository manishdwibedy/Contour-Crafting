
class Input(object):
    def __init__(self):
        self.matrix = {
            0: {0: 0,1: 3,2:12,3:6},
            1: {0: 3,1: 0,2:5, 3:-4},
            2: {0: 12,1: 5,2:0, 3:-4},
            3: {0: 6,1: -4,2:-4, 3:0},
        }

    def Distance(self, from_node, to_node):
        return self.matrix[from_node][to_node]