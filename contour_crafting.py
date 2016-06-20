from ArtificialNodes import artificial_nodes
from TSP.TSP import TSP
from IFCParsing.ifc_parsing import IFCParsing
from GCode.gcode import GCode

class ContourCrafting(object):
    def __init__(self):
        pass

    def run(self):
        '''
        Solving the Contour Crafting problem
        :return:
        '''
        # ifc_parsing = IFCParsing('Project1.ifc')
        # graph_data = ifc_parsing.parse()

        nodes = artificial_nodes.ArtiticialNodes()
        graph = nodes.main()

        TSP_object = TSP(graph)
        self.solution = TSP_object.run()

        gcode = GCode(graph, self.solution)
        gcode.run()

        pass

    def get_solution(self):
        return self.solution