class Grafo_arquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
    def gerar_arquivo(self):
        f = open(self.arquivo,"r")
        lines = f.read().split("\n")
        vetor = list()
        for i in lines:
            vetor.append(i.split(" "))
        for i in range(len(vetor)):
            for k in range(len(vetor[i])):
                vetor[i][k] = int(vetor[i][k])
        return vetor