
class GCode(object):
    def __init__(self, graph, solution):
        self.graph = graph
        self.solution = solution

    def run(self):
        print 'Starting with GCode\n'

        graph = self.graph.graph
        for node in self.solution['nodes']:
            print "Current Node - " + node
            position = graph.node[node]
            print "Position - (" + str(position['X']) + "," + str(position['Y']) + ')'
            print ''