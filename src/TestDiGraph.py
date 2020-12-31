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
        node = g.all_nodes[11]
        print(node.edges_from)
        print(node.edges_towards)
        for i in range(10):
            flag = g.remove_node(i)
            if not flag:
                break
        # self.assertEqual(flag, True)

    def test_add_edge_and_remove_edge(self):
        g = DiGraph()
        for i in range(10):
            g.add_node(i)
        for i in range(4):
            g.add_edge(i, i + 3, i * 5 / 2)
        my_dict = g.get_all_v()
        for i in range(4):
            current_node = my_dict[i]
            edge_dic = current_node.edges_towards
            self.assertEqual(edge_dic[i+3], i*5/2)
            for i in range(4):
                g.remove_edge(i, i+3)
                my_dict = g.get_all_v()
                self.assertEqual()


if __name__ == '__main__':
    unittest.main()
