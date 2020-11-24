file = open('data/grafo-25000.txt')

grafo = {}
cont = 0
adjCont = []

for linha in file:
    vertices = linha.split()
    v_main = vertices.pop(0)
    v_adj = vertices
    grafo.setdefault(v_main, []).append(v_adj)
    adjCont.append(len(v_adj))
    print(v_main + " tem " + str(len(v_adj)) + " vértices adjacente(s).")
    cont += 1

print(f"Quantidade de Vértices: {cont}")
print(f"Complexidade: {cont + sum(adjCont)}")
#print(grafo)
#print(grafo['121875200'][0][1])