import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox



f = open("arquivos/file1.txt")
lines = f.read().split("\n")
vetor = list()

for i in lines:
    vetor.append(i.split("-"))

print(vetor)


for i in range(0,len(vetor)):
    print(i)
    if vetor[i][1]:
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
        print(key, values)
        G.add_edge(key, value)

corA = "white"
corB = "white"

pos = nx.bipartite_layout(G, conjunto1)
plt.figure(figsize=(8,6))


for node in conjunto2:
    path = "languages/" + node.lower() + ".png"
    image_path = path.format(node) 
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.4)
    imagebox.image.axes = plt.gca()
    ab = AnnotationBbox(imagebox, pos[node], frameon=False)
    plt.gca().add_artist(ab)
    

for node in conjunto1:
    path = "people/" + node.lower() + ".png"
    image_path = path.format(node) 
    image = plt.imread(image_path)
    imagebox = OffsetImage(image, zoom=0.4)
    imagebox.image.axes = plt.gca()
    ab = AnnotationBbox(imagebox, pos[node], frameon=False)
    plt.gca().add_artist(ab)


connection_colors = {
    "Python": "Blue",
    "Java" : "Green",
    "PHP" : "Red",
    "C#" : "Purple",
    "C++": "Orange"
}   

edge_colors = [connection_colors[dicionario[u][dicionario[u].index(v)]] for u, v in G.edges()]

nx.draw(
    G,
    pos,
    with_labels=False,
    node_size=3000,
    node_color=[corA if node in conjunto1 else corB for node in G.nodes()],
    font_size=12,
    width=1.5,
    edge_color=edge_colors
)
plt.show()






