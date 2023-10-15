import networkx as nx
import matplotlib.pyplot as plt

grafo1 = [[1, 3], [0, 2], [1, 3], [0, 2]]

m, n = 4, 4

K = nx.complete_bipartite_graph(m, n)
pos = {}
pos.update((i, (i - m/2, 1)) for i in range(m))
pos.update((i, (i - m - n/2, 0)) for i in range(m, m + n))

fig, ax = plt.subplots()
fig.set_size_inches(15, 4)
nx.draw(K, with_labels=True, pos=pos, node_size=300, width=0.4)
plt.show()