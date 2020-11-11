file = open('grafo.txt', 'r', encoding="utf8")

arrAux = []

for line in file:
    arrAux.append(line)

file.close()

for i in range(0, len(arrAux)):
    arrAux[i] = arrAux[i].strip("\n")

arrAux2 = ' '.join([str(elem) for elem in arrAux])
arrMain = arrAux2.split(" ")

x = 0
y = 1

col1 = []
col2 = []

for i in range(0, int(len(arrMain)/2)):
    col1.append(int(arrMain[x]))
    x += 2

for i in range(0, int(len(arrMain)/2)):
    col2.append(int(arrMain[y]))
    y += 2

colunas, linhas = 4, 6

listaAdj = dict()

for i in range(0, len(col1)):
    listaAdj[col1[i]] = col2[i]

print(arrMain)
print(col1)
print(col2)
print(listaAdj)
