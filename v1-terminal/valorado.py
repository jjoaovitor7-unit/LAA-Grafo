import networkx as nx
import matplotlib.pyplot as plt

# Abrindo arquivo
file = open('v2-terminal/data/grafo-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    v_inicial, v_final, peso = linha.split()
    grafo.setdefault(int(v_inicial), []).append((int(v_final), int(peso)))
    # grafo.setdefault(int(v_final), []).append((int(v_inicial), int(peso)))

print(f"Lista de Adjacência: {grafo}")

view_graph_option = input("Deseja visualizar o grafo em imagem?\n<S/n>:")
if (view_graph_option.upper() == "S"):
    g = nx.read_weighted_edgelist('v3-gui/data/grafo-valorado.txt',
                                  create_using=nx.DiGraph(), nodetype=int)
    nx.draw_shell(g, with_labels=True)
    plt.show()
