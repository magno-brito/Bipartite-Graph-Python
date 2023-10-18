def simbolo(arquivo):
    empresas = {}
    with open("file.txt") as f:
     texto = f.read()
     for i in range(len(texto.split("\n")) - 1) :
        empresas.setdefault(texto.split("\n")[i].strip().replace('\t',''),texto.split("\n")[i+1].strip().replace('\t',''))
    return empresas


empresas = simbolo("nasdaq.txt")
print(empresas)