import networkx as nx
import matplotlib.pyplot as plt

# Abrindo arquivo
file = open('v2-terminal/data/grafo-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal, peso = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal), int(peso)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial), int(peso)))

print(f"Lista de Adjacência: {grafo}")

cond = input("Deseja visualizar o grafo em imagem?\n<S/n>:")
if (cond.upper() == "S"):
    g = nx.read_weighted_edgelist('v3-gui/data/grafo-valorado.txt', create_using=nx.DiGraph(), nodetype=int)
    nx.draw_shell(g, with_labels=True)
    plt.show()