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
        self._tag = None
        """" Used for complex algorithms on graph"""
        self.info = None
        """" Used for complex algorithms on graph"""
    def add_edge_from(self, node_id: int, weight: float):
        if node_id not in self.edges_from:
            self.edges_from[node_id] = weight

    def add_edges_towards(self, node_id: int, weight: float):
        if node_id not in self.edges_towards:
            self.edges_towards[node_id] = weight

    def get_id(self):
        return self.node_id

    def set_tag(self, tag: int):
        self._tag = tag

    def get_tag(self) -> int:
        return self._tag

    def __repr__(self):
        x=(f"{self.node_id}: |edges out| {len(self.edges_towards)} , |edges in| {len(self.edges_from)} ")
        return x

    def setPosition (self,x:int=0,y:int=0):
        self.pos=(x,y)


class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
