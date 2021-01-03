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
        t=GraphAlgo(g)
        print(t.save_to_json("hey"))
        v=GraphAlgo()
        v.load_from_json("data_file.json")
        v.get_graph().add_edge(1,3,4)
        v.save_to_json()








if __name__ == '__main__':
    unittest.main()
