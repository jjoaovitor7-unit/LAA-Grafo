# Passando os dados do arquivo grafo.txt para um array
file = open('grafo.txt', 'r', encoding="utf8")
arrAux = []
for line in file:
    arrAux.append(line)
file.close()


# Retirando caracteres especiais
for i in range(0, len(arrAux)):
    arrAux[i] = arrAux[i].strip("\n")

arrAux2 = ' '.join([str(elem) for elem in arrAux])
arrMain = arrAux2.split(" ")


# Variável auxiliar para Coluna 1
x = 0
# Variável auxiliar para Coluna 2
y = 1


# Coluna 1 do txt
col1 = []
# Coluna 2 do txt
col2 = []


# Valores p/ Coluna 1
for i in range(0, int(len(arrMain)/2)):
    col1.append(int(arrMain[x]))
    x += 2

# Valores p/ Coluna 2
for i in range(0, int(len(arrMain)/2)):
    col2.append(int(arrMain[y]))
    y += 2


# Lista de adjacência
listaAdj = dict()
for i in range(0, len(col1)):
    listaAdj[col1[i]] = col2[i]


# Printando os valores
print("Array Completo: " + arrMain)
print("Coluna 1: " + col1)
print("Coluna 2: " + col2)
print("Lista de Adjacência: " + listaAdj)
