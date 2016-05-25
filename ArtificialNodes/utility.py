
def getDistance(graph, start_node, end_node):
    if start_node in graph.node and end_node in graph.node:
        start_node = graph.node[start_node]
        end_node = graph.node[end_node]
        x_diff = start_node['X'] - end_node['X']
        y_diff = start_node['Y'] - end_node['Y']
        distance = pow(x_diff ** 2 + y_diff ** 2, 0.5)
        return distance
    else:
        return -1