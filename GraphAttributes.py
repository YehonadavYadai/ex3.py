class Node:

    def __init__(self, node_id: int = 0, pos: tuple = None):
        self.node_id = node_id
        """"" This node ID """
        self.edges_from = dict()
        """"" Dictionary that holds edges from this node: key - the destination node of the edge, value - the edge 
                weight """
        self.edges_towards = dict()
        """"" Dictionary that holds edges that going to this node: key - the source node of the edge, value - the edge 
                weight """
        self.pos = pos
        """"" Tuple that holds this node location"""

    def add_edge_from(self, node_id: int, weight: float):
        if node_id not in self.edges_from:
            self.edges_from[node_id] = weight

    def add_edges_towards(self, node_id: int, weight: float):
        if node_id not in self.edges_towards:
            self.edges_towards[node_id] = weight


class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
