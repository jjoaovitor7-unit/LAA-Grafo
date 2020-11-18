import networkx as nx
import matplotlib.pyplot as plt

representation_option = int(input("Representação do Grafo:\n1-Matriz de Adjacência\n2-Lista de Adjacência\n:"))
if (representation_option == 1):
    import numpy as np
    file = open("v2-terminal/data/grafo-nao-valorado.txt", "r", encoding="utf-8")

    arr_aux = []
    for linha in file:
        v_inicial, v_final = linha.split()
        arr_aux.append(int(v_inicial))
        arr_aux.append(int(v_final))
    file.close()

    file = open("v2-terminal/data/grafo-nao-valorado.txt", "r", encoding="utf-8")
    matriz = np.zeros((max(arr_aux)+1, max(arr_aux)+1))
    for linha in file:
        v_inicial, v_final = linha.split()
        matriz[int(v_inicial), int(v_final)] = 1
    print(f"\nMatriz de Adjacência:\n{matriz}")
    file.close()


if (representation_option == 2):
    # Abrindo arquivo
    file = open('v2-terminal/data/grafo-nao-valorado.txt', 'r', encoding='utf8')

    # Inicializando grafo
    grafo = {}

    for linha in file:
        v_inicial, v_final = linha.split()
        grafo.setdefault(int(v_inicial), []).append((int(v_final)))
        # grafo.setdefault(int(v_final), []).append((int(v_inicial)))

    print(f"\nLista de Adjacência: {grafo}")
    file.close()


view_graph_option = input("\nDeseja visualizar o grafo em imagem?\n<S/n>:")
if (view_graph_option.upper() == "S"):
    g = nx.read_edgelist('v3-gui/data/grafo-nao-valorado.txt',
                         create_using=nx.DiGraph(), nodetype=int)
    nx.draw_shell(g, with_labels=True)
    plt.show()
