# Grafos Bipartidos com Python

## Grafo bipartido

<em> [No campo matemático da teoria dos grafos, um grafo bipartido (ou bigrafo) é um grafo cujos vértices podem ser divididos em dois conjuntos disjuntos e independentes U e V, ou seja, cada aresta conecta um vértice em U a um em V. Conjuntos de vértices U e V são geralmente chamados de partes do gráfico](https://en.wikipedia.org/wiki/Bipartite_graph). </em>

## O problema

<em>Existem M candidatos a uma vaga de   emprego e N empresas com vagas disponíveis buscando candidatos que saibam  programar  em uma linguagem  específica. Cada candidato tem um  subconjunto de empregos/linguagens nos  quais está interessado.</em>
<br>

<p align="center">
  <img src="https://github.com/magno-brito/Bipartite-Graph-Python/assets/84158231/d61951c7-a05f-4f4e-843c-ec9a47504fd3" width="50%" height="50%">
</p>

## Tecnologias

As principais bibliotecas utilizadas para a geração da interface e dos grafos forma

- Customertkinter
- matplotlib
- Networkx
- Tkinter
- Numpy

[Para saber mais sobre grafos bipartidos](https://tutorialhorizon.com/algorithms/maximum-bipartite-matching-problem-java/)

## Metodologia e o algoritmo

Separamos o código em dois blocos principais: a solução é onde foi implementado o algoritmo de Ford-Fulkerson com algumas modificações. Neste algoritmo um grafo é recebido como entrada e como saída é uma lista com o máximo número de combinações entre candidatos e vagas. O segundo bloco é o main onde foi feito uma interface para o usuário interagir com o problema e a solução de forma mais dinâmica. A partir das soluções, arquivos txt das listas foram criados e com eles é possível visualizar os grafos. Na interface podemos também interagir com  um grafo bipartido em 3D.

```
class GFG:
	def __init__(self,graph):
		self.graph = graph 
		self.ppl = len(graph)
		self.jobs = len(graph[0])
		self.vezes = 0

	def bpm(self, u, matchR, seen):

		for v in range(self.jobs):
			if (self.graph[u][v] != 0) and seen[v] == False:
				seen[v] = True
				if matchR[v] == -1 or self.bpm(matchR[v], 
											matchR, seen):
					matchR[v] = u
					return True
		return False
	
	def maxBPM(self):
		matchR = [-1] * self.jobs
		
		result = 0
		for i in range(self.ppl):
			seen = [False] * self.jobs
			if self.bpm(i, matchR, seen):
				result += 1

		return matchR

```
Fizemos algumas pequenas alterações no algoritmo original. Esta soluções foi baseada no código disponível na seguinte página:[Maximum Bipartite Matching](https://www.geeksforgeeks.org/maximum-bipartite-matching/)

## Resultados

[Gravação de tela de 21-11-2023 09:44:25.webm](https://github.com/magno-brito/Bipartite-Graph-Python/assets/84158231/bdd2fe0a-d85c-479a-b8b1-c517093d9197)

