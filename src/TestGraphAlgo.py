import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_connected_component_b(self):
        g = DiGraph()
        k = GraphAlgo(g)
        for i in range(10):
            g.add_node(i)
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
        all_components = [{0, 1, 2}, {3, 7}, {4, 5, 6}, {8}, {9}]  # all the components in the graph
        self.assertEqual(all_components, k.connected_components())

    def test_connected_component_a(self):
        g = DiGraph()
        k = GraphAlgo(g)
        for i in range(10):
            g.add_node(i)
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
        l0 = k.connected_component(0)
        l1 = k.connected_component(1)
        l2 = k.connected_component(2)
        l3 = k.connected_component(3)
        l4 = k.connected_component(4)
        l5 = k.connected_component(5)
        l6 = k.connected_component(6)
        l7 = k.connected_component(7)
        self.assertEqual(l0, l1, l2)  # one component
        self.assertEqual(l3, l7)  # one component
        self.assertEqual(l4, l5, l6)  # one component

    def test_transpose(self):
        g = DiGraph()
        k = GraphAlgo(g)
        for i in range(10):
            g.add_node(i)
        g.add_edge(0, 1, 2)
        g.add_edge(1, 2, 2)
        g.add_edge(3, 8, 6)
        g.add_edge(8, 9, 5)
        g.add_edge(7, 4, 1)
        g_t = k.transpose()
        # if there isn't existing edge - return true
        self.assertTrue(g_t.add_edge(0, 1, 2))
        self.assertTrue(g_t.add_edge(1, 2, 2))
        self.assertTrue(g_t.add_edge(3, 8, 6))
        self.assertTrue(g_t.add_edge(8, 9, 5))
        self.assertTrue(g_t.add_edge(7, 4, 1))
        # if there is existing edge - return false
        self.assertFalse(g_t.add_edge(1, 0, 2))
        self.assertFalse(g_t.add_edge(2, 1, 2))
        self.assertFalse(g_t.add_edge(8, 3, 6))
        self.assertFalse(g_t.add_edge(3, 8, 5))
        self.assertFalse(g_t.add_edge(4, 7, 1))
        self.assertEqual(g_t.v_size(), g.v_size())

    def test_dfs(self):
        g = DiGraph()
        k = GraphAlgo(g)
        for i in range(100):
            g.add_node(i)
        g.add_edge(4, 1, 2)
        g.add_edge(1, 10, 2)
        g.add_edge(10, 1, 2)
        g.add_edge(9, 6, 6)
        self.assertEqual([1, 10], k.dfs(1, g))
        self.assertEqual([4, 1, 10], k.dfs(4, g))
        self.assertEqual([9, 6], k.dfs(9, g))
        self.assertEqual([6], k.dfs(6, g))
        self.assertEqual([20], k.dfs(20, g))


    def test_shortest_path(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        k = GraphAlgo(g)
        self.assertEqual((float('inf'), ()), k.shortest_path(0, 9))
        g.add_edge(0, 1, 2)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 6.2)
        g.add_edge(3, 2, 1)
        g.add_edge(0, 3, 3)
        g.add_edge(0, 8, 16)
        g.add_edge(0, 4, 14)
        g.add_edge(0, 5, 3)
        g.add_edge(5, 6, 15)
        g.add_edge(5, 7, 7)
        g.add_edge(4, 7, 2.5)
        g.add_edge(7, 9, 3)
        g.add_edge(7, 8, 4)
        g.add_edge(8, 1, 9)
        dis, l = k.shortest_path(0, 9)
        self.assertEqual(l, [0, 5, 7, 9])
        self.assertEqual(dis, 13)
        g.remove_node(9)
        g.add_node(9)
        self.assertEqual((float('inf'), ()), k.shortest_path(0, 9))

    def test_load_from_json(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 5)
        g.add_edge(2, 1, 3)
        g.add_edge(1, 3, 3)
        t = GraphAlgo(g)
        t.save_to_json("t1.json")
        t.get_graph().add_edge(3, 1, 4)
        t.save_to_json("t2.json")
        t.load_from_json("t1.json")
        t.save_to_json("test.json")


if __name__ == '__main__':
    unittest.main()
