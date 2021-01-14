import datetime
import time
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_Graph_G_10_80_1(self):
        print("G_10_80_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_10_80_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)

    def test_Graph_G_100_800_1(self):
        print("G_100_800_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_100_800_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)

    def test_Graph_G_1000_8000_1(self):
        print("G_1000_8000_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_1000_8000_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)

    def test_Graph_G_10000_80000_1(self):
        print("G_10000_80000_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_10000_80000_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)

    def test_Graph_G_20000_160000_1(self):
        print("G_20000_160000_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_20000_160000_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)

    def test_Graph_G_30000_240000_1(self):
        print("G_30000_240000_1:")
        g = DiGraph()
        k = GraphAlgo(g)
        start_time = datetime.datetime.now()
        k.load_from_json("C:/Users/Stycks/PycharmProjects/Ex3 -- PY/resources/G_30000_240000_1.json")
        #  k.plot_graph()
        k.shortest_path(5, 4)
        c = datetime.datetime.now() - start_time
        print("----------shortest path:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_component(8)
        c = datetime.datetime.now() - start_time
        print("----connected component:  %s microseconds ---" % c)
        start_time = datetime.datetime.now()
        k.connected_components()
        c = datetime.datetime.now() - start_time
        print("---connected components:  %s microseconds ---" % c)


if __name__ == '__main__':
    unittest.main()
