from browser import document, html

# Abrindo arquivo
file = open('data/grafo-valorado.txt', 'r', encoding='utf8')

# Inicializando grafo
grafo = {}

for linha in file:
    vInicial, vFinal, peso = linha.split()
    grafo.setdefault(int(vInicial), []).append((int(vFinal), int(peso)))
    # grafo.setdefault(int(vFinal), []).append((int(vInicial), int(peso)))

document.attach(html.P("Representação do Grafo Valorado"))
for i in grafo:
    document.attach(str(i) + " -> " + str(grafo[i]) + html.BR())
