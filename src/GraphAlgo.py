import copy
from abc import ABC
from collections import deque
from queue import LifoQueue
import numpy as np
import matplotlib.pyplot as plt
import random
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json
import numpy as np
import matplotlib.pyplot as plt
import random
from GraphAttributes import Node
from types import SimpleNamespace


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph()):

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
        g_loaded = DiGraph()
        file = open(file_name)
        loaded_json = json.load(file)
        node_from_json = loaded_json["Nodes"]
        for currentNode in node_from_json:
            id = currentNode["id"]
            if len(currentNode) > 1:
                list_pos = currentNode['pos'].split(",")
                x = float(list_pos[0])
                y = float(list_pos[1])
                pos = (x, y)
                g_loaded.add_node(id, pos)  # add the node with his "pos"
            else:
                g_loaded.add_node(id)
        edges_From_Json = loaded_json["Edges"]
        for curretnEdge in edges_From_Json:
            g_loaded.add_edge(curretnEdge["src"], curretnEdge["dest"], curretnEdge["w"])
        file.close()
        self.g = g_loaded
        return True

    def save_to_json(self, file_name: str = "save.json") -> bool:
        """
              Saves the graph in JSON format to a file
              @param file_name: The path to the out file
              @return: True if the save was successful, False o.w.
                     """


        arrNodes = []
        arrEdges = []

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
            print(e)
            return False


    """
    Saves the graph in JSON format to a file
    @param Node: current node we want to check his pos in the plot
    @param limit: tuple of limits of the plot
    @return: it the node have pos return his pos , if he does not have ,return random pos in the limit
                         """

    def getPos(self, v: Node, limit):
        if v.x() is None:
            temp_x = random.randint(limit[0], limit[1])
        else:
            temp_x = v.x()
        if v.y() is None:
            temp_y = random.randint(limit[2], limit[3])
        else:
            temp_y = v.y()
        return temp_x, temp_y

    """
    gives the limit of the plot from the pos of the nodes of the graph
    
    @return: tuple of the limits of the graph(max and min value of x and y from all the nodes)
            if all nodes dont have pos as diff we set 0 to 10 min and max value of x,y.
                         """

    def getLimits(self):
        nodes = self.g.get_all_v()
        x = []
        y = []

        for k, v in nodes.items():  # check limits of random unknow pos nodes
            if v.x() is not None:
                x.append(v.getPos()[0])
                y.append(v.getPos()[1])
        if len(x) == 0:
            x_max = 10
            x_min = 0
        else:
            x_max = max(x)
            x_min = min(x)
        if len(y) == 0:
            y_max = 10
            y_min = 0
        else:
            y_max = max(y)
            y_min = min(y)
        return x_min, x_max, y_min, y_max

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None
            """

    def plot_graph(self) -> None:
        nodes = self.g.get_all_v()
        # tuple that hold the limit of the graph
        limit = self.getLimits()
        # dict that hold {id:(x,y)}
        nodes_pos = dict()
        # add the nodes to the plot
        for k, v in nodes.items():
            c_pos = self.getPos(v, limit)
            nodes_pos[k] = c_pos
            plt.text(c_pos[0], c_pos[1], k, color='green')
            plt.plot(c_pos[0], c_pos[1], 'o', color='red')

        # dest of salnt of the limit fo the graph
        l_min = [limit[0], limit[2]]  # let down
        l_max = [limit[1], limit[3]]  # right up
        dif = np.math.dist(l_min, l_max)

        # add arrow for each edge of the graph
        for id_s in nodes.keys():
            edges_to = self.g.all_out_edges_of_node(id_s)
            for id_d in edges_to.keys():
                x1 = nodes_pos[id_s][0]  # x of src
                y1 = nodes_pos[id_s][1]  # y of src
                x2 = nodes_pos[id_d][0]
                y2 = nodes_pos[id_d][1]
                # doing some math for the size of the edge and the heaf of the edge
                p = [x2, y2]
                q = [x1, y1]
                dis = np.math.dist(q, p)
                a = dis / dif
                plt.arrow(x1, y1, x2 - x1, y2 - y1, head_width=dis / 30, width=a / 10000, color="black",
                          length_includes_head=True)
        plt.show()
