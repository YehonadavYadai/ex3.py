from GraphAlgoInterface import GraphAlgoInterface
from GraphAttributes import *
from DiGraph import DiGraph
from src import GraphInterface
import json
from GraphAttributes import Node
from types import SimpleNamespace


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, hey=DiGraph()):
        self.g = hey

    def get_graph(self) -> GraphInterface:
        return self.g

    """
           Loads a graph from a json file.
           @param file_name: The path to the json file
           @returns True if the loading was successful, False o.w.
           """

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        file=open(file_name)
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

        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
               """

    def save_to_json(self, file_name: str = "save.json") -> bool:
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
