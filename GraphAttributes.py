class Node:

    def __init__(self, node_id: int = 0, node_data: int = 0):
        self.node_id = id
        self.node_data = node_data
        self.edges_from = dict()
        self.edges_to = dict()


class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
