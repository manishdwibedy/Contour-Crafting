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

            for node, edges in self.graph.adj.iteritems():
                edge_count = len(edges)
                node_info = self.graph.node[node]
                if edge_count > 1:
                    for index in range(1, edge_count + 1):
                        extra_node = str(node) + '_' + str(index)
                        self.graph.add_node(extra_node, X = node_info['X'], Y = node_info['Y'])


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
