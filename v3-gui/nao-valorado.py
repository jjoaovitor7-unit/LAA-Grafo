import tkinter as tk
from tkinter import ttk

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

    # Widgets
    titleLabel = ttk.Label(self, text="LAA-Grafo",
                style='main.TLabel')

    titleLabel.grid(row=1, column=0)

    graphRepresentation = tk.Text(self, height=5, width=50)
    graphRepresentation.grid(row=2, column=0)
    graphRepresentation.insert(tk.END, listaAdj())


def run():
    root = tk.Tk()
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == '__main__':
    run()
