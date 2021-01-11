import copy
from abc import ABC
from collections import deque
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph):
        self.g = g

    def set_g(self, g: DiGraph):
        self.g = g

    def get_graph(self) -> GraphInterface:
        return self.g

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        graph = self.get_graph()
        # if one of the nodes isn't in the graph
        if id1 not in graph.get_all_v() or id2 not in graph.get_all_v():
            return float('inf'), []
        graph_size = graph.v_size()
        visited = [False]  # list to mark if node has been visited
        visited *= graph_size
        prev = dict()  # list that holds the id of the nodes by order of the shortest path
        distance = list()
        distance.append(float('inf'))  # list that holds the current distance between a node to given source node.
        # At first, all elements initiates to infinity
        distance *= graph_size
        nodes_in_graph = dict()  # dictionary that holds the graph's nodes for comfort use - key: node's tag,
        # value: node address
        pq = dict()  # dictionary that used as priority Q - key: node's tag, value: node's current shortest distance
        # from source node
        i = 0
        # tagging all the nodes and updating the above lists
        for node_id in graph.get_all_v():
            node = graph.get_all_v()[node_id]
            node.set_tag(i)
            nodes_in_graph[i] = node
            prev[i] = None
            i += 1
        src_node = graph.get_all_v()[id1]
        distance[src_node.get_tag()] = 0  # distance of a node to itself is 0
        prev[src_node.get_tag] = src_node.get_tag
        pq[src_node.get_tag()] = 0
        while pq:
            keys = list(pq.keys())
            val = list(pq.values())
            min_value = min(val)  # priority Q - always takes the smallest cost node as next
            tag = keys[val.index(min_value)]  # the node index in pq
            pq.pop(tag)
            visited[tag] = True
            if distance[tag] <= min_value:
                current_node = nodes_in_graph[tag]
                # adding all the neighbors nodes that weren't already in the graph
                for node_id in current_node.edges_towards:
                    neighbor = graph.get_all_v()[node_id]
                    neighbor_tag = neighbor.get_tag()
                    if not visited[neighbor_tag]:
                        new_dist = distance[tag] + current_node.edges_towards[node_id]
                        if new_dist < distance[neighbor_tag]:
                            distance[neighbor_tag] = new_dist
                            prev[neighbor_tag] = current_node.get_tag()
                            pq[neighbor_tag] = distance[neighbor_tag]
        dest_node = graph.get_all_v()[id2]
        at = dest_node.get_tag()
        path = list()
        # if there's no path
        if distance[at] == float('inf'):
            path = ()
            return distance[at], path
        i = 0
        while at != src_node.get_tag:
            path.append(at)
            if prev[at] is None:
                break
            at = prev[at]
            i += 1
        path.reverse()
        path_result = list()
        for tag in path:
            node_id = nodes_in_graph[tag].get_id()
            path_result.append(node_id)
        dest_tag = dest_node.get_tag()
        for data in graph.get_all_v():
            node = graph.get_all_v()[data]
            node.set_tag(None)
        return distance[dest_tag], path_result

    def transpose(self):
        """ Returns the transpose of self's graph."""
        g = self.get_graph()
        ans = copy.deepcopy(g)
        # cleaning all edges
        for node_id in ans.get_all_v():
            current_node = ans.get_all_v()[node_id]
            nodes_to_current = copy.deepcopy(current_node.edges_from)
            nodes_from_current = copy.deepcopy(current_node.edges_towards)  # current node's edges dict  it's the source
            for dest in nodes_from_current:
                ans.remove_edge(node_id, dest)
            for src in nodes_to_current:
                ans.remove_edge(src, node_id)
        for node_id in g.get_all_v():
            node = g.get_all_v()[node_id]
            for neighbor_id in node.edges_from:
                edge_weight = node.edges_from[neighbor_id]
                ans.add_edge(node_id, neighbor_id, edge_weight)
        return ans

    def connected_component(self, id1: int):
        g = self.get_graph()
        # if id1 not in the graph
        if id1 not in g.get_all_v():
            raise Exception
        component = self.dfs(id1, g)
        g_t = self.transpose()
        component_t = self.dfs(id1, g_t)
        s = set(component).intersection(component_t)
        ans = list()
        for value in s:
            ans.append(value)
        # removing info from dfs
        for node_id in g.get_all_v():
            node = g.get_all_v()[node_id]
            node.info = ''
        return ans

    def connected_components(self):
        my_list = list()
        ans = list()
        g = self.get_graph()
        # if id1 not in the graph
        for node_id in g.get_all_v():
            component = self.dfs(node_id, g)
            g_t = self.transpose()
            component_t = self.dfs(node_id, g_t)
            s = set(component).intersection(component_t)
            my_list.append(s)
        for node_id in g.get_all_v():
            node = g.get_all_v()[node_id]
            node.info = ''
        for i in my_list:
            if i not in ans:
                ans.append(i)
        return ans

    def dfs(self, id1: int, g: DiGraph) -> list:
        ans = list()
        ans.append(id1)
        for node_id in g.get_all_v():
            node = g.get_all_v()[node_id]
            node.info = 'X'
        stack = deque()
        stack.append(id1)
        while stack:
            current_node = g.get_all_v()[stack.pop()]
            if current_node.info != 'V':
                current_node.info = 'V'
            for neighbor_id in current_node.edges_towards:
                neighbor = g.get_all_v()[neighbor_id]
                if neighbor.info != 'V':
                    stack.append(neighbor_id)
                    ans.append(neighbor_id)
        return ans

    def load_from_json(self, file_name: str) -> bool:
        """ Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w."""
        g = DiGraph()
        file = open(file_name)
        loaded_json = json.load(file)
        node_from_json = loaded_json["Nodes"]
        for currentNode in node_from_json:
            id = currentNode["id"]
            if len(currentNode) > 1:
                self.g.add_node(id, currentNode["pos"])
            else:
                self.g.add_node(id)
        edges_From_Json = loaded_json["Edges"]
        for curretnEdge in edges_From_Json:
            g.add_edge(curretnEdge["src"], curretnEdge["dest"], curretnEdge["w"])
        file.close()
        return True

    def save_to_json(self, file_name: str = "save.json") -> bool:
        """
              Saves the graph in JSON format to a file
              @param file_name: The path to the out file
              @return: True if the save was successful, False o.w.
                     """

        json_to_save = {}
        arrNodes = []
        arrEdges = []
        i = 0
        nodes = self.g.get_all_v()  # dict with {key:Node}
        try:
            with open(file_name, "w")as write_file:
                for key in nodes.keys():  #
                    arrNodes.append({"id": key})
                    for dest, w in self.g.all_out_edges_of_node(key).items():
                        arrEdges.append({"src": key, "dest": dest, "w": w})

                json_to_save = {'Nodes': arrNodes, "Edges": arrEdges}
                json.dump(json_to_save, write_file)
                return True

        except IOError as e:
            return False
            print(e)
