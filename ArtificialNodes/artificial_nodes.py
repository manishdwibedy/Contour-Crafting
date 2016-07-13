import input, basic_graph, add_nodes, deposition_cost
from common.constant import FILE_NAME

class ArtiticialNodes(object):
    def __init__(self):
        pass

    def readFile(self):
        # Reading the graph from the input file
        self.graphInput = input.Input()
        self.graphInput.readFile(FILE_NAME)

    def makeGraph(self):
        # Construction the graph from the input
        self.graph = basic_graph.BasicGraph(self.graphInput.data)
        self.graph.createBasicGraph()

    def addAdditionalNodes(self):
        # Adding the extra nodes in the graph depending upon the degree of the node.
        self.graph = add_nodes.AddingNodes(self.graph)
        self.graph.addNodes()

    def addDepositionCost(self):
         # Assigning the deposition costs
        self.graph = deposition_cost.DepositionCost(self.graph)
        self.graph.assignDepositionCost()

    #
    # Start : Fix for the wrong graph being generated after adding artificial node
    #
    def isArtificialNodePresent(self, node):
        # Checks if the node has a artificial node
        if node + '_1' in self.graph.graph.node:
            return True
        return False

    def getArtificialNodeID(self, node):
        num = 0
        while(True):
            num += 1
            if not node + '_' + str(num) in self.graph.graph.node:
                return num
        return num

    def getArtificialNodeList(self, node, num):
        node_list = []

        for index in range(1,num):
            nodeID = node + '_' + str(index)
            node_list.append(nodeID)

        return node_list

    def getNeighborNodes(self, node):
        edges = self.graph.graph.edge[node]

        edge_list = []
        for edge, edge_data in edges.iteritems():
            if not edge.startswith(node) and 'DEPOSITION_EDGE' in edge_data:
                edge_list.append(edge)

        return edge_list

    def fixCostOfNode(self, node):
        num_of_nodes =  self.getArtificialNodeID(node)

        node_list = self.getArtificialNodeList(node, num_of_nodes)

        neighbours = self.getNeighborNodes(node)
        for edge in neighbours[1:]:
            self.swapCost(node, edge)
            # self.graph.graph.edge[node][edge]['DEPOSITION_COST'] =

    def findMissingDepositionEdge(self, node):
        edges = self.graph.graph.edge

        for nodeID in self.getArtificialNodeList(node, self.getArtificialNodeID(node)):
            for edge, edge_data in edges.iteritems():
                if nodeID != edge:
                    edge_info = self.graph.graph.edge[nodeID][edge]
                    if "DEPOSITION_EDGE" in edge_info:
                        break
            else:
                return nodeID
        return nodeID

    def swapCost(self, node, destination):

        deposition_cost = self.graph.graph.edge[node][destination]['DEPOSITION_COST']
        idle_cost = self.graph.graph.edge[node + '_1'][destination]['IDLE_COST']

        del self.graph.graph.edge[node][destination]
        self.graph.graph.add_edge(node, destination, IDLE_COST = idle_cost)

        nodeID = self.findMissingDepositionEdge(node)
        del self.graph.graph.edge[nodeID][destination]
        self.graph.graph.add_edge(nodeID, destination, DEPOSITION_COST = deposition_cost, DEPOSITION_EDGE= True)

        # # self.graph.graph.edge[node][destination]['IDLE_COST'] = idle_cost
        # for nodeID in self.getNodeID(node, self.getArtificialNodes(node)):
        #
        #     # self.graph.graph.edge[nodeID][destination]['DEPOSITION_COST'] = deposition_cost
        #     # self.graph.graph.edge[nodeID][destination]['DEPOSITION_EDGE'] = True

    def fixCompleteGraph(self):
        for node in self.graph.graph:
            if '_' not in node and self.isArtificialNodePresent(node):
                self.fixCostOfNode(node)
        pass

    #
    # END : Fix for the wrong graph being generated after adding artificial node
    #
    def main(self):
        self.readFile()
        self.makeGraph()
        self.addAdditionalNodes()
        self.addDepositionCost()
        self.fixCompleteGraph()

        return self.graph