import math

from GraphAlgoInterface import GraphAlgoInterface
from GraphAttributes import *
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json
from GraphAttributes import Node
from types import SimpleNamespace


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, hey=DiGraph()):
        self.g = hey

    def get_graph(self) -> GraphInterface:
        return self.g

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        graph = self.get_graph()
        # if one of the nodes isn't in the graph
        if id1 not in graph.get_all_v() or id2 not in graph.get_all_v():
            return -1
        graph_size = graph.v_size()
        visited = [False]  # list to mark if node has been visited
        visited *= graph_size
        prev = dict()  # list that holds the id of the nodes by order of the shortest path
        distance = [math.inf]  # list that holds the current distance between a node to given source node. At first
        # all initiates to infinity
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
        if distance[at] is math.inf:
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
        return distance[dest_node.get_tag()], path_result

    def load_from_json(self, file_name: str) -> bool:
        """
                  Loads a graph from a json file.
                  @param file_name: The path to the json file
                  @returns True if the loading was successful, False o.w.
                  """
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
