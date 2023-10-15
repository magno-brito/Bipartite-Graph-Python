"""Existem M candidatos a emprego e N empregos. Cada candidato tem um subconjunto de empregos nos quais está interessado. Cada vaga de emprego só pode aceitar um candidato e um candidato pode ser nomeado para apenas um emprego. Encontre uma atribuição de empregos aos candidatos de forma que o maior número possível de candidatos consiga empregos.

https://gurobi-optimization-gurobi-optimods.readthedocs-hosted.com/en/latest/mods/bipartite-matching.html

"""


from Grafo_arquivo import Grafo_arquivo

grafo = Grafo_arquivo("file.txt").gerar_arquivo()
print(grafo[0][0])
