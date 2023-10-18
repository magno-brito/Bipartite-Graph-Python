
f = open("file.txt")
lines = f.read().split("\n")
vetor = list()
for i in lines:
    vetor.append(i.split("-"))

for i in range(len(vetor)):
    vetor[i][1] = vetor[i][1].split()
print(vetor)

dicionario = dict()
for item in vetor:
    chave = item[0].strip()
    valor = item[1]
    dicionario[chave] = valor
print(dicionario)
    


