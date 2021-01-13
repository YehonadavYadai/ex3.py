# Object-Oriented Programming Course Assignment #3
Authors: Raphael Suliman and Yehonadav Yadai
this project is to implement directed weighted data structure and graph algorithms using Python Programming language, in this project we have three parts:

# DiGraph class:
main methods:
1. add_edge- add edge to the Graph with the wighte of the edge, return True if the edge was added to the Graph, False if not.

2. add_node- add node to the Graph, return True if the node was added to the Graph, false if not .

3. all_out_edges_of_node)- return a dict of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight) 

4. get_all_v- return a dict of all the nodes in the Graph, each node is represented using a pair (node_id, node_data). 

5. all_in_edges_of_node(self, id1: int)- return a dict of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight).

6. remove_node(node_id) - remove node from the graph and all the connections with other nodes

7. remove_edge(node1_id, node2_id) - removing connection between node1_id and node2_id

8. e_size- Returns the number of edges in this graph O(1)

9. get_mc() - return graph mode count

# GraphAlgo class:
 main methods:
1. get_graph- return the init graph

2. save_to_json- save the graph to  json file with the file name that is given

3. load_from_json - load the graph from a json file by the give file name

4. shortest_path - compute the shortest path between to nodes using Dijkstra's algorithm, and return tuple that holds (weight, path)

5. connected_component- search and find the Strongly Connected Component(SCC) that node id1 is a part of him.

6. connected_components- Finds all the Strongly Connected Component(SCC) in the graph. 

7. plot_graph-Plot The Graph


# Comparisons:

in ths part we will compare the algorithms between EX2 that we built in java and beyween NetWorkX LIbary , libary that build and have algo for Graphs.




