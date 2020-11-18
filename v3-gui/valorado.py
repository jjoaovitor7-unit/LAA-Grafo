import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

def lista_adjacencia():
    # Abrindo arquivo
    file = open('v3-gui/data/grafo-valorado.txt', 'r', encoding='utf8')

    # Inicializando grafo
    grafo = {}

    for linha in file:
        v_inicial, v_final, peso = linha.split()
        grafo.setdefault(int(v_inicial), []).append((int(v_final), int(peso)))
        # grafo.setdefault(int(v_final), []).append((int(v_inicial), int(peso)))

    return grafo


def visualizar_grafo():
    g = nx.read_weighted_edgelist('v3-gui/data/grafo-valorado.txt',
                                  create_using=nx.DiGraph(), nodetype=int)
    nx.draw_shell(g, with_labels=True)
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

    grafo_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Grafo', menu=grafo_menu)
    grafo_menu.add_command(label='Visualizar Grafo', command=visualizar_grafo)

    # Widgets
    title_label = ttk.Label(self, text="LAA-Grafo",
                style='main.TLabel')
    title_label.grid(row=1, column=0)

    graph_representation = tk.Text(self, height=5, width=50)
    graph_representation.grid(row=2, column=0)
    for i in range(0, len(lista_adjacencia())+1):
        if i in lista_adjacencia().keys():
            graph_representation.insert(tk.END, str(i) + " -> " + str(lista_adjacencia()[i]) + "\n")
        else:
            i += 1
    graph_representation.configure(state='disabled')


def run():
    root = tk.Tk()
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
