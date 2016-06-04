from ArtificialNodes import artificial_nodes
from TSP.TSP import TSP
if __name__ == '__main__':
    nodes = artificial_nodes.ArtiticialNodes()
    graph = nodes.main()

    TSP = TSP(graph).run()
    pass