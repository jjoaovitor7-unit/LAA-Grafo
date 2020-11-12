# Abrindo arquivo
file = open('v2/data/grafo-nao-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal)))
    # grafo.setdefault(vFinal, []).append((vInicial, peso))

print(f"Lista de Adjacência: {grafo}")