import input, basic_graph, add_nodes

if __name__ == '__main__':
    graphInput = input.Input()
    graphInput.readFile('input.json')

    graph = basic_graph.BasicGraph(graphInput.data)
    graph.createBasicGraph()

    extra_nodes = add_nodes.AddingNodes(graph)
    extra_nodes.addNodes()
    pass