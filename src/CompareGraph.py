import datetime
import time
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    g = DiGraph()
    k = GraphAlgo(g)
    start_time = datetime.datetime.now()
    print(k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_10_80_1.json"))
    k.plot_graph()
    print(k.shortest_path(5, 4))
    c = datetime.datetime.now() - start_time
    print("--- %s milliseconds ---" % c.total_seconds()*1000 )


if __name__ == '__main__':
    unittest.main()
