import networkx as nx
import matplotlib.pyplot as plt


f = open("file.txt")
lines = f.read().split("\n")
vetor = list()
for i in lines:
    vetor.append(i.split("-"))

for i in range(len(vetor)):
    vetor[i][1] = vetor[i][1].split()


dicionario = dict()
for item in vetor:
    chave = item[0].strip()
    valor = item[1]
    dicionario[chave] = valor


lista = list(dicionario.keys())



#-------------------------------------------------#

G = nx.Graph()
conjunto1 = list(dicionario.keys())
conjunto2 = list()

vetor = list(dicionario.values())
for i in vetor:
    for p in i:
        if p not in conjunto2:
            conjunto2.append(p)


print(conjunto2)
print(conjunto1)
    
G.add_nodes_from(conjunto1, bipartite=0)
G.add_nodes_from(conjunto2, bipartite=1)

for key, values in dicionario.items():
    for value in values:
        G.add_edge(key, value)

corA = "blue"
corB = "red"

pos = nx.bipartite_layout(G, conjunto1)
plt.figure(figsize=(8,6))

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color = [corA if node in conjunto1 else corB for node in G.nodes()], font_size=12, width=1.5, edge_color='gray')
plt.show()
