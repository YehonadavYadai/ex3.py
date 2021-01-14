import copy
import math
from collections import deque
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import json
import datetime
import time
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx

from GraphAttributes import Node
from types import SimpleNamespace
def time_ms() :
    return int(round(time.time() * 1000))

def net2(file_name):
    try:
        with open(file_name, "r")as file:
            graph_dict = json.load(file)
            nodes = graph_dict.get("Nodes")
            edges = graph_dict.get("Edges")
            return (nodes, edges)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    ga=GraphAlgo()
    graphs = ["G_10_80_1.json", "G_100_800_1.json", "G_1000_8000_1.json", "G_10000_80000_1.json",
              "G_20000_160000_1.json"
        , "G_30000_240000_1.json"]
    paths = [(0, 9), (1, 99), (1, 999), (1, 9000), (1, 18000), (1, 29979)]
    for number in range(6):
        file_name = graphs[number]
        ga.load_from_json(file_name)
        print("graph" + str(file_name))
        dicts = net2(file_name)
        nodes=dicts[0]
        edges=dicts[1]
        graph=nx.DiGraph()
        for currentNode in nodes:
            id=currentNode.get('id')
            #print(id)
            graph.add_node(graph)
        for e in edges:
            src=e.get('src')
            dest=e.get('dest')
            w=e.get('w')
            graph.add_edge(src,dest,weight=w)

        src=paths[number][0]
        dest=paths[number][1]
        nx.dijkstra_path(graph,source=src,target=dest,weight='weight')

        print("Networkx time")
        #NetWork - ShortestPath
        start =time_ms()
        strong = nx.strongly_connected_components(graph)
        end =time_ms()
        print("shortestPath - time:"+str(end - start) + " ms")


        #NetWork - componets
        start =time_ms()
        components = nx.strongly_connected_components(graph)
        for i in components:
            if 0 in i:
                break
        end =time_ms()
        print("componet - time:"+str(end - start) + " ms")


        #Network - componet
        start = time_ms()
        nx.strongly_connected_components(graph)
        end = time_ms()
        print("componet - time:"+str(end - start) + " ms")



        print("GA time:")
        #GraphAlgo - Shortestpath
        start =time_ms()
        ga.shortest_path(src,dest)
        end = time_ms()
        print("shortestPath - time:"+str(end - start)+" ms")


        #GraphAlgo - componets
        start =time_ms()
        l=ga.connected_components()
        end =time_ms()
        # print(nx.edges(graph))
        print("componets - time:"+str(end - start) + " ms")


        #GraphAlgo - compnet
        start =time_ms()
        l=ga.connected_component(0)
        end = time_ms()
        # print(nx.edges(graph))
        print("componet - time:"+str(end - start) + " ms")

        print("")
        print("")




