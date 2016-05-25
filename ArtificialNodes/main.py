import input, basic_graph

if __name__ == '__main__':
    input = input.Input()
    input.readFile('input.json')

    graph = basic_graph.BasicGraph(input.data)
    graph.createBasicGraph()
    graph.addIdleEdges()
    graph.addNodes()
    pass