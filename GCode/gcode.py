
class GCode(object):
    def __init__(self, graph, solution):
        self.graph = graph
        self.solution = solution

    def run(self):
        print 'Starting with GCode\n'

        graph = self.graph.graph
        for index, node in enumerate(self.solution['nodes']):
            print "Current Node - " + node
            position = graph.node[node]
            print "Position - (" + str(position['X']) + "," + str(position['Y']) + ')\n'

            # Excluding the last node in the solution
            if index < len(self.solution['nodes']) - 1:
                next_node = self.solution['nodes'][index+1]

                position = graph.node[next_node]
                print "Position - (" + str(position['X']) + "," + str(position['Y']) + ')\n'

                pass

