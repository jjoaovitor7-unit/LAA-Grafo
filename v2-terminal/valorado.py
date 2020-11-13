# Abrindo arquivo
file = open('v2-terminal/data/grafo-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal, peso = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal), int(peso)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial), int(peso)))

print(f"Lista de Adjacência: {grafo}")