from GraphInterface import GraphInterface
from GraphAttributes import *


class DiGraph(GraphInterface):

    def __init__(self):
        # the amount of nodes currently in this graph
        self.number_of_v = 0
        # the amount of edges currently in this graph
        self.number_of_e = 0
        # key - node ID, value - Node object with the ID of key
        self.all_nodes = dict()
        # number of changes in that occurred in the graph
        self.mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.number_of_v

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.number_of_e

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.all_nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        if id1 in self.all_nodes:
            node = self.all_nodes[id1]
            return node.edges_from

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        if id1 in self.all_nodes:
            return self.all_nodes[id1].edges_to

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        flag = False
        # if the user tries to connect a node to itself
        if id1 == id2:
            return True  # vacuously true
        # if both of the id's are in this graph
        if id1 in self.all_nodes and id2 in self.all_nodes:
            node_src = self.all_nodes[id1]
            node_dest = self.all_nodes[id2]
            # if there isn't an existing edge between id1 to id2
            if id2 not in node_src.edges_towards:
                node_src.add_edges_towards(id2, weight)
                node_dest.add_edge_from(id1, weight)
                self.mc += 1
                self.number_of_e += 1
                flag = True
        return flag

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """"
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        flag = False
        # if there isn't existing node with the same id - add to this graph
        if node_id not in self.all_nodes:
            new_node = Node(node_id, pos)
            self.all_nodes[node_id] = new_node
            self.mc += 1
            self.number_of_v += 1
            flag = True
        return flag

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        flag = False
        if node_id in self.all_nodes:
            node_to_remove = self.all_nodes.pop(node_id)
            # remove all the edges that this node is the destination from the source node's list
            for key in node_to_remove.edges_from:
                current_node = self.all_nodes[key]
                current_node.edges_towards.pop(node_id)
            # remove all the edges that this node is the source from the destination node's list
            for key in node_to_remove.edges_towards:
                current_node = self.all_nodes[key]
                current_node.edges_from.pop(node_id)
            del node_to_remove
            self.mc += 1
            self.number_of_v -= 1
            flag = True
        return flag

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        flag = False
        if node_id1 in self.all_nodes and node_id2 in self.all_nodes:
            node_src = self.all_nodes[node_id1]
            if node_id2 in node_src.edges_to:
                node_src.edges_to.pop(node_id2)
                self.mc += 1
                self.number_of_e -= 1
                flag = True
        return flag
