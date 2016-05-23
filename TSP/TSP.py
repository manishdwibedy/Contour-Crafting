from ortools.constraint_solver import pywrapcp
from input import Input

class TSP(object):
    def __init__(self):
        self.tsp_size = 4
        self.tsp_use_random_matrix = True
        self.use_light_propagation = False


    def run(self):
        param = pywrapcp.RoutingParameters()
        param.use_light_propagation = self.use_light_propagation
        pywrapcp.RoutingModel.SetGlobalParameters(param)

        # TSP of size FLAGS.tsp_size
        # Second argument = 1 to build a single tour (it's a TSP).
        # Nodes are indexed from 0 to FLAGS_tsp_size - 1, by default the start of
        # the route is node 0.
        routing = pywrapcp.RoutingModel(self.tsp_size, 1)

        parameters = pywrapcp.RoutingSearchParameters()
        # Setting first solution heuristic (cheapest addition).
        parameters.first_solution = 'PathCheapestArc'
        # Disabling Large Neighborhood Search, comment out to activate it.
        parameters.no_lns = True
        parameters.no_tsp = False

        # Setting the cost function.
        # Put a callback to the distance accessor here. The callback takes two
        # arguments (the from and to node inidices) and returns the distance between
        # these nodes.
        # input = Input()
        matrix = Input()
        matrix.transform()
        matrix_callback = matrix.Distance
        if self.tsp_use_random_matrix:
            routing.SetArcCostEvaluatorOfAllVehicles(matrix_callback)
        else:
            routing.SetArcCostEvaluatorOfAllVehicles(self.Distance)

        # Solve, returns a solution if any.
        assignment = routing.SolveWithParameters(parameters, None)
        if assignment:
            # Solution cost.
            print 'Final Cost is ', assignment.ObjectiveValue()
            # Inspect solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            node = routing.Start(route_number)
            route = ''

            print '\n\nThe solution is the following: '
            while not routing.IsEnd(node):
                route += str(node) + ' -> '
                node = assignment.Value(routing.NextVar(node))
                print 'Route : ', route
            else:
                route += '0'
                print '\n\nFinal Route is ', route
        else:
            print 'Specify an instance greater than 0.'

    def Distance(i, j):
      """Sample function."""
      # Put your distance code here.
      return i + j


if __name__ == '__main__':
    TSP().run()