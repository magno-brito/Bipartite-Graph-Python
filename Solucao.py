
class GFG:
	def __init__(self,graph):
		self.graph = graph 
		self.ppl = len(graph)
		self.jobs = len(graph[0])

	def bpm(self, u, matchR, seen):
		for v in range(self.jobs):
			if self.graph[u][v] and seen[v] == False:
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


bpGraph =[[0, 1, 1, 0, 0, 0],
		[1, 0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0, 0],
		[0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1]]

grafo1 = [[0, 1, 2, 0], [1, 0, 0, 1]]

grafo2 = [["Java","Python",0,0,0],[0,"Python",0,0,0],[0,0,"C#","C++",0],["Java",0,0,0,"PHP"]]

g = GFG(grafo2)



print ("Maximum number of applicants that can get job is  ")
print(g.maxBPM())


#-----------------------------------------
linguagens = ["Java", "Python", "C#", "C++", "PHP"]
pessoas = ["Juca", "Ludimilo","Maria","Obito"]

dicionario = dict()

for i in range(len(pessoas)):
	for k in g.maxBPM():
		if i == k:
			dicionario[pessoas[i]] = linguagens[g.maxBPM().index(k)]

print(dicionario)


	




