import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

grafo1 = [[2], [3], [0],[1]]

# Convertendo a lista de adjacências para uma matriz de adjacência
matriz_adjacencia = np.zeros((len(grafo1), len(grafo1)), dtype=int)
for i, adj_list in enumerate(grafo1):
    for adj in adj_list:
        matriz_adjacencia[i][adj] = 1

grafo = nx.from_numpy_array(matriz_adjacencia)
nx.draw_networkx(grafo, with_labels=True)
plt.show()