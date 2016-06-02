import input, basic_graph, add_nodes

if __name__ == '__main__':
    # Reading the graph from the input file
    graphInput = input.Input()
    graphInput.readFile('input.json')

    # Construction the graph from the input
    graph = basic_graph.BasicGraph(graphInput.data)
    graph.createBasicGraph()

    # Adding the extra nodes in the graph depending upon the degree of the node.
    graph = add_nodes.AddingNodes(graph)
    graph.addNodes()
    pass