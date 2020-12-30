from Ex3.DiGraph import DiGraph

if __name__ == '__main__':
    g = DiGraph()
    g.add_node(4)
    dict = {1:("a","c")}
    print(g.remove_node(3))
    print(type(dict[1]))
    print(g.all_in_edges_of_node(4))