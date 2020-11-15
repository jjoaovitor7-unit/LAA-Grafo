import networkx as nx
import matplotlib.pyplot as plt

# Abrindo arquivo
file = open('v2-terminal/data/grafo-nao-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial)))

print(f"Lista de Adjacência: {grafo}")

cond = input("Deseja visualizar o grafo em imagem?\n<S/n>:")
if (cond.upper() == "S"):
    g = nx.read_edgelist('v3-gui/data/grafo-nao-valorado.txt', create_using=nx.DiGraph(), nodetype=int)
    nx.draw_shell(g, with_labels=True)
    plt.show()