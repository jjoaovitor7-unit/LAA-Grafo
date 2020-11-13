# Passando os dados do arquivo grafo.txt para um array
file = open('v1-terminal/data/grafo-valorado.txt', 'r', encoding="utf8")
arrAux = []
for line in file:
    arrAux.append(line)
file.close()


# Retirando caracteres especiais
for i in range(0, len(arrAux)):
    arrAux[i] = arrAux[i].strip("\n")

arrAux2 = ' '.join([str(elem) for elem in arrAux])
arrMain = arrAux2.split(" ")


x = 0 # Variável auxiliar para Coluna 1
y = 1 # Variável auxiliar para Coluna 2
z = 2 # Variável auxiliar para Coluna 3
col1 = [] # Coluna 1 do txt
col2 = [] # Coluna 2 do txt
col3 = [] # Coluna 3 do txt (pesos)

# Valores para Coluna 1
for i in range(0, int(len(arrMain)/3)):
    col1.append(int(arrMain[x]))
    x += 3

# Valores para Coluna 2
for i in range(0, int(len(arrMain)/3)):
    col2.append(int(arrMain[y]))
    y += 3

# Valores para Coluna 3
for i in range(0, int(len(arrMain)/3)):
    col3.append(int(arrMain[z]))
    z += 3

# Lista de Adjacência
listaAdj = dict()
for i in range(0, len(col1)):
    if (col1[i] in listaAdj):
        if(isinstance(listaAdj[col1[i]], int)):
            arrAuxla = []
            arrAuxla.append(listaAdj[col1[i]])
            arrAuxla.append(col2[i])

            arrAuxla2 = []
            # arrAuxla2.append(str(str(col3[i-1]) + " " + str(col3[i])).split(" "))
            arrAuxla2.append(col3[i-1])

            listaAdj.update({col1[i]: arrAuxla + ["pesos:"] + arrAuxla2 + list(map(int, str(col3[i])))})

        else:
            arrAuxla.append(col2[i])
            arrAuxla2.append(col3[i-1])
            listaAdj.update({col1[i]: arrAuxla + ["pesos:"] + arrAuxla2 + list(map(int, str(col3[i])))})

    else:
        listaAdj[col1[i]] = col2[i]


# Printando os valores com F-strings
# print(f"Array Completo: {arrMain}")
# print(f"Coluna 1: {col1}")
# print(f"Coluna 2: {col2}")
# print(f"Coluna 3: {col3}")
print(f"Lista de Adjacência: \n{listaAdj}")
