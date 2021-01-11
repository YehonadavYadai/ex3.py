import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import numpy as np
import matplotlib.pyplot as plt
import random
if __name__ == '__main__':

   k=GraphAlgo()
   k.load_from_json("A1")

   #lets add the graph and draw with networkx
   print(k.get_graph().get_all_v())
   g=nx.Graph()
   for key in k.get_graph().get_all_v().keys():
      print(key)
      g.add_node(key)



   nx.draw(g,with_labels=1)
   plt.show()