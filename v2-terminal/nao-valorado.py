# Abrindo arquivo
file = open('v2-terminal/data/grafo-nao-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial)))

print(f"Lista de Adjacência: {grafo}")