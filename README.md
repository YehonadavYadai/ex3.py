# Object-Oriented Programming Course Assignment #3
Authors: Raphel Suliman and Yehonadav Yadai
this project is to implement directed weighted data structure and graph algorithms using Python Programming language, in this project we have three parts:

##DiGraph class:
### main methods:
add_edge- add edge to the Graph with the wighte of the edge, return True if the edge was added to the Graph, False if not.

add_node- add node to the Graph, return True if the node was added to the Graph, false if not .

all_out_edges_of_node)- return a dict of all the nodes connected from node_id , each node is represented using a pair
(other_node_id, weight) 

get_all_v- return a dict of all the nodes in the Graph, each node is represented using a pair (node_id, node_data). 

all_in_edges_of_node(self, id1: int)- return a dict of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight).

remove_node(node_id) - remove node from the graph and all the connections with other nodes

remove_edge(node1_id, node2_id) - removing connection between node1_id and node2_id

e_size- Returns the number of edges in this graph O(1)

get_mc() - return graph mode count

##GraphAlgo class:
### main methods:
