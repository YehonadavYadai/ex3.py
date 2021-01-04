import unittest
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_add_node(self):
        g = DiGraph()
        flag = True
        for i in range(10):
            g.add_node(i)
            if not flag:
                break
        self.assertEqual(flag, True)

    def test_remove_node(self):
        g = DiGraph()
        flag = True
        g.add_node(11)
        for i in range(10):
            g.add_node(i)
            g.add_edge(i, 11, 1)
        for i in range(10):
            flag = g.remove_node(i)
            if not flag:
                break
        self.assertEqual(flag, True)

    def test_add_edge_and_remove_edge(self):
        g = DiGraph()
        # adding nodes to the graph
        for i in range(10):
            g.add_node(i)
        # creating edges
        for i in range(4):
            g.add_edge(i, i + 3, i * 5 / 2)
        my_dict = g.get_all_v()
        # checking if the edges successfully added in the node
        for i in range(4):
            current_node = my_dict[i]
            edge_dic = current_node.edges_towards
            self.assertEqual(edge_dic[i + 3], i * 5 / 2)
            # removing the edges
        for i in range(4):
            g.remove_edge(i, i + 3)
        my_dict = g.get_all_v()
        flag = True
        # checking if the edges were removed successfully
        for i in range(4):
            current_node = my_dict[i]
            empty_dict = {}
            if empty_dict != current_node.edges_towards:
                flag = False
                break
        self.assertEqual(True, flag)

    def test_v_size(self):
        counter = 0
        g = DiGraph()
        for i in range(10000):
            g.add_node(i)
            counter += 1
        for i in range(500):
            g.remove_node(i)
            counter -= 1
        self.assertEqual(counter, g.v_size())

    def test_e_size(self):
        counter = 0
        g = DiGraph()
        for i in range(10000):
            g.add_node(i)
        for i in range(500):
            g.add_edge(i, (i + 1) * 10, i * 10 / 5)
            counter += 1
        self.assertEqual(counter, g.e_size())
        for i in range(100):
            g.remove_edge(i, (i + 1) * 10)
            counter -= 1
        self.assertEqual(counter, g.e_size())

    def test_get_all_v(self):
        g = DiGraph()
        my_dict = {}
        for i in range(10000):
            g.add_node(i)
            current_node = g.get_all_v()[i]
            my_dict[i] = current_node
        self.assertEqual(my_dict, g.get_all_v())

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        my_dict = dict()
        for i in range(15):
            g.add_node(i)
        for i in range(9):
            g.add_edge(i + 2, 0, i * 5)
            my_dict[i + 2] = i * 5
        self.assertEqual(my_dict, g.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        my_dict = dict()
        for i in range(15):
            g.add_node(i)
        for i in range(9):
            g.add_edge(0, i + 2, i * 5)
            my_dict[i + 2] = i * 5
        self.assertEqual(my_dict, g.all_out_edges_of_node(0))

    def test_get_mc(self):
        counter = 0
        g = DiGraph()
        for i in range(10000):
            g.add_node(i)
            counter += 1
        for i in range(500):
            g.add_edge(i, (i + 1) * 10, i * 10 / 5)
            counter += 1
        for i in range(100):
            g.remove_edge(i, (i + 1) * 10)
            counter += 1
        self.assertEqual(counter, g.get_mc())


if __name__ == '__main__':
    unittest.main()
