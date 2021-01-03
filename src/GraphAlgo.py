from GraphAlgoInterface import GraphAlgoInterface
from GraphAttributes import *
from DiGraph import DiGraph
from src import GraphInterface
import json
from types import SimpleNamespace



class GraphAlgo(GraphAlgoInterface):

    def __init__(self,hey=DiGraph()):
        self.g = hey

    def get_graph(self) -> GraphInterface:
        return self.g
    """
           Loads a graph from a json file.
           @param file_name: The path to the json file
           @returns True if the loading was successful, False o.w.
           """

    # def makeJson (self):
    #     str_Json= json.dump(self.g.__dict__)
    #     return str_Json

    # def load_from_json(self, file_name: str) -> bool:
    #     new_graph = {}
    #     try:
    #         with open(file_name,"r") as json_file:
    #              my_dict=json.load(json_file)
    #              for  k,v in my_dict.items() :
    #                  hey=DiGraph(**v)
    #                 new_graph[k]=hey
    #         return True
    #     except IOError as e:
    #         print(e)
    #         return False
    #
    #     self.g = new_graph.__dict__


        #
        # """
        # Saves the graph in JSON format to a file
        # @param file_name: The path to the out file
        # @return: True if the save was successful, False o.w.
        #        """w

    # def save_to_json(self, file_name: str="save.json") -> bool:
    #     arr=[]
    #     i=0
    #     nodes=self.g.get_all_v()
    #     try:
    #         with open("data_file.json","w")as write_file:
    #          for key in nodes.keys():#
    #             arr.append({key:nodes[key]})
    #
    #             return True
    #
    #     except IOError as e:
    #         print(e)











