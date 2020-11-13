import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

def listaAdj():
    # Abrindo arquivo
    file = open('v3-gui/data/grafo-nao-valorado.txt', 'r', encoding='utf8')

    # Inicializando grafo
    grafo = {}

    for linha in file:
        vInicial, vFinal = linha.split()
        grafo.setdefault(int(vInicial), []).append((int(vFinal)))
        # grafo.setdefault(int(vFinal), []).append((int(vInicial)))

    return grafo


def visualizar_grafo():
    g = nx.read_edgelist('v3-gui/data/grafo-nao-valorado.txt', create_using=nx.DiGraph(), nodetype=int)
    nx.draw(g)
    plt.show()


def main(self):
    # Título
    self.title("LAA-Grafo")

    # Tamanho da Janela
    self.geometry('500x175')
    self.grid_columnconfigure(0, weight=1)

    # Tema
    self.config(bg='#fff')
    style = ttk.Style()
    style.configure('main.TLabel', background='#fff',
                foreground='#000',
                font=('Times New Roman', '14'))

    # Menu
    menubar = tk.Menu(self)
    self.config(menu=menubar)

    grafoMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Grafo', menu=grafoMenu)

    grafoMenu.add_command(label='Visualizar Grafo', command=visualizar_grafo)

    # Widgets
    titleLabel = ttk.Label(self, text="LAA-Grafo",
                style='main.TLabel')

    titleLabel.grid(row=1, column=0)

    graphRepresentation = tk.Text(self, height=5, width=50)
    graphRepresentation.grid(row=2, column=0)
    for i in range(0, len(listaAdj())+1):
        if i in listaAdj().keys():
            graphRepresentation.insert(tk.END, str(i) + " -> " + str(listaAdj()[i]) + "\n")
        else:
            i += 1
    graphRepresentation.configure(state='disabled')


def run():
    root = tk.Tk()
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
