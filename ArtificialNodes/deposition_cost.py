
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
        pass

    def computeMaxIdleCost(self):
        '''
        :return: Retuning the the maximum idle edge cost.
        '''
        pass

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
        pass

