import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.Graph()
# G = nx.DiGraph()
# G = nx.MultiGraph()
# G = nx.MultiDiGraph()
G.add_edge(1,2)
G.add_edge(2,3, weight=0.9)
G.add_edge("A","B")
G.add_edge("A","B")
G.add_edge("A","A")
G.add_node("C")

#We can use a list to create a graph
# edge_list = [(1,2),(2,3),(3,4),(4,4)]
# G = nx.from_edgelist(edge_list)

# print(nx.adjacency_matrix(G))

G = nx.from_numpy_array(np.array(
    [
        [0,1,0],
        [1,1,1],
        [0,0,0]
    ]
))
nx.draw_spring(G,with_labels=True)
nx.draw_circular(G,with_labels=True)
plt.show()

