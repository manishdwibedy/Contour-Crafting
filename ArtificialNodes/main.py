import input, basic_graph, add_nodes

if __name__ == '__main__':
    input = input.Input()
    input.readFile('input.json')

    graph = basic_graph.BasicGraph(input.data)
    graph.createBasicGraph()

    extra_nodes = add_nodes.AddingNodes(graph)
    extra_nodes.addNodes()
    # graph.addIdleEdges()
    graph.addNodes()
    pass