import utility

class AddingNodes(object):
    def __init__(self, input):
        self.data = input.data
        self.graph = input.graph

    def addNodes(self):
        '''
        Addition of extra nodes
        :return:
        '''
        # If graph data exists
        if self.graph:
            nodes = self.data['nodes']

            for node in nodes:
                extra_node = node['id'] + '_1'
                self.graph.add_node(extra_node, X = node['X'], Y = node['Y'])

                other_nodes = self.getOtherNodes(extra_node)
                for to_node in other_nodes:
                    weight = utility.getDistance(self.graph, extra_node, to_node)
                    self.graph.add_edge(extra_node, to_node, weight = weight, IDLE_EDGES = True)

    def getOtherNodes(self, node):
        '''
        Get all nodes other than the current node
        :param node: the current node's ID
        :return: a list of nodes other than the current node
        '''
        node_list = []
        for node_object in self.graph.node:
            if node != node_object:
                node_list.append(node_object)

        return node_list
