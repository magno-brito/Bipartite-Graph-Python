import networkx as nx
import matplotlib.pyplot as plt

# Dados do grafo bipartido
grafo_bipartido = {'a': [1, 3], 'b': [3], 'c': [2, 4], 'd': [1, 5]}

# Crie um grafo bipartido vazio
G = nx.Graph()

# Separe os nós em conjuntos distintos
conjunto1 = ['a', 'b', 'c', 'd']
conjunto2 = [1, 2, 3, 4, 5]

# Adicione os nós aos conjuntos correspondentes
G.add_nodes_from(conjunto1, bipartite=0)
G.add_nodes_from(conjunto2, bipartite=1)

# Adicione as arestas entre os conjuntos
for key, values in grafo_bipartido.items():
    for value in values:
        G.add_edge(key, value)

# Defina as cores para os conjuntos
cores_conjunto1 = 'blue'
cores_conjunto2 = 'red'

# Desenhe o gráfico com cores diferentes para cada conjunto
pos = nx.bipartite_layout(G, conjunto1)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color=[cores_conjunto1 if node in conjunto1 else cores_conjunto2 for node in G.nodes()], font_size=12, width=1.5, edge_color='gray')
plt.show()
