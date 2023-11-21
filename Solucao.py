
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
	
#-------------------------------------------------------------------------------

# Grafo menor

grafo3 = [
	["Pyhont", "Java"], 
	["Python",0],
	[0,"Java",],
	]

# Grafo maior

grafo4 = [ 
	["Java","Python","C#", 0, 0, 0], 
	["Java","Python",0,0,0,0],
	["Java",0,0,0,0,0],
	[0,"Python",0, "C++",0,0], 
  	[0,0,"C\#","C++","PHP","Js"],
	[0,0,0,"C++",0,0],
	[0,0,0,0,0,"Js"], 
	[0,0,0,0,"PHP","Js"]
	]

# Ordem das linguagens -> Python Java C# C++ PHP Js
# Cada indice do vetor grafo3 corresponde a uma pessoa: index[0] = a; index[1] = b

g = GFG(grafo3)

print ("Grafo menor")
print(g.maxBPM())


#-----------------------------------------
# Esta parte é para atribuir cada nome de pessoa e linguagem a list retornada da classe GFG
# A ordem dos nomes das linguagens e das pessoas importa na hora da atribuição.

linguagens = ["Python", "Java", "C#", "C++", "PHP", "Js"]
pessoas1 = ["A", "B","C","D","E","F","G","H", "Maria","Juca", "Obito", "Ludimilo"]
pessoas2 = ["Maria","Juca","Obito","Ludimilo"]

dicionario = dict()

for i in range(len(pessoas2)):
	for k in g.maxBPM():
		if i == k:
			dicionario[pessoas2[i]] = linguagens[g.maxBPM().index(k)]

print(dicionario)

#-----------------------------------------------------

g = GFG(grafo4)

print ("Grafo maior")
print(g.maxBPM())


linguagens = ["Python", "Java", "C#", "C++", "PHP", "Js"]
pessoas1 = ["A", "B","C","D","E","F","G","H", "Juca","Ludimilo","Maria","Obito"]
pessoas2 = ["Maria","Juca","Obito","Ludimilo"]

dicionario = dict()

for i in range(len(pessoas1)):
	for k in g.maxBPM():
		if i == k:
			dicionario[pessoas1[i]] = linguagens[g.maxBPM().index(k)]

print(dicionario)





