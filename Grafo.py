#Create a graph
#Verify wether a graph is bipartite or not

from collections import deque


class Grafo:

    def __init__(self, vertice):
        self.vertice = vertice
        self.lista_adj = [[] for i in range(self.vertice)]
        
    def add_aresta_lista(self, v1, v2):
        if(v1 == v2):
            pass
        else:
            self.lista_adj[v1].append(v2)
            self.lista_adj[v2].append(v1)
            print("")

    def add_lista(self, lista):
        if len(lista) == self.vertice:
            for i in range(len(lista)):
                for k in lista[i]:
                    print(k, end="")
                    self.lista_adj[i].append(k)
                print("")

    def mostra_lista(self):
        print("Lista de adjacências")
        for i in range(self.vertice):
            print(f'{i}:', end=" ")
            for j in self.lista_adj[i]:
                print(f'{j} -> ', end="")
            print("")

    def pega_lista(self):
        return self.lista_adj
    
    def isBipartite(self, graph) -> bool:
        color = {}
        def dfs(curr_node, curr_color):
            
            if curr_node in color:
                if color[curr_node] != curr_color:
                    return False
                else:
                    return True
            else:
                color[curr_node] = curr_color
            for each_node in graph[curr_node]:
                if not dfs(each_node, not curr_color):
                    return False
            return True
        
        for all_node in range(len(graph)):
            if all_node not in color:
                if not dfs(all_node, True):
                    return False
        return True
    

g = Grafo(5)






grafo1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
grafo3 = [[1, 3, 4], [0, 2], [1, 3], [0, 2], [0]]

g.add_lista(grafo3)

print(g.mostra_lista())

print(g.isBipartite(g.pega_lista()))

