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

        extra_node_list = []

        # If graph data exists
        if self.graph:

            for node, edges in self.graph.edge.iteritems():
                edge_count = len(edges)
                node_info = self.graph.node[node]
                if edge_count > 1:
                    for index in range(1, edge_count):
                        extra_node = str(node) + '_' + str(index)
                        node_object = {
                                'id': extra_node,
                                'X' : node_info['X'],
                                'Y' : node_info['Y']
                            }
                        extra_node_list.append(node_object)

            for node in extra_node_list:
                node_id = node['id']
                node_x = node['X']
                node_y = node['Y']
                self.graph.add_node(node_id, X = node_x, Y = node_y)