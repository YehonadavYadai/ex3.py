import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_save (self):
        g=DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1,2,3)
        g.add_edge(2,3,5)
        g.add_edge(2,1,3)
        g.add_edge(1,3,3)
        t=GraphAlgo(g)
        t.save_to_json("t1.json")
        t.get_graph().add_edge(3,1,4)
        t.save_to_json("t2.json")
        t.load_from_json("t1.json")
        t.save_to_json("test.json")










if __name__ == '__main__':
    unittest.main()
