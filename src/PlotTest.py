import unittest
import math
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import numpy as np
import matplotlib.pyplot as plt
import random


if __name__ == '__main__':
    g = DiGraph()
    for i in range(10):
        g.add_node(i,(i,i+1))
    g.add_edge(3, 4, 1)
    g.add_edge(3, 7, 1)
    g.add_edge(7, 3, 1)
    g.add_edge(7, 5, 1)
    g.add_edge(5, 0, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(6, 4, 1)
    g.add_edge(6, 0, 1)
    g.add_edge(6, 2, 1)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 0, 1)
    g.add_node(10)

    k=GraphAlgo(g)
    #k.plot_graph()
    k.load_from_json("A5")

    k.plot_graph()


