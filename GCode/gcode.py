
class GCode(object):
    def __init__(self, graph, solution):
        self.graph = graph
        self.solution = solution

    def run(self):
        print 'Starting with GCode'

        for node in self.solution['nodes']:
            print node