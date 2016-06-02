
class DepositionCost(object):
    '''
    This class would be computing the depostion cost for the deposition edges
    and would then assign them to the deposition edges.

    The deposition cost would be computed using the 5 times than maximum IDLE time in the graph.
    '''

    def __init__(self, graph):
        self.graph = graph.graph

    def computeMaxRotationCost(self):
        '''
        :return: Retuning the the maximum rotation cost.
        '''
        return 0

    def computeMaxIdleCost(self):
        '''
        :return: Retuning the the maximum idle edge cost.
        '''
        return 0

    def comptuteDepositionCost(self):
        '''
        :return: Retuning the the deposition cost
        '''
        idle_cost  = self.computeMaxIdleCost()
        rotation_cost = self.computeMaxRotationCost()

        deposition_cost = 5 * (idle_cost + rotation_cost)

        return deposition_cost

    def assignDepositionCost(self):
        '''
        Assigning the deposition cost to the edges
        :return:
        '''
        deposition_cost = self.comptuteDepositionCost()
        # edges = self.graph.edges_iter(data='DEPOSITION_EDGE',default=1)
        edges = self.graph.edges(data=True)

        # Assigning the deposition edges the required deposition cost
        for edge in edges:
            data = edge[2]
            if "DEPOSITION_EDGE" in data:
                data['DEPOSITION_COST'] = -10

        pass

