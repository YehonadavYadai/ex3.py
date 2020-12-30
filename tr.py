from Ex3.DiGraph import DiGraph

if __name__ == '__main__':
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    for i in range(4):
        g.add_edge(i, i + 3, i * 5 / 2)
    my_dict = g.get_all_v()
    for i in range(4):
        current_node = my_dict[i]
        edge_dic = current_node.edges_towards
        print(edge_dic[i+3])
        # current_edge = edge_dic[i]

