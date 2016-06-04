import csv
from constant import INPUT

class Input(object):
    def __init__(self):
        self.size = -1

    def getInput(self, filename, headerRow = False):

        with open('data/'+filename + INPUT.value, 'rb') as f:
            reader = csv.reader(f)
            if headerRow:
                self.input = list(reader)[1:]
            else:
                self.input = list(reader)
            self.cleanInput()

    def cleanInput(self):
        list = []
        try:
            for line in self.input:
                (start, end, weight) = line
                i_start = int(start)
                i_end = int(end)
                f_weight = float(weight)
                list.append((i_start, i_end, f_weight))

            self.input = list
        except:
            print 'Error in the data'
    def transform(self,):
        # {start : [{end, weight},{end, weight},....],... }
        matrix = {}
        for input in self.input:
            (start, end, weight) = input
            if start in matrix:
                matrix[start][end] = weight
            else:
                matrix[start] = {end : weight}

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