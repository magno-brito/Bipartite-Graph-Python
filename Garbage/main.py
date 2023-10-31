"""Existem M candidatos a emprego e N empregos. Cada candidato tem um subconjunto de empregos nos quais está interessado. Cada vaga de emprego só pode aceitar um candidato e um candidato pode ser nomeado para apenas um emprego. Encontre uma atribuição de empregos aos candidatos de forma que o maior número possível de candidatos consiga empregos.

# acha o caminho de aumento
# aumenta emparelhamento
# com o resultado das funções anteriores aumenta o emparelhamento parcial

# Este algorítmo encontra emparelhamento máximo em grafos bipartidos

https://gurobi-optimization-gurobi-optimods.readthedocs-hosted.com/en/latest/mods/bipartite-matching.html

"""

"""
    1) Ler o arquivo e gerar um grafo a partir dele
    2) Verificar se este grafo é bipartido e gerar o grafo com as conexões
    3) Chamar a solução e gerar o número máximo de combinações
    4) Plotar o grafo novamente porém agora mostrando as novas combinações
"""


from Garbage.Grafo_arquivo import Grafo_arquivo
from Solucao import GFG
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#Ler arquivo e pegar grafo
grafo = Grafo_arquivo("file.txt").gerar_arquivo()
print(grafo)



